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
RUSH_SCRIPTS_DIR = WORKSPACE / "Rush" / "Scripts"
RUSH_CARDS_DB = WORKSPACE / "rush_cards.cdb"
RUSH_TUTORIAL_IDS = {120105006, 120150002, 120150001, 120102001, 120280030, 120280031}
EXAMPLE_LIMIT = 96
USAGE_TABLE_LIMIT = 24
USAGE_SNIPPET_LIMIT = 3
USAGE_SNIPPET_CONTEXT = 2

DOT_CALL_RE = re.compile(r"\b([A-Za-z_]\w*)\.([A-Za-z_]\w*)")
COLON_CALL_RE = re.compile(r"\b[A-Za-z_]\w*:([A-Za-z_]\w*)")
SCRIPT_CONSTANT_RE = re.compile(r"\b[A-Z][A-Z0-9_]*_[A-Z0-9_]+\b")
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
RUSH_TYPE_LABELS = TYPE_LABELS + [(0x8, "Legend"), (0x8000, "Maximum")]

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
    if not path.resolve().is_relative_to(DOCS_DIR.resolve()):
        raise ValueError(f"Refusing to clean generated directory outside docs: {path}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def load_api_names(format: str = "standard") -> tuple[set[str], dict[str, list[str]]]:
    api_json = GENERATED_DIR / "api_functions.generated.json"
    if not api_json.exists():
        raise FileNotFoundError(
            f"Missing {api_json}. Run Tools/FunctionDocs/generate_function_docs.py first."
        )
    payload = json.loads(read_text(api_json))
    names = {entry["name"] for entry in payload["functions"]}
    if format == "rush":
        rush_payload = json.loads(read_text(GENERATED_DIR / "rush" / "api_functions.generated.json"))
        names.update(entry["name"] for entry in rush_payload["functions"])
    by_short: dict[str, list[str]] = {}
    for name in names:
        if "." not in name:
            continue
        namespace, short = name.rsplit(".", 1)
        if namespace in {"Card", "Effect", "Group"}:
            by_short.setdefault(short, []).append(name)
    return names, by_short


def load_cards(database: Path = CARDS_DB) -> dict[int, CardRecord]:
    if not database.exists():
        raise FileNotFoundError(f"Missing card database: {database}")
    con = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
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
        namespace = {"aux": "Auxiliary", "RD": "RushDuel"}.get(namespace, namespace)
        name = f"{namespace}.{short}"
        if name in api_names:
            calls.add(name)
    for short in COLON_CALL_RE.findall(script):
        for name in method_names.get(short, []):
            calls.add(name)
    return sorted(calls)


def extract_script_constants(script: str) -> list[str]:
    code = "\n".join(line.split("--", 1)[0] for line in script.splitlines())
    return sorted(set(SCRIPT_CONSTANT_RE.findall(code)))


def split_api_name(name: str) -> tuple[str, str]:
    if "." in name:
        return name.rsplit(".", 1)
    return "Global", name


def api_link(name: str, rush_names: set[str] | None = None) -> str:
    namespace, short = split_api_name(name)
    prefix = "/rush" if rush_names and name in rush_names else ""
    return f"{prefix}/api/functions/{safe_filename(namespace)}/{safe_filename(short)}"


def example_link(item: dict[str, object]) -> str:
    folder = "rush-cards" if item["format"] == "rush" else "cards"
    return f"/examples/{folder}/{item['id']}"


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
    elif namespace == "RushDuel":
        patterns.extend([
            rf"\bRD\s*\.\s*{escaped_short}\b",
            rf"\bRushDuel\s*\.\s*{escaped_short}\b",
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


def count_api_calls(script: str, name: str) -> int:
    return sum(len(pattern.findall(script)) for pattern in call_patterns(name))


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


def api_page_path(name: str, format: str = "standard") -> Path:
    namespace, short = split_api_name(name)
    root = DOCS_DIR / "rush" if format == "rush" else DOCS_DIR
    return root / "api" / "functions" / safe_filename(namespace) / f"{safe_filename(short)}.md"


def append_api_usage_sections(examples: list[dict[str, object]], featured_ids: set[int], format: str = "standard") -> None:
    generated = GENERATED_DIR / "rush" if format == "rush" else GENERATED_DIR
    api_payload = json.loads(read_text(generated / "api_functions.generated.json"))
    usage = usage_by_function(examples)

    for doc in api_payload["functions"]:
        name = str(doc["name"])
        page = api_page_path(name, format)
        if not page.exists():
            continue

        items = sort_usage_items(usage.get(name, []), featured_ids)
        lines = [
            "",
            "## Used By",
            "",
            "Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`." if format == "rush" else "Generated from the local `Scripts/` folder and `cards.cdb`.",
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
                    f"- Search this function in the [Script Explorer](/tools/script-explorer?format={format}&mode=code&q={name}) with `{name}`.",
                    "",
                    "| Card | ID | Script | Detected Calls |",
                    "| --- | ---: | --- | ---: |",
                ]
            )
            for item in items[:USAGE_TABLE_LIMIT]:
                card_id = int(item["id"])
                card_name = markdown_table_escape(str(item["name"]))
                card_label = (
                    f"[{card_name}]({example_link(item)})"
                    if card_id in featured_ids
                    else card_name
                )
                script_path = str(item["script"])
                detected_calls = count_api_calls(str(item["_script_text"]), name)
                lines.append(
                    f"| {card_label} | `{card_id}` | [{markdown_table_escape(script_path)}]({github_script_url(script_path)}) | {detected_calls} |"
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


def sync_api_reference(format: str = "standard") -> None:
    generated = GENERATED_DIR / "rush" if format == "rush" else GENERATED_DIR
    source = generated / "wiki" / "api"
    if not source.exists():
        raise FileNotFoundError(
            f"Missing {source}. Run Tools/FunctionDocs/generate_function_docs.py first."
        )
    target = DOCS_DIR / "rush" / "api" if format == "rush" else DOCS_DIR / "api"
    clean_generated_dir(target)
    shutil.copytree(source, target, dirs_exist_ok=True)


def scan_examples(format: str = "standard") -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    api_names, method_names = load_api_names(format)
    scripts_dir = RUSH_SCRIPTS_DIR if format == "rush" else SCRIPTS_DIR
    cards = load_cards(RUSH_CARDS_DB if format == "rush" else CARDS_DB)
    rush_names = set()
    if format == "rush":
        rush_payload = json.loads(read_text(GENERATED_DIR / "rush" / "api_functions.generated.json"))
        rush_names = {entry["name"] for entry in rush_payload["functions"]}
    examples: list[dict[str, object]] = []

    for script_path in sorted(scripts_dir.glob("c*.lua")):
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
        constants = extract_script_constants(script)
        examples.append(
            {
                "id": card.id,
                "format": format,
                "name": card.name,
                "script": script_path.relative_to(WORKSPACE).as_posix(),
                "type": card.type,
                "atk": card.atk,
                "def": card.defense,
                "level": card.level,
                "race": card.race,
                "attribute": card.attribute,
                "category": card.category,
                "desc": card.desc,
                "card_type_labels": labels_from_mask(card.type, RUSH_TYPE_LABELS if format == "rush" else TYPE_LABELS),
                "category_labels": category_labels_from_mask(card.category),
                "api_calls": calls,
                "api_links": {name: api_link(name, rush_names) for name in calls} if format == "rush" else {},
                "script_constants": constants,
                "script_length": len(script),
                "desc_length": len(card.desc),
                "_desc": card.desc,
                "_script_text": script,
            }
        )

    featured = sorted(
        examples,
        key=lambda item: (
            format == "rush" and int(item["id"]) not in RUSH_TUTORIAL_IDS,
            -len(item["api_calls"]),
            -int(item["desc_length"]),
            str(item["name"]).casefold(),
            int(item["id"]),
        ),
    )[:EXAMPLE_LIMIT]
    return examples, featured


def write_id_usage_index(path: Path, usage: dict[str, list[int]]) -> None:
    for card_ids in usage.values():
        card_ids.sort()
    usage = dict(sorted(usage.items(), key=lambda pair: pair[0].casefold()))
    lines = ["{"]
    for index, (name, card_ids) in enumerate(usage.items()):
        comma = "," if index + 1 < len(usage) else ""
        encoded_name = json.dumps(name, ensure_ascii=False)
        encoded_ids = json.dumps(card_ids, ensure_ascii=False, separators=(",", ":"))
        lines.append(f"  {encoded_name}: {encoded_ids}{comma}")
    lines.append("}")
    write_text(path, "\n".join(lines))


def write_examples(format: str = "standard") -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    examples, featured = scan_examples(format)
    examples_dir = DOCS_DIR / "examples"
    cards_dir = examples_dir / ("rush-cards" if format == "rush" else "cards")
    clean_generated_dir(cards_dir)

    public_dir = DOCS_DIR / "public" / "data"
    if format == "rush":
        public_dir /= "rush"
    public_dir.mkdir(parents=True, exist_ok=True)
    featured_ids = {int(item["id"]) for item in featured}
    public_examples = [
        {
            key: value
            for key, value in item.items()
            if not key.startswith("_") and key != "script_constants"
        }
        for item in examples
    ]
    write_text(public_dir / "card-examples.json", json.dumps(public_examples, ensure_ascii=False, indent=2))
    write_text(public_dir / "featured-card-ids.json", json.dumps(sorted(featured_ids), ensure_ascii=False, indent=2))

    function_usage: dict[str, list[int]] = {}
    for item in public_examples:
        for name in item["api_calls"]:
            function_usage.setdefault(str(name), []).append(int(item["id"]))
    write_id_usage_index(public_dir / "function-usage.json", function_usage)

    constant_usage: dict[str, list[int]] = {}
    for item in examples:
        for name in item["script_constants"]:
            constant_usage.setdefault(str(name), []).append(int(item["id"]))
    write_id_usage_index(public_dir / "constant-usage.json", constant_usage)

    for item in featured:
        card_id = int(item["id"])
        page = cards_dir / f"{card_id}.md"
        calls = list(item["api_calls"])
        api_lines = [f"- [`{name}`]({item['api_links'].get(name, api_link(name))})" for name in calls[:40]]
        if len(calls) > 40:
            api_lines.append(f"- ...and {len(calls) - 40} more")
        if not api_lines:
            api_lines = ["- No generated API calls detected."]

        lines = [
            f"# {item['name']}",
            "",
            f"- **Card ID:** `{card_id}`",
            f"- **Format:** {'Rush Duel' if format == 'rush' else 'Standard'}",
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
            code_block(str(item["_desc"]).strip() or "(no text in this format's database)"),
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
        "Generated from `rush_cards.cdb` and `Rush/Scripts/`." if format == "rush" else "Generated from `cards.cdb` and `Scripts/`.",
        "",
        f"- Script files scanned: **{len(examples)}**",
        f"- Featured pages generated: **{len(featured)}**",
        "- Full machine-readable index: `/data/card-examples.json`",
        "- Featured card IDs: `/data/featured-card-ids.json`",
        "- Function usage index: `/data/function-usage.json`",
        "- Constant usage index: `/data/constant-usage.json`",
        f"- Interactive search: [Script Explorer](/tools/script-explorer?format={format})",
        "",
        "The featured pages are selected from scripts with many detected API calls and card text available. The Script Explorer can search the full local script set by card ID, card name, script path, detected API function, or named Lua constant.",
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
            f"[{markdown_table_escape(str(item['name']))}]({example_link(item)})"
            f" | `{card_id}` | {len(item['api_calls'])} | `{item['script']}` |"
        )
    if format == "rush":
        index_lines[0] = "# Rush Duel Script Examples"
        start = index_lines.index("## Case Studies")
        end = index_lines.index("## Featured Examples")
        index_lines[start:end] = ["Study the [Rush Duel learning track](/learn/rush-duel) before adapting these scripts.", ""]
        index_lines = [line.replace("`/data/", "`/data/rush/") for line in index_lines]
    else:
        index_lines[4:4] = ["See also [Rush Duel examples](/examples/rush) and the [Rush Duel learning track](/learn/rush-duel).", ""]
    write_text(examples_dir / ("rush.md" if format == "rush" else "index.md"), "\n".join(index_lines))
    return examples, featured


def write_navigation(featured: list[dict[str, object]]) -> None:
    """Only generated navigation belongs here; keep authored site config intact."""
    namespaces = sorted((DOCS_DIR / "api" / "functions").glob("*"))
    payload = {
        "namespaces": [
            {"text": path.name, "link": f"/api/functions/{path.name}/"}
            for path in namespaces if path.is_dir()
        ],
        "examples": [
            {"text": str(item["name"])[:42], "link": example_link(item)}
            for item in featured if item["format"] == "standard"
        ][:24],
    }
    write_text(DOCS_DIR / ".vitepress" / "navigation.generated.json", json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> int:
    sync_api_reference()
    examples, featured = write_examples()
    featured_ids = {int(item["id"]) for item in featured}
    append_api_usage_sections(examples, featured_ids)
    sync_api_reference("rush")
    rush_examples, rush_featured = write_examples("rush")
    append_api_usage_sections(rush_examples, {int(item["id"]) for item in rush_featured}, "rush")
    write_navigation(featured)
    print(f"Synced API reference into {DOCS_DIR / 'api'}")
    print(f"Generated {len(featured)} featured card example pages")
    print(f"Indexed {len(rush_examples)} Rush scripts with {len(rush_featured)} featured pages")
    print("Added API usage sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
