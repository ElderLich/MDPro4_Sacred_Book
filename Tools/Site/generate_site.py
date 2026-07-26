#!/usr/bin/env python3
"""Assemble the public Sacred Book VitePress site."""

from __future__ import annotations

import json
import re
import shutil
import sqlite3
from dataclasses import dataclass
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
DOCS_DIR = WORKSPACE / "docs"
GENERATED_DIR = WORKSPACE / "Generated" / "FunctionDocs"
SCRIPTS_DIR = WORKSPACE / "Scripts"
CARDS_DB = WORKSPACE / "cards.cdb"
EXAMPLE_LIMIT = 96
USAGE_TABLE_LIMIT = 24
USAGE_SNIPPET_LIMIT = 3
USAGE_SNIPPET_CONTEXT = 2

DOT_CALL_RE = re.compile(r"\b(aux|Auxiliary|Duel|Card|Effect|Group|Debug|bit)\.([A-Za-z_]\w*)")
COLON_CALL_RE = re.compile(r"\b[A-Za-z_]\w*:([A-Za-z_]\w*)")
SCRIPT_RE = re.compile(r"^c(\d+)\.lua$", re.IGNORECASE)

TYPE_LABELS = [
    (0x1, "Monster"),
    (0x2, "Spell"),
    (0x4, "Trap"),
    (0x10, "Normal"),
    (0x20, "Effect"),
    (0x40, "Fusion"),
    (0x80, "Ritual"),
    (0x100, "Trap Monster"),
    (0x200, "Spirit"),
    (0x400, "Union"),
    (0x800, "Gemini"),
    (0x1000, "Tuner"),
    (0x2000, "Synchro"),
    (0x4000, "Token"),
    (0x10000, "Quick-Play"),
    (0x20000, "Continuous"),
    (0x40000, "Equip"),
    (0x80000, "Field"),
    (0x100000, "Counter"),
    (0x200000, "Flip"),
    (0x400000, "Toon"),
    (0x800000, "Xyz"),
    (0x1000000, "Pendulum"),
    (0x2000000, "Special Summon"),
    (0x4000000, "Link"),
]

CATEGORY_LABELS = [
    (0x1, "Destroy"),
    (0x2, "Release"),
    (0x4, "Banish"),
    (0x8, "To hand"),
    (0x10, "To Deck"),
    (0x20, "To GY"),
    (0x40, "Deck send"),
    (0x80, "Discard self"),
    (0x100, "Normal Summon"),
    (0x200, "Special Summon"),
    (0x400, "Token"),
    (0x800, "GY action"),
    (0x1000, "Position"),
    (0x2000, "Control"),
    (0x4000, "Effect negation"),
    (0x8000, "Summon negation"),
    (0x10000, "Draw"),
    (0x20000, "Search"),
    (0x40000, "Equip"),
    (0x80000, "Damage"),
    (0x100000, "Recover"),
    (0x200000, "ATK change"),
    (0x400000, "DEF change"),
    (0x800000, "Counter"),
    (0x1000000, "Coin"),
    (0x2000000, "Dice"),
    (0x4000000, "Leave GY"),
    (0x8000000, "GY Special Summon"),
    (0x10000000, "Activation negation"),
    (0x20000000, "Declare name"),
    (0x40000000, "Fusion Summon"),
    (0x80000000, "To Extra Deck"),
    (0x100000000, "Set monster"),
    (0x200000000, "Set Spell/Trap"),
    (0x400000000, "Discard opponent"),
]


@dataclass(frozen=True)
class CardRecord:
    id: int
    name: str
    desc: str
    type: int
    atk: int
    defense: int
    level: int
    race: int
    attribute: int
    category: int


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)


def clean_generated_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def load_api_names() -> tuple[set[str], dict[str, list[str]]]:
    api_json = GENERATED_DIR / "api_functions.generated.json"
    if not api_json.exists():
        raise FileNotFoundError(
            f"Missing {api_json}. Run Tools/FunctionDocs/generate_function_docs.py first."
        )
    payload = json.loads(read_text(api_json))
    names = {entry["name"] for entry in payload["functions"]}
    by_short: dict[str, list[str]] = {}
    for name in names:
        if "." not in name:
            continue
        namespace, short = name.rsplit(".", 1)
        if namespace in {"Card", "Effect", "Group"}:
            by_short.setdefault(short, []).append(name)
    return names, by_short


def load_cards() -> dict[int, CardRecord]:
    if not CARDS_DB.exists():
        return {}
    con = sqlite3.connect(CARDS_DB)
    try:
        rows = con.execute(
            """
            select datas.id, texts.name, texts.desc, datas.type, datas.atk,
                   datas.def, datas.level, datas.race, datas.attribute, datas.category
            from datas
            join texts on texts.id = datas.id
            """
        ).fetchall()
    finally:
        con.close()
    return {
        int(row[0]): CardRecord(
            id=int(row[0]),
            name=row[1] or f"Card {row[0]}",
            desc=row[2] or "",
            type=int(row[3] or 0),
            atk=int(row[4] or 0),
            defense=int(row[5] or 0),
            level=int(row[6] or 0),
            race=int(row[7] or 0),
            attribute=int(row[8] or 0),
            category=int(row[9] or 0),
        )
        for row in rows
    }


def format_stat(value: int) -> str:
    if value == -2:
        return "?"
    if value < 0:
        return "-"
    return str(value)


def labels_from_mask(value: int, labels: list[tuple[int, str]]) -> list[str]:
    return [label for bit, label in labels if value & bit]


def category_labels_from_mask(value: int) -> list[str]:
    # Some legacy category values are stored as signed 32-bit integers.
    mask = value & 0xFFFFFFFF if value < 0 else value
    return labels_from_mask(mask, CATEGORY_LABELS)


def extract_api_calls(script: str, api_names: set[str], method_names: dict[str, list[str]]) -> list[str]:
    calls: set[str] = set()
    for namespace, short in DOT_CALL_RE.findall(script):
        namespace = "Auxiliary" if namespace == "aux" else namespace
        name = f"{namespace}.{short}"
        if name in api_names:
            calls.add(name)
    for short in COLON_CALL_RE.findall(script):
        for name in method_names.get(short, []):
            calls.add(name)
    return sorted(calls)


def split_api_name(name: str) -> tuple[str, str]:
    if "." in name:
        return name.rsplit(".", 1)
    return "Global", name


def api_link(name: str) -> str:
    namespace, short = split_api_name(name)
    return f"/api/functions/{safe_filename(namespace)}/{safe_filename(short)}"


def markdown_table_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("|", "\\|")
        .replace("\n", " ")
    )


def code_block(text: str) -> str:
    return text.replace("```", "` ` `")


def github_script_url(script_path: str) -> str:
    return f"https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/{script_path}"


def call_patterns(name: str) -> list[re.Pattern[str]]:
    namespace, short = split_api_name(name)
    escaped_short = re.escape(short)
    escaped_name = re.escape(name)
    patterns: list[str] = []

    if namespace == "Auxiliary":
        patterns.extend([
            rf"\baux\s*\.\s*{escaped_short}\b",
            rf"\bAuxiliary\s*\.\s*{escaped_short}\b",
        ])
    elif namespace in {"Card", "Effect", "Group"}:
        patterns.extend([
            rf":\s*{escaped_short}\b",
            rf"\b{re.escape(namespace)}\s*\.\s*{escaped_short}\b",
        ])
    elif namespace == "Global":
        patterns.append(rf"\b{escaped_short}\b")
    else:
        patterns.append(rf"\b{escaped_name}\b")

    return [re.compile(pattern) for pattern in patterns]


def extract_call_snippet(script: str, name: str) -> str:
    patterns = call_patterns(name)
    lines = script.splitlines()
    for index, line in enumerate(lines):
        if not any(pattern.search(line) for pattern in patterns):
            continue
        start = max(0, index - USAGE_SNIPPET_CONTEXT)
        end = min(len(lines), index + USAGE_SNIPPET_CONTEXT + 1)
        snippet = "\n".join(lines[start:end]).strip("\n")
        if len(snippet) > 1800:
            snippet = snippet[:1800].rstrip() + "\n-- ..."
        return snippet
    return ""


def usage_by_function(examples: list[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    usage: dict[str, list[dict[str, object]]] = {}
    for item in examples:
        for name in item["api_calls"]:
            usage.setdefault(str(name), []).append(item)
    return usage


def sort_usage_items(
    items: list[dict[str, object]],
    featured_ids: set[int],
) -> list[dict[str, object]]:
    return sorted(
        items,
        key=lambda item: (
            int(item["id"]) not in featured_ids,
            -len(item["api_calls"]),
            -int(item["desc_length"]),
            str(item["name"]).casefold(),
            int(item["id"]),
        ),
    )


def api_page_path(name: str) -> Path:
    namespace, short = split_api_name(name)
    return DOCS_DIR / "api" / "functions" / safe_filename(namespace) / f"{safe_filename(short)}.md"


def append_api_usage_sections(examples: list[dict[str, object]], featured_ids: set[int]) -> None:
    api_payload = json.loads(read_text(GENERATED_DIR / "api_functions.generated.json"))
    usage = usage_by_function(examples)

    for doc in api_payload["functions"]:
        name = str(doc["name"])
        page = api_page_path(name)
        if not page.exists():
            continue

        items = sort_usage_items(usage.get(name, []), featured_ids)
        lines = [
            "",
            "## Used By",
            "",
            "Generated from the local `Scripts/` folder and `cards.cdb`.",
            "",
        ]

        if not items:
            lines.extend(
                [
                    "No indexed local card script currently calls this function.",
                    "",
                    "This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.",
                ]
            )
        else:
            lines.extend(
                [
                    f"- Detected in **{len(items)}** indexed script(s).",
                    f"- Search this function in the [Script Explorer](/tools/script-explorer) with `{name}`.",
                    "",
                    "| Card | ID | Script | Detected Calls |",
                    "| --- | ---: | --- | ---: |",
                ]
            )
            for item in items[:USAGE_TABLE_LIMIT]:
                card_id = int(item["id"])
                card_name = markdown_table_escape(str(item["name"]))
                card_label = (
                    f"[{card_name}](/examples/cards/{card_id})"
                    if card_id in featured_ids
                    else card_name
                )
                script_path = str(item["script"])
                lines.append(
                    f"| {card_label} | `{card_id}` | [{markdown_table_escape(script_path)}]({github_script_url(script_path)}) | {len(item['api_calls'])} |"
                )
            if len(items) > USAGE_TABLE_LIMIT:
                lines.append(f"| ...and {len(items) - USAGE_TABLE_LIMIT} more |  |  |  |")

            snippet_entries: list[tuple[dict[str, object], str]] = []
            for item in items:
                snippet = extract_call_snippet(str(item["_script_text"]), name)
                if snippet:
                    snippet_entries.append((item, snippet))
                if len(snippet_entries) >= USAGE_SNIPPET_LIMIT:
                    break

            lines.extend(["", "## Script Examples", ""])
            if not snippet_entries:
                lines.append("No direct snippet was generated for this function call pattern yet.")
            else:
                for item, snippet in snippet_entries:
                    card_id = int(item["id"])
                    script_path = str(item["script"])
                    lines.extend(
                        [
                            f"### {item['name']} (`{card_id}`)",
                            "",
                            f"Source: [{script_path}]({github_script_url(script_path)})",
                            "",
                            "```lua",
                            code_block(snippet),
                            "```",
                            "",
                        ]
                    )

        page_text = read_text(page).rstrip()
        marker = "\n## Used By\n"
        if marker in page_text:
            page_text = page_text.split(marker, 1)[0].rstrip()
        write_text(page, page_text + "\n" + "\n".join(lines).rstrip())


def sync_api_reference() -> None:
    source = GENERATED_DIR / "wiki" / "api"
    if not source.exists():
        raise FileNotFoundError(
            f"Missing {source}. Run Tools/FunctionDocs/generate_function_docs.py first."
        )
    target = DOCS_DIR / "api"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def scan_examples() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    api_names, method_names = load_api_names()
    cards = load_cards()
    examples: list[dict[str, object]] = []

    for script_path in sorted(SCRIPTS_DIR.glob("c*.lua")):
        match = SCRIPT_RE.match(script_path.name)
        if not match:
            continue
        card_id = int(match.group(1))
        script = read_text(script_path)
        card = cards.get(
            card_id,
            CardRecord(card_id, f"Card {card_id}", "", 0, 0, 0, 0, 0, 0, 0),
        )
        calls = extract_api_calls(script, api_names, method_names)
        examples.append(
            {
                "id": card.id,
                "name": card.name,
                "script": f"Scripts/{script_path.name}",
                "type": card.type,
                "atk": card.atk,
                "def": card.defense,
                "level": card.level,
                "race": card.race,
                "attribute": card.attribute,
                "category": card.category,
                "desc": card.desc,
                "card_type_labels": labels_from_mask(card.type, TYPE_LABELS),
                "category_labels": category_labels_from_mask(card.category),
                "api_calls": calls,
                "script_length": len(script),
                "desc_length": len(card.desc),
                "_desc": card.desc,
                "_script_text": script,
            }
        )

    featured = sorted(
        examples,
        key=lambda item: (
            -len(item["api_calls"]),
            -int(item["desc_length"]),
            str(item["name"]).casefold(),
            int(item["id"]),
        ),
    )[:EXAMPLE_LIMIT]
    return examples, featured


def write_examples() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    examples, featured = scan_examples()
    examples_dir = DOCS_DIR / "examples"
    cards_dir = examples_dir / "cards"
    clean_generated_dir(cards_dir)

    public_dir = DOCS_DIR / "public" / "data"
    public_dir.mkdir(parents=True, exist_ok=True)
    featured_ids = {int(item["id"]) for item in featured}
    public_examples = [
        {key: value for key, value in item.items() if not key.startswith("_")}
        for item in examples
    ]
    write_text(public_dir / "card-examples.json", json.dumps(public_examples, ensure_ascii=False, indent=2))
    write_text(public_dir / "featured-card-ids.json", json.dumps(sorted(featured_ids), ensure_ascii=False, indent=2))

    function_usage: dict[str, list[int]] = {}
    for item in public_examples:
        for name in item["api_calls"]:
            function_usage.setdefault(str(name), []).append(int(item["id"]))
    for card_ids in function_usage.values():
        card_ids.sort()
    function_usage = dict(sorted(function_usage.items(), key=lambda pair: pair[0].casefold()))
    usage_lines = ["{"]
    for index, (name, card_ids) in enumerate(function_usage.items()):
        comma = "," if index + 1 < len(function_usage) else ""
        encoded_name = json.dumps(name, ensure_ascii=False)
        encoded_ids = json.dumps(card_ids, ensure_ascii=False, separators=(",", ":"))
        usage_lines.append(f"  {encoded_name}: {encoded_ids}{comma}")
    usage_lines.append("}")
    write_text(public_dir / "function-usage.json", "\n".join(usage_lines))

    for item in featured:
        card_id = int(item["id"])
        page = cards_dir / f"{card_id}.md"
        calls = list(item["api_calls"])
        api_lines = [f"- [`{name}`]({api_link(name)})" for name in calls[:40]]
        if len(calls) > 40:
            api_lines.append(f"- ...and {len(calls) - 40} more")
        if not api_lines:
            api_lines = ["- No generated API calls detected."]

        lines = [
            f"# {item['name']}",
            "",
            f"- **Card ID:** `{card_id}`",
            f"- **Script:** `{item['script']}`",
            "",
            "## Stats",
            "",
            "| Field | Value |",
            "| --- | --- |",
            f"| Type | `0x{int(item['type']):x}` |",
            f"| ATK | {format_stat(int(item['atk']))} |",
            f"| DEF | {format_stat(int(item['def']))} |",
            f"| Level/Rank/Link | `0x{int(item['level']):x}` |",
            f"| Race | `0x{int(item['race']):x}` |",
            f"| Attribute | `0x{int(item['attribute']):x}` |",
            f"| Category | `0x{int(item['category']):x}` |",
            "",
            "## Card Text",
            "",
            "```text",
            code_block(str(item["_desc"]).strip() or "(no text in cards.cdb)"),
            "```",
            "",
            "## Detected API Calls",
            "",
            *api_lines,
            "",
            "## Script",
            "",
            "```lua",
            code_block(str(item["_script_text"]).rstrip()),
            "```",
            "",
        ]
        write_text(page, "\n".join(lines))

    index_lines = [
        "# Card Script Examples",
        "",
        f"Generated from `{CARDS_DB.name}` and `{SCRIPTS_DIR.name}/`.",
        "",
        f"- Script files scanned: **{len(examples)}**",
        f"- Featured pages generated: **{len(featured)}**",
        "- Full machine-readable index: `/data/card-examples.json`",
        "- Featured card IDs: `/data/featured-card-ids.json`",
        "- Function usage index: `/data/function-usage.json`",
        "- Interactive search: [Script Explorer](/tools/script-explorer)",
        "",
        "The featured pages are selected from scripts with many detected API calls and card text available. The Script Explorer can search the full local script set by card ID, card name, script path, or detected API function.",
        "",
        "## Case Studies",
        "",
        "| Card | ID | Focus | Script |",
        "| --- | ---: | --- | --- |",
        "| [Mind Scan](mind-scan) | `34298391` | Continuous Trap information effects, `EFFECT_REVEAL_ONFIELD`, and declared-name negation | `Scripts/c34298391.lua` |",
        "",
        "## Featured Examples",
        "",
        "| Card | ID | API Calls | Script |",
        "| --- | ---: | ---: | --- |",
    ]
    for item in featured:
        card_id = int(item["id"])
        index_lines.append(
            "| "
            f"[{markdown_table_escape(str(item['name']))}](cards/{card_id})"
            f" | `{card_id}` | {len(item['api_calls'])} | `{item['script']}` |"
        )
    write_text(examples_dir / "index.md", "\n".join(index_lines))
    return examples, featured


def ts_string(value: object, limit: int | None = None) -> str:
    text = str(value)
    if limit is not None:
        text = text[:limit]
    return json.dumps(text, ensure_ascii=False)


def write_vitepress_config(featured: list[dict[str, object]]) -> None:
    namespace_dirs = sorted((DOCS_DIR / "api" / "functions").glob("*"))
    namespace_items = [
        f"              {{ text: {ts_string(path.name)}, link: '/api/functions/{path.name}/' }},"
        for path in namespace_dirs
        if path.is_dir()
    ]
    example_items = [
        f"            {{ text: {ts_string(item['name'], 42)}, link: '/examples/cards/{int(item['id'])}' }},"
        for item in featured[:24]
    ]
    lines = [
        "import { defineConfig } from 'vitepress';",
        "",
        "const analyticsToken = process.env.CLOUDFLARE_WEB_ANALYTICS_TOKEN?.trim();",
        "",
        "function renderSearchMarkdown(src: string, env: any, md: any) {",
        "  const relativePath = String(env.relativePath || '').replace(/\\\\/g, '/');",
        "  if (relativePath.startsWith('examples/cards/')) {",
        "    return '';",
        "  }",
        "  if (relativePath.startsWith('api/functions/')) {",
        "    src = src.split(/\\n## Used By\\n/)[0];",
        "  }",
        "  return md.render(src, env);",
        "}",
        "",
        "export default defineConfig({",
        "  title: 'MDPro3 Sacred Book',",
        "  description: 'MDPro3/YGOPro Lua card scripting lessons, examples, and API reference.',",
        "  base: '/MDPro3_Sacred_Book/',",
        "  cleanUrls: true,",
        "  head: analyticsToken",
        "    ? [",
        "        [",
        "          'script',",
        "          {",
        "            type: 'module',",
        "            src: 'https://static.cloudflareinsights.com/beacon.min.js',",
        "            'data-cf-beacon': JSON.stringify({ token: analyticsToken, spa: true }),",
        "          },",
        "        ],",
        "      ]",
        "    : [],",
        "  themeConfig: {",
        "    nav: [",
        "      { text: 'Home', link: '/' },",
        "      { text: 'Learn', link: '/learn/' },",
        "      { text: 'API', link: '/api/' },",
        "      { text: 'Examples', link: '/examples/' },",
        "      { text: 'Script Explorer', link: '/tools/script-explorer' },",
        "    ],",
        "    sidebar: {",
        "      '/learn/': [",
        "        {",
        "          text: 'Learning Path',",
        "          items: [",
        "            { text: 'Overview', link: '/learn/' },",
        "            { text: 'Script Structure', link: '/learn/script-structure' },",
        "            { text: 'First Scripts', link: '/learn/first-scripts' },",
        "            { text: 'Beginner Script Ladder', link: '/learn/beginner-script-ladder' },",
        "            { text: 'First Custom Card', link: '/learn/first-custom-card' },",
        "            { text: 'Card Data and Script Wiring', link: '/learn/card-data-and-script-wiring' },",
        "            { text: 'Effect Object', link: '/learn/effect-object' },",
        "            { text: 'Effect Types', link: '/learn/effect-types' },",
        "            { text: 'Categories and Properties', link: '/learn/categories-properties-and-hints' },",
        "            { text: 'Client UI and Prompts', link: '/learn/client-ui-and-prompt-behavior' },",
        "            { text: 'Callbacks', link: '/learn/effect-callbacks' },",
        "            { text: 'Activated Effects', link: '/learn/activated-effects' },",
        "            { text: 'Activation Legality', link: '/learn/activation-legality' },",
        "            { text: 'Chain Timing', link: '/learn/chain-timing-and-activation-windows' },",
        "            { text: 'Spell Cards', link: '/learn/spell-card-patterns' },",
        "            { text: 'Quick-Play Spells', link: '/learn/quick-play-spells' },",
        "            { text: 'Trap Cards', link: '/learn/trap-card-patterns' },",
        "            { text: 'Normal and Continuous Traps', link: '/learn/normal-and-continuous-traps' },",
        "            { text: 'Counter Traps', link: '/learn/counter-traps' },",
        "            { text: 'Ritual Procedure', link: '/learn/ritual-procedure' },",
        "            { text: 'Fusion Procedure', link: '/learn/fusion-procedure' },",
        "            { text: 'Synchro Procedure', link: '/learn/synchro-procedure' },",
        "            { text: 'Xyz Procedure', link: '/learn/xyz-procedure' },",
        "            { text: 'Link Procedure', link: '/learn/link-procedure' },",
        "            { text: 'Pendulum Procedure', link: '/learn/pendulum-procedure' },",
        "            { text: 'Special Summon-only Monsters', link: '/learn/special-summon-only-monsters' },",
        "            { text: 'Gemini Monsters', link: '/learn/gemini-monsters' },",
        "            { text: 'Toon Monsters', link: '/learn/toon-monsters' },",
        "            { text: 'Union Monsters', link: '/learn/union-monsters' },",
        "            { text: 'Spirit Monsters', link: '/learn/spirit-monsters' },",
        "            { text: 'Tribute Summon Materials', link: '/learn/tribute-summon-materials' },",
        "            { text: 'Counters', link: '/learn/counters' },",
        "            { text: 'Filters and Groups', link: '/learn/filters-and-groups' },",
        "            { text: 'Selection and Group Handling', link: '/learn/selection-and-group-handling' },",
        "            { text: 'Min/Max Stat Selection', link: '/learn/min-max-stat-selection' },",
        "            { text: 'Reset Flags and Duration', link: '/learn/reset-flags-and-duration' },",
        "            { text: 'Moving Cards', link: '/learn/moving-cards' },",
        "            { text: 'Negation and Immunity', link: '/learn/negation-and-immunity' },",
        "            { text: 'Control Change', link: '/learn/control-change' },",
        "            { text: 'Battle Position Effects', link: '/learn/battle-position-effects' },",
        "            { text: 'Field Zones', link: '/learn/field-zones-and-sequences' },",
        "            { text: 'Field Spells', link: '/learn/field-spells' },",
        "            { text: 'Targeting Flow', link: '/learn/targeting-flow' },",
        "            { text: 'Effect Lifecycle', link: '/learn/cost-target-operation-lifecycle' },",
        "            { text: 'Continuous Effects', link: '/learn/continuous-effects' },",
        "            { text: 'Stat Modifiers', link: '/learn/continuous-stat-modifiers' },",
        "            { text: 'Equip Spells', link: '/learn/equip-spells' },",
        "            { text: 'LP and Damage', link: '/learn/lp-recovery-and-damage' },",
        "            { text: 'Player-Targeted Effects', link: '/learn/player-targeted-effects' },",
        "            { text: 'Player Restrictions', link: '/learn/player-restrictions' },",
        "            { text: 'Draw, Hand, and Deck Effects', link: '/learn/draw-hand-and-deck-effects' },",
        "            { text: 'Flag Effects', link: '/learn/flag-effects' },",
        "            { text: 'Count Limits', link: '/learn/count-limits' },",
        "            { text: 'Common Script Errors', link: '/learn/common-script-errors-and-debugging' },",
        "            { text: 'Affecting Cards', link: '/learn/affecting-cards' },",
        "            { text: 'Archetypes and Set Codes', link: '/learn/archetypes-and-setcodes' },",
        "          ],",
        "        },",
        "      ],",
        "      '/getting-started/': [",
        "        {",
        "          text: 'Getting Started',",
        "          items: [",
        "            { text: 'Overview', link: '/getting-started/' },",
        "            { text: 'Setup', link: '/getting-started/setup' },",
        "            { text: 'Your First Card', link: '/getting-started/first-card' },",
        "            { text: 'Reading Card Scripts', link: '/getting-started/reading-scripts' },",
        "          ],",
        "        },",
        "      ],",
        "      '/guides/': [",
        "        {",
        "          text: 'Guides',",
        "          items: [",
        "            { text: 'Overview', link: '/guides/' },",
        "            { text: 'Effect Anatomy', link: '/guides/effect-anatomy' },",
        "            { text: 'Card Database', link: '/guides/card-database' },",
        "            { text: 'Common Patterns', link: '/guides/common-patterns' },",
        "          ],",
        "        },",
        "      ],",
        "      '/tools/': [",
        "        {",
        "          text: 'Tools',",
        "          items: [",
        "            { text: 'Script Explorer', link: '/tools/script-explorer' },",
        "          ],",
        "        },",
        "      ],",
        "      '/api/functions/': [",
        "        { text: 'Function Index', link: '/api/functions/' },",
        "        {",
        "          text: 'Namespaces',",
        "          collapsed: false,",
        "          items: [",
        *namespace_items,
        "          ],",
        "        },",
        "      ],",
        "      '/api/': [",
        "        { text: 'API Overview', link: '/api/' },",
        "        { text: 'Functions', link: '/api/functions/' },",
        "        { text: 'Constants', link: '/api/constants' },",
        "      ],",
        "      '/examples/': [",
        "        {",
        "          text: 'Examples',",
        "          items: [",
        "            { text: 'Overview', link: '/examples/' },",
        "            { text: 'Mind Scan', link: '/examples/mind-scan' },",
        *example_items,
        "          ],",
        "        },",
        "      ],",
        "    },",
        "    outline: {",
        "      label: 'Contents',",
        "      level: [2, 4],",
        "    },",
        "    search: {",
        "      provider: 'local',",
        "      options: {",
        "        detailedView: true,",
        "        disableQueryPersistence: true,",
        "        miniSearch: {",
        "          searchOptions: {",
        "            prefix: true,",
        "            fuzzy: 0.2,",
        "            boost: { title: 4, titles: 2, text: 1 },",
        "          },",
        "        },",
        "        _render: renderSearchMarkdown,",
        "      },",
        "    },",
        "    socialLinks: [",
        "      { icon: 'github', link: 'https://github.com/ElderLich/MDPro3_Sacred_Book' },",
        "    ],",
        "    footer: {",
        "      message: '<a href=\"/MDPro3_Sacred_Book/privacy\">Privacy & analytics</a>',",
        "    },",
        "  },",
        "});",
        "",
    ]
    write_text(DOCS_DIR / ".vitepress" / "config.mts", "\n".join(lines))


def main() -> int:
    sync_api_reference()
    examples, featured = write_examples()
    featured_ids = {int(item["id"]) for item in featured}
    append_api_usage_sections(examples, featured_ids)
    write_vitepress_config(featured)
    print(f"Synced API reference into {DOCS_DIR / 'api'}")
    print(f"Generated {len(featured)} featured card example pages")
    print("Added API usage sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
