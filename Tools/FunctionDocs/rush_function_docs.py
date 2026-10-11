"""Source-backed reference for the separately versioned Rush Duel Lua helpers.

Do not merge Rush constants into the standard environment: several bit values
have a different meaning, and RD is an alias provided by the Rush bootstrap.
"""
from __future__ import annotations

import json
import html
import re
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path


DECLARATION = re.compile(r"^function\s+(RushDuel\.[A-Za-z_]\w*)\s*\(([^)]*)\)", re.MULTILINE)


def prose(text: str) -> str:
    """Escape literal HTML outside inline code; preserve intentional code spans."""
    return "`".join(part if index % 2 else html.escape(part, quote=False)
                    for index, part in enumerate(text.split("`")))


def generate_rush_docs(workspace: Path, out: Path, api) -> tuple[int, int]:
    source_root = workspace / "Rush" / "Utilities"
    if not source_root.exists():
        return 0, 0
    overrides = json.loads(api.read_text(Path(__file__).with_name("rush_doc_overrides.json")))
    reviewed = overrides["functions"]
    docs = []
    snippets = {}
    constants = {}
    bootstrap = api.read_text(source_root / "special.lua")
    source_paths = [source_root / name for name in re.findall(r'Duel\.LoadScript\("(RD[^"/]+\.lua)"\)', bootstrap)]
    if not source_paths:
        raise ValueError("Rush bootstrap did not declare its helper loading order.")
    shadowed = []
    for path in source_paths:
        text = api.read_text(path)
        declarations = list(DECLARATION.finditer(text))
        for index, match in enumerate(declarations):
            name, raw_args = match.groups()
            short = name.split(".", 1)[1]
            if short.startswith("_"):
                continue
            line = text.count("\n", 0, match.start()) + 1
            source = api.SourceRef(api.display_path(path, workspace), line, "rush-utility")
            end = declarations[index + 1].start() if index + 1 < len(declarations) else len(text)
            body_lines = text[match.start():end].strip().splitlines()
            while body_lines and (not body_lines[-1].strip() or body_lines[-1].lstrip().startswith("--")):
                body_lines.pop()
            body = "\n".join(body_lines)
            comments = []
            for previous in reversed(text[:match.start()].splitlines()):
                if previous.strip().startswith("--"):
                    comments.insert(0, previous.strip().lstrip("-").strip())
                elif previous.strip() or comments:
                    break
            params = [api.ParamDoc(name=arg, type="any") for arg in api.split_args(raw_args)]
            # A missing annotation is not evidence of a void function. Curated
            # contracts below are authoritative; other types stay unspecified.
            returns = [api.ReturnDoc(type="any", description="Return contract has not been reviewed; inspect the source below.")]
            entry = reviewed.get(short, {})
            if "params" in entry:
                by_name = {param["name"]: param for param in entry["params"]}
                unknown = set(by_name) - {param.name for param in params}
                if unknown:
                    raise ValueError(f"Stale Rush parameter documentation for {name}: {unknown}")
                params = [api.ParamDoc(**by_name.get(param.name, asdict(param))) for param in params]
            if "returns" in entry:
                returns = [api.ReturnDoc(**ret) for ret in entry["returns"]]
            description = entry.get("summary_en", [
                f"Rush Duel helper declared in `{path.name}`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.",
            ])
            doc = api.FunctionDoc(
                name=name, namespace="RushDuel", short_name=short, params=params,
                returns=returns, description_zh=comments, description_en=description,
                english_status="reviewed_english" if entry else "source_only",
                source_files=[source], aliases=[f"RD.{short}"], tags=["rush-duel", "lua-helper"],
            )
            previous = next((old for old in docs if old.name == name), None)
            if previous is not None:
                shadowed.append({"name": name, "replaced": asdict(previous.source_files[0]), "active": asdict(source)})
                docs.remove(previous)
            docs.append(doc)
            snippets[name] = body
        for name, doc in api.parse_constant_docs(path, workspace, "rush-utility").items():
            if name != name.upper():
                continue
            doc.section = "Rush Duel"
            if name in overrides["constants"]:
                doc.comment_en = overrides["constants"][name]
                doc.english_status = "reviewed_english"
            else:
                doc.comment_en = "Rush-specific constant; see the upstream source comment."
                doc.english_status = "source_only"
            constants[name] = doc
    docs.sort(key=lambda doc: doc.short_name.lower())
    names = [doc.name for doc in docs]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate Rush helper declaration; resolve bootstrap ordering before publishing.")
    stale = set(reviewed) - {doc.short_name for doc in docs}
    if stale:
        raise ValueError(f"Rush overrides reference missing helpers: {sorted(stale)}")
    metadata = {
        "ruleset": "rush", "namespace": "RushDuel", "alias": "RD",
        "source_files": [api.display_path(path, workspace) for path in source_paths],
        "shadowed_declarations": shadowed,
        "bootstrap": "Rush/Utilities/special.lua",
        "note": "Requires the matching Rush Duel bootstrap; these are Lua helpers, not native core bindings. Keep Rush constants separate from standard constants.",
    }
    api.write_json(out / "api_functions.generated.json", docs, metadata)
    api.write_compat_file(out / "_functions.generated.txt", docs, "zh")
    api.write_compat_file(out / "_function_english.generated.txt", docs, "en")
    # DataEditorX's lookup uses the literal name: publish both real spellings.
    for filename in ("_functions.generated.txt", "_function_english.generated.txt"):
        path = out / filename
        content = api.read_text(path)
        api.write_text(path, content + "\n" + content.replace("RushDuel.", "RD."))
    api.write_constant_json(out / "constants.generated.json", list(constants.values()), metadata)
    api.write_text(out / "constant_english.generated.lua", "\n".join([
        "-- Rush Duel editor tooltips only. Do not load into a standard duel.",
        *[f"{doc.name} = {doc.value} -- {doc.comment_en}" for doc in constants.values()], "",
    ]))
    base = out / "wiki" / "api"
    index = ["# Rush Duel helper reference", "", metadata["note"], "",
             f"{len(docs)} public helpers; {len(reviewed)} have reviewed English contracts. Other entries show their pinned source and explicitly leave unreviewed types unspecified.", "",
             "Use `RushDuel.Name(...)` or the bootstrap alias `RD.Name(...)`.", "",
             "- [Rush constants](constants)", "- [All helpers](functions/)", ""]
    api.write_text(base / "index.md", "\n".join(index))
    grouped = defaultdict(list)
    for doc in docs:
        grouped[Path(doc.source_files[0].path).name].append(doc)
        source = doc.source_files[0]
        lines = [f"# {doc.name}", "", f"Alias: `RD.{doc.short_name}`. Requires the matching Rush Duel Lua bootstrap.", "",
                 "## Signature", "", "```lua", api.markdown_signature(doc), "```", "",
                 "## Description", "", *[prose(line) for line in doc.description_en], ""]
        if doc.english_status == "source_only" and doc.description_zh:
            lines.extend(["### Upstream source comment", "", "```text", *doc.description_zh, "```", ""])
        if doc.params:
            lines.extend(["## Parameters", ""])
            for param in doc.params:
                optional = " (optional)" if param.optional else ""
                lines.append(f"- `{param.name}` `{param.type}`{optional}: {prose(param.description) or 'Type and behavior are not yet reviewed; see the source.'}")
            lines.append("")
        lines.extend(["## Returns", ""])
        lines.extend([f"- `{ret.type}`: {prose(ret.description)}" for ret in doc.returns] or ["No return values."])
        if reviewed.get(doc.short_name, {}).get("example"):
            lines.extend(["", "## Example", "", "```lua", *reviewed[doc.short_name]["example"], "```"])
        lines.extend(["", "## Source", "", f"`{source.path}:{source.line}`", "", "```lua", snippets[doc.name], "```", ""])
        api.write_text(base / "functions" / "RushDuel" / f"{doc.short_name}.md", "\n".join(lines))
    all_lines = ["# Rush Duel helpers", "", "Public helpers from the pinned Rush Lua library. Internal underscore helpers are omitted.", ""]
    for filename, members in sorted(grouped.items()):
        all_lines.extend([f"## {filename}", ""])
        all_lines.extend(f"- [{doc.name}](RushDuel/{doc.short_name})" for doc in members)
        all_lines.append("")
    api.write_text(base / "functions" / "index.md", "\n".join(all_lines))
    api.write_text(base / "functions" / "RushDuel" / "index.md", "\n".join(all_lines).replace("](RushDuel/", "]("))
    constant_lines = ["# Rush Duel constants", "", "These values belong to the Rush bootstrap. `TYPE_LEGEND = 0x8` and `TYPE_MAXIMUM = 0x8000` overlap standard type bits; do not combine the two environments.", ""]
    for doc in constants.values():
        constant_lines.extend([f"## {doc.name}", "", f"`{doc.name} = {doc.value}`", "", prose(doc.comment_en), ""])
        if doc.comment_zh:
            constant_lines.extend(["Upstream comment:", "", "```text", doc.comment_zh, "```", ""])
    api.write_text(base / "constants.md", "\n".join(constant_lines))
    return len(docs), len(constants)
