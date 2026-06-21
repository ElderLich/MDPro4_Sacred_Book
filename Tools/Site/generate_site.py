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

DOT_CALL_RE = re.compile(r"\b(aux|Auxiliary|Duel|Card|Effect|Group|Debug|bit)\.([A-Za-z_]\w*)")
COLON_CALL_RE = re.compile(r"\b[A-Za-z_]\w*:([A-Za-z_]\w*)")
SCRIPT_RE = re.compile(r"^c(\d+)\.lua$", re.IGNORECASE)


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


def api_link(name: str) -> str:
    namespace, short = name.rsplit(".", 1)
    return f"/api/functions/{safe_filename(namespace)}/{safe_filename(short)}"


def markdown_table_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def code_block(text: str) -> str:
    return text.replace("```", "` ` `")


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


def write_examples() -> list[dict[str, object]]:
    examples, featured = scan_examples()
    examples_dir = DOCS_DIR / "examples"
    cards_dir = examples_dir / "cards"
    clean_generated_dir(cards_dir)

    public_dir = DOCS_DIR / "public" / "data"
    public_dir.mkdir(parents=True, exist_ok=True)
    public_examples = [
        {key: value for key, value in item.items() if not key.startswith("_")}
        for item in examples
    ]
    write_text(public_dir / "card-examples.json", json.dumps(public_examples, ensure_ascii=False, indent=2))

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
        "",
        "The featured pages are selected from scripts with many detected API calls and card text available. They are meant as a practical reading set while the API reference stays nearby.",
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
    return featured


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
        "export default defineConfig({",
        "  title: 'MDPro3 Sacred Book',",
        "  description: 'MDPro3/YGOPro Lua card scripting lessons, examples, and API reference.',",
        "  base: '/MDPro3_Sacred_Book/',",
        "  cleanUrls: true,",
        "  themeConfig: {",
        "    nav: [",
        "      { text: 'Home', link: '/' },",
        "      { text: 'Getting Started', link: '/getting-started/' },",
        "      { text: 'Guides', link: '/guides/' },",
        "      { text: 'API', link: '/api/' },",
        "      { text: 'Examples', link: '/examples/' },",
        "    ],",
        "    sidebar: {",
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
        *example_items,
        "          ],",
        "        },",
        "      ],",
        "    },",
        "    outline: {",
        "      label: 'Contents',",
        "      level: [2, 4],",
        "    },",
        "    search: { provider: 'local' },",
        "    socialLinks: [",
        "      { icon: 'github', link: 'https://github.com/ElderLich/MDPro3_Sacred_Book' },",
        "    ],",
        "  },",
        "});",
        "",
    ]
    write_text(DOCS_DIR / ".vitepress" / "config.mts", "\n".join(lines))


def main() -> int:
    sync_api_reference()
    featured = write_examples()
    write_vitepress_config(featured)
    print(f"Synced API reference into {DOCS_DIR / 'api'}")
    print(f"Generated {len(featured)} featured card example pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
