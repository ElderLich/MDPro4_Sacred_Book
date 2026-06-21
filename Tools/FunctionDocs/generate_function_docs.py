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
    "Card.CancelToGrave": [
        "Cancels the confirmed-to-Graveyard state for c. If cancel is false, sets that state again.",
        "This state is used for non-continuous Spell/Trap Cards activated on the field before they leave the field; while set, they cannot return to the hand or Deck and are sent to the Graveyard when the Chain ends.",
        "Use this helper to keep such cards on the field, as with Swords of Revealing Light or Scrap-Iron Scarecrow.",
    ],
    "Card.IsEffectProperty": ["Checks whether c has an effect matching filter."],
    "Card.IsFaceupEx": ["Checks whether c is face-up; returns true for cards in the hand, Graveyard, Main Deck, and similar hidden/non-field locations."],
    "Card.IsHasDefense": ["Checks whether c has DEF."],
    "Card.IsHasLevel": ["Checks whether c has a Level."],
    "Card.IsAbleToGrave": ["Checks whether c can be sent to the Graveyard."],
    "Card.IsAbleToGraveAsCost": ["Checks whether c can be sent to the Graveyard as a cost."],
    "Card.IsCanBeRitualMaterial": ["Checks whether c can be used as Ritual Material for sc; pass nil when no Ritual Monster is being checked."],
    "Card.IsDiscardable": [
        "Checks whether c can be discarded for reason.",
        "This is only a check: sending a card from the hand to the Graveyard with REASON_DISCARD does not by itself make that card unable to be discarded.",
    ],
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
    "Card.IsSummonable": [
        "Checks whether c can be Normal Summoned, excluding Normal Summon/Set.",
        "If e is not nil, checks whether c can be Normal Summoned by that effect. min is the minimum number of Tributes, and zone restricts the zone it must be Summoned to.",
    ],
    "Card.IsTuner": [
        "Checks whether c is a Tuner monster for scard.",
        "Besides TYPE_TUNER, this also checks effects that can make c be treated as a Tuner.",
    ],
    "Duel.AdjustAll": ["Immediately refreshes field information."],
    "Duel.CheckMustMaterial": ["Checks whether the card group satisfies mandatory material requirements."],
    "Duel.DiscardDeck": ["Sends count cards from the top of player's Deck to the Graveyard for reason, and returns the number actually moved."],
    "Duel.GetLastSelectHint": ["Returns the last HINT_SELECTMSG hint sent to player."],
    "Duel.GetMustMaterial": ["Returns the group of cards that must be used as material."],
    "Duel.GetRitualMaterial": ["Returns the cards player can use as Ritual Material, including cards in the hand/field that can be Tributed and cards such as Ritual Djinn monsters in the Graveyard."],
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
    "Duel.IsPlayerCanDiscardDeck": ["Checks whether player can send count cards from the top of the Deck to the Graveyard."],
    "Duel.IsPlayerCanDiscardDeckAsCost": ["Checks whether player can send count cards from the top of the Deck to the Graveyard as a cost."],
    "Duel.IsPlayerCanSendtoGrave": ["Checks whether player can send c to the Graveyard."],
    "Duel.IsPhase": ["Returns whether the current phase is phase."],
    "Duel.IsTurnPlayer": ["Returns whether playerid is the current turn player."],
    "Duel.MSet": [
        "Makes player Set c by a Normal Summon procedure, optionally using effect e and requiring at least min Tributes.",
        "If e is nil, regular Normal Summon/Set rules are used. If ignore_count is true, the once-per-turn Normal Summon limit is ignored.",
    ],
    "Duel.ReleaseRitualMaterial": ["Tributes the Ritual Materials in g; materials such as Ritual Djinn monsters in the Graveyard are banished instead."],
    "Duel.RevealSelectDeckSequence": ["Enables showing the real sequence when selecting cards from the Deck."],
    "Duel.SendtoGrave": ["Sends targets to the Graveyard for reason, optionally treating reason_player as the player that moved them, and returns the number actually moved."],
    "Duel.Summon": [
        "Makes player Normal Summon c, not Set it, optionally by effect e and requiring at least min Tributes.",
        "If e is nil, regular Normal Summon rules are used. If ignore_count is true, the once-per-turn Normal Summon limit is ignored.",
    ],
    "Duel.SwapDeckAndGrave": ["For Exchange of the Spirit-style effects, swaps player's Deck and Graveyard."],
    "Effect.GetActiveType": ["Returns the active effect type, such as monster, Spell, or Trap. This can differ from the type of the card that activated the effect, such as Pendulum effects being treated as Spell effects."],
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
    "Auxiliary.ChangeBattleDamage": ["Returns a value function for EFFECT_CHANGE_BATTLE_DAMAGE. player=0 changes damage taken by the effect owner, player=1 changes damage taken by the opponent; otherwise it returns -1 to keep the damage unchanged."],
    "Auxiliary.CheckGroupRecursive": ["Internal recursive helper for Group.CheckSubGroup. It tries adding c to sg, respects Auxiliary.GCheckAdditional, and searches for a subgroup between min and max that satisfies f."],
    "Auxiliary.CheckGroupRecursiveCapture": ["Internal recursive helper for Group.SelectSubGroup. It searches like Auxiliary.CheckGroupRecursive and stores one valid subgroup in Auxiliary.SubGroupCaptured."],
    "Auxiliary.CheckGroupRecursiveEach": ["Internal recursive helper for Group.CheckSubGroupEach and Group.SelectSubGroupEach. Each selected card must satisfy the filter at the matching position in checks before the final group is tested by f."],
    "Auxiliary.CreateMaterialReasonCardRelation": ["Registers an EVENT_BE_MATERIAL continuous effect on c so that, when c is used as material, the Summoned monster creates an effect relation with te."],
    "Auxiliary.dabcheck": ["Returns true if every card in g has a different Attribute."],
    "Auxiliary.DimensionalFissureTarget": ["Target filter for Dimensional Fissure-style replacement effects. It matches cards whose original type includes Monster, excluding Xyz Materials and cards currently treated as Spell/Trap Cards."],
    "Auxiliary.dlkcheck": ["Returns true if every card in g has a different Link Rating."],
    "Auxiliary.dlvcheck": ["Returns true if every card in g has a different Level."],
    "Auxiliary.dncheck": ["Returns true if every card in g has a different card code."],
    "Auxiliary.dogfcon": ["Condition for EVENT_TO_GRAVE triggers: true when the handler was previously on the field under tp's control, was destroyed, and the opponent was the reason player."],
    "Auxiliary.drccheck": ["Returns true if every card in g has a different Race."],
    "Auxiliary.drkcheck": ["Returns true if every card in g has a different Rank."],
    "Auxiliary.DrytronCostFilter": ["Cost filter for the shared Drytron Special Summon effect. It accepts Drytron monsters and Ritual Monsters that can be Tributed from the hand or field while leaving tp an open Monster Zone."],
    "Auxiliary.DrytronCounterFilter": ["Activity-counter filter for the shared Drytron Special Summon effect. It returns true for cards that cannot be Normal Summoned/Set, so the counter can detect whether tp Special Summoned a monster that can be Normal Summoned/Set this turn."],
    "Auxiliary.DrytronExtraCostFilter": ["Checks whether c can be banished by tp as a replacement cost through effect code 89771220."],
    "Auxiliary.DrytronSpSummonCost": [
        "Checks and pays the shared Drytron self-Summon cost.",
        "The player must not have Special Summoned a monster that can be Normal Summoned/Set this turn. On payment, it applies the matching Special Summon oath, then either Tributes one valid cost card or banishes one valid replacement-cost card.",
    ],
    "Auxiliary.DrytronSpSummonLimit": ["Oath target for the shared Drytron cost; it prevents Special Summoning monsters that can be Normal Summoned/Set, excluding cards whose original type is Spell/Trap or Trap Monster."],
    "Auxiliary.DrytronSpSummonOperation": ["Returns the shared Drytron operation wrapper. It Special Summons the handler in face-up Defense Position, completes its procedure, then calls func(e,tp)."],
    "Auxiliary.DrytronSpSummonTarget": ["Target function for the shared Drytron self-Summon effect. It checks the Monster Zone requirement, confirms the handler can be Special Summoned in face-up Defense Position, and sets Special Summon operation info."],
    "Auxiliary.dscon": ["Condition for Quick Effects that change ATK/DEF; true outside the Damage Phase, or during the Damage Phase before damage calculation has been performed."],
    "Auxiliary.dsercon": ["Condition for EVENT_DAMAGE_STEP_END effects; true if the handler is still related to battle or was battle destroyed."],
    "Auxiliary.EffectCategoryFilter": ["Returns a predicate that checks whether an Effect has category."],
    "Auxiliary.EffectPropertyFilter": ["Returns a predicate that checks whether an Effect has property flag."],
    "Auxiliary.EnableBESRemove": ["Registers the shared B.E.S. maintenance trigger on c. After c battles, it removes one 0x1f counter if possible; otherwise it destroys c."],
    "Auxiliary.EnableChangeCode": [
        "Registers code as a listed code for c and gives c an EFFECT_CHANGE_CODE effect with that value.",
        "If location is omitted, monsters use the Monster Zone and non-monsters use the Spell & Trap Zone. If condition is omitted, the code change is always active.",
    ],
    "Auxiliary.EnableExtraDeckSummonCountLimit": ["Initializes the shared Extra Deck Summon count table with one count for each player and registers a global Draw Phase Start reset. The helper only manages the counter; individual card scripts still check and decrement it."],
    "Auxiliary.EnableNeosReturn": ["Registers the shared Elemental HERO Neos Fusion End Phase return effects on c. It creates a mandatory return effect and an optional version used while c is affected by effect code 42015635, then returns both effects."],
    "Auxiliary.EPDestroyOperation": ["Operation for delayed End Phase destruction effects. It destroys the Card or Group stored as e's label object."],
    "Auxiliary.EquipSpellOperation": ["Returns the shared Equip Spell operation. It equips the handler to the first target if both cards are still related to the effect, the target is face-up, and eqlimit allows it."],
    "Auxiliary.EquipSpellTarget": ["Returns the shared Equip Spell target function. is_self and is_opponent choose which Monster Zones can be targeted, filter selects a valid target, and eqlimit is rechecked for chained target changes and resolution."],
    "Auxiliary.ExtraDeckSummonCountLimitReset": ["Resets the shared Extra Deck Summon count table to one count for each player."],
    "Auxiliary.ExtraReleaseFilter": ["Returns true for an opponent's card that has EFFECT_EXTRA_RELEASE_NONSUM available to tp."],
    "Auxiliary.FALSE": ["Returns false."],
    "Auxiliary.GetAttributeCount": ["Returns how many different Attributes are represented among the cards in g; an empty group returns 0."],
    "Auxiliary.GetCappedAttack": ["Returns c's current ATK, capped at MAX_PARAMETER."],
    "Auxiliary.GetCappedLevel": ["Returns c's current Level, capped at MAX_PARAMETER."],
    "Auxiliary.GetCappedXyzLevel": ["Returns c's current Level, capped at MAX_XYZ_LEVEL."],
    "Auxiliary.GetGlobalColumn": ["Returns the column index for location and sequence from player 0's viewpoint. For player 1, the local column is mirrored. Invalid locations/sequences return NULL_VALUE."],
    "Auxiliary.GetGlobalRow": ["Returns the row index for location and sequence from player 0's viewpoint. For player 1, the local row is mirrored. Invalid locations/sequences return NULL_VALUE."],
    "Auxiliary.GetLocalColumn": ["Returns the local column index for a Spell & Trap Zone or Monster Zone sequence. Extra Monster Zone sequences 5 and 6 map to columns 1 and 3; invalid inputs return NULL_VALUE."],
    "Auxiliary.GetLocalRow": ["Returns the local row index for a Spell & Trap Zone or Monster Zone sequence. Main Monster Zones are row 1, Extra Monster Zones are row 2, and invalid inputs return NULL_VALUE."],
    "Auxiliary.GetMaterialListCount": ["Returns c's stored minimum and maximum material counts. If c has no material_count table, returns 0,0."],
    "Auxiliary.GetMultiLinkedZone": ["Returns the zone mask of tp's Monster Zones that are linked by at least two face-up Link Monsters on either field."],
    "Auxiliary.GetXyzNumber": ["Returns the stored Xyz Number value for v, where v can be a Card or a numeric card code. Returns nil when no value is registered."],
    "Auxiliary.gfcheck": ["Checks a 2-card group against one filter in either order: one card must satisfy f(c,a1) and the other f(c,a2)."],
    "Auxiliary.gffcheck": ["Checks a 2-card group against two filters in either order: one card must satisfy f1(c,a1) and the other f2(c,a2)."],
    "Auxiliary.GiveUpNormalDraw": ["Makes tp give up the normal draw for the current Draw Phase by setting EFFECT_DRAW_COUNT to 0 and registering FLAG_ID_NO_NORMAL_DRAW."],
    "Auxiliary.IsCodeOrListed": ["Returns true if c's current code matches code or code is registered in c's listed-code table."],
    "Auxiliary.IsCounterAdded": ["Returns true if counter is registered in c.counter_add_list."],
    "Auxiliary.IsInGroup": ["Returns true if g contains c."],
    "Auxiliary.IsMaterialListType": ["Returns true if c's stored material type mask contains type."],
    "Auxiliary.IsPlayerCanNormalDraw": ["Checks whether tp can perform a normal draw: draw count is positive, the Deck is not empty, and FLAG_ID_NO_NORMAL_DRAW is not set."],
    "Auxiliary.IsSetNameMonsterListed": ["Returns true if setcode matches one of the monster set codes registered for c, using the same set-code comparison rules as set membership helpers."],
    "Auxiliary.IsTypeInText": ["Returns true if c's text-registered type mask contains type."],
    "Auxiliary.LabrynthDestroyOp": ["Shared extra destroy operation for the Labrynth field effect. After a non-hand-activated Welcome Labrynth Normal Trap resolves, it can destroy one card on the field and consumes the field effect's count limit."],
    "Auxiliary.MaterialReasonCardReg": ["EVENT_BE_MATERIAL callback used by Auxiliary.CreateMaterialReasonCardRelation. It creates an effect relation between the Summoned monster and the stored effect object."],
    "Auxiliary.MergedDelayEventCheck1": ["Internal callback for Auxiliary.RegisterMergedDelayedEvent. It collects event cards and, if not inside a Chain, raises EVENT_CUSTOM plus the stored code immediately."],
    "Auxiliary.MergedDelayEventCheck2": ["Internal callback for Auxiliary.RegisterMergedDelayedEvent. At Chain End, it raises one merged custom event for all collected cards, then clears the stored group."],
    "Auxiliary.MergedDelayEventCheck1_ToSingleCard": ["Internal callback for single-card merged delayed events. It collects event cards, clears them if the owner card moved, and raises the stored custom event immediately when possible."],
    "Auxiliary.MergedDelayEventCheck2_ToSingleCard": ["Internal Chain End callback for single-card merged delayed events. It clears stale public-move entries, raises the stored custom event for collected cards, then clears the group."],
    "Auxiliary.MimighoulFlipCondition": ["Returns true during either Main Phase."],
    "Auxiliary.MonsterEffectPropertyFilter": ["Returns a predicate that checks whether an Effect has property flag and is not ranged to the Pendulum Zone."],
    "Auxiliary.mzctcheck": ["Returns true if tp would have an open Monster Zone after releasing g."],
    "Auxiliary.nbcon": ["Condition helper for effects that negate an activation and banish the activating card. It requires tp to be able to banish, and the activating card must either no longer be related to its effect or be able to be banished."],
    "Auxiliary.nbtg": ["Target helper for effects that negate an activation and banish the activating card. It sets negate operation info, adds banish info when the activating card is still related, and marks CATEGORY_GRAVE_ACTION for effects activated in the Graveyard."],
    "Auxiliary.ndcon": ["Condition helper for effects that negate an activation and return the activating card to the Deck. It accepts Spell/Trap activations, unrelated cards, or related cards that can be returned to the Deck."],
    "Auxiliary.NecroValleyNegateCheck": ["Checks whether v, a Card or Group, contains a card affected by Necrovalley. If the current Chain is disablable and a matching card is found, it negates the current effect and returns true."],
    "Auxiliary.NegateAnyFilter": ["Filter for effects that negate a face-up card. Trap Monsters only need to be face-up, Spell/Trap Cards must be face-up and not already disabled, and monsters use Auxiliary.NegateMonsterFilter."],
    "Auxiliary.NegateEffectMonsterFilter": ["Filter for effects that negate an Effect Monster, such as Effect Veiler: c must be face-up, not already disabled, and currently an Effect Monster."],
    "Auxiliary.NegateMonsterFilter": ["Filter for effects that negate a face-up monster, such as Infinite Impermanence: c must be face-up, not already disabled, and be or originally be an Effect Monster."],
    "Auxiliary.NegateSummonCondition": ["Returns true when no Chain is ready, for effects that negate a Summon."],
    "Auxiliary.NeosReturnConditionForced": ["Condition for the mandatory Elemental HERO Neos Fusion End Phase return effect; true while the handler is not affected by Neo Space's effect code 42015635."],
    "Auxiliary.NeosReturnConditionOptional": ["Condition for the optional Elemental HERO Neos Fusion End Phase return effect; true while the handler is affected by Neo Space's effect code 42015635."],
    "Auxiliary.NeosReturnTargetForced": ["Returns the mandatory End Phase return target function for Elemental HERO Neos Fusions. It always allows targeting, sets to-Deck operation info, and calls set_category when provided."],
    "Auxiliary.NeosReturnTargetOptional": ["Returns the optional End Phase return target function for Elemental HERO Neos Fusions. It requires the handler to be able to return to the Extra Deck, sets to-Deck operation info, and calls set_category when provided."],
    "Auxiliary.NOT": ["Returns a predicate that negates f's result."],
    "Auxiliary.NULL": ["Empty helper function that intentionally does nothing."],
    "Auxiliary.OR": ["Returns a composed predicate that calls each function with the same arguments and stops at the first truthy result."],
    "Auxiliary.PlaceCardsOnDeckBottom": ["Sends g to the top of the Deck by reason, lets p order cards that reached either Deck, moves them to the bottom, and returns the number of operated cards."],
    "Auxiliary.PlaceCardsOnDeckTop": ["Sends g to the top of the Deck by reason, lets p order cards that reached either Deck when needed, and returns the number of operated cards."],
    "Auxiliary.PuzzleOp": ["Puzzle-mode End Phase operation that sets player 0's LP to 0."],
    "Auxiliary.RegisterMergedDelayedEvent": ["Registers global listeners that merge multiple occurrences of event into one EVENT_CUSTOM+code event. The merged event is raised immediately outside a Chain, or at Chain End while in a Chain."],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard": ["Registers single-card merged delayed event listeners for one event or a table of events, returning the generated custom event code. The helper clears stored cards when the owner moves to a public state and installs the shared Chain End raiser when needed."],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_AddOperation": ["Internal helper that registers one event listener and its Chain End companion for Auxiliary.RegisterMergedDelayedEvent_ToSingleCard."],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_RaiseEvent": ["Global Chain End helper for single-card merged delayed events. It raises each pending generated custom event once, then clears its stored group."],
    "Auxiliary.SelectCardFromFieldFirst": ["Selection helper that first offers matching on-field cards with HINTMSG_FIELD_FIRST. If that selection is canceled, it restores the previous hint and falls back to Duel.SelectMatchingCard."],
    "Auxiliary.SelectTargetFromFieldFirst": ["Target-selection helper that first offers matching on-field effect targets with HINTMSG_FIELD_FIRST. If accepted, it sets those cards as targets; otherwise it restores the previous hint and falls back to Duel.SelectTarget."],
    "Auxiliary.SelfEquipFilter": ["Returns true if c has a flag with id, used by Auxiliary.IsSelfEquip to identify cards equipped by their own effect."],
    "Auxiliary.SequenceToGlobal": ["Converts a player's local Monster Zone or Spell & Trap Zone sequence into a global zone bit. Invalid players, locations, or sequences return 0."],
    "Auxiliary.SpiritReturnConditionForced": ["Condition for the mandatory Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does not have the optional-return permission effect."],
    "Auxiliary.SpiritReturnConditionOptional": ["Condition for the optional Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does have the optional-return permission effect."],
    "Auxiliary.SpiritReturnOperation": ["Operation for the shared Spirit Monster End Phase return effect. If the handler is still related to the effect, it returns that card to the hand."],
    "Auxiliary.SpiritReturnReg": ["Registers the temporary End Phase return effects created by Auxiliary.EnableSpiritReturn: one mandatory trigger and one optional trigger."],
    "Auxiliary.SpiritReturnTargetForced": ["Target function for the mandatory Spirit Monster End Phase return effect. During the check step it always returns true, then registers return-to-hand operation info."],
    "Auxiliary.SpiritReturnTargetOptional": ["Target function for the optional Spirit Monster End Phase return effect. During the check step it requires the handler to be able to return to the hand, then registers return-to-hand operation info."],
    "Auxiliary.SZoneSequence": ["Returns the local column for a Spell & Trap Zone sequence from the controller's viewpoint."],
    "Auxiliary.ThisCardInGraveAlreadyCheckReg": ["Condition callback used by Auxiliary.AddThisCardInGraveAlreadyCheck. When this card is sent to the Graveyard by an effect, material use, or non-activated cost, it stores the responsible effect and installs reset effects; it then returns false so no separate effect operation runs."],
    "Auxiliary.ThisCardInGraveAlreadyReset1": ["Clears the stored responsible effect from the tracking effect and resets this temporary reset effect."],
    "Auxiliary.ThisCardInGraveAlreadyReset2": ["Clears the stored responsible effect through the paired reset effect, then resets both temporary reset effects."],
    "Auxiliary.ThisCardMovedToPublicResetCheck_ToSingleCard": ["Reset check used by single-card merged delayed events. If the owner card is now face-up or public, it clears the stored event group."],
    "Auxiliary.tkfcon": ["Returns true if tp controls a Token on the field. If tp is omitted and e is provided, tp defaults to e's handler player."],
    "Auxiliary.TRUE": ["Returns true."],
    "Auxiliary.TurnPlayers": ["Returns an iterator that yields the current turn player first, then the other player."],
    "Auxiliary.UnionEquipFilter": ["Returns a filter for modern Union equip effects. The target must be face-up, controlled by tp, have no modern Union monster equipped, and satisfy filter."],
    "Auxiliary.UnionEquipLimit": ["Returns an Equip Limit value function for modern Union monsters. It allows cards controlled by the handler's player that satisfy filter, and also keeps the current equip target legal."],
    "Auxiliary.UnionEquipOperation": ["Returns the operation function for the shared modern Union equip effect. It equips the handler to the selected target, or sends the handler to the Graveyard by rule if the target is no longer valid."],
    "Auxiliary.UnionEquipTarget": ["Returns the target function for the shared modern Union equip effect. It checks the once-per-turn Union flag, requires an open Spell & Trap Zone, selects a valid target, and registers equip operation info."],
    "Auxiliary.UnionReplaceFilter": ["Destroy-substitute value function for modern Union monsters; returns true for destruction by battle or card effect."],
    "Auxiliary.UnionUnequipOperation": ["Operation for the shared modern Union unequip effect; Special Summons the handler in face-up position if it is still related to the effect."],
    "Auxiliary.UnionUnequipTarget": ["Target function for the shared modern Union unequip effect. It checks the Union flag, available Monster Zone, current equip target, and whether the handler can be Special Summoned."],
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
        "为c添加「北极天熊」共通的手牌快速效果，在主要阶段特殊召唤自身。",
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
    "Auxiliary.ChangeBattleDamage": ["返回用于EFFECT_CHANGE_BATTLE_DAMAGE的Value函数。player=0时改写效果持有者受到的战斗伤害，player=1时改写对方受到的战斗伤害；其他情况返回-1表示不改写。"],
    "Auxiliary.CheckGroupRecursive": ["Group.CheckSubGroup使用的内部递归辅助函数；尝试把c加入sg，遵守Auxiliary.GCheckAdditional，并寻找数量在min到max之间且满足f的子组。"],
    "Auxiliary.CheckGroupRecursiveCapture": ["Group.SelectSubGroup使用的内部递归辅助函数；按Auxiliary.CheckGroupRecursive的方式搜索，并把找到的一个有效子组保存到Auxiliary.SubGroupCaptured。"],
    "Auxiliary.CheckGroupRecursiveEach": ["Group.CheckSubGroupEach和Group.SelectSubGroupEach使用的内部递归辅助函数；每张被选卡必须满足checks中对应位置的筛选函数，最终组再交给f检查。"],
    "Auxiliary.CreateMaterialReasonCardRelation": ["为c登记EVENT_BE_MATERIAL持续效果；当c作为素材使用时，让召唤出的怪兽与te建立效果关联。"],
    "Auxiliary.dabcheck": ["判断g中的每张卡是否具有不同属性。"],
    "Auxiliary.DimensionalFissureTarget": ["「次元裂缝」类替代效果使用的目标筛选；匹配原本种类包含怪兽的卡，但排除超量素材以及当前作为魔法/陷阱处理的卡。"],
    "Auxiliary.dlkcheck": ["判断g中的每张卡是否具有不同连接数值。"],
    "Auxiliary.dlvcheck": ["判断g中的每张卡是否具有不同等级。"],
    "Auxiliary.dncheck": ["判断g中的每张卡是否具有不同卡名编号。"],
    "Auxiliary.dogfcon": ["EVENT_TO_GRAVE触发条件：处理对象之前在tp场上，被破坏，且原因玩家是对方时返回true。"],
    "Auxiliary.drccheck": ["判断g中的每张卡是否具有不同种族。"],
    "Auxiliary.drkcheck": ["判断g中的每张卡是否具有不同阶级。"],
    "Auxiliary.DrytronCostFilter": ["「龙辉巧」共通特殊召唤效果的费用筛选；匹配可以从手牌或场上解放、且解放后会给tp留下可用怪兽区域的「龙辉巧」怪兽或仪式怪兽。"],
    "Auxiliary.DrytronCounterFilter": ["「龙辉巧」共通特殊召唤效果的活动计数筛选；对不能通常召唤/盖放的卡返回true，从而让计数器判断tp本回合是否特殊召唤过可以通常召唤/盖放的怪兽。"],
    "Auxiliary.DrytronExtraCostFilter": ["判断c是否可以由tp通过编号89771220的效果作为代替费用从墓地除外。"],
    "Auxiliary.DrytronSpSummonCost": [
        "检查并支付「龙辉巧」共通的自身特殊召唤费用。",
        "玩家本回合不能已经特殊召唤过可以通常召唤/盖放的怪兽。支付时登记对应的特殊召唤誓约，然后解放1张可用费用卡，或除外1张可用的代替费用卡。",
    ],
    "Auxiliary.DrytronSpSummonLimit": ["「龙辉巧」共通费用登记的誓约目标；阻止特殊召唤可以通常召唤/盖放的怪兽，但排除原本种类为魔法/陷阱或陷阱怪兽的卡。"],
    "Auxiliary.DrytronSpSummonOperation": ["返回「龙辉巧」共通的操作包装函数；将处理对象守备表示特殊召唤，完成正规手续，然后调用func(e,tp)。"],
    "Auxiliary.DrytronSpSummonTarget": ["「龙辉巧」共通自身特殊召唤效果的目标处理；检查怪兽区域需求，确认处理对象能以表侧守备表示特殊召唤，并登记特殊召唤信息。"],
    "Auxiliary.dscon": ["改变攻击力/守备力的快速效果条件；不在伤害阶段时为true，或在伤害阶段且尚未进行伤害计算时为true。"],
    "Auxiliary.dsercon": ["EVENT_DAMAGE_STEP_END效果的条件；处理对象仍与战斗关联，或已被战斗破坏时返回true。"],
    "Auxiliary.EffectCategoryFilter": ["返回谓词函数，用于判断Effect是否包含category类别。"],
    "Auxiliary.EffectPropertyFilter": ["返回谓词函数，用于判断Effect是否包含flag属性。"],
    "Auxiliary.EnableBESRemove": ["为c登记B.E.S.共通维持触发效果；战斗后能取除1个0x1f指示物则取除，否则破坏c。"],
    "Auxiliary.EnableChangeCode": [
        "把code登记为c的列名编号，并给c登记取该值的EFFECT_CHANGE_CODE效果。",
        "省略location时，怪兽默认在怪兽区域适用，非怪兽默认在魔法与陷阱区域适用。省略condition时，该卡名变更始终适用。",
    ],
    "Auxiliary.EnableExtraDeckSummonCountLimit": ["初始化共通的额外卡组召唤次数表，双方各为1次，并登记每个抽卡阶段开始时重置的全局效果。此辅助函数只管理计数，具体卡片脚本仍需自行检查并扣除次数。"],
    "Auxiliary.EnableNeosReturn": ["为c登记「元素英雄 新宇侠」融合怪兽共通的结束阶段返回效果；会创建强制返回效果，以及受编号42015635效果影响时使用的可选版本，并返回这两个效果。"],
    "Auxiliary.EPDestroyOperation": ["延迟到结束阶段破坏的操作函数；破坏保存在e的label object中的Card或Group。"],
    "Auxiliary.EquipSpellOperation": ["返回共通装备魔法操作函数；若处理对象与第一个目标仍与效果关联、目标表侧表示且eqlimit允许，则把处理对象装备给该目标。"],
    "Auxiliary.EquipSpellTarget": ["返回共通装备魔法目标函数；is_self和is_opponent决定可选择哪一方怪兽区域，filter选择有效目标，eqlimit会在连锁中改选目标和处理时再次检查。"],
    "Auxiliary.ExtraDeckSummonCountLimitReset": ["把共通额外卡组召唤次数表重置为双方各1次。"],
    "Auxiliary.ExtraReleaseFilter": ["判断c是否为对方控制、且对tp具有EFFECT_EXTRA_RELEASE_NONSUM效果的卡。"],
    "Auxiliary.FALSE": ["返回false。"],
    "Auxiliary.GetAttributeCount": ["返回g中包含的不同属性数量；空Group返回0。"],
    "Auxiliary.GetCappedAttack": ["返回c的当前攻击力，但最高限制为MAX_PARAMETER。"],
    "Auxiliary.GetCappedLevel": ["返回c的当前等级，但最高限制为MAX_PARAMETER。"],
    "Auxiliary.GetCappedXyzLevel": ["返回c的当前等级，但最高限制为MAX_XYZ_LEVEL。"],
    "Auxiliary.GetGlobalColumn": ["从玩家0视角返回location和sequence对应的列编号。若p为玩家1，则会把本地列镜像；无效位置或序号返回NULL_VALUE。"],
    "Auxiliary.GetGlobalRow": ["从玩家0视角返回location和sequence对应的行编号。若p为玩家1，则会把本地行镜像；无效位置或序号返回NULL_VALUE。"],
    "Auxiliary.GetLocalColumn": ["返回魔法与陷阱区域或怪兽区域序号对应的本地列编号。额外怪兽区域序号5和6分别对应列1和列3；无效输入返回NULL_VALUE。"],
    "Auxiliary.GetLocalRow": ["返回魔法与陷阱区域或怪兽区域序号对应的本地行编号。主要怪兽区域为行1，额外怪兽区域为行2；无效输入返回NULL_VALUE。"],
    "Auxiliary.GetMaterialListCount": ["返回c登记的素材数量下限和上限。若c没有material_count表，则返回0,0。"],
    "Auxiliary.GetMultiLinkedZone": ["返回tp的怪兽区域中，被任意场上至少2只表侧连接怪兽连接到的区域掩码。"],
    "Auxiliary.GetXyzNumber": ["返回v对应的已登记「No.」数值；v可以是Card或数字卡名编号。未登记时返回nil。"],
    "Auxiliary.gfcheck": ["检查2张卡的Group是否能按任意顺序满足同一个筛选：一张满足f(c,a1)，另一张满足f(c,a2)。"],
    "Auxiliary.gffcheck": ["检查2张卡的Group是否能按任意顺序满足两个筛选：一张满足f1(c,a1)，另一张满足f2(c,a2)。"],
    "Auxiliary.GiveUpNormalDraw": ["让tp放弃当前抽卡阶段的通常抽卡：登记EFFECT_DRAW_COUNT为0，并登记FLAG_ID_NO_NORMAL_DRAW。"],
    "Auxiliary.IsCodeOrListed": ["判断c的当前卡名是否为code，或code是否已登记在c的列名编号表中。"],
    "Auxiliary.IsCounterAdded": ["判断counter是否已登记在c.counter_add_list中。"],
    "Auxiliary.IsInGroup": ["判断g是否包含c。"],
    "Auxiliary.IsMaterialListType": ["判断c登记的素材种类掩码是否包含type。"],
    "Auxiliary.IsPlayerCanNormalDraw": ["判断tp是否可以进行通常抽卡：抽卡数量大于0，卡组不为空，且没有FLAG_ID_NO_NORMAL_DRAW。"],
    "Auxiliary.IsSetNameMonsterListed": ["判断setcode是否匹配c登记的怪兽系列编号；比较规则与系列判断辅助函数一致。"],
    "Auxiliary.IsTypeInText": ["判断c文本登记的种类掩码是否包含type。"],
    "Auxiliary.LabrynthDestroyOp": ["「白银之迷宫城」共通的追加破坏处理；非从手牌发动的「拉比林斯迷宫欢迎」通常陷阱处理后，可破坏场上1张卡，并使用场地效果的次数限制。"],
    "Auxiliary.MaterialReasonCardReg": ["Auxiliary.CreateMaterialReasonCardRelation使用的EVENT_BE_MATERIAL回调；让召唤出的怪兽与保存的效果对象建立效果关联。"],
    "Auxiliary.MergedDelayEventCheck1": ["Auxiliary.RegisterMergedDelayedEvent使用的内部回调；收集事件卡，若当前不在连锁中，则立刻触发EVENT_CUSTOM加保存编号的事件。"],
    "Auxiliary.MergedDelayEventCheck2": ["Auxiliary.RegisterMergedDelayedEvent使用的内部回调；在连锁结束时，对已收集的卡只触发1次合并后的自定义事件，然后清空保存的Group。"],
    "Auxiliary.MergedDelayEventCheck1_ToSingleCard": ["单卡合并延迟事件使用的内部回调；收集事件卡，若持有者自身移动则清空，并在可立即处理时触发保存的自定义事件。"],
    "Auxiliary.MergedDelayEventCheck2_ToSingleCard": ["单卡合并延迟事件使用的连锁结束内部回调；清理因公开移动而失效的记录，对收集到的卡触发保存的自定义事件，然后清空Group。"],
    "Auxiliary.MimighoulFlipCondition": ["当前处于任一主要阶段时返回true。"],
    "Auxiliary.MonsterEffectPropertyFilter": ["返回谓词函数，用于判断Effect是否包含flag属性，且效果范围不在灵摆区域。"],
    "Auxiliary.mzctcheck": ["判断tp在解放g之后是否会有可用怪兽区域。"],
    "Auxiliary.nbcon": ["「把发动无效并除外」类效果的条件辅助函数；要求tp可以除外，且发动的卡不再与其效果关联，或仍关联但可以被除外。"],
    "Auxiliary.nbtg": ["「把发动无效并除外」类效果的目标辅助函数；登记无效信息，发动的卡仍与效果关联时登记除外信息，并在效果从墓地发动时标记CATEGORY_GRAVE_ACTION。"],
    "Auxiliary.ndcon": ["「把发动无效并回到卡组」类效果的条件辅助函数；魔法/陷阱的发动、已不与效果关联的卡，或仍关联且可以回到卡组的卡均满足。"],
    "Auxiliary.NecroValleyNegateCheck": ["检查v这个Card或Group中是否包含受「王家长眠之谷」影响的卡。若当前连锁可被无效且找到匹配卡，则无效当前效果并返回true。"],
    "Auxiliary.NegateAnyFilter": ["用于无效表侧卡效果的筛选。陷阱怪兽只需表侧表示，魔法/陷阱卡需表侧表示且尚未被无效，怪兽则使用Auxiliary.NegateMonsterFilter。"],
    "Auxiliary.NegateEffectMonsterFilter": ["用于无效效果怪兽效果的筛选，例如「效果遮蒙者」；c必须表侧表示、尚未被无效，且当前为效果怪兽。"],
    "Auxiliary.NegateMonsterFilter": ["用于无效表侧怪兽效果的筛选，例如「无限泡影」；c必须表侧表示、尚未被无效，且当前或原本为效果怪兽。"],
    "Auxiliary.NegateSummonCondition": ["没有待处理连锁时返回true，用于无效召唤的效果。"],
    "Auxiliary.NeosReturnConditionForced": ["「元素英雄 新宇侠」融合怪兽结束阶段强制返回效果的条件；处理对象未受编号42015635（「新宇宙」）效果影响时返回true。"],
    "Auxiliary.NeosReturnConditionOptional": ["「元素英雄 新宇侠」融合怪兽结束阶段可选返回效果的条件；处理对象受编号42015635（「新宇宙」）效果影响时返回true。"],
    "Auxiliary.NeosReturnTargetForced": ["返回「元素英雄 新宇侠」融合怪兽强制结束阶段返回效果的目标函数；始终允许处理，登记回到卡组信息，并在提供set_category时调用它。"],
    "Auxiliary.NeosReturnTargetOptional": ["返回「元素英雄 新宇侠」融合怪兽可选结束阶段返回效果的目标函数；要求处理对象可以回到额外卡组，登记回到卡组信息，并在提供set_category时调用它。"],
    "Auxiliary.NOT": ["返回将f结果取反的谓词函数。"],
    "Auxiliary.NULL": ["空辅助函数；有意不执行任何处理。"],
    "Auxiliary.OR": ["返回组合条件函数；调用时会用相同参数依次执行传入的函数，并在第一个真值处停止。"],
    "Auxiliary.PlaceCardsOnDeckBottom": ["以reason把g送到卡组最上方；让p为进入双方卡组的卡排序后，再移动到卡组最下方，并返回实际处理的卡数量。"],
    "Auxiliary.PlaceCardsOnDeckTop": ["以reason把g送到卡组最上方；需要时让p为进入双方卡组的卡排序，并返回实际处理的卡数量。"],
    "Auxiliary.PuzzleOp": ["残局模式的结束阶段操作；把玩家0的LP变为0。"],
    "Auxiliary.RegisterMergedDelayedEvent": ["登记全局监听，把同一连锁内多次发生的event合并成1次EVENT_CUSTOM+code事件。不在连锁中则立即触发，在连锁中则于连锁结束触发。"],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard": ["为单张卡登记1个事件或事件表的合并延迟监听，并返回生成的自定义事件编号。持有者移动到公开状态时会清空保存的卡，并在需要时安装共通的连锁结束触发器。"],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_AddOperation": ["Auxiliary.RegisterMergedDelayedEvent_ToSingleCard使用的内部辅助函数；登记1个事件监听及其连锁结束配套监听。"],
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_RaiseEvent": ["单卡合并延迟事件使用的全局连锁结束辅助函数；对每个待处理的生成自定义事件触发1次，然后清空对应Group。"],
    "Auxiliary.SelectCardFromFieldFirst": ["选择辅助函数；先用HINTMSG_FIELD_FIRST提示玩家选择满足条件的场上卡。若取消该选择，则恢复之前的提示并回退到Duel.SelectMatchingCard。"],
    "Auxiliary.SelectTargetFromFieldFirst": ["取对象选择辅助函数；先用HINTMSG_FIELD_FIRST提示玩家选择满足条件的场上效果对象。若接受则登记为对象；否则恢复之前的提示并回退到Duel.SelectTarget。"],
    "Auxiliary.SelfEquipFilter": ["c持有id标记时返回true；Auxiliary.IsSelfEquip用它判断由自身效果装备的卡。"],
    "Auxiliary.SequenceToGlobal": ["把玩家本地的怪兽区域或魔法与陷阱区域序号转换为全局区域位。玩家、位置或序号无效时返回0。"],
    "Auxiliary.SpiritReturnConditionForced": ["灵魂怪兽结束阶段强制回到手牌效果的条件；处理对象没有禁止回手效果，且没有可选择不回手效果时返回true。"],
    "Auxiliary.SpiritReturnConditionOptional": ["灵魂怪兽结束阶段可选回到手牌效果的条件；处理对象没有禁止回手效果，且具有可选择不回手效果时返回true。"],
    "Auxiliary.SpiritReturnOperation": ["灵魂怪兽共通结束阶段回到手牌效果的操作；处理对象仍与效果关联时，将其回到手牌。"],
    "Auxiliary.SpiritReturnReg": ["登记Auxiliary.EnableSpiritReturn创建的临时结束阶段回手效果：1个强制触发效果和1个可选触发效果。"],
    "Auxiliary.SpiritReturnTargetForced": ["灵魂怪兽结束阶段强制回到手牌效果的目标函数；检查阶段始终返回true，之后登记回到手牌的操作信息。"],
    "Auxiliary.SpiritReturnTargetOptional": ["灵魂怪兽结束阶段可选回到手牌效果的目标函数；检查阶段要求处理对象可以回到手牌，之后登记回到手牌的操作信息。"],
    "Auxiliary.SZoneSequence": ["从控制者视角返回魔法与陷阱区域序号对应的本地列编号。"],
    "Auxiliary.ThisCardInGraveAlreadyCheckReg": ["Auxiliary.AddThisCardInGraveAlreadyCheck使用的条件回调；当此卡因效果、作为素材或未发动的费用送去墓地时，保存相关效果并登记重置效果，随后返回false让自身不再执行操作。"],
    "Auxiliary.ThisCardInGraveAlreadyReset1": ["清除跟踪效果保存的相关效果，并重置这个临时重置效果。"],
    "Auxiliary.ThisCardInGraveAlreadyReset2": ["通过配对的重置效果清除保存的相关效果，并重置两个临时重置效果。"],
    "Auxiliary.ThisCardMovedToPublicResetCheck_ToSingleCard": ["单卡合并延迟事件使用的重置检查；若持有者已经表侧表示或处于公开状态，则清空保存的事件Group。"],
    "Auxiliary.tkfcon": ["判断tp场上是否存在衍生物。省略tp且提供e时，tp默认使用e的持有者玩家。"],
    "Auxiliary.TRUE": ["返回true。"],
    "Auxiliary.TurnPlayers": ["返回一个迭代器，先返回当前回合玩家，再返回另一名玩家。"],
    "Auxiliary.UnionEquipFilter": ["返回现代同盟怪兽装备效果使用的筛选函数；对象必须表侧表示、由tp控制、没有装备现代同盟怪兽，并满足filter。"],
    "Auxiliary.UnionEquipLimit": ["返回现代同盟怪兽使用的装备限制Value函数；允许处理者玩家控制且满足filter的卡，并保持当前装备对象合法。"],
    "Auxiliary.UnionEquipOperation": ["返回现代同盟怪兽共通装备效果的操作函数；将处理对象装备给选中的目标，若目标不再有效则因规则把处理对象送去墓地。"],
    "Auxiliary.UnionEquipTarget": ["返回现代同盟怪兽共通装备效果的目标函数；检查同盟次数标记、可用魔法与陷阱区域，选择有效目标，并登记装备操作信息。"],
    "Auxiliary.UnionReplaceFilter": ["现代同盟怪兽的破坏代替Value函数；因战斗或卡片效果将被破坏时返回true。"],
    "Auxiliary.UnionUnequipOperation": ["现代同盟怪兽共通解除装备效果的操作；处理对象仍与效果关联时，将其表侧表示特殊召唤。"],
    "Auxiliary.UnionUnequipTarget": ["现代同盟怪兽共通解除装备效果的目标函数；检查同盟次数标记、可用怪兽区域、当前装备对象，以及处理对象能否特殊召唤。"],
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
    "Auxiliary.GetGlobalColumn": {
        "params": [ParamDoc("p", "int"), ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("int", "The global column index, or NULL_VALUE for invalid input.")],
        "description": ["Returns the column index for location and sequence from player 0's viewpoint."],
    },
    "Auxiliary.GetGlobalRow": {
        "params": [ParamDoc("p", "int"), ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("int", "The global row index, or NULL_VALUE for invalid input.")],
        "description": ["Returns the row index for location and sequence from player 0's viewpoint."],
    },
    "Auxiliary.GetLocalColumn": {
        "params": [ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("int", "The local column index, or NULL_VALUE for invalid input.")],
        "description": ["Returns the local column index for a Spell & Trap Zone or Monster Zone sequence."],
    },
    "Auxiliary.GetLocalRow": {
        "params": [ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("int", "The local row index, or NULL_VALUE for invalid input.")],
        "description": ["Returns the local row index for a Spell & Trap Zone or Monster Zone sequence."],
    },
    "Auxiliary.GetMaterialListCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Minimum material count."), ReturnDoc("int", "Maximum material count.")],
        "description": ["Returns c's stored minimum and maximum material counts."],
    },
    "Auxiliary.GetMultiLinkedZone": {
        "params": [ParamDoc("tp", "int")],
        "returns": [ReturnDoc("int", "Zone mask for zones linked by at least two Link Monsters.")],
        "description": ["Returns tp's multi-linked Monster Zone mask."],
    },
    "Auxiliary.GetXyzNumber": {
        "params": [ParamDoc("v", "any")],
        "returns": [ReturnDoc("int|nil", "Registered Xyz Number value, if any.")],
        "description": ["Returns the stored Xyz Number value for a Card or card code."],
    },
    "Auxiliary.gfcheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("a1", "any"), ParamDoc("a2", "any")],
        "returns": [ReturnDoc("bool", "true if the two cards satisfy the filter in either order.")],
        "description": ["Checks a 2-card group against one filter in either order."],
    },
    "Auxiliary.gffcheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f1", "function"), ParamDoc("a1", "any"), ParamDoc("f2", "function"), ParamDoc("a2", "any")],
        "returns": [ReturnDoc("bool", "true if the two cards satisfy both filters in either order.")],
        "description": ["Checks a 2-card group against two filters in either order."],
    },
    "Auxiliary.IsCodeOrListed": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("bool", "true if c has or lists code.")],
        "description": ["Checks whether c's current code is code or c lists code."],
    },
    "Auxiliary.IsCounterAdded": {
        "params": [ParamDoc("c", "Card"), ParamDoc("counter", "int")],
        "returns": [ReturnDoc("bool", "true if counter is registered on c.")],
        "description": ["Checks whether counter is registered in c.counter_add_list."],
    },
    "Auxiliary.IsInGroup": {
        "params": [ParamDoc("c", "Card"), ParamDoc("g", "Group")],
        "returns": [ReturnDoc("bool", "true if g contains c.")],
        "description": ["Checks whether g contains c."],
    },
    "Auxiliary.IsMaterialListType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool", "true if c's material type mask contains type.")],
        "description": ["Checks whether c's stored material type mask contains type."],
    },
    "Auxiliary.IsSetNameMonsterListed": {
        "params": [ParamDoc("c", "Card"), ParamDoc("setcode", "int")],
        "returns": [ReturnDoc("bool", "true if c lists a matching monster set code.")],
        "description": ["Checks whether setcode matches one of c's registered monster set codes."],
    },
    "Auxiliary.IsTypeInText": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool", "true if c's text type mask contains type.")],
        "description": ["Checks whether c's text-registered type mask contains type."],
    },
    "Auxiliary.MimighoulFlipCondition": {
        "params": [
            ParamDoc("e", "Effect"),
            ParamDoc("tp", "int"),
            ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"),
            ParamDoc("ev", "any"),
            ParamDoc("re", "Effect"),
            ParamDoc("r", "any"),
            ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true during either Main Phase.")],
        "description": ["Returns true during either Main Phase."],
    },
    "Auxiliary.mzctcheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if tp has an open Monster Zone after releasing g.")],
        "description": ["Checks whether tp would have an open Monster Zone after releasing g."],
    },
    "Auxiliary.nbcon": {
        "params": [ParamDoc("tp", "int"), ParamDoc("re", "Effect")],
        "returns": [ReturnDoc("bool", "true if the activation can be negated and the card can be banished if needed.")],
        "description": ["Condition helper for effects that negate an activation and banish the activating card."],
    },
    "Auxiliary.ndcon": {
        "params": [ParamDoc("tp", "int"), ParamDoc("re", "Effect")],
        "returns": [ReturnDoc("bool", "true if the activation can be negated and the card can be returned to the Deck if needed.")],
        "description": ["Condition helper for effects that negate an activation and return the activating card to the Deck."],
    },
    "Auxiliary.NecroValleyNegateCheck": {
        "params": [ParamDoc("v", "Card|Group")],
        "returns": [ReturnDoc("bool", "true if the current effect was negated by the Necrovalley check.")],
        "description": ["Checks whether v contains a card affected by Necrovalley, and negates the current effect if so."],
    },
    "Auxiliary.NegateAnyFilter": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c is a valid card to have its effects negated.")],
        "description": ["Filter for effects that negate a face-up card."],
    },
    "Auxiliary.NegateEffectMonsterFilter": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c is a valid Effect Monster to have its effects negated.")],
        "description": ["Filter for effects that negate an Effect Monster."],
    },
    "Auxiliary.NegateMonsterFilter": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c is a valid face-up monster to have its effects negated.")],
        "description": ["Filter for effects that negate a face-up monster."],
    },
    "Auxiliary.NegateSummonCondition": {
        "params": [],
        "returns": [ReturnDoc("bool", "true when no Chain is ready.")],
        "description": ["Condition helper for effects that negate a Summon."],
    },
    "Auxiliary.NeosReturnConditionForced": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if the forced Neos return effect should apply.")],
        "description": ["Condition for the mandatory Elemental HERO Neos Fusion End Phase return effect."],
    },
    "Auxiliary.NeosReturnConditionOptional": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if the optional Neos return effect should apply.")],
        "description": ["Condition for the optional Elemental HERO Neos Fusion End Phase return effect."],
    },
    "Auxiliary.NeosReturnTargetForced": {
        "params": [ParamDoc("set_category", "function|nil", True)],
        "returns": [ReturnDoc("function", "Target function for the mandatory return effect.")],
        "description": ["Returns the mandatory End Phase return target function for Elemental HERO Neos Fusions."],
    },
    "Auxiliary.NeosReturnTargetOptional": {
        "params": [ParamDoc("set_category", "function|nil", True)],
        "returns": [ReturnDoc("function", "Target function for the optional return effect.")],
        "description": ["Returns the optional End Phase return target function for Elemental HERO Neos Fusions."],
    },
    "Auxiliary.NOT": {
        "params": [ParamDoc("f", "function")],
        "returns": [ReturnDoc("function", "A predicate that returns not f(...).")],
        "description": ["Returns a predicate that negates f's result."],
    },
    "Auxiliary.OR": {
        "params": [ParamDoc("...", "function")],
        "returns": [ReturnDoc("function", "A composed predicate.")],
        "description": ["Returns a composed predicate that stops at the first truthy result."],
    },
    "Auxiliary.PlaceCardsOnDeckBottom": {
        "params": [ParamDoc("p", "int"), ParamDoc("g", "Group"), ParamDoc("reason", "int", True, "Defaults to REASON_EFFECT.")],
        "returns": [ReturnDoc("int", "The number of operated cards.")],
        "description": ["Places cards on the bottom of the Deck in player-chosen order."],
    },
    "Auxiliary.PlaceCardsOnDeckTop": {
        "params": [ParamDoc("p", "int"), ParamDoc("g", "Group"), ParamDoc("reason", "int", True, "Defaults to REASON_EFFECT.")],
        "returns": [ReturnDoc("int", "The number of operated cards.")],
        "description": ["Places cards on the top of the Deck in player-chosen order."],
    },
    "Auxiliary.RegisterMergedDelayedEvent": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("event", "int"), ParamDoc("g", "Group|nil", True, "Optional storage group; a kept-alive group is created when omitted.")],
        "returns": [],
        "description": ["Registers global listeners that merge multiple event occurrences into one custom event."],
    },
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("events", "int|table")],
        "returns": [ReturnDoc("int", "The generated custom event code.")],
        "description": ["Registers single-card merged delayed event listeners."],
    },
    "Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_AddOperation": {
        "params": [ParamDoc("c", "Card"), ParamDoc("g", "Group"), ParamDoc("event", "int"), ParamDoc("event_code_single", "int")],
        "returns": [],
        "description": ["Registers one single-card merged delayed event listener and its Chain End companion."],
    },
    "Auxiliary.SelectCardFromFieldFirst": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("f", "function"), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("ex", "any"), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group", "The selected cards.")],
        "description": ["Selects matching cards, offering on-field cards first."],
    },
    "Auxiliary.SelectTargetFromFieldFirst": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("f", "function"), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("ex", "any"), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group", "The selected target cards.")],
        "description": ["Selects matching effect targets, offering on-field cards first."],
    },
    "Auxiliary.SelfEquipFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("id", "int")],
        "returns": [ReturnDoc("bool", "true if c has the flag id.")],
        "description": ["Filter used by Auxiliary.IsSelfEquip."],
    },
    "Auxiliary.SequenceToGlobal": {
        "params": [ParamDoc("p", "int"), ParamDoc("loc", "int"), ParamDoc("seq", "int")],
        "returns": [ReturnDoc("int", "The global zone bit, or 0 for invalid input.")],
        "description": ["Converts a local zone sequence to a global zone bit."],
    },
    "Auxiliary.SpiritReturnConditionForced": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if the mandatory Spirit return effect should apply.")],
        "description": ["Condition for the mandatory Spirit Monster End Phase return effect."],
    },
    "Auxiliary.SpiritReturnConditionOptional": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if the optional Spirit return effect should apply.")],
        "description": ["Condition for the optional Spirit Monster End Phase return effect."],
    },
    "Auxiliary.SpiritReturnOperation": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Operation for the shared Spirit Monster End Phase return effect."],
    },
    "Auxiliary.SpiritReturnReg": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Registers the temporary Spirit Monster End Phase return effects."],
    },
    "Auxiliary.SpiritReturnTargetForced": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
            ParamDoc("chk", "bool"),
        ],
        "returns": [ReturnDoc("bool|nil", "true during target checks; otherwise no meaningful return value.")],
        "description": ["Target function for the mandatory Spirit Monster End Phase return effect."],
    },
    "Auxiliary.SpiritReturnTargetOptional": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
            ParamDoc("chk", "bool"),
        ],
        "returns": [ReturnDoc("bool|nil", "true during valid target checks; otherwise no meaningful return value.")],
        "description": ["Target function for the optional Spirit Monster End Phase return effect."],
    },
    "Auxiliary.SZoneSequence": {
        "params": [ParamDoc("seq", "int")],
        "returns": [ReturnDoc("int", "The local column index, or NULL_VALUE for invalid input.")],
        "description": ["Returns the local column for a Spell & Trap Zone sequence."],
    },
    "Auxiliary.ThisCardInGraveAlreadyCheckReg": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "Always false after any tracking setup is done.")],
        "description": ["Condition callback for Auxiliary.AddThisCardInGraveAlreadyCheck."],
    },
    "Auxiliary.ThisCardInGraveAlreadyReset1": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [],
        "description": ["Clears the stored responsible effect and resets this temporary reset effect."],
    },
    "Auxiliary.ThisCardInGraveAlreadyReset2": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [],
        "description": ["Clears the stored responsible effect and resets paired temporary reset effects."],
    },
    "Auxiliary.ThisCardMovedToPublicResetCheck_ToSingleCard": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Clears the stored single-card merged-event group if the owner card is public."],
    },
    "Auxiliary.tkfcon": {
        "params": [ParamDoc("e", "Effect|nil", True), ParamDoc("tp", "int|nil", True)],
        "returns": [ReturnDoc("bool", "true if tp controls a Token on the field.")],
        "description": ["Checks whether tp controls a Token."],
    },
    "Auxiliary.TRUE": {
        "params": [],
        "returns": [ReturnDoc("bool", "Always true.")],
        "description": ["Returns true."],
    },
    "Auxiliary.TurnPlayers": {
        "params": [],
        "returns": [ReturnDoc("function", "Iterator that yields the turn player, then the other player.")],
        "description": ["Returns an iterator over the current turn player and the other player."],
    },
    "Auxiliary.UnionEquipFilter": {
        "params": [ParamDoc("filter", "function")],
        "returns": [ReturnDoc("function", "Filter function taking Card c and int tp.")],
        "description": ["Returns the target filter for modern Union equip effects."],
    },
    "Auxiliary.UnionEquipLimit": {
        "params": [ParamDoc("filter", "function")],
        "returns": [ReturnDoc("function", "Equip Limit value function.")],
        "description": ["Returns the Equip Limit value function for modern Union monsters."],
    },
    "Auxiliary.UnionEquipOperation": {
        "params": [ParamDoc("equip_filter", "function")],
        "returns": [ReturnDoc("function", "Operation function for the shared Union equip effect.")],
        "description": ["Returns the operation function for modern Union equip effects."],
    },
    "Auxiliary.UnionEquipTarget": {
        "params": [ParamDoc("equip_filter", "function")],
        "returns": [ReturnDoc("function", "Target function for the shared Union equip effect.")],
        "description": ["Returns the target function for modern Union equip effects."],
    },
    "Auxiliary.UnionReplaceFilter": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool", "true for destruction by battle or card effect.")],
        "description": ["Destroy-substitute value function for modern Union monsters."],
    },
    "Auxiliary.UnionUnequipOperation": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Operation for the shared modern Union unequip effect."],
    },
    "Auxiliary.UnionUnequipTarget": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
            ParamDoc("chk", "bool"),
        ],
        "returns": [ReturnDoc("bool|nil", "true during valid target checks; otherwise no meaningful return value.")],
        "description": ["Target function for the shared modern Union unequip effect."],
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
