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


@dataclass
class ReturnDoc:
    type: str = "nil"
    description: str = ""


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
    if lname in {"e", "re", "te", "effect"} or lname.endswith("e"):
        return "Effect"
    if lname in {"tp", "ep", "rp", "player", "playerid", "count", "code", "loc", "seq"}:
        return "int"
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


FUNCTION_EN_OVERRIDES = {
    "Card.GetPreviousOverlayCountOnField": ["Returns the number of cards that were overlaid on c while it was previously on the field."],
    "Card.GetSpecialSummonInfo": [
        "Returns Special Summon information for c.",
        "Supported fields include SUMMON_INFO_CODE, SUMMON_INFO_CODE2, SUMMON_INFO_TYPE, SUMMON_INFO_LEVEL, SUMMON_INFO_RANK, SUMMON_INFO_ATTRIBUTE, SUMMON_INFO_RACE, SUMMON_INFO_ATTACK, SUMMON_INFO_DEFENSE, SUMMON_INFO_REASON_EFFECT, and SUMMON_INFO_REASON_PLAYER.",
    ],
    "Card.IsAllReasons": ["Checks whether c includes all reasons in reason."],
    "Card.IsAllTypes": ["Checks whether c includes all types in type."],
    "Card.IsCanBeDisabledByEffect": [
        "Checks whether c's effects can be negated by e.",
        "Cards that are already negated, have no original effects, or are unaffected by e cannot be negated.",
        "The optional third parameter indicates whether this is a monster effect.",
    ],
    "Card.IsCanBePlacedOnField": [
        "Checks whether c can be placed onto the target player's field.",
        "Returns false if the target player is invalid, c is forbidden, or placing c there would violate uniqueness checks.",
    ],
    "Card.IsEffectProperty": ["Checks whether c has an effect matching filter."],
    "Card.IsFaceupEx": ["Checks whether c is face-up; returns true for cards in the hand, Graveyard, Main Deck, and similar hidden/non-field locations."],
    "Card.IsHasDefense": ["Checks whether c has DEF."],
    "Card.IsHasLevel": ["Checks whether c has a Level."],
    "Card.IsNonAttribute": [
        "Checks whether c has any Attribute other than attribute.",
        "For example, if a monster is both DARK and WIND, IsAttribute(DARK) is true, but IsNonAttribute(DARK) is also true.",
    ],
    "Card.IsOriginalEffectProperty": ["Checks whether c is originally a card with an effect matching filter."],
    "Card.IsSpecialSummonableCard": [
        "Checks whether c can be Special Summoned by a proper procedure.",
        "c must have an available Special Summon procedure.",
    ],
    "Card.IsSpecialSummonSetCard": ["Checks whether c was Special Summoned by a card whose name includes setname."],
    "Card.IsTuner": [
        "Checks whether c is a Tuner monster for scard.",
        "Besides TYPE_TUNER, this also checks effects that can make c be treated as a Tuner.",
    ],
    "Duel.AdjustAll": ["Immediately refreshes field information."],
    "Duel.CheckMustMaterial": ["Checks whether the card group satisfies mandatory material requirements."],
    "Duel.GetLastSelectHint": ["Returns the last HINT_SELECTMSG hint sent to player."],
    "Duel.GetMustMaterial": ["Returns the group of cards that must be used as material."],
    "Duel.GetRitualMaterialEx": ["Returns the group of cards player can use as Ritual Material, including monsters without a Level."],
    "Duel.GetReadyChain": ["Returns the number of chains whose Target function has already been executed."],
    "Duel.GetSynchroMaterial": ["Gets the group of cards player can use as Synchro Material."],
    "Duel.GetSZoneCount": [
        "Returns the number of available Spell & Trap Zones for player after targets leave, optionally restricted by zone. The Field Zone is not included.",
        "The additional use_player and reason parameters are used by effects that restrict zones, such as Kaiser Colosseum.",
    ],
    "Duel.GetTargetsRelateToChain": ["Returns all target cards currently related to the Chain."],
    "Duel.IsBattlePhase": ["Returns whether the current phase is the Battle Phase."],
    "Duel.IsChainDisabled": ["Checks whether chainc has already been negated."],
    "Duel.IsChainSolving": ["Checks whether the game is currently resolving a Chain or resolving an effect that does not start a Chain."],
    "Duel.IsMainPhase": ["Returns whether the current phase is a Main Phase."],
    "Duel.IsPhase": ["Returns whether the current phase is phase."],
    "Duel.IsTurnPlayer": ["Returns whether playerid is the current turn player."],
    "Duel.RevealSelectDeckSequence": ["Enables showing the real sequence when selecting cards from the Deck."],
    "Effect.IsCostChecked": ["Checks whether e's cost has already been checked, which indicates whether it was copied."],
    "Effect.IsHasRange": ["Checks whether the effect includes range."],
    "Effect.SetCostCheck": ["Sets e's cost-check flag to b."],
    "Group.CancelableSelect": ["Lets player select min to max cards from g, excluding ex; the selection can be canceled and return nil."],
    "Auxiliary.AddCodeList": ["Registers one or more card codes as codes listed by c, so later checks such as Auxiliary.IsCodeListed can find them. Skipped while c is copying an effect."],
    "Auxiliary.AddDrytronSpSummonEffect": [
        "Adds the shared Drytron ignition effect that Special Summons c from the hand or Graveyard.",
        "The effect uses the common Drytron release cost, target, operation wrapper, and custom activity counter.",
    ],
    "Auxiliary.AddMaterialCodeList": [
        "Registers one or more material card codes for c and also adds each code to c's listed-code table.",
        "Fusion Monsters normally do not need this helper.",
    ],
    "Auxiliary.AddSetNameMonsterList": ["Registers set codes of monsters listed by c, so Auxiliary.IsSetNameMonsterListed can check them later. Skipped while c is copying an effect."],
    "Auxiliary.AddThisCardInGraveAlreadyCheck": [
        "Registers a continuous effect on c that records the effect that sent c to the Graveyard.",
        "This lets later Graveyard-condition checks distinguish a card that was already in the Graveyard from one sent there by the currently resolving effect.",
    ],
    "Auxiliary.AddUrsarcticSpSummonEffect": [
        "Adds the shared Ursarctic hand Quick Effect that Special Summons c during the Main Phase.",
        "The cost releases a Level 7 or higher monster from the hand, or banishes a valid replacement card from the Graveyard.",
    ],
    "Auxiliary.AND": ["Returns a composed predicate that calls each function with the same arguments and stops at the first falsy result."],
    "Auxiliary.ArcanaCoinOperation": [
        "Performs the shared Arcana Force coin-toss operation.",
        "It tosses a coin, or lets the player choose the result while affected by the relevant replacement effect, then stores the result on c with client hints.",
    ],
    "Auxiliary.ArcanaCoinTarget": ["Declares that the shared Arcana Force effect will perform one coin toss for tp."],
    "Auxiliary.AtkEqualsDef": ["Returns true for a non-Link Monster whose ATK equals DEF, using current values on the field or known printed values elsewhere."],
    "Auxiliary.BanishRedirectCondition": ["Default condition for banish-redirect effects; returns true while the handler is face-up."],
    "Auxiliary.BESRemoveCondition": ["Condition for the shared B.E.S. maintenance effect after battle; returns true if the handler is still related to that battle."],
    "Auxiliary.BESRemoveOperation": ["Resolves the shared B.E.S. maintenance effect by removing one 0x1f counter from the handler, or destroying it if no counter can be removed."],
    "Auxiliary.BESRemoveTarget": ["Sets destruction operation info for the shared B.E.S. maintenance effect when the handler cannot remove one 0x1f counter."],
    "Auxiliary.bpcon": ["Returns true if the player can enter the Battle Phase, or if the current phase is already within the Battle Phase window."],
    "Card.branded_fusion_check": ["Material check for Branded Fusion."],
    "Card.cyber_fusion_check": ["Material check for Cyberload Fusion."],
    "Card.destruction_swordsman_fusion_check": ["Material check for Destruction Swordsman Fusion."],
    "Card.hero_fusion_check": ["Material check for Favorite Contact."],
    "Card.mat_filter": ["Release filter condition for Ritual Monsters."],
    "Card.mat_group_check": ["Release group check condition for Ritual Monsters."],
    "Card.red_eyes_fusion_check": ["Material check for Red-Eyes Fusion."],
    "Card.synchro_fusion_check": ["Material check for Miracle Synchro Fusion."],
    "Card.ultimate_fusion_check": ["Material check for Ultimate Fusion."],
    "Card.zw_equip_monster": ["Equips this card as an Equip Card for ZW - monsters."],
}


FUNCTION_ZH_OVERRIDES = {
    "Auxiliary.AddCodeList": ["为c登记1个或多个卡名编号，供Auxiliary.IsCodeListed等函数判断这些编号是否被c列名。复制效果时不处理。"],
    "Auxiliary.AddDrytronSpSummonEffect": [
        "为c添加「龙辉巧」共通的从手牌或墓地特殊召唤自身的起动效果。",
        "该效果使用共通的解放费用、目标、操作包装函数以及特殊召唤限制计数器。",
    ],
    "Auxiliary.AddMaterialCodeList": [
        "为c登记1个或多个素材卡名编号，并同时把这些编号加入c的列名编号表。",
        "融合怪兽通常不需要使用此辅助函数。",
    ],
    "Auxiliary.AddSetNameMonsterList": ["为c登记其文本中列名的怪兽系列编号，供Auxiliary.IsSetNameMonsterListed等函数之后判断。复制效果时不处理。"],
    "Auxiliary.AddThisCardInGraveAlreadyCheck": [
        "为c登记一个持续效果，用于记录把c送去墓地的效果。",
        "这样后续的墓地条件可以区分此卡原本就在墓地，还是被当前正在处理的效果送去墓地。",
    ],
    "Auxiliary.AddUrsarcticSpSummonEffect": [
        "为c添加「北斗天熊」共通的手牌快速效果，在主要阶段特殊召唤自身。",
        "费用为解放手牌中1只7星以上怪兽，或从墓地除外可代替费用的对应卡。",
    ],
    "Auxiliary.AND": ["返回组合条件函数；调用时会用相同参数依次执行传入的函数，并在第一个假值处停止。"],
    "Auxiliary.ArcanaCoinOperation": [
        "处理「秘仪之力」共通的投掷硬币操作。",
        "通常投掷1次硬币；若受对应替代效果影响，则让玩家选择结果，然后把结果以标记和客户端提示记录在c上。",
    ],
    "Auxiliary.ArcanaCoinTarget": ["声明「秘仪之力」共通效果会为tp进行1次投掷硬币。"],
    "Auxiliary.AtkEqualsDef": ["判断c是否为攻击力和守备力相同的非连接怪兽；在场上使用当前数值，其他位置要求原本数值可确认。"],
    "Auxiliary.BanishRedirectCondition": ["除外重定向效果的默认条件；处理对象表侧表示时返回true。"],
    "Auxiliary.BESRemoveCondition": ["B.E.S.共通战斗后维持效果的条件；处理对象仍与该次战斗关联时返回true。"],
    "Auxiliary.BESRemoveOperation": ["处理B.E.S.共通战斗后维持效果：能取除1个0x1f指示物则取除，否则破坏自身。"],
    "Auxiliary.BESRemoveTarget": ["B.E.S.共通战斗后维持效果的目标处理；若不能取除1个0x1f指示物，则登记破坏自身的信息。"],
    "Auxiliary.bpcon": ["判断玩家是否可以进入战斗阶段，或当前阶段是否已经处于战斗阶段范围内。"],
}


CORE_DOC_OVERRIDES = {
    "Card.IsCanBePlacedOnField": {
        "params": [
            ParamDoc("c", "Card"),
            ParamDoc("toplayer", "int", True, "Target player. Defaults to the current reason player."),
            ParamDoc("tolocation", "int", True, "Target location. Defaults to LOCATION_SZONE."),
        ],
        "returns": [ReturnDoc("bool", "true if c can be placed on that player's field.")],
        "description": [
            "Checks whether c can be placed onto the target player's field.",
            "Returns false if the target player is invalid, c is forbidden, or placing c there would violate uniqueness checks.",
        ],
    },
    "Group.__add": {
        "params": [
            ParamDoc("left", "Group|Card"),
            ParamDoc("right", "Group|Card"),
        ],
        "returns": [ReturnDoc("Group", "A new group containing cards from both operands.")],
        "description": ["Union operator for Group/Card operands. Equivalent to combining both operands into a new Group."],
    },
    "Group.__bor": {
        "params": [
            ParamDoc("left", "Group|Card"),
            ParamDoc("right", "Group|Card"),
        ],
        "returns": [ReturnDoc("Group", "A new group containing cards from both operands.")],
        "description": ["Bitwise-or/union operator for Group/Card operands. It uses the same core handler as Group.__add."],
    },
    "Group.__sub": {
        "params": [
            ParamDoc("left", "Group|Card"),
            ParamDoc("right", "Group|Card"),
        ],
        "returns": [ReturnDoc("Group", "A new group with cards from left that are not in right.")],
        "description": ["Difference operator for Group/Card operands. It removes the right operand's cards from the left operand."],
    },
    "Group.__band": {
        "params": [
            ParamDoc("left", "Group|Card"),
            ParamDoc("right", "Group|Card"),
        ],
        "returns": [ReturnDoc("Group", "A new group containing cards present in both operands.")],
        "description": ["Intersection operator for Group/Card operands."],
    },
    "Group.__bxor": {
        "params": [
            ParamDoc("left", "Group|Card"),
            ParamDoc("right", "Group|Card"),
        ],
        "returns": [ReturnDoc("Group", "A new group containing cards present in exactly one operand.")],
        "description": ["Symmetric-difference operator for Group/Card operands."],
    },
    "Group.__len": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("int", "The number of cards in g.")],
        "description": ["Length operator for Group. Equivalent to Group.GetCount."],
    },
}


def copy_params(params: list[ParamDoc]) -> list[ParamDoc]:
    return [
        ParamDoc(param.name, param.type, param.optional, param.description)
        for param in params
    ]


def copy_returns(returns: list[ReturnDoc]) -> list[ReturnDoc]:
    return [ReturnDoc(ret.type, ret.description) for ret in returns]


def apply_core_doc_overrides(docs: dict[str, FunctionDoc]) -> None:
    for name, override in CORE_DOC_OVERRIDES.items():
        doc = docs.get(name)
        if not doc:
            continue
        doc.params = copy_params(override["params"])
        doc.returns = copy_returns(override["returns"])
        doc.description_zh = list(override["description"])
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
                suffix = f" - {param.description}" if param.description else ""
                optional = " optional" if param.optional else ""
                lines.append(f"  {param.name}: {clean_type(param.type)}{optional}{suffix}")
        if doc.returns:
            useful_returns = [ret for ret in doc.returns if clean_type(ret.type) != "nil"]
            if useful_returns:
                lines.append("Returns:")
                for ret in useful_returns:
                    suffix = f" - {ret.description}" if ret.description else ""
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
        lines.extend(description)
        lines.append("")
        if doc.params:
            lines.extend(["## Parameters", ""])
            for param in doc.params:
                optional = " optional" if param.optional else ""
                desc = f" - {param.description}" if param.description else ""
                lines.append(f"- `{param.name}` `{clean_type(param.type)}`{optional}{desc}")
            lines.append("")
        useful_returns = [ret for ret in doc.returns if clean_type(ret.type) != "nil"]
        if useful_returns:
            lines.extend(["## Returns", ""])
            for ret in useful_returns:
                desc = f" - {ret.description}" if ret.description else ""
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
}


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
            section = stripped[2:].strip()
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
        section = SECTION_TRANSLATIONS.get(doc.section, doc.section)
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
        section = SECTION_TRANSLATIONS.get(doc.section, doc.section)
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
    return (value or "").replace("|", "\\|").replace("\n", "<br>")


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
                f"- Section: `{SECTION_TRANSLATIONS.get(doc.section, doc.section)}`",
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


def parse_effect_creator(path: Path) -> set[str]:
    effects: set[str] = set()
    if not path.exists():
        return effects
    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if stripped.startswith("EFFECT_"):
            effects.add(stripped.split(None, 1)[0])
    return effects


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
    local_effects = {name for name in local_constant if name.startswith("EFFECT_")}

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
        "effect_creator_effect_count": len(effect_creator),
        "local_effect_constant_count": len(local_effects),
        "effect_creator_missing_effects": sorted(local_effects - effect_creator),
        "effect_creator_unknown_effects": sorted(effect_creator - local_effects),
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
            "## Compatibility Findings",
            "",
            "- DataEditorX currently consumes `_functions.txt` through `CodeConfig.AddFunction()`, so the generated bullet text keeps that format.",
            "- The structured JSON is the better source for a future wiki or richer editor integration.",
            "- `MySyntaxHighlighter.cs` also hardcodes many function names, so editor highlighting will remain stale until it is changed to read generated data.",
            "",
            "## Constant Findings",
            "",
            f"- DataEditorX constants: {constants['dataeditorx_constant_count']}",
            f"- Local utility constants: {constants['local_constant_count']}",
            f"- Missing in DataEditorX: {len(constants['missing_in_dataeditorx'])}",
            f"- Changed values: {len(constants['changed_values'])}",
            f"- Removed from local: {len(constants['removed_from_local'])}",
            f"- Effect creator effect names: {constants['effect_creator_effect_count']}",
            f"- Local `EFFECT_*` constants: {constants['local_effect_constant_count']}",
            f"- `effect_creator_settings.txt` missing local `EFFECT_*`: {len(constants['effect_creator_missing_effects'])}",
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
            "2. Replace the hardcoded function regex lists in `MySyntaxHighlighter.cs` with generated namespace lists.",
            "3. Translate missing English entries from the JSON source instead of editing `_function_english.txt` by hand.",
            "4. Use the generated markdown tree as the seed for a VitePress wiki like scrapi-book, but keep this project's core-specific API separate.",
        ]
    )

    write_text(path, "\n".join(lines).rstrip() + "\n")


def write_json(path: Path, docs: list[FunctionDoc], metadata: dict[str, object]) -> None:
    payload = {
        "metadata": metadata,
        "functions": [asdict(doc) for doc in docs],
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
