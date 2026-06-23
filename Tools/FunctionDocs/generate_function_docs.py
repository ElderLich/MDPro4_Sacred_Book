#!/usr/bin/env python3
"""Generate YGOPro Lua API docs from local stubs and helper sources."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


DEFAULT_DATAEDITORX_DATA = Path(r"D:\Programs\GitHub\DataEditorX\DataEditorX\data")
DEFAULT_MDPRO3_LOCALES = Path(r"D:\Programs\GitHub\MDPro3_Data\Data\locales")
DEFAULT_YGOPRO_CORE = Path(r"D:\Programs\GitHub\ygopro-core")

FUNCTION_RE = re.compile(
    r"^\s*function\s+([A-Za-z_]\w*(?:[.:][A-Za-z_]\w*)?)\s*\(([^)]*)\)"
)
ASSIGNED_FUNCTION_RE = re.compile(
    r"^\s*([A-Za-z_]\w*(?:[.:][A-Za-z_]\w*)?)\s*=\s*function\s*\(([^)]*)\)"
)
LUA_FUNCTION_START_RE = re.compile(
    r"^\s*(?:local\s+)?function\s+[A-Za-z_]\w*(?:[.:][A-Za-z_]\w*)?\s*\("
    r"|^\s*[A-Za-z_]\w*(?:[.:][A-Za-z_]\w*)?\s*=\s*function\s*\("
)
BULLET_RE = re.compile(r"^.(?:[^\s]+\s+)*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)\s*\(")


TYPE_MAP = {
    "integer": "int",
    "boolean": "bool",
    "nil": "nil",
    "function": "function",
    "string": "string",
    "number": "number",
    "table": "table",
    "any": "any",
}

SOURCE_PRIORITY = {
    "core": 0,
    "def": 1,
    "utility": 2,
    "procedure": 3,
}

LIB_NAMESPACE = {
    "card": "Card",
    "effect": "Effect",
    "group": "Group",
    "duel": "Duel",
    "debug": "Debug",
}


@dataclass
class SourceRef:
    path: str
    line: int
    origin: str


@dataclass
class ParamDoc:
    name: str
    type: str = "any"
    optional: bool = False
    description: str = ""
    description_zh: str = ""


@dataclass
class ReturnDoc:
    type: str = "nil"
    description: str = ""
    description_zh: str = ""


@dataclass
class FunctionDoc:
    name: str
    namespace: str
    short_name: str
    params: list[ParamDoc]
    returns: list[ReturnDoc]
    description_zh: list[str] = field(default_factory=list)
    description_en: list[str] = field(default_factory=list)
    english_status: str = "missing"
    source_files: list[SourceRef] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    core_binding: bool = False
    core_handler: str = ""


@dataclass
class ConstantDoc:
    name: str
    value: str
    section: str
    comment_zh: str = ""
    comment_en: str = ""
    english_status: str = "missing"
    dataeditorx_value: str = ""
    dataeditorx_comment: str = ""
    old_value: str = ""
    old_comment: str = ""
    source_files: list[SourceRef] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def display_path(path: Path, workspace: Path) -> str:
    try:
        return str(path.resolve().relative_to(workspace.resolve())).replace("\\", "/")
    except ValueError:
        return str(path)


def split_args(raw: str) -> list[str]:
    if not raw.strip():
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def normalize_param_name(name: str) -> str:
    return name.strip().rstrip("?")


def clean_type(type_name: str) -> str:
    type_name = type_name.strip()
    if not type_name:
        return "any"
    parts = []
    for part in type_name.split("|"):
        opt = part.endswith("?")
        base = part.rstrip("?")
        base = TYPE_MAP.get(base, base)
        parts.append(base + ("?" if opt else ""))
    return "|".join(parts)


def infer_type_from_name(name: str) -> str:
    lname = name.lower().rstrip("?")
    if lname in {"c", "tc", "ec", "sc", "fc", "rc", "syncard", "xyzc", "fcard"}:
        return "Card"
    if lname in {"g", "mg", "sg", "eg", "targets", "cards"} or lname.endswith("g"):
        return "Group"
    if lname in {
        "tp",
        "ep",
        "rp",
        "p",
        "player",
        "playerid",
        "count",
        "code",
        "event",
        "event_code_single",
        "flag",
        "id",
        "loc",
        "location",
        "race",
        "reason",
        "seq",
        "sequence",
        "setcode",
        "sumpos",
        "sump",
        "sumtype",
        "targetp",
        "type",
    }:
        return "int"
    if lname in {"events", "value"}:
        return "any"
    if lname in {"e", "re", "te", "se", "effect"} or lname.endswith("e"):
        return "Effect"
    if lname.startswith("is_") or lname in {"chk", "cancelable", "enable", "forced"}:
        return "bool"
    if lname in {"f", "filter", "func", "operation", "condition"} or lname.endswith("_func"):
        return "function"
    return "any"


def parse_param_annotation(rest: str) -> ParamDoc | None:
    parts = rest.split(None, 2)
    if len(parts) < 2:
        return None
    name = parts[0]
    type_name = parts[1]
    description = parts[2].strip() if len(parts) > 2 else ""
    optional = name.endswith("?") or "|nil" in type_name or type_name.endswith("?")
    return ParamDoc(
        name=normalize_param_name(name),
        type=clean_type(type_name),
        optional=optional,
        description=description,
    )


def parse_return_annotation(rest: str) -> ReturnDoc:
    parts = rest.split(None, 1)
    if not parts:
        return ReturnDoc()
    type_name = clean_type(parts[0])
    description = parts[1].strip() if len(parts) > 1 else ""
    return ReturnDoc(type=type_name, description=description)


def parse_comment_block(lines: list[str]) -> tuple[list[str], dict[str, ParamDoc], list[ReturnDoc], list[str]]:
    description: list[str] = []
    params: dict[str, ParamDoc] = OrderedDict()
    returns: list[ReturnDoc] = []
    tags: list[str] = []

    for raw in lines:
        text = raw.strip()
        if text.startswith("---@param"):
            doc = parse_param_annotation(text.removeprefix("---@param").strip())
            if doc:
                params[doc.name] = doc
            continue
        if text.startswith("---@return"):
            returns.append(parse_return_annotation(text.removeprefix("---@return").strip()))
            continue
        if text.startswith("---@"):
            tags.append(text[4:].strip())
            continue
        if text.startswith("---"):
            description.append(text[3:].strip())

    return description, params, returns, tags


def namespace_for(name: str) -> tuple[str, str]:
    if "." in name:
        namespace, short = name.rsplit(".", 1)
        return namespace, short
    if ":" in name:
        namespace, short = name.rsplit(":", 1)
        return namespace, short
    return "Global", name


def normalize_api_name(name: str) -> str:
    if name.startswith("aux."):
        return "Auxiliary." + name[4:]
    return name


def build_params(args: list[str], annotations: dict[str, ParamDoc]) -> list[ParamDoc]:
    params: list[ParamDoc] = []
    for arg in args:
        name = normalize_param_name(arg)
        ann = annotations.get(name) or annotations.get(arg)
        if ann:
            params.append(ann)
        else:
            params.append(ParamDoc(name=name, type=infer_type_from_name(name)))
    return params


def make_doc(name: str, args: list[str], comments: list[str], source: SourceRef) -> FunctionDoc:
    description, param_docs, returns, tags = parse_comment_block(comments)
    namespace, short = namespace_for(name)
    if not returns:
        returns = [ReturnDoc(type="nil")]
    aliases = ["aux." + short] if namespace == "Auxiliary" else []
    return FunctionDoc(
        name=name,
        namespace=namespace,
        short_name=short,
        params=build_params(args, param_docs),
        returns=returns,
        description_zh=[line for line in description if line],
        source_files=[source],
        aliases=aliases,
        tags=tags,
    )


def merge_doc(existing: FunctionDoc, new_doc: FunctionDoc) -> None:
    existing.source_files.extend(new_doc.source_files)
    for tag in new_doc.tags:
        if tag not in existing.tags:
            existing.tags.append(tag)
    if not existing.description_zh and new_doc.description_zh:
        existing.description_zh = new_doc.description_zh
    if (
        existing.core_binding
        and existing.description_zh
        and existing.description_zh[0].startswith("TODO document core binding")
        and new_doc.description_zh
        and not new_doc.core_binding
    ):
        existing.description_zh = new_doc.description_zh
    if existing.returns == [ReturnDoc(type="nil")] and new_doc.returns != [ReturnDoc(type="nil")]:
        existing.returns = new_doc.returns
    if not existing.params and new_doc.params:
        existing.params = new_doc.params
    if new_doc.core_binding:
        existing.core_binding = True
        existing.core_handler = new_doc.core_handler


def parse_lua_functions(path: Path, workspace: Path, origin: str) -> OrderedDict[str, FunctionDoc]:
    docs: OrderedDict[str, FunctionDoc] = OrderedDict()
    if not path.exists():
        return docs

    pending_comments: list[str] = []
    for line_number, raw in enumerate(read_text(path).splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("---"):
            pending_comments.append(raw)
            continue

        match = FUNCTION_RE.match(raw) or ASSIGNED_FUNCTION_RE.match(raw)
        if match:
            name = match.group(1).replace(":", ".")
            args = split_args(match.group(2))
            source = SourceRef(display_path(path, workspace), line_number, origin)
            doc = make_doc(name, args, pending_comments, source)
            if name in docs:
                merge_doc(docs[name], doc)
            else:
                docs[name] = doc
            pending_comments = []
            continue

        if stripped and not stripped.startswith("--"):
            pending_comments = []

    return docs


def parse_core_bindings(core_root: Path, workspace: Path) -> OrderedDict[str, FunctionDoc]:
    docs: OrderedDict[str, FunctionDoc] = OrderedDict()
    if not core_root.exists():
        return docs

    binding_re = re.compile(r'\{\s*"([^"]+)"\s*,\s*scriptlib::([A-Za-z_]\w*)\s*\}')
    lib_re = re.compile(r"static\s+const\s+struct\s+luaL_Reg\s+([a-z]+)lib\[\]\s*=")

    for file_name, namespace_key in [
        ("libcard.cpp", "card"),
        ("libeffect.cpp", "effect"),
        ("libgroup.cpp", "group"),
        ("libduel.cpp", "duel"),
        ("libdebug.cpp", "debug"),
    ]:
        path = core_root / file_name
        if not path.exists():
            continue
        active_namespace = LIB_NAMESPACE[namespace_key]
        in_lib = False
        for line_number, raw in enumerate(read_text(path).splitlines(), start=1):
            lib_match = lib_re.search(raw)
            if lib_match:
                active_namespace = LIB_NAMESPACE.get(lib_match.group(1), active_namespace)
                in_lib = True
                continue
            if in_lib and raw.strip().startswith("};"):
                in_lib = False
                continue
            if not in_lib:
                continue
            match = binding_re.search(raw)
            if not match:
                continue
            short_name, handler = match.groups()
            name = f"{active_namespace}.{short_name}"
            source = SourceRef(display_path(path, workspace), line_number, "core")
            docs[name] = FunctionDoc(
                name=name,
                namespace=active_namespace,
                short_name=short_name,
                params=[],
                returns=[ReturnDoc(type="nil")],
                description_zh=[f"TODO document core binding `{handler}`."],
                source_files=[source],
                tags=["core-binding"],
                core_binding=True,
                core_handler=handler,
            )
    return docs


def load_all_function_docs(workspace: Path, core_root: Path) -> OrderedDict[str, FunctionDoc]:
    sources = [
        ("def", workspace / "Define" / "def.lua"),
        ("utility", workspace / "Utilities" / "utility.lua"),
        ("procedure", workspace / "Utilities" / "procedure.lua"),
    ]
    all_docs: OrderedDict[str, FunctionDoc] = parse_core_bindings(core_root, workspace)
    for origin, path in sources:
        parsed = parse_lua_functions(path, workspace, origin)
        for name, doc in parsed.items():
            if name in all_docs:
                merge_doc(all_docs[name], doc)
            else:
                all_docs[name] = doc
    apply_core_doc_overrides(all_docs)
    apply_function_zh_overrides(all_docs)

    return OrderedDict(
        sorted(
            all_docs.items(),
            key=lambda item: (
                min(SOURCE_PRIORITY.get(src.origin, 99) for src in item[1].source_files),
                item[1].namespace,
                item[1].short_name.lower(),
            ),
        )
    )


def parse_bullet_file(path: Path) -> dict[str, list[str]]:
    records: dict[str, list[str]] = {}
    if not path.exists():
        return records

    current_name = ""
    current_lines: list[str] = []

    def flush() -> None:
        if current_name:
            records[current_name] = [line for line in current_lines if line.strip()]

    for line in read_text(path).splitlines():
        if line.startswith("●"):
            flush()
            current_lines = []
            match = BULLET_RE.search(line)
            current_name = match.group(1) if match else ""
            continue
        if current_name and line and not line.startswith("=") and not line.startswith("#"):
            current_lines.append(line.rstrip())
    flush()
    return records


FUNCTION_DOC_OVERRIDES_PATH = Path(__file__).with_name("function_doc_overrides.json")


def _override_lines(value: object) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("Function doc override text fields must be arrays of strings.")
    return [str(line) for line in value]


def _override_params(value: object) -> list[ParamDoc]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("Function doc override params must be an array.")
    params: list[ParamDoc] = []
    for raw in value:
        if not isinstance(raw, dict):
            raise ValueError("Function doc override param entries must be objects.")
        params.append(
            ParamDoc(
                name=str(raw.get("name", "")),
                type=str(raw.get("type", "any")),
                optional=bool(raw.get("optional", False)),
                description=str(raw.get("description", "")),
                description_zh=str(raw.get("description_zh", "")),
            )
        )
    return params


def _override_returns(value: object) -> list[ReturnDoc]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("Function doc override returns must be an array.")
    returns: list[ReturnDoc] = []
    for raw in value:
        if not isinstance(raw, dict):
            raise ValueError("Function doc override return entries must be objects.")
        returns.append(
            ReturnDoc(
                type=str(raw.get("type", "nil")),
                description=str(raw.get("description", "")),
                description_zh=str(raw.get("description_zh", "")),
            )
        )
    return returns


def load_function_doc_overrides(
    path: Path = FUNCTION_DOC_OVERRIDES_PATH,
) -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, dict[str, object]]]:
    payload = json.loads(read_text(path))
    raw_functions = payload.get("functions", {})
    if not isinstance(raw_functions, dict):
        raise ValueError("Function doc overrides must contain a functions object.")

    english: dict[str, list[str]] = {}
    chinese: dict[str, list[str]] = {}
    core: dict[str, dict[str, object]] = {}

    for name, raw_entry in raw_functions.items():
        if not isinstance(raw_entry, dict):
            raise ValueError(f"Function doc override for {name} must be an object.")

        summary_en = _override_lines(raw_entry.get("summary_en"))
        summary_zh = _override_lines(raw_entry.get("summary_zh"))
        if summary_en:
            english[str(name)] = summary_en
        if summary_zh:
            chinese[str(name)] = summary_zh

        if "params" in raw_entry or "returns" in raw_entry:
            core_summary_en = _override_lines(raw_entry.get("core_summary_en"))
            core_summary_zh = _override_lines(raw_entry.get("core_summary_zh"))
            core[str(name)] = {
                "params": _override_params(raw_entry.get("params")),
                "returns": _override_returns(raw_entry.get("returns")),
                "description": core_summary_en or summary_en,
                "description_zh": core_summary_zh or summary_zh or core_summary_en or summary_en,
            }

    return english, chinese, core


FUNCTION_EN_OVERRIDES, FUNCTION_ZH_OVERRIDES, CORE_DOC_OVERRIDES = load_function_doc_overrides()


FUNCTION_ANNOTATION_TRANSLATIONS = {
    "可能为空": "may be nil",
    "EFFECT_MUST_BE_FMATERIAL等": "for example, EFFECT_MUST_BE_FMATERIAL",
    "material_all 包含受EFFECT_EXTRA_FUSION_MATERIAL影响的卡": "material_all includes cards affected by EFFECT_EXTRA_FUSION_MATERIAL",
    "material_base 只取那些区域的卡": "material_base contains only cards from the requested locations",
    "不能为空": "cannot be nil when selecting materials",
    "已选的卡，可以从中取消选择": "already selected cards that can be unselected",
}


def translate_function_annotation(text: str) -> str:
    translated = text
    for source, replacement in FUNCTION_ANNOTATION_TRANSLATIONS.items():
        translated = translated.replace(source, replacement)
    return translated


def translate_function_annotations(docs: Iterable[FunctionDoc]) -> None:
    for doc in docs:
        doc.description_en = [translate_function_annotation(line) for line in doc.description_en]
        for param in doc.params:
            param.description = translate_function_annotation(param.description)
        for ret in doc.returns:
            ret.description = translate_function_annotation(ret.description)


def copy_params(params: list[ParamDoc]) -> list[ParamDoc]:
    return [
        ParamDoc(param.name, param.type, param.optional, param.description, param.description_zh)
        for param in params
    ]


def copy_returns(returns: list[ReturnDoc]) -> list[ReturnDoc]:
    return [ReturnDoc(ret.type, ret.description, ret.description_zh) for ret in returns]


def apply_core_doc_overrides(docs: dict[str, FunctionDoc]) -> None:
    for name, override in CORE_DOC_OVERRIDES.items():
        doc = docs.get(name)
        if not doc:
            continue
        doc.params = copy_params(override["params"])
        doc.returns = copy_returns(override["returns"])
        doc.description_zh = list(override.get("description_zh", override["description"]))
        if "core-doc-override" not in doc.tags:
            doc.tags.append("core-doc-override")


def apply_function_zh_overrides(docs: dict[str, FunctionDoc]) -> None:
    for name, description in FUNCTION_ZH_OVERRIDES.items():
        doc = docs.get(name)
        if not doc:
            continue
        doc.description_zh = list(description)
        if "manual-zh-doc" not in doc.tags:
            doc.tags.append("manual-zh-doc")


def normalize_bullet_records(records: dict[str, list[str]]) -> dict[str, list[str]]:
    normalized: dict[str, list[str]] = {}
    for name, lines in records.items():
        cleaned = clean_imported_description(lines)
        if cleaned:
            normalized[normalize_api_name(name)] = cleaned
    return normalized


def clean_imported_description(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped in {"Parameters:", "Returns:"} or stripped.startswith("Source:"):
            break
        cleaned.append(line)
    meaningful = [line.strip() for line in cleaned if line.strip()]
    if not meaningful or meaningful[0] in {"TODO document.", "TODO translate."}:
        return []
    return cleaned


def attach_english(
    docs: Iterable[FunctionDoc],
    english_sources: list[tuple[str, dict[str, list[str]]]],
) -> None:
    normalized_sources = [
        (status, normalize_bullet_records(records))
        for status, records in english_sources
    ]

    for doc in docs:
        if doc.name in FUNCTION_EN_OVERRIDES:
            doc.description_en = FUNCTION_EN_OVERRIDES[doc.name]
            doc.english_status = "translated_exact"
            continue

        candidates = [doc.name]
        if doc.namespace == "Auxiliary":
            candidates.append("aux." + doc.short_name)
        if doc.namespace == "aux":
            candidates.append("Auxiliary." + doc.short_name)
        candidates = [normalize_api_name(candidate) for candidate in candidates]

        matched = False
        for status, records in normalized_sources:
            for candidate in candidates:
                if candidate in records:
                    doc.description_en = records[candidate]
                    doc.english_status = status
                    matched = True
                    break
            if matched:
                break
        if matched:
            continue

        if doc.description_zh and all(not re.search(r"[\u3400-\u9fff]", line) for line in doc.description_zh):
            doc.description_en = doc.description_zh
            doc.english_status = "existing_english"
            continue

        if doc.description_zh:
            doc.description_en = ["TODO translate.", *doc.description_zh]
            doc.english_status = "missing_translation"
        else:
            doc.description_en = ["TODO document."]
            doc.english_status = "missing_documentation"


def format_param(param: ParamDoc) -> str:
    type_name = clean_type(param.type)
    if param.name == "...":
        text = f"... {type_name}"
    else:
        text = f"{type_name} {param.name}"
    return f"[{text}]" if param.optional else text


def format_returns(returns: list[ReturnDoc]) -> str:
    types = [clean_type(ret.type) for ret in returns if clean_type(ret.type) not in {"nil", ""}]
    return ",".join(types) if types else "void"


def lua_signature(doc: FunctionDoc) -> str:
    params = ", ".join(format_param(param) for param in doc.params)
    return f"{format_returns(doc.returns)} {doc.name}({params})"

FUNCTION_RELATED_GUIDES = {
    "Duel.ChangePosition": ["Card.IsCanChangePosition", "Card.IsPosition"],
    "Duel.Destroy": ["Card.IsDestructable", "Duel.SetOperationInfo", "Duel.SendtoGrave"],
    "Duel.Equip": ["Card.CheckEquipTarget", "Duel.EquipComplete", "Auxiliary.AddEquipSpellEffect"],
    "Duel.EquipComplete": ["Duel.Equip"],
    "Duel.GetControl": ["Card.IsControler", "Duel.SwapControl", "Duel.CheckLocation"],
    "Duel.MoveToField": ["Duel.GetLocationCount", "Duel.GetSZoneCount", "Duel.ReturnToField"],
    "Duel.Overlay": ["Duel.GetOverlayGroup", "Duel.RemoveOverlayCard", "Card.GetOverlayGroup"],
    "Duel.Release": ["Card.IsReleasable", "Duel.GetReleaseGroup", "Duel.SelectReleaseGroupEx"],
    "Duel.Remove": ["Card.IsAbleToRemove", "Duel.ReturnToField", "Duel.SetOperationInfo"],
    "Duel.SendtoDeck": ["Card.IsAbleToDeck", "Duel.SetOperationInfo", "Auxiliary.PlaceCardsOnDeckTop"],
    "Duel.SendtoGrave": ["Card.IsAbleToGrave", "Duel.SetOperationInfo", "Duel.Destroy"],
    "Duel.SendtoHand": ["Card.IsAbleToHand", "Duel.SetOperationInfo"],
    "Duel.SpecialSummon": ["Card.IsCanBeSpecialSummoned", "Duel.SpecialSummonStep", "Duel.SpecialSummonComplete", "Duel.GetLocationCount"],
    "Duel.SpecialSummonComplete": ["Duel.SpecialSummonStep", "Duel.SpecialSummon"],
    "Duel.SpecialSummonStep": ["Duel.SpecialSummonComplete", "Card.IsCanBeSpecialSummoned"],
    "Effect.SetAbsoluteRange": ["Effect.SetTargetRange", "Effect.SetProperty"],
    "Effect.SetCategory": ["Duel.SetOperationInfo", "Duel.GetOperationInfo"],
    "Effect.SetCode": ["Effect.SetType", "Effect.SetRange"],
    "Effect.SetCondition": ["Effect.SetCost", "Effect.SetTarget", "Effect.SetOperation"],
    "Effect.SetCost": ["Duel.CheckLPCost", "Duel.PayLPCost", "Effect.IsCostChecked"],
    "Effect.SetCountLimit": ["Effect.CheckCountLimit", "Effect.UseCountLimit"],
    "Effect.SetDescription": ["Auxiliary.Stringid", "Duel.Hint"],
    "Effect.SetOperation": ["Effect.SetTarget", "Duel.GetFirstTarget", "Duel.GetTargetsRelateToChain"],
    "Effect.SetProperty": ["Effect.IsHasProperty", "Effect.SetTargetRange"],
    "Effect.SetRange": ["Card.RegisterEffect", "Effect.SetTargetRange", "Duel.GetLocationCount"],
    "Effect.SetReset": ["Card.RegisterEffect", "Effect.Reset"],
    "Effect.SetTarget": ["Duel.IsExistingTarget", "Duel.SelectTarget", "Duel.SetOperationInfo"],
    "Effect.SetTargetRange": ["Effect.SetRange", "Effect.SetAbsoluteRange", "Effect.SetProperty"],
    "Effect.SetType": ["Effect.SetCode", "Effect.SetRange", "Card.RegisterEffect"],
    "Effect.SetValue": ["Effect.GetValue", "Effect.SetCode"],
}


FUNCTION_DETAIL_GUIDES = {
    "Duel.IsExistingMatchingCard": [
        "Use this for activation checks that only need to know whether matching cards exist.",
        "",
        "The filter receives each candidate card first, followed by any extra arguments after `ex`:",
        "",
        "```lua",
        "function s.filter(c,e,tp)",
        "    return c:IsFaceup() and c:IsCanBeSpecialSummoned(e,0,tp,false,false)",
        "end",
        "",
        "if chk==0 then",
        "    return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_GRAVE,0,1,nil,e,tp)",
        "end",
        "```",
        "",
        "Use `Duel.IsExistingTarget` instead when the card must become an official target of the activating effect.",
    ],
    "Duel.SelectMatchingCard": [
        "Use this when the selected cards do not need to become official effect targets.",
        "",
        "A common pattern is to check with `Duel.IsExistingMatchingCard`, select with `Duel.SelectMatchingCard`, then move or modify the selected group during the operation:",
        "",
        "```lua",
        "local g=Duel.SelectMatchingCard(tp,s.filter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)",
        "if #g>0 then",
        "    Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)",
        "end",
        "```",
        "",
        "Use `Duel.SelectTarget` in a Target callback when later resolution must re-check `tc:IsRelateToEffect(e)`.",
    ],
    "Duel.IsExistingTarget": [
        "Use this in a Target callback when the effect text chooses target cards.",
        "",
        "`Duel.IsExistingTarget` is like `Duel.IsExistingMatchingCard`, but it also checks whether each candidate can become a target of the current effect. That matters for cards unaffected by targeting, cards protected by effects, and target restrictions.",
        "",
        "```lua",
        "function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)",
        "    if chkc then return chkc:IsOnField() and s.filter(chkc) end",
        "    if chk==0 then",
        "        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)",
        "    end",
        "    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)",
        "end",
        "```",
    ],
    "Duel.SelectTarget": [
        "Use this in the Target callback of an activated effect that targets cards.",
        "",
        "The selected cards are saved as the Chain's targets. For one target, read it with `Duel.GetFirstTarget` and check `tc:IsRelateToEffect(e)` before applying the effect.",
        "For several targets, use `Duel.GetTargetsRelateToChain` to get the target group that is still related to the resolving Chain.",
        "",
        "```lua",
        "function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)",
        "    if chkc then return chkc:IsOnField() and s.filter(chkc) end",
        "    if chk==0 then return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil) end",
        "    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)",
        "    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)",
        "end",
        "",
        "function s.operation(e,tp,eg,ep,ev,re,r,rp)",
        "    local tc=Duel.GetFirstTarget()",
        "    if tc and tc:IsRelateToEffect(e) then",
        "        Duel.Destroy(tc,REASON_EFFECT)",
        "    end",
        "end",
        "```",
    ],
    "Duel.GetFirstTarget": [
        "Use this during resolution when the effect selected exactly one target card.",
        "",
        "Always check that the returned card still exists and is still related to the resolving effect before moving, destroying, equipping, or changing it:",
        "",
        "```lua",
        "local tc=Duel.GetFirstTarget()",
        "if tc and tc:IsRelateToEffect(e) then",
        "    Duel.SendtoHand(tc,nil,REASON_EFFECT)",
        "end",
        "```",
        "",
        "For multiple targets, use `Duel.GetTargetsRelateToChain()` when you need the group of targets that are still related to the resolving Chain.",
    ],
    "Duel.GetMatchingGroup": [
        "Use this when you need to keep or further process all matching cards rather than only checking if they exist.",
        "",
        "`s` and `o` are location masks from `player`'s point of view. For example, `LOCATION_MZONE,0` means that player's Monster Zone, while `0,LOCATION_MZONE` means the opponent's Monster Zone.",
        "",
        "```lua",
        "local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)",
        "if #g>0 then",
        "    Duel.HintSelection(g)",
        "end",
        "```",
    ],
    "Duel.SpecialSummon": [
        "`targets` can be one Card or a Group. The return value is the number of cards actually Special Summoned, so check it if later steps depend on success.",
        "",
        "`sumplayer` is the player performing the Summon. `target_player` is the player whose field receives the monster. For most simple effects, both are `tp`.",
        "",
        "```lua",
        "local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)",
        "if #g>0 then",
        "    Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)",
        "end",
        "```",
        "",
        "Use `nocheck=true` only when the effect intentionally ignores the monster's usual Summoning condition. Use `nolimit=true` only when the effect intentionally ignores the proper Summon/revive limit.",
    ],
    "Duel.ChangePosition": [
        "Use this when an effect changes battle position during resolution.",
        "",
        "The short form changes every target to the same position:",
        "",
        "```lua",
        "if tc:IsRelateToEffect(e) then",
        "    Duel.ChangePosition(tc,POS_FACEUP_DEFENSE)",
        "end",
        "```",
        "",
        "For mixed current positions, pass the destination for face-up Attack, face-down Attack, face-up Defense, and face-down Defense in that order. MDPro3's core does not read the old seventh `setavailable` argument.",
    ],
    "Duel.Destroy": [
        "Use this during resolution after checking that the target is still related to the effect.",
        "",
        "The return value is important. It is 0 when no card was actually destroyed, for example because the card left the expected place or could not be destroyed.",
        "",
        "```lua",
        "local tc=Duel.GetFirstTarget()",
        "if tc and tc:IsRelateToEffect(e) and Duel.Destroy(tc,REASON_EFFECT)>0 then",
        "    -- follow-up that requires successful destruction",
        "end",
        "```",
        "",
        "Use `Duel.SetOperationInfo(0,CATEGORY_DESTROY,...)` in the Target callback when the destruction is known before resolution.",
    ],
    "Duel.Equip": [
        "Use this after both the Equip Card and the monster it will equip to are still valid.",
        "",
        "A self-equip effect usually creates an Equip Limit after the equip succeeds so the card stays attached only to the intended monster:",
        "",
        "```lua",
        "local tc=Duel.GetFirstTarget()",
        "local c=e:GetHandler()",
        "if tc and tc:IsRelateToEffect(e) and c:IsRelateToEffect(e) and Duel.Equip(tp,c,tc) then",
        "    local e1=Effect.CreateEffect(c)",
        "    e1:SetType(EFFECT_TYPE_SINGLE)",
        "    e1:SetCode(EFFECT_EQUIP_LIMIT)",
        "    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)",
        "    e1:SetValue(function(e,ec) return ec==tc end)",
        "    e1:SetReset(RESET_EVENT+RESETS_STANDARD)",
        "    c:RegisterEffect(e1)",
        "end",
        "```",
        "",
        "When several cards are equipped as one procedure with `is_step=true`, call `Duel.EquipComplete()` after the final successful step.",
    ],
    "Duel.EquipComplete": [
        "Use this only after one or more `Duel.Equip(..., true)` step equips.",
        "",
        "It enables the equipped cards and raises the equip events as one completed procedure:",
        "",
        "```lua",
        "if Duel.Equip(tp,ec,tc,true,true) then",
        "    -- more step equips can be added here",
        "    Duel.EquipComplete()",
        "end",
        "```",
    ],
    "Duel.GetControl": [
        "Use this when an effect takes control of cards.",
        "",
        "For temporary control, pass a phase and count. For permanent control, omit those arguments. If you only need to restrict the destination zone, pass `0,0,zone` before the zone mask.",
        "",
        "```lua",
        "local tc=Duel.GetFirstTarget()",
        "if tc and tc:IsRelateToEffect(e) then",
        "    Duel.GetControl(tc,tp,PHASE_END,1)",
        "end",
        "```",
        "",
        "The return value is the number of cards that actually changed control, so use `>0` when later logic depends on success.",
    ],
    "Duel.MoveToField": [
        "Use this for effects that place an existing card directly onto the field, such as moving a card to the Field Zone, Pendulum Zone, or Spell & Trap Zone.",
        "",
        "```lua",
        "if tc:IsRelateToEffect(e) then",
        "    Duel.MoveToField(tc,tp,tp,LOCATION_SZONE,POS_FACEUP,true)",
        "end",
        "```",
        "",
        "`enable=true` applies the moved card's field effects immediately. The optional `zone` mask restricts which zone can be used.",
    ],
    "Duel.Overlay": [
        "Use this when a procedure or effect turns cards into Xyz Materials under an Xyz Monster.",
        "",
        "The first argument is the Xyz Monster that will receive the materials. The second argument can be one Card or a Group:",
        "",
        "```lua",
        "Duel.Overlay(xyzc,mg)",
        "```",
        "",
        "Leave `adjust` omitted for normal scripts. Pass `false` only inside a larger procedure that will adjust the field afterward.",
    ],
    "Duel.Release": [
        "Use this to Tribute/Release cards as a cost, effect, or Summon procedure.",
        "",
        "When selecting a release cost, select cards that are legal to release, then release them with the same reason used for the cost:",
        "",
        "```lua",
        "local g=Duel.SelectReleaseGroupEx(tp,nil,1,1,REASON_COST,false,nil)",
        "if #g>0 then",
        "    Duel.Release(g,REASON_COST)",
        "end",
        "```",
        "",
        "The return value is the number of cards actually released.",
    ],
    "Duel.Remove": [
        "Use this for banishing cards. The second argument is the banished position, usually `POS_FACEUP` or `POS_FACEDOWN`.",
        "",
        "```lua",
        "if c:IsRelateToEffect(e) then",
        "    Duel.Remove(c,POS_FACEUP,REASON_EFFECT)",
        "end",
        "```",
        "",
        "For temporary banish effects, scripts commonly include `REASON_TEMPORARY`; those cards can later be returned with `Duel.ReturnToField`.",
    ],
    "Duel.SendtoDeck": [
        "Use this for returning cards to the Main Deck or Extra Deck.",
        "",
        "`player` can be nil for the normal return destination. `seq` controls placement: `SEQ_DECKTOP`, `SEQ_DECKBOTTOM`, or `SEQ_DECKSHUFFLE`.",
        "",
        "```lua",
        "if #g>0 then",
        "    Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)",
        "end",
        "```",
        "",
        "Check the return value when a later part of the effect depends on a card actually reaching the Deck or Extra Deck.",
    ],
    "Duel.SendtoGrave": [
        "Use this for sending cards to the Graveyard by effect, cost, discard, or material handling.",
        "",
        "```lua",
        "if #g>0 then",
        "    Duel.SendtoGrave(g,REASON_EFFECT)",
        "end",
        "```",
        "",
        "This is not the same as destroying. A card sent to the Graveyard by `Duel.SendtoGrave` was not destroyed unless the reason and prior action also say it was destroyed.",
    ],
    "Duel.SendtoHand": [
        "Use this for adding or returning cards to the hand.",
        "",
        "Pass nil for `player` when the card should go to its normal return destination. Pass a specific player only when the effect explicitly sends the card to that player's hand.",
        "",
        "```lua",
        "if Duel.SendtoHand(sg,nil,REASON_EFFECT)>0 then",
        "    Duel.ConfirmCards(1-tp,sg)",
        "end",
        "```",
        "",
        "When the card came from a hidden location and must be shown, reveal the result with `Duel.ConfirmCards` after it reaches the hand.",
    ],
    "Duel.SpecialSummonComplete": [
        "Use this after a batch of successful `Duel.SpecialSummonStep` calls.",
        "",
        "```lua",
        "if Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then",
        "    Duel.SpecialSummonComplete()",
        "end",
        "```",
        "",
        "Without the complete call, the step Summons do not finish their event handling correctly.",
    ],
    "Duel.SpecialSummonStep": [
        "Use this only for procedures that need to Special Summon cards one at a time before raising the final Summon events.",
        "",
        "Every batch must end with `Duel.SpecialSummonComplete`. For ordinary effects that just Special Summon one Card or Group, use `Duel.SpecialSummon` instead.",
    ],
    "Card.IsCanBeSpecialSummoned": [
        "Use this in activation checks before selecting a monster to Special Summon.",
        "",
        "The parameters should match the later `Duel.SpecialSummon` call as closely as possible: same effect, Summon type, Summon player, target player, position, and zone restrictions.",
        "",
        "```lua",
        "function s.spfilter(c,e,tp)",
        "    return c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,tp)",
        "end",
        "```",
        "",
        "This is only a legality check. It does not reserve a zone or Summon the card.",
    ],
    "Effect.SetType": [
        "Use `SetType` near the start of an effect definition. It decides whether the effect is activated, continuous, single-card, field-wide, trigger, ignition, or Quick.",
        "",
        "A common activated ignition effect skeleton looks like this:",
        "",
        "```lua",
        "local e1=Effect.CreateEffect(c)",
        "e1:SetDescription(aux.Stringid(id,0))",
        "e1:SetCategory(CATEGORY_DESTROY)",
        "e1:SetType(EFFECT_TYPE_IGNITION)",
        "e1:SetRange(LOCATION_MZONE)",
        "e1:SetCountLimit(1,id)",
        "e1:SetTarget(s.destg)",
        "e1:SetOperation(s.desop)",
        "c:RegisterEffect(e1)",
        "```",
        "",
        "MDPro3 normalizes some type combinations. Spell/Trap activation effects become field activation effects and receive the usual hand/Spell & Trap/Field Zone activation range. Flip Effects are converted to `EVENT_FLIP` handling. Ignition and Quick effects gain field behavior internally.",
    ],
    "Effect.SetCode": [
        "`SetCode` means different things depending on the effect type.",
        "",
        "For trigger effects, it is usually the event that makes the effect eligible to activate:",
        "",
        "```lua",
        "e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)",
        "e1:SetCode(EVENT_SUMMON_SUCCESS)",
        "```",
        "",
        "For continuous or single effects, it is usually the effect code being applied:",
        "",
        "```lua",
        "e1:SetType(EFFECT_TYPE_SINGLE)",
        "e1:SetCode(EFFECT_UPDATE_ATTACK)",
        "e1:SetValue(500)",
        "```",
        "",
        "Choose the code to match the type. A valid callback with the wrong event or effect code will still feel like it never works.",
    ],
    "Effect.SetProperty": [
        "Use `SetProperty` for flags that change targeting, timing, visibility, and activation rules.",
        "",
        "For targeting effects, `EFFECT_FLAG_CARD_TARGET` should be paired with `Duel.SelectTarget` in the Target callback:",
        "",
        "```lua",
        "e1:SetProperty(EFFECT_FLAG_CARD_TARGET)",
        "e1:SetTarget(s.target)",
        "```",
        "",
        "Other common flags include `EFFECT_FLAG_DELAY` for missed-timing-sensitive triggers, `EFFECT_FLAG_DAMAGE_STEP` for effects that can activate in the Damage Step, and `EFFECT_FLAG_CANNOT_DISABLE` for rules or equip limits that should not be negated normally.",
    ],
    "Effect.SetRange": [
        "`SetRange` tells the engine where the handler must be for this effect to apply or be activated.",
        "",
        "For an ignition effect that can be activated while the monster is face-up on the field:",
        "",
        "```lua",
        "e1:SetType(EFFECT_TYPE_IGNITION)",
        "e1:SetRange(LOCATION_MZONE)",
        "```",
        "",
        "For a Graveyard trigger or ignition effect, use `LOCATION_GRAVE`. For a continuous field effect, `SetRange` is the handler's location, while `SetTargetRange` describes which cards or players are affected.",
    ],
    "Effect.SetTargetRange": [
        "For field effects, target range decides which side and location the effect can apply to.",
        "",
        "```lua",
        "e1:SetType(EFFECT_TYPE_FIELD)",
        "e1:SetCode(EFFECT_UPDATE_ATTACK)",
        "e1:SetRange(LOCATION_MZONE)",
        "e1:SetTargetRange(LOCATION_MZONE,0)",
        "```",
        "",
        "With normal range handling, the first value is the handler controller's side and the second value is the opponent's side. `SetTargetRange` clears the absolute-target flag. Use `Effect.SetAbsoluteRange` when the ranges must mean player 0 and player 1 regardless of who controls the handler.",
        "",
        "For Special Summon procedure effects using `EFFECT_FLAG_SPSUM_PARAM`, these fields store the Summon destination player and allowed position instead of card locations.",
    ],
    "Effect.SetAbsoluteRange": [
        "Use this for field effects whose affected side must be fixed to player 0/player 1 instead of relative to the handler's controller.",
        "",
        "```lua",
        "e1:SetType(EFFECT_TYPE_FIELD)",
        "e1:SetCode(EFFECT_CANNOT_ATTACK)",
        "e1:SetRange(LOCATION_MZONE)",
        "e1:SetAbsoluteRange(tp,0,LOCATION_MZONE)",
        "```",
        "",
        "The core stores the ranges with `EFFECT_FLAG_ABSOLUTE_TARGET` set. If `playerid` is 1, it swaps `s_range` and `o_range` internally so the final effect still points at the intended absolute player.",
    ],
    "Effect.SetValue": [
        "`SetValue` supplies the amount, flag, card code, or callback required by the effect code.",
        "",
        "Simple stat changes usually use a number:",
        "",
        "```lua",
        "e1:SetCode(EFFECT_UPDATE_ATTACK)",
        "e1:SetValue(500)",
        "```",
        "",
        "Some effect codes need a function instead:",
        "",
        "```lua",
        "e1:SetCode(EFFECT_EQUIP_LIMIT)",
        "e1:SetValue(function(e,c) return c==e:GetLabelObject() end)",
        "```",
        "",
        "When a function is supplied, the core marks the effect as using a function value. Replacing it with a number or boolean clears that function-value flag.",
    ],
    "Effect.SetReset": [
        "`SetReset` controls when a temporary effect disappears.",
        "",
        "Card-bound effects usually reset when the card leaves normal field relation:",
        "",
        "```lua",
        "e1:SetReset(RESET_EVENT+RESETS_STANDARD)",
        "```",
        "",
        "Phase resets take an optional count:",
        "",
        "```lua",
        "e1:SetReset(RESET_PHASE+PHASE_END,2)",
        "```",
        "",
        "If the count is omitted or 0, MDPro3 stores 1. If a phase reset does not specify `RESET_SELF_TURN` or `RESET_OPPO_TURN`, the core adds both turn flags.",
    ],
    "Effect.SetCountLimit": [
        "Use `SetCountLimit` for once-per-turn and shared-count restrictions.",
        "",
        "A normal hard once per turn usually uses the card id as the shared code:",
        "",
        "```lua",
        "e1:SetCountLimit(1,id)",
        "```",
        "",
        "Effects with the same nonzero code share the same count. Special flags such as `EFFECT_COUNT_CODE_OATH`, `EFFECT_COUNT_CODE_DUEL`, `EFFECT_COUNT_CODE_SINGLE`, and `EFFECT_COUNT_CODE_CHAIN` change how that count is scoped. If `count` is 0, MDPro3 stores it as 1.",
    ],
    "Effect.SetCondition": [
        "Conditions answer whether the effect can apply or be activated in the current context.",
        "",
        "Keep condition callbacks side-effect free. They may be called while the engine is only checking legality:",
        "",
        "```lua",
        "function s.spcon(e,tp,eg,ep,ev,re,r,rp)",
        "    return e:GetHandler():IsSummonType(SUMMON_TYPE_SPECIAL)",
        "end",
        "",
        "e1:SetCondition(s.spcon)",
        "```",
        "",
        "For activated effects, costs and targets still get their own legality checks. The condition should describe the timing or state requirement that belongs to the effect itself.",
    ],
    "Effect.SetCost": [
        "Cost callbacks usually have two phases. When `chk==0`, only answer whether the cost can be paid. When `chk` is not 0, actually pay the cost.",
        "",
        "```lua",
        "function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)",
        "    if chk==0 then return Duel.CheckLPCost(tp,1000) end",
        "    Duel.PayLPCost(tp,1000)",
        "end",
        "```",
        "",
        "Do not perform irreversible actions during the `chk==0` check. The engine may call that branch just to test activation legality.",
    ],
    "Effect.SetTarget": [
        "Target callbacks do two jobs for activated effects: answer activation legality during `chk==0`, then record targets and operation information when activation is accepted.",
        "",
        "```lua",
        "function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)",
        "    if chkc then return chkc:IsOnField() and chkc:IsControler(1-tp) end",
        "    if chk==0 then",
        "        return Duel.IsExistingTarget(aux.TRUE,tp,0,LOCATION_ONFIELD,1,nil)",
        "    end",
        "    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)",
        "    Duel.SelectTarget(tp,aux.TRUE,tp,0,LOCATION_ONFIELD,1,1,nil)",
        "    Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,1-tp,LOCATION_ONFIELD)",
        "end",
        "```",
        "",
        "Use `Duel.SelectTarget` for cards that are official targets. Use `Duel.SetOperationInfo` so chained cards can see what the effect is expected to do.",
    ],
    "Effect.SetOperation": [
        "The operation callback performs the effect when the Chain resolves.",
        "",
        "For targeted cards, retrieve the target and re-check that it is still related to the resolving effect before applying the action:",
        "",
        "```lua",
        "function s.operation(e,tp,eg,ep,ev,re,r,rp)",
        "    local tc=Duel.GetFirstTarget()",
        "    if tc and tc:IsRelateToEffect(e) then",
        "        Duel.Destroy(tc,REASON_EFFECT)",
        "    end",
        "end",
        "```",
        "",
        "Passing nil to `SetOperation` clears the operation. That is occasionally useful for effects whose category or target data is enough and no resolution callback is needed.",
    ],
    "Effect.SetCategory": [
        "Categories tell the engine and response checks what kind of action the effect may perform.",
        "",
        "```lua",
        "e1:SetCategory(CATEGORY_DESTROY+CATEGORY_TOHAND)",
        "```",
        "",
        "The category is not the actual operation. If the affected cards, player, or count are known during targeting, also call `Duel.SetOperationInfo` in the Target callback.",
    ],
    "Effect.SetDescription": [
        "Descriptions are integer string ids, not raw text.",
        "",
        "Most card scripts use `aux.Stringid(id,n)` to point at the nth string for that card:",
        "",
        "```lua",
        "e1:SetDescription(aux.Stringid(id,0))",
        "```",
        "",
        "Descriptions are commonly shown for optional triggers, selectable effects, and effects registered to Spell/Trap activations.",
    ],
    "Card.IsCode": [
        "Use this in filters when a card must specifically be one or more card IDs.",
        "",
        "```lua",
        "function s.matfilter(c)",
        "    return c:IsCode(89631139,23995346)",
        "end",
        "```",
        "",
        "This checks the card's current code and alternate code, so copied or changed-code effects can matter.",
    ],
    "Group.Filter": [
        "Use this when you already have a Group and want a smaller Group from it.",
        "",
        "```lua",
        "local g=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)",
        "local fg=g:Filter(Card.IsFaceup,nil)",
        "```",
        "",
        "Extra arguments after `ex` are passed to the filter after the card. The original Group is not destroyed; the function returns a new Group.",
    ],
    "Group.Select": [
        "Use this when you already built the candidate Group and only need the player to choose from it.",
        "",
        "```lua",
        "local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_GRAVE,0,nil)",
        "Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)",
        "local sg=g:Select(tp,1,1,nil)",
        "Duel.SendtoHand(sg,nil,REASON_EFFECT)",
        "```",
        "",
        "If you still need to filter while selecting, use `Group.FilterSelect` or `Duel.SelectMatchingCard` instead.",
    ],
    "Group.IsExists": [
        "Use this to check whether a Group contains enough cards with a property.",
        "",
        "```lua",
        "if g:IsExists(Card.IsRace,1,nil,RACE_DRAGON) then",
        "    -- at least one Dragon is in g",
        "end",
        "```",
        "",
        "The `count` parameter is useful for requirements such as \"2 or more monsters with different names\" once the filter captures the condition you need.",
    ],
    "Group.GetFirst": [
        "Use `GetFirst`/`GetNext` to iterate through a Group when helper iterators are not available.",
        "",
        "```lua",
        "local tc=g:GetFirst()",
        "while tc do",
        "    -- work with tc",
        "    tc=g:GetNext()",
        "end",
        "```",
        "",
        "`GetFirst` resets the Group's internal pointer. Starting a second iteration on the same Group resets that pointer again.",
    ],
    "Group.GetNext": [
        "`GetNext` belongs to the `GetFirst` iteration pattern. It advances the same internal pointer and returns nil after the final card.",
        "",
        "```lua",
        "for tc in aux.Next(g) do",
        "    -- aux.Next wraps GetFirst/GetNext",
        "end",
        "```",
        "",
        "When you only need the number of cards, use `#g` or `g:GetCount()` instead of iterating.",
    ],
}


FUNCTION_GUIDE_ZH = [
    "###############################################",
    "# 脚本中用到的数据类型为以下几类：",
    "# int:\t\t整数类型",
    "# bool:\t\t布尔类型(true 或者 false)",
    "# string:\t字符串",
    "# function:\t函数",
    "# Card:\t\t卡片类",
    "# Effect:\t效果类",
    "# Group:\t卡片组类",
    "# table:\t表类型",
    "# nil:\t\t空类型，也表示空的变量",
    "# any:\t\t任意类型",
    "# 为方便说明，采用类似C的函数表示方法说明",
    "# []表示有默认值可省略的参数",
    "# 只说明有意义的nil类型参数或返回值",
    "#",
    "# 注：关于过滤条件函数",
    "#  过滤条件函数是指第一个参数是Card类型，并且返回值是boolean的函数。此函数用于在一些获取满足条件的卡片组的过滤函数中重复调用。过滤条件函数可以有不定的参数，第二个开始的参数从过滤函数的额外参数获得。举例：",
    "# function sample_filter(c, atk, def)",
    "# \treturn c:GetAttack()>=atk and c:GetDefense()>=def",
    "# end",
    "# 此函数对于一张卡c，如果攻击力>=atk并且守备力>=def则返回true，否则返回false",
    "# g=Duel.GetFieldGroup(0,LOCATION_HAND,0) --获取玩家1的手卡",
    "# fg=g:Filter(sample_filter,nil,1000,500) --从g中筛选攻击力>=1000并且守备>=500的卡",
    "# Group.Filter只需要3个参数，第4个参数开始为额外参数，额外的参数会传给sample_filter",
    "#",
    "# 注：关于指定位置",
    "# 一些函数可以获取指定位置的卡，通过三个参数指定 int player, int s, int o",
    "# s指对玩家player来说的己方的位置，o指对玩家player来说的对方的位置",
    "# 比如Duel.GetFieldGroup(0,LOCATION_GRAVE,LOCATION_MZONE)",
    "# 返回玩家0墓地和玩家1的怪兽区的所有卡",
    "#",
    "# 注：关于描述",
    "# 脚本系统并不是直接使用字符串显示提示文字，而是由系统通过一个整数(int desc)查找相应的描述",
    "# 对于desc<2048，系统在string.conf里面寻找，其中一些常用的数字(通常是提示选择的文字)在constant.lua中有记录",
    "# 对于desc>10000，系统在卡片数据库中寻找描述，通常使用aux.Stringid()函数指定",
    "#",
    "#●void Duel.ReplaceAttacker(Card c)",
    "#用c代替当前攻击的卡进行伤害阶段（此函数已不存在）",
    "#●void Duel.ReplaceAttackTarget(Card c)",
    "#(预留）（函数不存在）",
    "#",
    "#",
    "# 区域相关：",
    "# 自己场上从左往右，序号依次是0~4，额外怪兽区是5~6，0x7f则表示全部主怪兽区+额外怪兽区",
    "# 获取的区域值zone是以2为底、区号为次幂的数，所以要获取正确的区号，需要做对数 math.log(zone,2)",
    "# 涉及到对方的区域，则需要把对方的值左移16位",
    "#",
    "# 换成二进制比较好直观理解：（空格是为了方便分辨是第几位）",
    "#",
    "# 0x7f = 0111 1111",
    "# 把它从低位开始倒序排，就是1111 1110，前5个就代表自己的5个主要怪兽区，第6个就是左边的额外怪兽区，第7个是右边的额外怪兽区",
    "# (0)= 1  = 0x1  = 0000 0001",
    "# (1)= 2  = 0x2  = 0000 0010",
    "# (2)= 4  = 0x4  = 0000 0100",
    "# (3)= 8  = 0x8  = 0000 1000",
    "# (4)= 16 = 0x10 = 0001 0000",
    "# (5)= 32 = 0x20 = 0010 0000",
    "# (6)= 64 = 0x40 = 0100 0000",
    "#",
    "##############################################",
]


FUNCTION_GUIDE_EN = [
    "#####################################################",
    "# The data types used in scripts are:",
    "# int:\t\tInteger type",
    "# bool:\t\tBoolean type (true or false)",
    "# string:\tString",
    "# function:\tFunction",
    "# Card:\t\tCard class",
    "# Effect:\tEffect class",
    "# Group:\tCard group class",
    "# table:\tTable type",
    "# nil:\t\tEmpty type; also represents an empty variable",
    "# any:\t\tAny type",
    "# For clarity, function signatures are written in a C-like style.",
    "# [] means the parameter has a default value and can be omitted.",
    "# nil parameters or return values are listed only when they are meaningful.",
    "#",
    "# Note: filter condition functions",
    "# A filter condition function has a Card as its first parameter and returns a boolean. Filter APIs call this function repeatedly when building a group of cards that match a condition. Filter condition functions can accept extra parameters; parameters from the second one onward come from the filter API's extra arguments. Example:",
    "# function sample_filter(c, atk, def)",
    "# \treturn c:GetAttack()>=atk and c:GetDefense()>=def",
    "# end",
    "# For a card c, this function returns true if its ATK is at least atk and its DEF is at least def; otherwise it returns false.",
    "# g=Duel.GetFieldGroup(0,LOCATION_HAND,0) -- Get player 0's hand",
    "# fg=g:Filter(sample_filter,nil,1000,500) -- Select cards from g with ATK >= 1000 and DEF >= 500",
    "# Group.Filter needs only 3 fixed parameters. Arguments starting from the 4th are extra arguments and are passed to sample_filter.",
    "#",
    "# Note: specifying locations",
    "# Some functions get cards from specified locations using three parameters: int player, int s, int o.",
    "# s is the player's own locations from the perspective of player; o is the opponent's locations from the perspective of player.",
    "# For example, Duel.GetFieldGroup(0,LOCATION_GRAVE,LOCATION_MZONE)",
    "# returns all cards in player 0's Graveyard and player 1's Monster Zone.",
    "#",
    "# Note: descriptions",
    "# The script system does not directly display prompt text from strings. Instead, it uses an integer (int desc) to look up the matching description.",
    "# For desc < 2048, the system looks in string.conf. Some commonly used numbers, usually selection prompts, are recorded in constant.lua.",
    "# For desc > 10000, the system looks in the card database. These descriptions are usually selected with aux.Stringid().",
    "#",
    "#●void Duel.ReplaceAttacker(Card c)",
    "# Replaces the current attacking card with c during the Damage Step. This function no longer exists.",
    "#●void Duel.ReplaceAttackTarget(Card c)",
    "# Reserved; this function does not exist.",
    "#",
    "#",
    "# Zone notes:",
    "# On your field, Main Monster Zones are numbered 0~4 from left to right. Extra Monster Zones are 5~6. 0x7f means all Main Monster Zones plus Extra Monster Zones.",
    "# Zone values are bit flags: 2 raised to the zone index. To recover the zone index, use math.log(zone,2).",
    "# Opponent zone values are shifted left by 16 bits.",
    "#",
    "# Binary view:",
    "#",
    "# 0x7f = 0111 1111",
    "# Reading from the low bit upward gives 1111 1110: the first 5 bits are your Main Monster Zones, the 6th bit is the left Extra Monster Zone, and the 7th bit is the right Extra Monster Zone.",
    "# (0)= 1  = 0x1  = 0000 0001",
    "# (1)= 2  = 0x2  = 0000 0010",
    "# (2)= 4  = 0x4  = 0000 0100",
    "# (3)= 8  = 0x8  = 0000 1000",
    "# (4)= 16 = 0x10 = 0001 0000",
    "# (5)= 32 = 0x20 = 0010 0000",
    "# (6)= 64 = 0x40 = 0100 0000",
    "#",
    "#####################################################",
]


def function_guide(language: str) -> list[str]:
    return FUNCTION_GUIDE_EN if language == "en" else FUNCTION_GUIDE_ZH


def write_compat_file(path: Path, docs: Iterable[FunctionDoc], language: str) -> None:
    lines = [
        *function_guide(language),
        "",
        "#####################################################",
        "# Generated by Tools/FunctionDocs/generate_function_docs.py",
        "# Source files: ygopro-core lib*.cpp, Define/def.lua, Utilities/*.lua",
        "# Format kept compatible with DataEditorX CodeConfig.AddFunction().",
        "#####################################################",
        "",
    ]

    current_namespace = None
    for doc in docs:
        if doc.namespace != current_namespace:
            current_namespace = doc.namespace
            lines.append(f"========== {current_namespace} ==========")
        lines.append(f"●{lua_signature(doc)}")
        description = doc.description_en if language == "en" else doc.description_zh
        if not description:
            description = ["TODO document."]
        lines.extend(description)
        if doc.params:
            lines.append("Parameters:")
            for param in doc.params:
                param_description = param.description_zh if language == "zh" and param.description_zh else param.description
                suffix = f" - {param_description}" if param_description else ""
                optional = " optional" if param.optional else ""
                lines.append(f"  {param.name}: {clean_type(param.type)}{optional}{suffix}")
        if doc.returns:
            useful_returns = [ret for ret in doc.returns if clean_type(ret.type) != "nil"]
            if useful_returns:
                lines.append("Returns:")
                for ret in useful_returns:
                    return_description = ret.description_zh if language == "zh" and ret.description_zh else ret.description
                    suffix = f" - {return_description}" if return_description else ""
                    lines.append(f"  {clean_type(ret.type)}{suffix}")
        if doc.source_files:
            source = doc.source_files[0]
            lines.append(f"Source: {source.path}:{source.line}")
        lines.append("")

    write_text(path, "\n".join(lines).rstrip() + "\n")


def markdown_signature(doc: FunctionDoc) -> str:
    params = ", ".join(format_param(param) for param in doc.params)
    ret = format_returns(doc.returns)
    return f"{doc.name}({params}) -> {ret}"


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)


def markdown_inline_text(value: str) -> str:
    return (value or "").replace("[", "\\[").replace("]", "\\]").replace("<", "&lt;").replace(">", "&gt;")


def write_vitepress_config(base: Path, namespaces: Iterable[str]) -> None:
    namespace_items = [
        f"              {{ text: '{namespace}', link: '/api/functions/{safe_filename(namespace)}/' }},"
        for namespace in sorted(namespaces)
    ]
    lines = [
        "import { defineConfig } from 'vitepress';",
        "",
        "export default defineConfig({",
        "  title: 'MDPro3 Sacred Book',",
        "  description: 'MDPro3/YGOPro Lua card scripting reference.',",
        "  cleanUrls: true,",
        "  themeConfig: {",
        "    nav: [",
        "      { text: 'API', link: '/api/' },",
        "      { text: 'Functions', link: '/api/functions/' },",
        "      { text: 'Constants', link: '/api/constants' },",
        "    ],",
        "    sidebar: {",
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
        "    },",
        "  },",
        "});",
        "",
    ]
    write_text(base / ".vitepress" / "config.mts", "\n".join(lines))


def write_wiki_pages(base: Path, docs: Iterable[FunctionDoc], constant_docs: list[ConstantDoc]) -> None:
    index_by_namespace: dict[str, list[FunctionDoc]] = {}
    docs = list(docs)
    for doc in docs:
        index_by_namespace.setdefault(doc.namespace, []).append(doc)
        page = base / "api" / "functions" / safe_filename(doc.namespace) / f"{safe_filename(doc.short_name)}.md"
        description = doc.description_en or doc.description_zh or ["TODO document."]
        lines = [
            f"# {doc.name}",
            "",
            "## Signature",
            "",
            "```lua",
            markdown_signature(doc),
            "```",
            "",
            "## Description",
            "",
        ]
        lines.extend(markdown_inline_text(line) for line in description)
        lines.append("")
        guide = FUNCTION_DETAIL_GUIDES.get(doc.name, [])
        if guide:
            lines.extend(["## How To Use It", ""])
            lines.extend(guide)
            lines.append("")
        related = FUNCTION_RELATED_GUIDES.get(doc.name, [])
        if related:
            lines.extend(["## Related Functions", ""])
            for related_name in related:
                namespace, short_name = related_name.split(".", 1)
                lines.append(f"- [{related_name}](/api/functions/{safe_filename(namespace)}/{safe_filename(short_name)})")
            lines.append("")
        if doc.params:
            lines.extend(["## Parameters", ""])
            for param in doc.params:
                optional = " optional" if param.optional else ""
                desc = f" - {markdown_inline_text(param.description)}" if param.description else ""
                lines.append(f"- `{param.name}` `{clean_type(param.type)}`{optional}{desc}")
            lines.append("")
        useful_returns = [ret for ret in doc.returns if clean_type(ret.type) != "nil"]
        if useful_returns:
            lines.extend(["## Returns", ""])
            for ret in useful_returns:
                desc = f" - {markdown_inline_text(ret.description)}" if ret.description else ""
                lines.append(f"- `{clean_type(ret.type)}`{desc}")
            lines.append("")
        if doc.source_files:
            source = doc.source_files[0]
            lines.extend(["## Source", "", f"- `{source.path}:{source.line}`", ""])
        write_text(page, "\n".join(lines).rstrip() + "\n")

    core_count = sum(1 for doc in docs if doc.core_binding)
    helper_count = sum(
        1
        for doc in docs
        if not doc.core_binding and any(src.origin in {"utility", "procedure"} for src in doc.source_files)
    )
    root_lines = [
        "# MDPro3 Sacred Book",
        "",
        "Core-specific Lua scripting reference for MDPro3/YGOPro card scripts.",
        "",
        "## Reference",
        "",
        "- [API overview](api/)",
        "- [Function reference](api/functions/)",
        "- [Constant reference](api/constants)",
        "",
        "## Current Snapshot",
        "",
        f"- Functions: {len(docs)}",
        f"- Core-bound functions: {core_count}",
        f"- Lua helper/procedure functions: {helper_count}",
        f"- Constants: {len(constant_docs)}",
        "",
        "Generated from the local core bindings, function stubs, utility scripts, and DataEditorX locale data.",
        "",
    ]
    write_text(base / "index.md", "\n".join(root_lines).rstrip() + "\n")

    api_lines = [
        "# API",
        "",
        "This API reference is generated for this project's core and helper scripts. It is intentionally kept separate from Project Ignis scrapi-book because the available bindings and helper procedures differ.",
        "",
        "## Sections",
        "",
        "- [Functions](functions/)",
        "- [Constants](constants)",
        "",
        "## Sources",
        "",
        "- `D:\\Programs\\GitHub\\ygopro-core\\lib*.cpp`",
        "- `Define/def.lua`",
        "- `Utilities/utility.lua`",
        "- `Utilities/procedure.lua`",
        "",
    ]
    write_text(base / "api" / "index.md", "\n".join(api_lines).rstrip() + "\n")

    index_lines = [
        "# Lua API Functions",
        "",
        "Generated from ygopro-core bindings, `Define/def.lua`, `Utilities/utility.lua`, and `Utilities/procedure.lua`.",
        "",
        "## Namespaces",
        "",
    ]
    for namespace in sorted(index_by_namespace):
        namespace_docs = sorted(index_by_namespace[namespace], key=lambda d: d.short_name.lower())
        index_lines.append(f"- [{namespace}]({safe_filename(namespace)}/) ({len(namespace_docs)})")
    index_lines.extend(["", "## All Functions", ""])
    for namespace in sorted(index_by_namespace):
        namespace_docs = sorted(index_by_namespace[namespace], key=lambda d: d.short_name.lower())
        namespace_lines = [
            f"# {namespace}",
            "",
            f"{len(namespace_docs)} functions in the `{namespace}` namespace.",
            "",
        ]
        index_lines.extend([f"### {namespace}", ""])
        for doc in namespace_docs:
            rel = f"{safe_filename(namespace)}/{safe_filename(doc.short_name)}.md"
            index_lines.append(f"- [{doc.name}]({rel})")
            namespace_lines.append(f"- [{doc.name}]({safe_filename(doc.short_name)}.md)")
        index_lines.append("")
        write_text(
            base / "api" / "functions" / safe_filename(namespace) / "index.md",
            "\n".join(namespace_lines).rstrip() + "\n",
        )
    write_text(base / "api" / "functions" / "index.md", "\n".join(index_lines).rstrip() + "\n")
    write_constant_markdown(base / "api" / "constants.md", constant_docs)
    write_vitepress_config(base, index_by_namespace)


CONSTANT_COMMENT_TRANSLATIONS = {
    "卡组": "Deck",
    "手牌": "Hand",
    "主要怪兽区(0-4)+额外怪兽区(5-6)": "Main Monster Zones (0-4) + Extra Monster Zones (5-6)",
    "魔陷区(0-4)+场地区(5)": "Spell & Trap Zones (0-4) + Field Zone (5)",
    "墓地": "Graveyard",
    "除外区": "Banished Zone",
    "额外": "Extra Deck",
    "超量素材": "Xyz Material",
    "场上（LOCATION_MZONE+LOCATION_SZONE）": "Field (LOCATION_MZONE + LOCATION_SZONE)",
    "弹回卡组底部": "Return to the bottom of the Deck",
    "弹回卡组并洗牌": "Return to the Deck and shuffle",
    "弹回卡组顶端": "Return to the top of the Deck",
    "弹回卡组底端": "Return to the bottom of the Deck",
    "弹回卡组并洗牌（洗牌前暂时放在底端）": "Return to the Deck and shuffle (temporarily placed at the bottom before shuffling)",
    "场地区": "Field Zone",
    "灵摆区": "Pendulum Zone",
    "表侧攻击": "Face-up Attack Position",
    "表侧守备": "Face-up Defense Position",
    "里侧守备": "Face-down Defense Position",
    "正面表示": "Face-up",
    "背面表示": "Face-down",
    "攻击表示": "Attack Position",
    "守备表示": "Defense Position",
    "不发动反转效果": "Does not activate Flip Effects",
    "怪兽卡": "Monster Card",
    "魔法卡": "Spell Card",
    "陷阱卡": "Trap Card",
    "通常怪兽": "Normal Monster",
    "效果": "Effect",
    "融合": "Fusion",
    "仪式": "Ritual",
    "陷阱怪兽": "Trap Monster",
    "灵魂": "Spirit",
    "同盟": "Union",
    "二重": "Gemini",
    "调整": "Tuner",
    "同调": "Synchro",
    "衍生物": "Token",
    "速攻": "Quick-Play",
    "永续": "Continuous",
    "装备": "Equip",
    "场地": "Field",
    "反击": "Counter",
    "翻转": "Flip",
    "卡通": "Toon",
    "连接": "Link",
    "特殊召唤": "Special Summon",
    "全种族": "All Races",
    "战士": "Warrior",
    "魔法师": "Spellcaster",
    "天使": "Fairy",
    "恶魔": "Fiend",
    "不死": "Zombie",
    "机械": "Machine",
    "水": "Aqua",
    "炎": "Pyro",
    "岩石": "Rock",
    "鸟兽": "Winged Beast",
    "植物": "Plant",
    "昆虫": "Insect",
    "雷": "Thunder",
    "龙": "Dragon",
    "兽": "Beast",
    "兽战士": "Beast-Warrior",
    "恐龙": "Dinosaur",
    "鱼": "Fish",
    "海龙": "Sea Serpent",
    "爬虫类": "Reptile",
    "念动力": "Psychic",
    "幻神兽": "Divine-Beast",
    "创造神": "Creator God",
    "幻龙": "Wyrm",
    "电子界": "Cyberse",
    "幻想魔": "Illusion",
    "破坏": "Destroy",
    "解放": "Release",
    "暂时": "Temporary",
    "召唤": "Summon",
    "战斗破坏": "Destroyed by battle",
    "代替": "Replacement",
    "抽卡": "Draw",
    "改变去向": "Redirect",
    "规则": "Rule",
    "丢弃": "Discard",
    "回到墓地": "Return to Graveyard",
    "用于连接召唤": "Used for Link Summon",
    "超量素材随着超量怪兽离场": "Xyz Material lost when the Xyz Monster leaves the field",
    "维持代价": "Maintenance cost",
    "攻击宣言之际等": "Action timing, such as attack declaration",
    "通常召唤": "Normal Summon",
    "上级召唤": "Tribute Summon",
    "再度召唤": "Gemini Summon",
    "翻转召唤": "Flip Summon",
    "融合召唤": "Fusion Summon",
    "仪式召唤": "Ritual Summon",
    "同调召唤": "Synchro Summon",
    "超量召唤": "Xyz Summon",
    "灵摆召唤": "Pendulum Summon",
    "连接召唤": "Link Summon",
    "自身效果或条件": "Own effect or condition",
    "对应LV怪兽的效果": "Corresponds to LV monster effects",
    "剑斗兽": "Gladiator Beast",
    "进化虫": "Evoltile",
    "效果被无效": "Effect negated",
    "将变成有效": "Will become enabled",
    "将变成无效": "Will become disabled",
    "完成正规召唤（解除苏生限制）": "Completed proper summon (removes revive limit)",
    "在本回合覆盖": "Set this turn",
    "无等级": "No Level",
    "召唤中": "Being Summoned",
    "预定被破坏": "Scheduled to be destroyed",
    "正在复制效果": "Copying effect",
    "正在連鎖串中": "In a Chain",
    "不能play": "Cannot be played",
    "从手牌发动": "Activated from hand",
    "在本回合反转召唤": "Flip Summoned this turn",
    "在本回合特殊召唤": "Special Summoned this turn",
    "反转召唤被无效": "Flip Summon negated",
    "回合玩家不能手动改变表示形式": "The turn player cannot manually change battle position",
    "反转召唤中": "Being Flip Summoned",
    "可被禁止令停止適用的效果（與EFFECT_FLAG_CANNOT_DISABLE並用）": "Effect that can be stopped by Prohibition (used with EFFECT_FLAG_CANNOT_DISABLE)",
    "复制得到的效果(internal)": "Copied effect (internal)",
    "诱发效果即将发动时检查条件（手卡诱发之外的无此标记的诱发效果为触发事件时检查）": "Check the condition when a Trigger Effect is about to activate; Trigger Effects without this flag, except hand triggers, check when the event occurs",
    "最后计算的攻击力上升": "Final calculated ATK increase",
    "在手卡或对方场上也可以当作自己的同调素材": "Can be treated as your Synchro Material from the hand or opponent's field",
    "同调召唤时可以当作调整（百檎龙-苹果鳞虫）": "Can be treated as a Tuner for a Synchro Summon (Hundred Apple Dragon - Apple Wyrm)",
    "皇帝斗技场": "Kaiser Colosseum",
    "伤害由特定行动代替": "Damage is replaced by a specific action",
    "只能用在X只以上的超量召唤": "Can only be used for an Xyz Summon with at least X materials",
    "支持使用没有等级的怪兽作为同调素材": "Allows monsters without Levels to be used as Synchro Material",
    "支持使用没有等级的怪兽作为仪式素材": "Allows monsters without Levels to be used as Ritual Material",
    "召唤需3只以上作素材的超量怪兽时可以作为2只数量的素材": "Counts as 2 materials when Xyz Summoning a monster that requires 3 or more materials",
    "标记类效果，即RegisterFlagEffect()创建的效果": "Flag effect created by RegisterFlagEffect()",
    "离开卡组或额外卡组时": "When leaving the Deck or Extra Deck",
    "EFFECT_SPSUMMON_PROC_G特殊召唤成功前(只能使用EFFECT_TYPE_CONTINUOUS)": "Before an EFFECT_SPSUMMON_PROC_G Special Summon succeeds (EFFECT_TYPE_CONTINUOUS only)",
    "捨棄自身手牌效果": "Effect that discards your own hand",
    "包含盖放怪兽的效果": "Effect that includes Setting a monster",
    "包含盖放魔陷的效果": "Effect that includes Setting a Spell/Trap",
    "捨棄對方手牌效果": "Effect that discards the opponent's hand",
    "请选择场上的卡（按取消可选择其他区域的卡）": "Select a card on the field (press Cancel to select a card from another zone)",
    "同一连锁中使用次数": "Use count within the same Chain",
    "从卡组选卡显示实际顺序（曾经的默认行为）": "Show the actual order when selecting cards from the Deck (previous default behavior)",
    "指示物": "Counter",
    "抽卡阶段": "Draw Phase",
    "准备阶段": "Standby Phase",
    "主要阶段1": "Main Phase 1",
    "战斗阶段开始": "Battle Phase Start",
    "战斗步驟": "Battle Step",
    "伤害步驟": "Damage Step",
    "伤害计算时": "Damage Calculation",
    "战斗阶段結束": "Battle Phase End",
    "主要阶段2": "Main Phase 2",
    "结束阶段": "End Phase",
    "2个玩家都不是": "Neither player",
    "2个玩家都是": "Both players",
}


SECTION_TRANSLATIONS = {
    "min/max value": "Min/Max Values",
    "Locations 区域": "Locations",
    "Locations (for redirect) 若在重定向类效果中仅指定LOCATION_DECK则为弹回卡组顶部": "Locations (for redirect)",
    "Sequences (for Duel.SendtoDeck)": "Sequences (for Duel.SendtoDeck)",
    "Locations of spell cards": "Locations of Spell Cards",
    "Positions 表示形式": "Positions",
    "Types 卡片类型": "Card Types",
    "组合类型": "Combined Types",
    "Attributes 属性": "Attributes",
    "Races 种族": "Races",
    "Reason 卡片到当前位置的原因": "Reasons",
    "Location Reason": "Location Reasons",
    "Summon Type --召唤类型": "Summon Types",
    "Summon Value --特定的召唤方式": "Summon Values",
    "Status\t--卡片当前状态": "Status",
    "Status --卡片当前状态": "Status",
    "Assume": "Assume",
    "Link Marker": "Link Markers",
    "Counter\t--指示物": "Counters",
    "Counter --指示物": "Counters",
    "Phase\t--阶段": "Phases",
    "Phase --阶段": "Phases",
    "Player\t--玩家": "Players",
    "Player --玩家": "Players",
    "Chain info\t--连锁信息": "Chain Info",
    "Chain info --连锁信息": "Chain Info",
    "Summon info": "Summon Info",
    "Reset": "Reset Conditions",
    "Types": "Effect Types",
    "Flags": "Effect Flags",
    "Codes": "Effect Codes",
    "下面是诱发效果的诱发事件、时点 （如果是TYPE_SINGLE则自己发生以下事件后触发，如果TYPE_FIELD则场上任何卡发生以下事件都触发）": "Events",
    "Category": "Categories",
    "Hint Message": "Hint Messages",
    "Select": "Selection Constants",
    "Timing": "Timings",
    "组合时点": "Combined Timings",
    "Global flag": "Global Flags",
    "特殊选项": "Duel Options",
}


CONSTANT_SECTION_TITLE_OVERRIDES = {
    "Summon Type": "Summon Types",
    "Summon Value": "Summon Values",
    "Counter": "Counters",
    "Phase": "Phases",
    "Player": "Players",
    "Chain info": "Chain Info",
    "Reset": "Reset Conditions",
    "Types": "Effect Types",
    "Flags": "Effect Flags",
    "Codes": "Effect Codes",
    "Category": "Categories",
    "Hint Message": "Hint Messages",
    "Select": "Selection Constants",
    "Timing": "Timings",
    "Global flag": "Global Flags",
    "特殊选项": "Duel Options",
}


CONSTANT_LUA_SECTION_HEADERS = {
    "Summon Type": "Summon Types",
    "Summon Value": "Summon Values",
    "Counter": "Counters",
    "Phase": "Phases",
    "Player": "Players",
    "Chain info": "Chain Info",
    "Reset": "========== Reset ==========\t--Reset conditions. Multiple reset flags can be combined.",
    "Types": "========== Types ==========\t--Effect types. Used with effect/event codes to define how an effect is handled.",
    "Flags": "========== Flags ==========\t--Special effect properties",
    "Codes": "========== Codes ==========\t--For continuous effects, EFFECT_* values describe behavior; for triggered effects, EVENT_* values describe event timing.",
    "下面是诱发效果的诱发事件、时点 （如果是TYPE_SINGLE则自己发生以下事件后触发，如果TYPE_FIELD则场上任何卡发生以下事件都触发）": "Trigger events and timings. TYPE_SINGLE reacts to events involving itself; TYPE_FIELD reacts to matching events involving any card on the field.",
    "Category": "Category\tEffect categories. Duel.SetOperationInfo records these so cards can respond to effect types, such as destruction prevention.",
    "Hint Message": "Hint Message\t--Prompt messages shown at the top of the client window",
    "Select": "Select\t--Selection constants",
    "Timing": "Timing\t--Prompt timings; free-chain cards can use these for automatic activation prompts",
    "Global flag": "Global flag\t--Special global flags",
    "特殊选项": "Special options",
}


REVIEWED_CONSTANT_TRANSLATIONS = {
    "REASON_MATERIAL": "Used as Fusion/Synchro/Xyz Material, Ritual Material, or as a Tribute for a Tribute Summon",
    "SUMMON_TYPE_ADVANCE": "Tribute Summon",
    "EFFECT_UNRELEASABLE_SUM": "Cannot be Tributed for a Tribute Summon",
    "EFFECT_UNRELEASABLE_NONSUM": "Cannot be Tributed except for a Tribute Summon",
    "EVENT_BE_MATERIAL": "When used as Synchro/Xyz/Link Material, used as Ritual/Fusion Material, or Tributed for a Tribute Summon",
    "EVENT_BE_PRE_MATERIAL": "When about to be used as Synchro/Xyz/Link Material or Tributed for a Tribute Summon",
    "HINTMSG_TRIBUTE": "Select a monster to Tribute for a Tribute Summon",
}


def constant_section_title(doc: ConstantDoc) -> str:
    if doc.section == "组合时点":
        if doc.name.startswith("RESETS_"):
            return "Combined Reset Masks"
        if doc.name.startswith("TIMINGS_"):
            return "Combined Timings"
    return CONSTANT_SECTION_TITLE_OVERRIDES.get(doc.section, SECTION_TRANSLATIONS.get(doc.section, doc.section))


def constant_lua_section_header(doc: ConstantDoc) -> str:
    if doc.section == "组合时点":
        if doc.name.startswith("RESETS_"):
            return "--Combined reset masks"
        if doc.name.startswith("TIMINGS_"):
            return "--Combined timings"
    return CONSTANT_LUA_SECTION_HEADERS.get(doc.section, constant_section_title(doc))


CONSTANT_NAME_TRANSLATIONS = {
    "MAX_PARAMETER": "Maximum parameter value",
    "MAX_XYZ_LEVEL": "Maximum Xyz Level value",
    "SUMMON_VALUE_MASK_CHANGE": "Mask Change summon value",
    "SUMMON_VALUE_ASSAULT_MODE": "Assault Mode summon value",
    "SUMMON_VALUE_DARK_FUSION": "Dark Fusion summon value",
    "SUMMON_VALUE_FOSSIL_FUSION": "Fossil Fusion summon value",
    "SUMMON_VALUE_FUTURE_FUSION": "Future Fusion summon value",
    "SUMMON_INFO_CODE": "Summon info: code",
    "SUMMON_INFO_CODE2": "Summon info: secondary code",
    "SUMMON_INFO_TYPE": "Summon info: type",
    "SUMMON_INFO_LEVEL": "Summon info: Level",
    "SUMMON_INFO_RANK": "Summon info: Rank",
    "SUMMON_INFO_ATTRIBUTE": "Summon info: Attribute",
    "SUMMON_INFO_RACE": "Summon info: Race",
    "SUMMON_INFO_ATTACK": "Summon info: ATK",
    "SUMMON_INFO_DEFENSE": "Summon info: DEF",
    "SUMMON_INFO_REASON_EFFECT": "Summon info: reason Effect",
    "SUMMON_INFO_REASON_PLAYER": "Summon info: reason player",
    "EFFECT_FLAG_COIN": "Effect uses a coin toss",
    "EFFECT_FLAG_DICE": "Effect uses a die roll",
    "EFFECT_FLAG_FUSION_SUMMON": "Effect performs a Fusion Summon",
    "FLAG_ID_CHAINING": "Internal flag id: chaining",
    "FLAG_ID_UNION": "Internal flag id: Union",
    "FLAG_ID_NO_NORMAL_DRAW": "Internal flag id: no normal draw",
    "FLAG_ID_ALLURE_QUEEN": "Internal flag id: Allure Queen",
    "FLAG_ID_ARCANA_COIN": "Internal flag id: Arcana Force coin",
    "FLAG_ID_REVERSAL_OF_FATE": "Internal flag id: Reversal of Fate",
}


def is_ascii_text(text: str) -> bool:
    return all(ord(ch) < 128 for ch in text)


def contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def is_english_like_comment(text: str) -> bool:
    return bool(text.strip()) and not contains_cjk(text)


def humanize_constant_name(name: str) -> str:
    parts = name.split("_")
    prefixes = {
        "EFFECT",
        "CATEGORY",
        "REASON",
        "STATUS",
        "TYPE",
        "RACE",
        "ATTRIBUTE",
        "LOCATION",
        "SUMMON",
        "EVENT",
        "RESET",
        "PHASE",
        "POS",
        "PLAYER",
        "CHAININFO",
        "HINT",
        "TIMING",
    }
    while parts and parts[0] in prefixes:
        parts = parts[1:]
    if not parts:
        parts = name.split("_")
    return " ".join(part.capitalize() for part in parts if part)


def seed_constant_translation(name: str, comment: str) -> tuple[str, str]:
    cleaned = comment.strip()
    if not cleaned:
        if name in CONSTANT_NAME_TRANSLATIONS:
            return CONSTANT_NAME_TRANSLATIONS[name], "translated_name"
        return humanize_constant_name(name), "generated_from_name"
    if is_english_like_comment(cleaned):
        return cleaned, "existing_english"
    if cleaned in CONSTANT_COMMENT_TRANSLATIONS:
        return CONSTANT_COMMENT_TRANSLATIONS[cleaned], "translated_exact"

    translated = cleaned
    for zh, en in sorted(CONSTANT_COMMENT_TRANSLATIONS.items(), key=lambda item: len(item[0]), reverse=True):
        translated = translated.replace(zh, en)
    if translated != cleaned and is_ascii_text(translated):
        return translated, "translated_phrase"
    return f"TODO translate: {cleaned}", "missing_translation"


def normalize_constant_section(section: str) -> str:
    section = section.strip().lstrip("-").strip()
    section = re.sub(r"^=+\s*", "", section)
    section = re.sub(r"\s*=+\s*", "", section).strip()
    if "--" in section:
        section = section.split("--", 1)[0].strip() or section.split("--", 1)[1].strip()
    if "\t" in section:
        head, _tail = section.split("\t", 1)
        if head.strip():
            section = head.strip()
    return section


def parse_constant_docs(path: Path, workspace: Path, origin: str) -> OrderedDict[str, ConstantDoc]:
    docs: OrderedDict[str, ConstantDoc] = OrderedDict()
    if not path.exists():
        return docs

    current_section = "General"
    const_re = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*(.*?)\s*(?:--(.*))?$")
    for line_number, raw in enumerate(read_text(path).splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("--"):
            section = normalize_constant_section(stripped[2:])
            if section:
                current_section = section
            continue
        match = const_re.match(raw)
        if not match:
            continue
        name, value, comment = match.groups()
        docs[name] = ConstantDoc(
            name=name,
            value=value.strip(),
            section=current_section,
            comment_zh=(comment or "").strip(),
            source_files=[SourceRef(display_path(path, workspace), line_number, origin)],
        )
    return docs


def parse_constant_json_cache(path: Path) -> dict[str, ConstantDoc]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(read_text(path))
    except json.JSONDecodeError:
        return {}

    docs: dict[str, ConstantDoc] = {}
    for item in payload.get("constants", []):
        name = item.get("name")
        if not name:
            continue
        docs[name] = ConstantDoc(
            name=name,
            value=item.get("value", ""),
            section=item.get("section", ""),
            comment_zh=item.get("comment_zh", ""),
            comment_en=item.get("comment_en", ""),
            english_status=item.get("english_status", "missing"),
            dataeditorx_value=item.get("dataeditorx_value", ""),
            dataeditorx_comment=item.get("dataeditorx_comment", ""),
            old_value=item.get("old_value", ""),
            old_comment=item.get("old_comment", ""),
            source_files=[
                SourceRef(
                    src.get("path", ""),
                    int(src.get("line", 0) or 0),
                    src.get("origin", ""),
                )
                for src in item.get("source_files", [])
                if isinstance(src, dict)
            ],
        )
    return docs


def build_constant_docs(workspace: Path, dataeditorx_data: Path) -> list[ConstantDoc]:
    current = parse_constant_docs(workspace / "Utilities" / "constant.lua", workspace, "current")
    generated_json_cache = parse_constant_json_cache(workspace / "Generated" / "FunctionDocs" / "constants.generated.json")
    generated_lua_cache = parse_constant_docs(
        workspace / "Generated" / "FunctionDocs" / "constant_english.generated.lua",
        workspace,
        "project-cache",
    )
    dataeditorx = parse_constant_docs(dataeditorx_data / "lua" / "constant.lua", workspace, "dataeditorx")

    docs: list[ConstantDoc] = []
    for name, doc in current.items():
        if name in generated_json_cache:
            cache_doc = generated_json_cache[name]
            if (
                cache_doc.english_status.startswith("from_")
                and cache_doc.comment_en
                and is_english_like_comment(cache_doc.comment_en)
            ):
                doc.comment_en = cache_doc.comment_en
                doc.english_status = "from_project_cache"
        elif name in generated_lua_cache:
            english_doc = generated_lua_cache[name]
            doc.source_files.extend(english_doc.source_files)
            if english_doc.comment_zh and is_english_like_comment(english_doc.comment_zh):
                doc.comment_en = english_doc.comment_zh
                doc.english_status = "from_project_cache"
        if name in dataeditorx:
            dex_doc = dataeditorx[name]
            doc.dataeditorx_value = dex_doc.value
            doc.dataeditorx_comment = dex_doc.comment_zh
            doc.source_files.extend(dex_doc.source_files)
        if not doc.comment_en:
            doc.comment_en, doc.english_status = seed_constant_translation(name, doc.comment_zh)
        if name in REVIEWED_CONSTANT_TRANSLATIONS:
            doc.comment_en = REVIEWED_CONSTANT_TRANSLATIONS[name]
            doc.english_status = "reviewed_english"
        docs.append(doc)
    return docs


def write_constant_json(path: Path, docs: list[ConstantDoc], metadata: dict[str, object]) -> None:
    payload = {
        "metadata": metadata,
        "constants": [asdict(doc) for doc in docs],
    }
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def write_constant_english_lua(path: Path, docs: list[ConstantDoc]) -> None:
    lines = [
        "-- Generated by Tools/FunctionDocs/generate_function_docs.py",
        "-- Source values: Utilities/constant.lua",
        "-- English comments are carried forward from the project cache where possible.",
        "",
    ]
    current_section = None
    for doc in docs:
        section = constant_lua_section_header(doc)
        if section != current_section:
            current_section = section
            lines.extend(["", f"--{section}"])
        comment = doc.comment_en or "TODO document"
        lines.append(f"{doc.name}\t={doc.value}\t--{comment}")
    write_text(path, "\n".join(lines).rstrip() + "\n")


def write_constant_markdown(path: Path, docs: list[ConstantDoc]) -> None:
    lines = [
        "# Constants",
        "",
        "Generated from `Utilities/constant.lua`, with English comments carried forward from the project cache where possible.",
        "",
    ]
    current_section = None
    for doc in docs:
        section = constant_section_title(doc)
        if section != current_section:
            if current_section is not None:
                lines.append("")
            current_section = section
            lines.extend([f"## {section}", "", "| Name | Value | English | Source comment |", "| --- | --- | --- | --- |"])
        lines.append(
            f"| `{doc.name}` | `{doc.value}` | {markdown_table_cell(doc.comment_en)} | {markdown_table_cell(doc.comment_zh)} |"
        )
    write_text(path, "\n".join(lines).rstrip() + "\n")


def markdown_table_cell(value: str) -> str:
    return markdown_inline_text(value or "").replace("|", "\\|").replace("\n", "<br>")


def write_constant_backlog(path: Path, docs: list[ConstantDoc]) -> None:
    review_statuses = {"generated_from_name", "missing_translation", "translated_phrase"}
    review_docs = [doc for doc in docs if doc.english_status in review_statuses]
    lines = [
        "# Constant Translation Backlog",
        "",
        f"Needs review: {len(review_docs)}",
        "",
    ]
    for doc in review_docs:
        lines.extend(
            [
                f"## {doc.name}",
                "",
                f"- Value: `{doc.value}`",
                f"- Section: `{constant_section_title(doc)}`",
                f"- Status: `{doc.english_status}`",
                f"- Current comment: {doc.comment_zh or '(none)'}",
                f"- Seed English: {doc.comment_en or '(none)'}",
                "",
            ]
        )
    write_text(path, "\n".join(lines).rstrip() + "\n")


def constant_summary(docs: list[ConstantDoc]) -> dict[str, object]:
    return {
        "generated_constant_count": len(docs),
        "english_status_counts": dict(sorted(Counter(doc.english_status for doc in docs).items())),
    }


def needs_function_backlog(doc: FunctionDoc) -> bool:
    has_core_todo = bool(
        doc.description_zh
        and doc.description_zh[0].startswith("TODO document core binding")
    )
    return doc.english_status in {"missing_translation", "missing_documentation"} or has_core_todo


def write_function_backlog(path: Path, docs: list[FunctionDoc]) -> None:
    backlog = [
        doc
        for doc in docs
        if needs_function_backlog(doc)
    ]
    lines = [
        "# Function Documentation And Translation Backlog",
        "",
        f"Needs documentation or translation: {len(backlog)}",
        "",
    ]
    for doc in backlog:
        lines.extend(
            [
                f"## {doc.name}",
                "",
                f"- Status: `{doc.english_status}`",
                f"- Signature: `{markdown_signature(doc)}`",
                f"- Core binding: `{doc.core_handler}`" if doc.core_handler else "- Core binding: `(none)`",
                f"- Aliases: {', '.join(f'`{alias}`' for alias in doc.aliases) if doc.aliases else '(none)'}",
                "",
                "Current description:",
                "",
            ]
        )
        if doc.description_zh:
            lines.extend(f"> {line}" for line in doc.description_zh)
        else:
            lines.append("> TODO document.")
        if doc.source_files:
            source = doc.source_files[0]
            lines.extend(["", f"Source: `{source.path}:{source.line}`"])
        lines.append("")
    write_text(path, "\n".join(lines).rstrip() + "\n")


def parse_constants(path: Path) -> dict[str, tuple[str, str]]:
    constants: dict[str, tuple[str, str]] = {}
    if not path.exists():
        return constants
    for raw in read_text(path).splitlines():
        if raw.strip().startswith("--") or "=" not in raw:
            continue
        code, _, comment = raw.partition("--")
        name, _, value = code.partition("=")
        name = name.strip()
        value = value.strip()
        if re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
            constants[name] = (value, comment.strip())
    return constants


def parse_effect_creator(path: Path) -> dict[str, object]:
    active: set[str] = set()
    commented: set[str] = set()
    active_by_section: dict[str, set[str]] = {}
    commented_by_section: dict[str, set[str]] = {}
    section = "__root__"
    active_by_section[section] = set()
    commented_by_section[section] = set()
    if not path.exists():
        return {
            "active": active,
            "commented": commented,
            "active_by_section": active_by_section,
            "commented_by_section": commented_by_section,
        }
    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("!"):
            section = stripped[1:].strip()
            active_by_section.setdefault(section, set())
            commented_by_section.setdefault(section, set())
            continue
        is_comment = stripped.startswith("#")
        payload = stripped[1:].strip() if is_comment else stripped
        if not payload.startswith("EFFECT_"):
            continue
        name = payload.split(None, 1)[0]
        if is_comment:
            commented.add(name)
            commented_by_section.setdefault(section, set()).add(name)
        else:
            active.add(name)
            active_by_section.setdefault(section, set()).add(name)
    return {
        "active": active,
        "commented": commented,
        "active_by_section": active_by_section,
        "commented_by_section": commented_by_section,
    }


EFFECT_CREATOR_IGNORED_EFFECT_CODES = {
    "EFFECT_ACTIVATION_COUNT_LIMIT",
    "EFFECT_DISABLE_CHAIN_FIELD",
    "EFFECT_MUST_BE_ATTACKED",
    "EFFECT_RISE_TO_FULL_HEIGHT",
    "EFFECT_UNSUMMONABLE_CARD",
}

EFFECT_CREATOR_INTERNAL_PROPERTIES = {
    "EFFECT_FLAG_COPY",
    "EFFECT_FLAG_COUNT_LIMIT",
    "EFFECT_FLAG_CVAL_CHECK",
    "EFFECT_FLAG_EFFECT",
    "EFFECT_FLAG_FIELD_ONLY",
    "EFFECT_FLAG_FUNC_VALUE",
    "EFFECT_FLAG_INITIAL",
}


def is_effect_creator_effect_code(name: str) -> bool:
    return (
        name.startswith("EFFECT_")
        and not name.startswith("EFFECT_FLAG")
        and not name.startswith("EFFECT_TYPE_")
        and not name.startswith("EFFECT_COUNT_CODE_")
    )


def is_effect_creator_property(name: str) -> bool:
    return name.startswith("EFFECT_FLAG")


def parse_mdpro3_systems(path: Path) -> dict[int, str]:
    systems: dict[int, str] = {}
    if not path.exists():
        return systems
    for raw in read_text(path).splitlines():
        if not raw.startswith("!system "):
            continue
        parts = raw.split(maxsplit=2)
        if len(parts) == 3:
            systems[int(parts[1], 0)] = parts[2].strip()
    return systems


def parse_cardinfo_category(path: Path) -> dict[int, str]:
    entries: dict[int, str] = {}
    if not path.exists():
        return entries
    in_category = False
    for raw in read_text(path).splitlines():
        if raw.startswith("##"):
            in_category = raw.lower().startswith("##category")
            continue
        if in_category and "\t" in raw:
            key, value = raw.split("\t", 1)
            entries[int(key.strip(), 0)] = value.strip()
    return entries


def analyze_constants(workspace: Path, dataeditorx_data: Path) -> dict[str, object]:
    dex_constant = parse_constants(dataeditorx_data / "lua" / "constant.lua")
    local_constant = parse_constants(workspace / "Utilities" / "constant.lua")
    effect_creator = parse_effect_creator(dataeditorx_data / "lua" / "effect_creator_settings.txt")
    effect_creator_active = effect_creator["active"]
    effect_creator_commented = effect_creator["commented"]
    effect_creator_sections = effect_creator["active_by_section"]
    local_effects = {name for name in local_constant if name.startswith("EFFECT_")}
    local_effect_codes = {name for name in local_effects if is_effect_creator_effect_code(name)}
    local_effect_properties = {name for name in local_effects if is_effect_creator_property(name)}
    effect_creator_codes = effect_creator_sections.get("EFFECT_CODES", set())
    effect_creator_properties = effect_creator_sections.get("EFFECT_PROPERTY", set())
    ignored_effect_codes = EFFECT_CREATOR_IGNORED_EFFECT_CODES & local_effect_codes
    ignored_properties = EFFECT_CREATOR_INTERNAL_PROPERTIES & local_effect_properties
    missing_effect_codes = sorted(local_effect_codes - effect_creator_codes - ignored_effect_codes)
    missing_properties = sorted(local_effect_properties - effect_creator_properties - ignored_properties)

    missing = sorted(set(local_constant) - set(dex_constant))
    removed = sorted(set(dex_constant) - set(local_constant))
    changed = sorted(
        name
        for name in set(local_constant) & set(dex_constant)
        if local_constant[name][0] != dex_constant[name][0]
    )

    return {
        "dataeditorx_constant_count": len(dex_constant),
        "local_constant_count": len(local_constant),
        "missing_in_dataeditorx": missing,
        "removed_from_local": removed,
        "changed_values": changed,
        "effect_creator_effect_count": len(effect_creator_active),
        "effect_creator_commented_count": len(effect_creator_commented),
        "effect_creator_effect_code_count": len(effect_creator_codes),
        "effect_creator_property_count": len(effect_creator_properties),
        "local_effect_constant_count": len(local_effects),
        "local_effect_code_constant_count": len(local_effect_codes),
        "local_effect_property_constant_count": len(local_effect_properties),
        "effect_creator_missing_effects": sorted(set(missing_effect_codes) | set(missing_properties)),
        "effect_creator_missing_effect_codes": missing_effect_codes,
        "effect_creator_missing_properties": missing_properties,
        "effect_creator_ignored_effect_codes": sorted(ignored_effect_codes),
        "effect_creator_ignored_properties": sorted(ignored_properties),
        "effect_creator_unknown_effects": sorted(effect_creator_active - set(local_constant)),
        "effect_creator_unknown_effect_codes": sorted(effect_creator_codes - local_effect_codes),
        "effect_creator_unknown_properties": sorted(effect_creator_properties - local_effect_properties),
    }


def analyze_categories(dataeditorx_data: Path, mdpro3_locales: Path) -> dict[str, object]:
    cardinfo = parse_cardinfo_category(dataeditorx_data / "languages" / "cardinfo_english.txt")
    systems = parse_mdpro3_systems(mdpro3_locales / "en-US" / "strings.conf")
    expected = {1 << index: systems.get(1100 + index, "") for index in range(32)}
    mismatches = {
        hex(key): {"dataeditorx": cardinfo.get(key, ""), "mdpro3": expected_value}
        for key, expected_value in expected.items()
        if expected_value and cardinfo.get(key, "") != expected_value
    }
    return {
        "dataeditorx_category_count": len(cardinfo),
        "mdpro3_category_count": len([value for value in expected.values() if value]),
        "mismatches": mismatches,
    }


def limited_list(values: list[str], limit: int = 40) -> list[str]:
    if len(values) <= limit:
        return values
    return values[:limit] + [f"... {len(values) - limit} more"]


def primary_helper_source(doc: FunctionDoc) -> SourceRef | None:
    for source in doc.source_files:
        if source.origin in {"utility", "procedure"}:
            return source
    return None


def source_path_for(source: SourceRef, workspace: Path) -> Path:
    path = Path(source.path)
    if path.is_absolute():
        return path
    return workspace / path


def source_span_contains_return(source: SourceRef, workspace: Path) -> bool:
    path = source_path_for(source, workspace)
    if not path.exists():
        return False
    lines = read_text(path).splitlines()
    start = max(source.line - 1, 0)
    for index in range(start, len(lines)):
        line = lines[index]
        if index > start and LUA_FUNCTION_START_RE.match(line):
            break
        code = line.split("--", 1)[0]
        match = re.search(r"\breturn\b(.*)", code)
        if not match:
            continue
        tail = match.group(1).strip()
        if tail and not tail.startswith(("end", "else")):
            return True
    return False


def default_void_helpers_with_return(docs: list[FunctionDoc], workspace: Path) -> list[str]:
    names: list[str] = []
    for doc in docs:
        if doc.core_binding or doc.returns:
            continue
        source = primary_helper_source(doc)
        if source and source_span_contains_return(source, workspace):
            names.append(doc.name)
    return sorted(names)


def write_report(
    path: Path,
    docs: list[FunctionDoc],
    old_zh: dict[str, list[str]],
    old_en: dict[str, list[str]],
    constants: dict[str, object],
    categories: dict[str, object],
    outputs: list[Path],
    workspace: Path,
) -> None:
    generated_names = {doc.name for doc in docs}
    generated_compare_names = {normalize_api_name(doc.name) for doc in docs}
    core_names = {doc.name for doc in docs if doc.core_binding}
    helper_names = {
        doc.name
        for doc in docs
        if not doc.core_binding and any(src.origin in {"utility", "procedure"} for src in doc.source_files)
    }
    suspicious_void_helpers = default_void_helpers_with_return(docs, workspace)
    stub_only_names = {
        doc.name
        for doc in docs
        if not doc.core_binding and all(src.origin == "def" for src in doc.source_files)
    }
    undocumented_core = sorted(
        doc.name
        for doc in docs
        if doc.core_binding
        and doc.description_zh
        and doc.description_zh[0].startswith("TODO document core binding")
    )
    old_zh_names = {normalize_api_name(name) for name in old_zh}
    namespace_counts = Counter(doc.namespace for doc in docs)
    english_counts = Counter(doc.english_status for doc in docs)
    added = sorted(generated_compare_names - old_zh_names)
    dropped = sorted(old_zh_names - generated_compare_names)
    suspicious_void_helpers = default_void_helpers_with_return(docs, workspace)

    lines = [
        "# Function Docs Refresh Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "## Outputs",
        "",
    ]
    for output in outputs:
        lines.append(f"- `{display_path(output, workspace)}`")
    lines.extend(
        [
            "",
            "## Function Sources",
            "",
            f"- Generated functions: {len(docs)}",
            f"- Core-bound functions: {len(core_names)}",
            f"- Lua helper functions: {len(helper_names)}",
            f"- Stub-only functions: {len(stub_only_names)}",
            f"- Core-bound functions without stub docs: {len(undocumented_core)}",
            f"- Existing DataEditorX `_functions.txt`: {len(old_zh)}",
            f"- Existing DataEditorX `_function_english.txt`: {len(old_en)}",
            f"- Added versus DataEditorX `_functions.txt`: {len(added)}",
            f"- Dropped versus DataEditorX `_functions.txt`: {len(dropped)}",
            "",
            "## Namespaces",
            "",
        ]
    )
    for namespace, count in sorted(namespace_counts.items()):
        lines.append(f"- `{namespace}`: {count}")

    lines.extend(["", "## English Coverage", ""])
    for status, count in sorted(english_counts.items()):
        lines.append(f"- `{status}`: {count}")

    lines.extend(["", "## Core Binding Gaps", ""])
    lines.append("Core-bound functions that were not documented by `Define/def.lua`:")
    lines.append("")
    if undocumented_core:
        for name in limited_list(undocumented_core, 40):
            lines.append(f"- `{name}`")
    else:
        lines.append("- None")
    lines.extend(["", "Documented stubs that do not appear in this core binding scan:", ""])
    if stub_only_names:
        for name in limited_list(sorted(stub_only_names), 40):
            lines.append(f"- `{name}`")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Return Signature Audit",
            "",
            "Lua helper docs that still render as `void` while their source body contains a `return`:",
            "",
            f"- Count: {len(suspicious_void_helpers)}",
            "",
        ]
    )
    if suspicious_void_helpers:
        for name in limited_list(suspicious_void_helpers, 60):
            lines.append(f"- `{name}`")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Compatibility Findings",
            "",
            "- DataEditorX currently consumes `_functions.txt` through `CodeConfig.AddFunction()`, so the generated bullet text keeps that format.",
            "- The structured JSON is the better source for a future wiki or richer editor integration.",
            "- Reviewed function summaries, signatures, parameters, and returns are loaded from `Tools/FunctionDocs/function_doc_overrides.json` instead of being embedded in the generator.",
            "- DataEditorX `MySyntaxHighlighter.cs` receives function names from `CodeConfig.LongTooltipDic`, so highlighting follows the generated `_functions` or `_function_english` file after tooltips are loaded.",
            "- The old hardcoded highlighter lists remain only as a startup fallback and should eventually be removed once generated function data is loaded before the first highlight pass.",
            "",
            "## Constant Findings",
            "",
            f"- DataEditorX constants: {constants['dataeditorx_constant_count']}",
            f"- Local utility constants: {constants['local_constant_count']}",
            f"- Missing in DataEditorX: {len(constants['missing_in_dataeditorx'])}",
            f"- Changed values: {len(constants['changed_values'])}",
            f"- Removed from local: {len(constants['removed_from_local'])}",
            f"- Effect creator active `EFFECT_*` names: {constants['effect_creator_effect_count']}",
            f"- Effect creator commented `EFFECT_*` names: {constants['effect_creator_commented_count']}",
            f"- Effect creator effect-code names: {constants['effect_creator_effect_code_count']}",
            f"- Effect creator property names: {constants['effect_creator_property_count']}",
            f"- Local `EFFECT_*` constants: {constants['local_effect_constant_count']}",
            f"- Local effect-code constants: {constants['local_effect_code_constant_count']}",
            f"- Local effect-property constants: {constants['local_effect_property_constant_count']}",
            f"- `effect_creator_settings.txt` missing effect-code constants: {len(constants['effect_creator_missing_effect_codes'])}",
            f"- `effect_creator_settings.txt` missing effect-property constants: {len(constants['effect_creator_missing_properties'])}",
            f"- Reserved/internal effect-code constants intentionally ignored: {len(constants['effect_creator_ignored_effect_codes'])}",
            f"- Internal property constants intentionally ignored: {len(constants['effect_creator_ignored_properties'])}",
            f"- Unknown active effect creator names: {len(constants['effect_creator_unknown_effects'])}",
            f"- Generated constant docs: {constants.get('generated_constant_count', 0)}",
            "",
            "Constant English status:",
            "",
        ]
    )
    for status, count in constants.get("english_status_counts", {}).items():
        lines.append(f"- `{status}`: {count}")

    lines.extend(
        [
            "",
            "Examples missing in DataEditorX constants:",
            "",
        ]
    )
    for name in limited_list(constants["missing_in_dataeditorx"], 20):
        lines.append(f"- `{name}`")

    lines.extend(["", "Examples changed constant values:", ""])
    for name in limited_list(constants["changed_values"], 20):
        lines.append(f"- `{name}`")

    lines.extend(
        [
            "",
            "## Category Findings",
            "",
            f"- DataEditorX English categories: {categories['dataeditorx_category_count']}",
            f"- MDPro3 English category labels: {categories['mdpro3_category_count']}",
            f"- Category mismatches: {len(categories['mismatches'])}",
            "",
            "## Added Function Examples",
            "",
        ]
    )
    for name in limited_list(added, 40):
        lines.append(f"- `{name}`")

    lines.extend(["", "## Dropped DataEditorX Function Examples", ""])
    for name in limited_list(dropped, 40):
        lines.append(f"- `{name}`")

    lines.extend(
        [
            "",
            "## Recommended Next Steps",
            "",
            "1. Review the generated compatibility text files and copy them into DataEditorX only after spot-checking tooltips.",
            "2. Finish DataEditorX autocomplete/highlighting cleanup by removing the startup fallback lists once generated Lua data is loaded before the first highlight pass.",
            "3. Translate missing English entries from the JSON source instead of editing `_function_english.txt` by hand.",
            "4. Use the generated markdown tree as the seed for a VitePress wiki like scrapi-book, but keep this project's core-specific API separate.",
        ]
    )

    write_text(path, "\n".join(lines).rstrip() + "\n")


def write_json(path: Path, docs: list[FunctionDoc], metadata: dict[str, object]) -> None:
    def doc_payload(doc: FunctionDoc) -> dict[str, object]:
        payload = asdict(doc)
        for param in payload["params"]:
            if not param.get("description_zh"):
                param.pop("description_zh", None)
        for ret in payload["returns"]:
            if not ret.get("description_zh"):
                ret.pop("description_zh", None)
        return payload

    payload = {
        "metadata": metadata,
        "functions": [doc_payload(doc) for doc in docs],
    }
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--dataeditorx-data", type=Path, default=DEFAULT_DATAEDITORX_DATA)
    parser.add_argument("--mdpro3-locales", type=Path, default=DEFAULT_MDPRO3_LOCALES)
    parser.add_argument("--ygopro-core", type=Path, default=DEFAULT_YGOPRO_CORE)
    parser.add_argument("--out", type=Path, default=Path("Generated") / "FunctionDocs")
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    out = (workspace / args.out).resolve() if not args.out.is_absolute() else args.out.resolve()
    dataeditorx_data = args.dataeditorx_data
    mdpro3_locales = args.mdpro3_locales
    ygopro_core = args.ygopro_core

    docs_by_name = load_all_function_docs(workspace, ygopro_core)
    old_zh = parse_bullet_file(dataeditorx_data / "lua" / "_functions.txt")
    old_en = parse_bullet_file(dataeditorx_data / "lua" / "_function_english.txt")
    docs = list(docs_by_name.values())
    attach_english(
        docs,
        [
            ("imported_from_dataeditorx", old_en),
        ],
    )
    translate_function_annotations(docs)

    constants = analyze_constants(workspace, dataeditorx_data)
    categories = analyze_categories(dataeditorx_data, mdpro3_locales)
    constant_docs = build_constant_docs(workspace, dataeditorx_data)
    constants.update(constant_summary(constant_docs))

    json_path = out / "api_functions.generated.json"
    zh_path = out / "_functions.generated.txt"
    en_path = out / "_function_english.generated.txt"
    constant_json_path = out / "constants.generated.json"
    constant_lua_path = out / "constant_english.generated.lua"
    constant_md_path = out / "constants.generated.md"
    constant_backlog_path = out / "constant_translation_backlog.md"
    function_backlog_path = out / "function_translation_backlog.md"
    report_path = out / "report.md"
    comparison_path = out / "comparison.generated.json"
    wiki_path = out / "wiki"

    metadata = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "workspace": str(workspace),
        "dataeditorx_data": str(dataeditorx_data),
        "mdpro3_locales": str(mdpro3_locales),
        "ygopro_core": str(ygopro_core),
        "source_files": [
            str(ygopro_core / "libcard.cpp"),
            str(ygopro_core / "libduel.cpp"),
            str(ygopro_core / "libeffect.cpp"),
            str(ygopro_core / "libgroup.cpp"),
            str(ygopro_core / "libdebug.cpp"),
            "Define/def.lua",
            "Utilities/utility.lua",
            "Utilities/procedure.lua",
            "Tools/FunctionDocs/function_doc_overrides.json",
            "Generated/FunctionDocs/api_functions.generated.json",
            "Generated/FunctionDocs/constants.generated.json",
        ],
    }
    write_json(json_path, docs, metadata)
    write_compat_file(zh_path, docs, "zh")
    write_compat_file(en_path, docs, "en")
    write_wiki_pages(wiki_path, docs, constant_docs)
    write_constant_json(constant_json_path, constant_docs, metadata)
    write_constant_english_lua(constant_lua_path, constant_docs)
    write_constant_markdown(constant_md_path, constant_docs)
    write_constant_backlog(constant_backlog_path, constant_docs)
    write_function_backlog(function_backlog_path, docs)

    generated_names = {doc.name for doc in docs}
    generated_compare_names = {normalize_api_name(doc.name) for doc in docs}
    old_zh_compare_names = {normalize_api_name(name) for name in old_zh}
    core_names = {doc.name for doc in docs if doc.core_binding}
    helper_names = {
        doc.name
        for doc in docs
        if not doc.core_binding and any(src.origin in {"utility", "procedure"} for src in doc.source_files)
    }
    suspicious_void_helpers = default_void_helpers_with_return(docs, workspace)
    stub_only_names = {
        doc.name
        for doc in docs
        if not doc.core_binding and all(src.origin == "def" for src in doc.source_files)
    }
    comparison = {
        "added_vs_dataeditorx_functions": sorted(generated_compare_names - old_zh_compare_names),
        "dropped_vs_dataeditorx_functions": sorted(old_zh_compare_names - generated_compare_names),
        "core_bound_functions": sorted(core_names),
        "lua_helper_functions": sorted(helper_names),
        "default_void_helpers_with_return": suspicious_void_helpers,
        "stub_only_functions": sorted(stub_only_names),
        "core_bound_missing_stub_docs": sorted(
            doc.name
            for doc in docs
            if doc.core_binding
            and doc.description_zh
            and doc.description_zh[0].startswith("TODO document core binding")
        ),
        "constants": constants,
        "categories": categories,
    }
    write_text(comparison_path, json.dumps(comparison, ensure_ascii=False, indent=2) + "\n")
    write_report(
        report_path,
        docs,
        old_zh,
        old_en,
        constants,
        categories,
        [
            json_path,
            zh_path,
            en_path,
            constant_json_path,
            constant_lua_path,
            constant_md_path,
            constant_backlog_path,
            function_backlog_path,
            comparison_path,
            report_path,
            wiki_path / "index.md",
            wiki_path / "api" / "index.md",
            wiki_path / "api" / "functions" / "index.md",
            wiki_path / "api" / "constants.md",
            wiki_path / ".vitepress" / "config.mts",
        ],
        workspace,
    )

    print(f"Generated {len(docs)} functions into {out}")
    print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
