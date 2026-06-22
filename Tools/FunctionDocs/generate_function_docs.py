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
    # High-use core/API functions reviewed from MDPro3/YGOPro sources.
    "Card.CheckFusionSubstitute": ["Checks whether c can substitute for a specifically named Fusion Material listed by Fusion Monster fcard."],
    "Card.GetPreviousLocation": ["Returns c's previous location bitmask from before its last location change."],
    "Duel.GetFlagEffectLabel": [
        "Returns the label values stored on player flag effects with code.",
        "If no matching flag effect exists, the core returns nil; if multiple matching flag effects exist, it returns one label value for each.",
    ],
    "Duel.GetOverlayGroup": ["Returns the Xyz Materials attached to cards in player-relative locations s and o."],
    "Duel.IsPlayerCanRelease": [
        "Checks whether player can release cards at all, or whether player can release c for reason.",
        "When c is supplied and reason is omitted, the core uses REASON_COST.",
    ],
    "Duel.SetFlagEffectLabel": ["Sets the first matching player flag effect's label to label and returns whether one was found."],
    "Duel.SetFusionMaterial": ["Replaces the core's current Fusion Material set with the cards in g."],
    "Auxiliary.AddFusionProcFunRep2": ["Registers a Fusion procedure requiring between minc and maxc materials that satisfy f."],
    "Auxiliary.DragonXyzSpSummonType": ["Returns true only for Soul Drain Dragon, used as a Special Summon procedure-type helper."],
    "Auxiliary.GetColumn": ["Returns c's column index from player p's viewpoint, or NULL_VALUE when c has no field column."],
    "Auxiliary.GetValueType": ["Returns Lua's type string for ordinary values, or Card, Group, or Effect for those userdata objects."],
    "Auxiliary.IsSelfEquip": ["Checks whether c has an equipped card carrying flag effect id, which marks equipment created by that card's own effect."],
    "Card.GetAttackableTarget": ["Returns the Group of cards c can attack and a boolean indicating whether c can attack directly."],
    "Card.GetAttackedCount": ["Returns c's attack count for the current turn."],
    "Card.GetLeaveFieldDest": ["Returns the location c would be redirected to by leave-field effects for REASON_EFFECT."],
    "Card.GetPreviousLevelOnField": ["Returns the Level value c had while it was previously on the field."],
    "Card.IsXyzLevel": ["Checks whether c can provide Xyz Level lv for Xyz Monster xyzc."],
    "Duel.DisableSelfDestroyCheck": ["Sets whether the core's self-destruction check is disabled; omitting disable disables the check."],
    "Effect.GetCondition": ["Returns e's condition callback, or nil when no condition is set."],
    "Auxiliary.AddRitualProcEqualCode": [
        "Creates a Ritual Summon activation effect for Ritual Monster code1.",
        "The selected materials' Ritual Levels must exactly equal the Ritual Monster's original Level, and optional Graveyard material, material filter, and extra callbacks are forwarded to the shared Ritual procedure.",
    ],
    "Auxiliary.ArcanaCondition": ["Arcana Force condition helper that checks whether the handler has a stored Arcana coin-result flag."],
    "Auxiliary.dogcon": ["EVENT_TO_GRAVE condition helper that checks whether the handler was previously controlled by tp and destroyed by the opponent."],
    "Auxiliary.DrytronSpSummonType": ["Returns whether c is a Special Summon procedure monster, used by Drytron Special Summon helpers."],
    "Auxiliary.indsval": ["Value helper for self-protection from effect destruction; it returns true when the reason player is the handler's player."],
    "Auxiliary.PhantasmsSpSummonType": ["Returns whether c is a Special Summon procedure monster, used by Phantasm Special Summon helpers."],
    "Auxiliary.TriamidSpSummonType": ["Returns whether c is a Special Summon procedure monster, used by Triamid Special Summon helpers."],
    "Card.CancelCardTarget": ["Removes target from c's persistent card-target relation list."],
    "Card.GetMutualLinkedGroup": ["Returns the Group of cards mutually linked with c."],
    "Card.IsCanBeLinkMaterial": ["Checks whether c can be used as Link Material, optionally for Link Monster scard."],
    "Card.IsLinkMarker": ["Checks whether c has Link Marker direction dir."],
    "Card.ReleaseEffectRelation": ["Releases c's relation to effect e."],
    "Card.ReverseInDeck": [
        "Marks c face-up while it is in the Deck.",
        "If c is the current top card of the Main Deck, the core also sends the top-of-Deck update to the client.",
    ],
    "Duel.ChangeBattleDamage": [
        "Changes player battle damage for the current battle to value.",
        "When check is true or omitted, existing 0 battle damage is left unchanged.",
    ],
    "Duel.GetCoinResult": ["Returns the stored coin toss results for the current coin-toss event, one result per coin."],
    "Duel.GetDrawCount": ["Returns player's current rule draw count for the Draw Phase."],
    "Effect.IsActivatable": ["Checks whether e can currently be activated by player, with optional booleans to ignore location and target checks."],
    "Auxiliary.AddFusionProcCode4": ["Registers a fixed four-name Fusion procedure requiring code1, code2, code3, and code4 as materials."],
    "Auxiliary.EnableReviveLimitPendulumSummonable": [
        "Enables revive-limit handling for c while also allowing it to be Pendulum Summoned from loc.",
        "The helper stores loc on c's metatable and completes c's procedure when it is successfully Pendulum Summoned.",
    ],
    "Auxiliary.FilterEqualFunction": ["Returns a card filter that calls f on the card and extra arguments, then checks whether the result equals value."],
    "Auxiliary.penlimit": ["Special Summon condition helper that returns true only when st contains SUMMON_TYPE_PENDULUM."],
    "Auxiliary.TargetEqualFunction": ["Returns an effect target-value function that calls f on the target card and extra arguments, then checks whether the result equals value."],
    "Auxiliary.tgsval": ["Value helper for self-targeting protection; it returns true when the reason player is the handler's player."],
    "Card.AssumeProperty": [
        "Temporarily assumes one property of c for core checks.",
        "assume_type is one of ASSUME_CODE, ASSUME_TYPE, ASSUME_LEVEL, ASSUME_RANK, ASSUME_ATTRIBUTE, ASSUME_RACE, ASSUME_ATTACK, or ASSUME_DEFENSE.",
    ],
    "Card.GetAttributeInGrave": ["Returns the Attribute c is treated as having in the GY for player, defaulting to the current reason player."],
    "Card.GetPreviousDefenseOnField": ["Returns the DEF value c had while it was previously on the field."],
    "Card.GetSummonLocation": ["Returns the location c was Summoned from, decoded from its summon information."],
    "Card.ReplaceEffect": [
        "Replaces c's effects with the effects of card code under the given reset flags and returns the replacement id.",
        "count defaults to 1; phase resets automatically include both players' turns when no turn side is specified.",
    ],
    "Duel.GetDiceResult": ["Returns the five stored dice-result slots for the current dice event."],
    "Duel.IsPlayerCanSSet": ["Checks whether player can Set Spell/Trap Cards at all, or whether player can Set c as a Spell/Trap Card."],
    "Duel.SetDiceResult": ["Sets the five stored dice-result slots; missing or out-of-range values are stored as 1."],
    "Card.IsCanBeSynchroMaterial": ["Checks whether c can be used as Synchro Material for scard, with tuner supplied when the core needs the paired Tuner."],
    "Duel.GetCounter": ["Returns the total number of countertype counters in player-relative locations s and o."],
    "Duel.GetUsableMZoneCount": [
        "Returns how many Monster Zones player can use for a monster entering the field.",
        "use_player defaults to the current reason player and is used for zone-limit checks involving the acting player.",
    ],
    "Effect.GetCategory": ["Returns e's category bitmask."],
    "Auxiliary.AddFusionProcCodeRep": ["Registers a fixed-count Fusion Material procedure requiring cc monsters with card code code1."],
    "Auxiliary.EnableArcanaCoin": [
        "Registers Arcana Force-style mandatory coin-toss trigger effects on c for event1 and any extra events.",
        "The shared operation records the coin result as FLAG_ID_ARCANA_COIN; Reversal of Fate replaces the toss with a player choice.",
    ],
    "Auxiliary.MZoneSequence": ["Returns the local column index for Monster Zone sequence seq from that controller's viewpoint."],
    "Auxiliary.AddBanishRedirect": ["Registers an EFFECT_LEAVE_FIELD_REDIRECT effect that banishes c when condition is true, defaulting to face-up c."],
    "Auxiliary.AddEquipSpellEffect": [
        "Creates an Equip Spell activation effect for c and registers the matching EFFECT_EQUIP_LIMIT.",
        "The activation effect is returned; when pause is true it is created but not registered on c.",
    ],
    "Auxiliary.AddFusionProcCodeFunRep": ["Registers a Fusion procedure requiring code1 plus between minc and maxc materials that satisfy f."],
    "Auxiliary.AddFusionProcFunFunRep": ["Registers a Fusion procedure requiring f1 plus between minc and maxc materials that satisfy f2."],
    "Card.GetBattledGroupCount": ["Returns the number of cards currently recorded in c's battled-cards set."],
    "Card.GetLinkAttribute": ["Returns the Attribute c uses as Link Material for player, defaulting to the current reason player."],
    "Card.IsNotTuner": ["Checks whether c is treated as a non-Tuner for Synchro Monster scard."],
    "Duel.GetOverlayCount": ["Returns the number of Xyz Materials attached to cards in player-relative locations s and o."],
    "Duel.Readjust": [
        "Requests a field readjust for the current reason effect's handler.",
        "If the same handler requests readjustment more than three times in the current tracking map, the core sends it to the Graveyard by rule instead.",
    ],
    "Auxiliary.IsMaterialListSetCard": ["Checks whether c lists setcode in its material_setcode metadata, including packed sub-set matching."],
    "Auxiliary.qlifilter": [
        "Qli immunity value helper.",
        "It accepts activated monster effects from monsters whose original Level or Rank is lower than the handler's current Level, and rejects Link Monsters.",
    ],
    "Card.GetOriginalRank": ["Returns c's printed Rank from card data, or 0 if c is not an Xyz Monster."],
    "Card.GetRightScale": ["Returns c's current right Pendulum Scale value."],
    "Card.GetSynchroLevel": ["Returns the Synchro Level value c contributes for Synchro Monster scard."],
    "Card.IsCanHaveCounter": ["Checks whether c can hold counters of countertype."],
    "Card.IsDualState": ["Checks whether c is currently affected by EFFECT_DUAL_STATUS."],
    "Card.IsRelateToCard": ["Checks whether c1 currently has a relation to c2."],
    "Auxiliary.AddFusionProcMix": [
        "Registers a fixed-count mixed Fusion Material procedure on fcard.",
        "Each extra argument is a required material slot and may be a card code, filter function, or table of alternatives. Numeric material slots update listed-material metadata.",
    ],
    "Auxiliary.CheckUnionEquip": ["Checks Union equip count compatibility between Union Monster uc and target tc, optionally ignoring some modern Union count."],
    "Auxiliary.linklimit": ["Special Summon condition helper that returns true only when st contains SUMMON_TYPE_LINK."],
    "bit.bxor": ["Returns the bitwise XOR of a and b."],
    "bit.rshift": ["Returns a shifted right by b bits."],
    "Card.CheckUnionTarget": [
        "Checks whether target is a valid Union equip target for c under EFFECT_UNION_LIMIT.",
        "The core also enforces new/old Union count compatibility between c and target.",
    ],
    "Card.EnableDualState": ["Registers an EFFECT_DUAL_STATUS client-hint effect on c."],
    "Card.GetColumnGroupCount": ["Returns the number of cards in columns overlapping c."],
    "Card.GetHandSynchro": [
        "Returns the hand-Synchro enabling effect on c, its target function, and the min/max hand-material counts.",
        "Only Monster Zone cards are checked. EFFECT_HAND_SYNCHRO has priority, then EFFECT_TUNER_MATERIAL_LIMIT with LOCATION_HAND.",
    ],
    "Card.GetTributeRequirement": ["Returns the minimum and maximum Tribute counts for Normal Summoning c."],
    "Card.SetHint": ["Sends a client card-hint message for c with hint type and value; types at or above CHINT_DESC_ADD are ignored."],
    "Duel.CheckChainUniqueness": ["Checks whether all current Chain Links have different handler card codes."],
    "Duel.SelectField": [
        "Lets player select count field zones from location1/location2 after applying filter as unavailable zones.",
        "When desc is supplied, the core shows it as a selection hint. The return value is a bitmask of selected zones from player's viewpoint.",
    ],
    "Group.Remove": ["Removes cards from mutable group g that satisfy f and are not ex, passing any extra arguments to f."],
    "Auxiliary.AddFusionProcShaddoll": ["Registers the Shaddoll Fusion Material procedure requiring one Shaddoll material and one material with attr as Fusion Attribute."],
    "Auxiliary.evospcon": ["Special Summon condition helper for Evolsaur-style effects and set 0x304e monster Special Summons."],
    "Card.GetDestination": ["Returns the destination location currently stored in c's send-to parameters."],
    "Card.GetPreviousAttackOnField": ["Returns the ATK value recorded for c's previous on-field state."],
    "Card.GetRitualLevel": ["Returns the Ritual Level value c contributes for Ritual Monster rc."],
    "Duel.SwapSequence": [
        "Swaps the Monster Zone sequences of c1 and c2 when both are controlled by the same player, both are affected by the current reason effect, and both are in the Monster Zone.",
        "The core raises move events for the swapped cards when the swap occurs.",
    ],
    "Auxiliary.AddFusionProcFunFun": ["Registers a Fusion procedure requiring one material satisfying f1 and cc materials satisfying f2."],
    "Auxiliary.nzdef": ["Returns true for face-up cards with current DEF greater than 0."],
    "bit.lshift": ["Returns a shifted left by b bits."],
    "Duel.GetLinkedGroup": ["Returns a Group of cards in player-relative locations s and o that are linked."],
    "Auxiliary.SelectSameCount": [
        "Lets tp build a selection that contains the same number of cards from g1 and g2.",
        "except is removed from both groups before selection. The result can be nil if min is greater than the computed max.",
    ],
    "Auxiliary.TuneMagicianCheckX": ["Checks whether c has an ecode effect whose value rejects at least one other card in selected group sg."],
    "Auxiliary.IsUnionState": [
        "Returns the equipped Union target for effect's handler when it has EFFECT_UNION_STATUS and is equipped.",
        "The Lua expression returns a truthy Card on success, false when the status effect is missing, or nil when no equip target exists.",
    ],
    "Card.IsLinkCode": [
        "Checks whether c matches any supplied code while used as Link Material.",
        "This includes c's current code, second code, and EFFECT_ADD_LINK_CODE values. If no link-code additions apply, the binding falls back to Card.IsCode.",
    ],
    "Duel.ChangeChainOperation": ["Replaces the operation function of Chain Link chainc with f."],
    "Group.Clear": ["Clears g unless it is a read-only group."],
    "Auxiliary.sumreg": ["For each card in eg whose original code equals e's label, registers a same-code flag effect that lasts through the End Phase/reset."],
    "Card.GetEffectCount": ["Returns the number of effects with code currently found by c's effect filter."],
    "Card.GetPreviousPosition": ["Returns c's previously recorded position value."],
    "Card.IsCanRemoveCounter": ["Checks whether player can remove count counters of countertype from c for reason."],
    "Card.IsLinkSummonable": [
        "Checks whether Link Monster c can be Link Summoned by the current reason player.",
        "Optional materials, lcard, minc, and maxc restrict the Link Material pool and material count used by the core check.",
    ],
    "Card.IsRankBelow": ["Checks whether c has a nonzero Rank that is less than or equal to rank."],
    "Duel.ClearTargetCard": ["Clears the target-card group recorded on the current Chain Link, if one exists."],
    "Duel.LinkSummon": [
        "Starts a rule Link Summon of c for player.",
        "materials, lcard, minc, and maxc become temporary Link Summon limits; the binding yields to the core and returns no Lua value.",
    ],
    "Duel.Win": ["Sets player as the duel winner with reason, but only if no winner has already been set."],
    "Auxiliary.AddFusionProcCode3": ["Registers a Fusion Material procedure requiring monsters with code1, code2, and code3 as fixed materials."],
    "Auxiliary.SameValueCheck": ["Checks whether every card in g shares at least one bit returned by f; groups of 0 or 1 card return true."],
    "Card.GetLinkCode": ["Returns c's Link Material codes: current code, second code when present, then EFFECT_ADD_LINK_CODE values."],
    "Card.GetUnionCount": ["Returns c's modern Union count and old Union count."],
    "Duel.CheckEvent": [
        "Without get_info, returns whether event is present in the current event state.",
        "With get_info true, returns true plus event cards, event player, event value, reason effect, reason, and reason player when found; otherwise returns false.",
    ],
    "Duel.SetSelectedCard": ["Sets the core must-select list to a Card or all cards in a Group for later selection helpers."],
    "Duel.SwapControl": [
        "Swaps control between two Cards or between two Groups and returns whether the swap processor succeeded.",
        "reset_phase and reset_count are optional temporary-control reset settings.",
    ],
    "Group.SelectWithSumEqual": [
        "Lets player select cards from g whose f-sum equals acc using between min and max cards.",
        "Cards previously set with Duel.SetSelectedCard are forced into the sum, removed from the selectable pool, cleared afterward, and are not included in the returned Group.",
    ],
    "Auxiliary.bdcon": ["Battle-destroying condition helper that returns true while the handler is still related to battle."],
    "Card.GetAttackAnnouncedCount": ["Returns c's attack declaration count."],
    "Card.GetTextDefense": ["Returns c's printed/stored DEF value, or 0 while c has no-Level status."],
    "Card.ResetEffect": ["Manually resets effects on c that match code and reset_type."],
    "Card.GetCardTargetCount": ["Returns the number of persistent card targets currently recorded on c."],
    "Card.GetFusionAttribute": ["Returns the Attribute c uses as Fusion Material for player, defaulting to the current reason player."],
    "Card.GetSummonPlayer": ["Returns the player recorded as having Summoned c."],
    "Auxiliary.gbspcon": ["Special Summon condition helper for Gladiator Beast-style returns and set 0x1019 monster Special Summons."],
    "Card.CreateRelation": ["Creates a relation from c1 to c2 that is cleared by reset."],
    "Card.GetMutualLinkedGroupCount": ["Returns the number of cards mutually linked with c."],
    "Card.IsExtraDeckMonster": ["Checks whether c is a card kind treated by the core as an Extra Deck monster."],
    "Duel.AnnounceCoin": ["Lets player choose one of the built-in coin-side options and returns the zero-based option index."],
    "Auxiliary.synlimit": ["Special Summon condition helper that returns true only when st contains SUMMON_TYPE_SYNCHRO."],
    "Card.GetCardTarget": ["Returns a Group containing all persistent card targets currently recorded on c."],
    "Card.GetLinkRace": ["Returns the Race c uses as Link Material for player, defaulting to the current reason player."],
    "Card.IsLinkBelow": ["Checks whether c has a nonzero Link Rating that is less than or equal to link."],
    "Card.IsLinkState": ["Checks whether c is currently in linked state."],
    "Auxiliary.AddXyzProcedureLevelFree": [
        "Registers a Level-free Xyz Summon procedure on c.",
        "This helper uses f, gf, minc, maxc, and optional alternate-summon settings, and returns no explicit value.",
    ],
    "Auxiliary.IsCanBeQuickEffect": ["Checks whether player tp is affected by code, code has a registered quick-effect filter, and that filter accepts c."],
    "Card.GetColumnZone": [
        "Returns the zone bitmask for columns overlapping c within loc.",
        "When player is supplied as the opposing perspective, the core swaps the player/opponent halves of the mask.",
    ],
    "Card.GetFusionCode": [
        "Returns c's Fusion Material codes: current code, second code when present, then EFFECT_ADD_FUSION_CODE values.",
        "When the core is checking with not_material set, only the current and second codes are returned.",
    ],
    "Card.IsOriginalSetCard": ["Checks whether c's original set data matches any supplied set code."],
    "Card.SetFlagEffectLabel": ["Sets the first matching flag effect label for code on c to label and returns whether a flag effect was found."],
    "Group.CheckWithSumGreater": [
        "Checks whether g can satisfy an f-sum of at least acc.",
        "Cards previously set with Duel.SetSelectedCard are forced into the sum and the must-select list is cleared before returning.",
    ],
    "Auxiliary.AddRitualProcEqual2": ["Registers an exact-Level Ritual Summon procedure using Card.GetLevel and returns the created Effect."],
    "Auxiliary.bdgcon": ["Battle-destroying condition helper for a handler whose battle target is a monster in the Graveyard."],
    "Card.GetLinkedGroupCount": ["Returns the number of cards in zones linked by c."],
    "Card.GetPosition": ["Returns c's current position value."],
    "Card.GetRealFieldID": ["Returns c's real field ID, the core field identifier used for relation tracking."],
    "Duel.ChangeTargetCard": ["Replaces the target card group recorded for Chain Link chainc with g."],
    "Card.RemoveCounter": [
        "Removes count counters of countertype from c for reason, using player as the removing player.",
        "When countertype is 0, the core clears every counter on c and returns no Lua value. Otherwise it yields and returns whether the requested counters were removed.",
    ],
    "Duel.CalculateDamage": [
        "Starts damage calculation between attacker and attack_target, or a direct attack when attack_target is nil.",
        "new_attack is optional and is passed to the damage-step processor. If attacker and attack_target are the same card, the binding returns no value and does not start damage calculation.",
    ],
    "Effect.GetProperty": ["Returns e's two property flag fields, flag1 and flag2."],
    "Auxiliary.SetUnionState": [
        "Applies the equipped Union state to c after it becomes equipped.",
        "If c has an EFFECT_UNION_LIMIT effect, this registers the matching EFFECT_EQUIP_LIMIT and EFFECT_UNION_STATUS reset effects. Old Union cards also receive EFFECT_OLDUNION_STATUS.",
    ],
    "Card.IsLinkAbove": ["Checks whether c has a nonzero Link Rating greater than or equal to link."],
    "Card.IsSummonableCard": [
        "Checks whether c's card data represents a monster that is allowed to be Normal Summoned or Set by card kind.",
        "This rejects non-monsters, Extra Deck monsters, Ritual Monsters, Special Summon-only monsters, and Tokens. It does not check current costs, Summon count, locations, or player restrictions.",
    ],
    "Duel.AnnounceRace": ["Lets player declare count Races from available and returns the selected RACE_* bitmask."],
    "Duel.ChangeAttackTarget": [
        "Changes the current attack target to target, or to a direct attack when target is nil, and returns whether the change succeeded.",
        "The current attacker must exist, be able to attack, and not have its attack canceled. A card target must be one of the current legal attack targets; direct attack requires that the attacker is not forbidden from attacking directly.",
    ],
    "Duel.IsPlayerCanSpecialSummon": [
        "With only player, checks whether player is allowed to perform a Special Summon and still has Special Summon count available.",
        "With the optional card-specific arguments, checks whether player can Special Summon c to target_player in sumpos with sumtype, using the current reason effect.",
    ],
    "Duel.ResetFlagEffect": ["Resets all player flag effects with code for player."],
    "Duel.SelectPosition": ["Lets player choose one of the allowed positions for c and returns the selected POS_* value."],
    "Effect.GetCost": ["Returns e's cost function, or nil when no cost function is set."],
    "Card.GetLeftScale": ["Returns c's current left Pendulum Scale value."],
    "Card.GetPreviousAttributeOnField": ["Returns the Attribute value recorded for c's previous on-field state."],
    "Card.GetSummonType": ["Returns c's recorded Summon Type bits masked to the default Summon Type field."],
    "Duel.IsPlayerCanSummon": [
        "With only player, checks whether player is not forbidden from performing a Normal Summon by an untargeted EFFECT_CANNOT_SUMMON.",
        "With sumtype and c, checks player EFFECT_CANNOT_SUMMON restrictions for Normal Summoning c with that sumtype. This binding does not check Summon count, costs, tribute availability, or zone availability.",
    ],
    "Card.CopyEffect": [
        "Copies the initial_effect of card code onto c and returns the generated copy id, or -1 if code belongs to a Normal Monster.",
        "reset defaults to RESETS_STANDARD when 0. count defaults to 1; phase resets without a turn side are normalized to both players' turns. If c is a non-Effect Monster, the core also adds TYPE_EFFECT for the same reset.",
    ],
    "Card.GetMaterialCount": ["Returns the number of cards currently recorded as c's materials."],
    "Card.IsRankAbove": ["Checks whether c has a nonzero Rank greater than or equal to rank."],
    "Duel.CheckPhaseActivity": ["Returns whether an action has been recorded for the current phase."],
    "Auxiliary.Tuner": ["Returns a material filter that accepts cards that are Tuners for syncard and also satisfy f(target, ...), when f is supplied."],
    "Card.GetBattlePosition": ["Returns c's temporary battle-position snapshot."],
    "Card.IsXyzType": ["Checks whether c's type while used as Xyz Material contains type."],
    "Duel.AnnounceLevel": [
        "Lets player declare a Level and returns the declared Level plus the zero-based option index.",
        "min and max default to 1 and 12 and are swapped if min is greater than max. Extra level arguments are excluded from the options; if no Levels remain, the binding returns no value.",
    ],
    "Duel.GetTargetCount": ["Counts cards matching filter in the given field locations that can be used as effect targets, excluding exception when supplied."],
    "Duel.IsCanAddCounter": [
        "With only player, checks whether player is not forbidden from placing counters.",
        "With countertype, count, and c, checks whether player can place that many counters of countertype on c.",
    ],
    "Duel.SendtoExtraP": ["Sends cards to player-side Extra Deck face-up for reason and returns the number of cards moved."],
    "Auxiliary.ritlimit": ["Special Summon condition helper that returns true only when the Summon Type contains SUMMON_TYPE_RITUAL."],
    "Card.GetCurrentScale": [
        "Returns the Pendulum Scale c currently uses.",
        "In a Pendulum Zone, this returns the left or right current scale according to c's zone sequence. Outside a Pendulum Zone, it returns c's printed left scale value.",
    ],
    "Card.GetLocation": ["Returns c's current location, or 0 if c is currently treated as not being on the field."],
    "Duel.AnnounceType": [
        "Lets player choose one of the engine's built-in Monster/Spell/Trap type options and returns the zero-based option index.",
        "The return value is the selected option index, not a TYPE_* bitmask.",
    ],
    "Duel.IsPlayerCanAdditionalSummon": ["Returns true when player has no pending extra Normal Summon marker in core.extra_summon."],
    "Group.GetMinGroup": [
        "Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the minimum value.",
        "The second return is the minimum integer value. If g is empty, this binding returns no Lua values.",
    ],
    "Card.GetPreviousCodeOnField": [
        "Returns the card code recorded for c's previous on-field state.",
        "If the previous state had a second code, that code is returned as a second value.",
    ],
    "Card.IsHasCardTarget": ["Checks whether c1 currently has c2 as a persistent card target."],
    "Duel.GetBattleDamage": ["Returns the battle damage currently recorded for player."],
    "Duel.GetLinkedZone": ["Returns the zone bitmask currently pointed to by Link Markers from player's perspective."],
    "Auxiliary.damcon1": [
        "Condition helper for effects that would make player tp take effect damage.",
        "It checks the operation info for damage to tp, or recovery to tp that is reversed into damage, and respects EFFECT_REVERSE_DAMAGE, EFFECT_REVERSE_RECOVER, and EFFECT_NO_EFFECT_DAMAGE.",
    ],
    "Auxiliary.EnableUnionAttribute": [
        "Registers the standard modern Union Monster package on c.",
        "The helper adds equipped-card destruction substitution, an EFFECT_UNION_LIMIT using filter, an ignition effect to equip c from the Monster Zone to a valid monster, and an ignition effect to Special Summon c from the Spell & Trap Zone.",
    ],
    "Card.GetReason": [
        "Returns c's current reason bitmask/value.",
        "This is the reason recorded in c's current state, such as REASON_EFFECT, REASON_COST, or REASON_BATTLE; it is not limited to position changes.",
    ],
    "Card.IsDefenseBelow": [
        "Checks whether c has known current DEF less than or equal to def.",
        "Link Monsters and non-monsters return false, and unknown or negative DEF also returns false.",
    ],
    "Card.IsFusionCode": [
        "Checks whether c can be treated as any supplied code while used as Fusion Material.",
        "The core includes c's current code, second code, and EFFECT_ADD_FUSION_CODE values. If no Fusion-only code additions apply, or material-code checks are disabled, it falls back to Card.IsCode.",
    ],
    "Auxiliary.EnableDualAttribute": [
        "Registers standard Gemini Monster handling on c.",
        "The card can be Normal Summoned again, and while face-up in the Monster Zone or GY and not in Dual State, it is treated as a Normal Monster instead of an Effect Monster.",
    ],
    "Card.GetPreviousEquipTarget": ["Returns c's previous Equip target, or nil."],
    "Duel.CheckRemoveOverlayCard": [
        "Checks whether player can remove at least count Xyz Materials from the specified own/opponent field locations for reason.",
        "s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. Applicable replacement effects can satisfy the check.",
    ],
    "Auxiliary.IsMaterialListCode": ["Checks whether code is present in c.material, normally populated by AddMaterialCodeList; returns true or nil."],
    "Card.IsChainAttackable": [
        "Checks whether the current attacker can make another attack under chain-attack rules.",
        "This core binding validates c but tests the duel's current attacker. ac defaults to 2, and monsteronly requires an attack target instead of allowing a direct attack.",
    ],
    "Auxiliary.IsDualState": ["Condition helper that is true when e's handler is not disabled and is in Dual State."],
    "Auxiliary.mzctcheckrel": ["Checks whether releasing group g by reason leaves a Monster Zone and g is a valid release group for tp."],
    "Duel.SetChainLimitTillChainEnd": ["Registers a chain-limit callback that persists until the current chain ends."],
    "Duel.IsDamageCalculated": ["Returns whether damage calculation has been performed in the current battle/damage-step state."],
    "Duel.RDComplete": ["Completes reserved step damage/recover processing after Duel.Damage or Duel.Recover is called with is_step=true."],
    "Card.IsReleasableByEffect": ["Checks whether c can be Released by the current resolving effect, using the current reason player and reason effect."],
    "Duel.AdjustInstantly": [
        "Runs immediate field adjustment.",
        "When c is supplied, the core refreshes disable relations for cards related to c before adjusting the field.",
    ],
    "Auxiliary.EnableSpiritReturn": [
        "Registers Spirit return setup for c.",
        "When any listed event happens, it creates End Phase return-to-hand effects in the Monster Zone, respecting EFFECT_SPIRIT_DONOT_RETURN and EFFECT_SPIRIT_MAYNOT_RETURN.",
    ],
    "Card.ResetFlagEffect": ["Resets all flag effects on c with code."],
    "Duel.RemoveOverlayCard": [
        "Lets player remove between min and max Xyz Materials from the specified own/opponent field locations for reason.",
        "s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The return value is the number of materials removed.",
    ],
    "Effect.IsHasCategory": ["Checks whether e's category bitmask contains cate."],
    "Card.GetTurnCounter": ["Returns c's turn counter."],
    "Card.IsLink": ["Checks whether c:GetLink() equals any supplied link value. Nil link arguments are skipped; non-Link cards compare as 0."],
    "Card.IsSynchroType": ["Checks whether c's type while used as Synchro Material contains type."],
    "Duel.ClearOperationInfo": ["Clears operation info for chain ct; it is a no-op if that Chain Link does not exist."],
    "Duel.ShuffleExtra": ["Shuffles player's Extra Deck."],
    "Auxiliary.AddRitualProcGreaterCode": [
        "Registers a Ritual Summon procedure for Ritual Monster code1, allowing material Ritual Levels to meet or exceed the Ritual Monster's original Level.",
        "The helper also adds code1 to c's code/material list and returns the created procedure effect.",
    ],
    "Card.SetTurnCounter": ["Sets c's turn counter."],
    "Auxiliary.AddSynchroMixProcedure": [
        "Registers a mixed Synchro Summon procedure requiring up to three fixed material filters plus f4 repeated between minc and maxc times.",
        "The maximum count is capped by c's Level after subtracting any required fixed materials.",
    ],
    "Auxiliary.nzatk": ["Filter helper that is true for face-up cards with current ATK greater than 0."],
    "Card.SetCounterLimit": ["Adds an EFFECT_COUNTER_LIMIT for countertype to c with value limit."],
    "Group.CheckWithSumEqual": ["Checks whether a subset of g, including any must-select cards, can make the f-sum exactly acc using between min and max cards."],
    "Duel.IsPlayerCanRemove": [
        "With only player, checks whether player is not forbidden from banishing.",
        "With c, checks whether player can banish c for reason; reason defaults to REASON_EFFECT.",
    ],
    "Duel.AnnounceCard": ["Lets player declare a card code matching the optional opcode/filter expression and returns the selected code."],
    "Duel.RaiseSingleEvent": ["Raises a single-card event for ec with code, re, r, rp, ep, and ev, then processes single-card events."],
    "Auxiliary.CreateChecks": ["Returns a table of one-card check functions where each function calls f(c, list[i])."],
    "Auxiliary.RitualCheck": ["Ritual material group predicate that checks zone availability, the requested Greater/Equal level rule, custom mat_group_check, and RCheckAdditional."],
    "Card.IsXyzSummonable": ["Checks whether Xyz Monster c can be Xyz Summoned by the current reason player with an optional material group and min/max constraints."],
    "Duel.XyzSummon": ["Performs a rule Xyz Summon for player and c using an optional material group and min/max constraints."],
    "Auxiliary.bdogcon": ["Condition helper for a battle-destroying monster: the handler is still related to battle, battled an opponent's monster, and that battle target is a monster in the GY."],
    "Card.GetEquipCount": ["Returns the number of Equip Cards currently equipped to c."],
    "Card.GetFirstCardTarget": ["Returns c's first persistent card target, or nil."],
    "Duel.SortDecktop": [
        "Lets sort_player reorder the top count cards of target_player's Main Deck.",
        "Both players must be valid and count must be at least 1. If count is larger than the remaining Deck size, the processor only sorts the available top cards.",
    ],
    "Duel.RemoveCounter": [
        "Lets player remove count counters of countertype from the selected field locations for reason and returns whether removal succeeded.",
        "s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The core can offer applicable counter-removal replacement effects before removing counters.",
    ],
    "Duel.TossDice": [
        "Tosses count1 dice for player and, when count2 is supplied, count2 dice for the opponent.",
        "Valid dice results are integers from 1 to 6. Normal script use should keep count1 + count2 at 5 or less; the core rejects count1 <= 0 and count2 < 0.",
    ],
    "Card.IsLinkAttribute": [
        "Checks whether c's Attribute while used as Link Material contains attribute.",
        "player defaults to the current reason player. The core uses c:GetLinkAttribute(player), so Link Material Attribute-changing effects are included.",
    ],
    "Card.IsOriginalCodeRule": [
        "Checks whether c's rule-original card code matches any supplied code.",
        "Nil code arguments are skipped. For double-code cards, the core checks both rule-original codes; otherwise it checks the card's duel code.",
    ],
    "Duel.GetBattleMonster": [
        "Returns the monster controlled by player that is currently in battle, followed by the monster controlled by the opponent that is currently in battle.",
        "Each return can be nil if there is no attacker or attack target for that controller.",
    ],
    "Duel.SkipPhase": [
        "Applies a temporary field effect that makes player skip phase.",
        "The phase must be one of PHASE_DRAW, PHASE_STANDBY, PHASE_MAIN1, PHASE_BATTLE, PHASE_MAIN2, or PHASE_END. reset_count values of 0 or less are treated as 1, and value is stored on the generated skip effect.",
    ],
    "Card.GetPreviousRaceOnField": ["Returns the Race value recorded for c's previous on-field state."],
    "Card.CreateEffectRelation": [
        "Creates a relation between c and effect e.",
        "If e is the triggering effect of a current Chain Link, the relation is tied to that Chain Link; otherwise the core stores a direct effect relation.",
    ],
    "Card.GetLink": ["Returns c's Link Rating, or 0 if c is not a Link Monster."],
    "Card.IsAttackable": [
        "Checks whether c currently satisfies the core's basic attack-capable conditions.",
        "The card must be face-up Attack Position, or face-up Defense Position with EFFECT_DEFENSE_ATTACK, and it must not be forbidden, unable to attack, attack-disabled, or under a skipped Battle Phase. This does not check attack-announcement costs.",
    ],
    "Card.SetStatus": [
        "Sets or clears status on c.",
        "This is an internal-status helper. The binding does nothing while c is copying another card's effect.",
    ],
    "Duel.AnnounceAttribute": [
        "Lets player declare count Attributes from the available Attribute bitmask and returns the selected Attribute bitmask.",
        "available should be a bitwise combination of ATTRIBUTE_* constants.",
    ],
    "Group.GetMaxGroup": [
        "Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the maximum value.",
        "The second return is the maximum integer value. If g is empty, this binding returns no Lua values.",
    ],
    "bit.bor": ["Returns the bitwise OR of a and b."],
    "Card.IsDefenseAbove": [
        "Checks whether c has current DEF greater than or equal to def.",
        "Link Monsters and cards that are not monsters or currently treated as monsters return false.",
    ],
    "Effect.SetOwnerPlayer": [
        "Sets e's owner player to player.",
        "Only player values 0 and 1 are accepted; any other value leaves the effect unchanged.",
    ],
    "Auxiliary.imval1": ["Default value helper for EFFECT_CANNOT_BE_BATTLE_TARGET; it returns true when c is not immune to e."],
    "Card.GetReasonEffect": ["Returns c's current reason effect, or nil when no reason effect is recorded."],
    "Card.GetTurnID": [
        "Returns c's stored turn ID.",
        "The core updates this value when the card is added to a location, so scripts commonly compare it with Duel.GetTurnCount() for same-turn timing checks.",
    ],
    "Card.IsDisabled": ["Checks whether c currently has STATUS_DISABLED."],
    "Duel.NegateSummon": [
        "Negates a current Normal Summon, Flip Summon, or Special Summon for targets.",
        "targets may be a Card or Group. Normal and Flip Summon negation require a single card; Special Summon negation can process a group and only negates cards whose Summon is negatable by the current reason effect. The core raises the matching *_SUMMON_NEGATED event and returns no Lua value.",
    ],
    "Duel.SelectDisableField": [
        "Lets player select count available field zones from the requested own-side and opponent-side locations, then returns the selected zone bitmask.",
        "location1 applies to player's field and location2 applies to the opponent's field. The core clamps count to the available number of zones and returns no value if no zone can be selected.",
    ],
    "Duel.IsPlayerCanSpecialSummonCount": [
        "Checks whether player can perform count Special Summons under the current remaining Special Summon-count limits.",
        "The core checks EFFECT_LEFT_SPSUMMON_COUNT effects and the player's Special Summon counter.",
    ],
    "Card.CheckEquipTarget": [
        "Checks whether c2 is a valid Equip target for c1.",
        "The core requires c1 to be affected by an EFFECT_EQUIP_LIMIT that accepts c2, and it also enforces old and modern Union count limits.",
    ],
    "Card.GetOriginalCodeRule": [
        "Returns c's rule-original card code.",
        "Double-code cards return two codes: the printed original code and the second rule code. Other cards return only the duel code used by the core.",
    ],
    "Auxiliary.chainreg": [
        "Registers FLAG_ID_CHAINING on e's handler if that flag is not already present.",
        "The flag resets by the standard event reset, except turn Set reset, and also at the end of the Chain.",
    ],
    "Duel.EnableGlobalFlag": ["Enables the supplied core global_flag bit for the Duel and returns no Lua value."],
    "Duel.TossCoin": [
        "Tosses count coins for player and returns one integer result per toss.",
        "Results are 0 or 1. Normal script use passes a positive count up to MAX_COIN_COUNT; the binding rejects 0 and values below -1, and clamps large positive counts to the core maximum.",
    ],
    "Card.GetColumnGroup": [
        "Returns a Group containing cards in the same column as c.",
        "This MDPro3/YGOPro binding only takes c. It uses c's current on-field column, including related Monster Zones, Spell & Trap Zones, and Extra Monster Zone column relationships; if c is not on the field, the returned Group is empty.",
    ],
    "Duel.GetFirstMatchingCard": [
        "Returns the first card in the specified locations that satisfies f and is not excluded by ex.",
        "f may be nil. ex may be a Card, a Group, or nil, and extra arguments after ex are passed to f. Returns nil when no matching card is found.",
    ],
    "Card.IsFusionAttribute": [
        "Checks whether c's Attribute while used as Fusion Material contains attribute.",
        "player defaults to the current reason player. The core uses c:GetFusionAttribute(player), so Fusion Material Attribute-changing effects are included.",
    ],
    "Duel.GetActivityCount": [
        "Returns activity counts for player in the same order as the requested activity_type values.",
        "Supported built-in activity types are ACTIVITY_SUMMON, ACTIVITY_NORMALSUMMON, ACTIVITY_SPSUMMON, ACTIVITY_FLIPSUMMON, ACTIVITY_ATTACK, and ACTIVITY_BATTLE_PHASE. Other values, including ACTIVITY_CHAIN in this binding, return 0.",
    ],
    "Effect.UseCountLimit": [
        "Manually consumes count uses of e's count limit for player p.",
        "count defaults to 1. If oath_only is true, the count is consumed only when e's count code includes EFFECT_COUNT_CODE_OATH; otherwise the binding decrements the count limit directly.",
    ],
    "Card.GetOriginalRace": ["Returns c's original Race from card data, or 0 while c is marked with STATUS_NO_LEVEL."],
    "Card.GetOverlayCount": ["Returns the number of current Xyz Materials attached to c."],
    "Card.IsCanAddCounter": [
        "Checks whether the current reason player can place count counters of countertype on c.",
        "When loc is 0, c must currently be face-up on the field. When loc is nonzero, the counter permit range is checked against loc instead. If singly is true, counter limits are tested as current count + 1 rather than current count + count.",
    ],
    "Duel.SetLP": ["Sets player's LP to lp, clamping negative lp values to 0, and sends the LP update message."],
    "Auxiliary.AddFusionProcCodeFun": [
        "Registers a Fusion Summon procedure on c requiring code1 and cc additional Fusion Materials matching f.",
        "The helper builds cc copies of f and forwards them to Auxiliary.AddFusionProcMix together with sub and insf.",
    ],
    "Duel.AnnounceNumber": [
        "Lets player choose one of the supplied numbers.",
        "Returns the selected number and the core's 0-based option index for that number.",
    ],
    "Card.GetBaseDefense": ["Returns c's current base DEF. Unknown or negative base DEF values are clamped to 0 by this binding."],
    "Card.SetSPSummonOnce": [
        "Marks c as sharing a once-per-turn Special Summon limit under spsummon_code.",
        "Cards with the same nonzero spsummon_code share the limit for each player. The binding does nothing while c is copying another card's effect.",
    ],
    "Card.IsPreviousSetCard": [
        "Checks whether c's previous card-code or added previous set-code data matches any supplied setcode value.",
        "Nil setcode arguments are skipped. This uses the previous state recorded before the last relevant field or position update, not c's current Set membership.",
    ],
    "Duel.IsAbleToEnterBP": [
        "Checks whether the current turn player can still enter the Battle Phase.",
        "The core requires the duel to allow first-turn attacks or not be turn 1, the current phase to be before PHASE_BATTLE_START, and the turn player not to be affected by EFFECT_CANNOT_BP.",
    ],
    "Duel.CheckTribute": [
        "Checks whether there is a valid Tribute set for Normal Summoning or Setting c.",
        "max defaults to min, mg can restrict the candidate pool, toplayer defaults to c's current controller, and zone defaults to the current extra-summon zone limit when present or 0x1f otherwise.",
    ],
    "Effect.GetActivateLocation": ["Returns the location from which effect e was activated."],
    "Card.AddMonsterAttribute": [
        "Adds temporary monster properties to c through effects.",
        "The binding clears STATUS_NO_LEVEL, applies EFFECT_PRE_MONSTER with type, and applies Attribute, Race, Level, base ATK, and base DEF changes for nonzero supplied values.",
    ],
    "Card.GetPreviousTypeOnField": ["Returns the Type value recorded for c's previous on-field state."],
    "Duel.GetFieldCard": [
        "Returns the card at player, location, and sequence, or nil if that slot is empty or invalid.",
        "The binding also returns nil while the card at that slot is in Summoning or Special Summon step status. Field Zone sequence 0 maps to the Field Zone, and Pendulum Zone sequences 0 and 1 only return cards currently marked as Pendulum Zone cards.",
    ],
    "Card.GetOriginalAttribute": ["Returns c's original Attribute from card data, or 0 while c is marked with STATUS_NO_LEVEL."],
    "Duel.SelectTribute": [
        "Lets player select min to max Tribute candidates for Normal Summoning or Setting c and returns the selected Group.",
        "mg can restrict the candidate pool. toplayer defaults to player; when toplayer differs, the core builds the extra release list for Tributing to that player's field.",
    ],
    "Auxiliary.bdocon": ["Condition helper for EVENT_BATTLE_DESTROYING effects; it returns true when the handler is still related to battle and battled an opponent's monster."],
    "Card.IsCanBeXyzMaterial": [
        "Checks whether c can be used as Xyz Material, optionally for sc.",
        "The core rejects Tokens, cards whose Xyz-material type is not a monster, cards with STATUS_FORBIDDEN, and applicable EFFECT_CANNOT_BE_XYZ_MATERIAL effects.",
    ],
    "Card.GetPreviousControler": ["Returns c's previous controller value."],
    "Card.GetEquipGroup": ["Returns the Equip Cards currently equipped to c as a Group."],
    "Card.GetLinkedGroup": ["Returns the cards currently occupying zones linked by c."],
    "Card.GetLinkedZone": [
        "Returns the linked-zone bitmask generated by c.",
        "By default the bitmask is from c's controller perspective. Passing the opponent as player swaps the self and opponent halves to that player's perspective.",
    ],
    "Card.GetPreviousSequence": ["Returns c's previous sequence value."],
    "Duel.ChainAttack": [
        "Marks the current attacker so it can make another attack, optionally against card c.",
        "The binding only sets chain-attack state. It returns no Lua value and does nothing if there is no current attacker or the attacker is not affected by the resolving effect.",
    ],
    "Duel.IsCanRemoveCounter": [
        "Checks whether player can remove count counters of countertype for reason from the selected field locations.",
        "s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective.",
    ],
    "Card.IsControlerCanBeChanged": [
        "Checks whether control of c can currently move to the other player.",
        "The card must be in the Monster Zone and must not be affected by EFFECT_CANNOT_CHANGE_CONTROL. Unless ignore_mzone is true, the opponent must also have an available Monster Zone in zone.",
    ],
    "Duel.NegateAttack": [
        "Attempts to negate the current attack and returns whether the attack was successfully negated.",
        "The core fails if there is no valid current attacker, if the attacker moved or changed field ID, if the attacker cannot attack, if the Damage Step state blocks attack negation, or if the attacker is not affected by the resolving effect.",
    ],
    "Card.GetCounter": [
        "Returns counters on c for countertype.",
        "When countertype is 0, this core returns the number of different counter types currently present on c, not the total number of all counters.",
    ],
    "Card.GetDefense": ["Returns c's current DEF. Unknown or negative DEF values are clamped to 0 by this binding."],
    "Card.IsDefensePos": ["Checks whether c's current position contains POS_DEFENSE."],
    "Card.IsReleasable": [
        "Checks whether c can be Released for a non-Summon reason by the current reason player.",
        "reason defaults to REASON_COST. The core rejects cards being Summoned, Xyz Materials, cards in the GY or banished, Spell/Trap Cards in the hand, cards the player cannot release, and cards affected by EFFECT_UNRELEASABLE_NONSUM.",
    ],
    "Card.SetCardTarget": [
        "Registers c2 as a persistent card target of c1.",
        "This stores a card-target relation used by functions such as Card.GetCardTarget and by related-card disable checks; it is separate from Duel.SelectTarget's Chain target list.",
    ],
    "Auxiliary.exccon": ["Condition helper for effects that cannot be activated during the same turn their handler was sent to the GY, unless that handler was returned."],
    "Card.GetOriginalLevel": ["Returns c's original Level from card data, or 0 for Xyz Monsters, Link Monsters, and cards marked with STATUS_NO_LEVEL."],
    "Group.RemoveCard": ["Removes c from g. The function mutates g unless g is read-only and returns no Lua value."],
    "Auxiliary.AddFusionProcCode2": [
        "Registers a Fusion Summon procedure on c requiring materials with card codes code1 and code2.",
        "The helper forwards sub and insf unchanged to Auxiliary.AddFusionProcMix.",
    ],
    "Duel.IsEnvironment": [
        "Checks whether code is currently treated as the environment card or as a matching face-up card in the requested locations.",
        "player defaults to PLAYER_ALL and loc defaults to LOCATION_ONFIELD. The core checks Field Zones first; if no face-up Field Zone card exists, it can also match the latest EFFECT_CHANGE_ENVIRONMENT effect.",
    ],
    "Auxiliary.indoval": ["Value helper for indestructibility against opponent's effects; it returns true when rp is the opponent of e's handler player."],
    "Duel.RaiseEvent": [
        "Raises event code for a Card or Group with the supplied effect, reason, reason player, event player, and event value.",
        "The core processes instant events after raising the event and yields without returning Lua values.",
    ],
    "Auxiliary.GCheckAdditional": [
        "Global additional subgroup-check hook used by Group.CheckSubGroup and related selection helpers.",
        "The default implementation returns true. Summon and selection procedures temporarily replace this function to enforce extra group constraints, then restore it.",
    ],
    "Card.IsRank": [
        "Checks whether c:GetRank() equals any supplied rank value.",
        "Nil rank arguments are skipped. The binding compares the numeric Rank directly; it does not separately require c to be an Xyz Monster, so non-Xyz cards compare as Rank 0.",
    ],
    "Card.GetTextAttack": [
        "Returns the ATK value recorded in c's card data.",
        "This is the printed/database value, not the current ATK. Unlike Card.GetAttack, the binding does not clamp unknown ATK to 0, except cards marked STATUS_NO_LEVEL return 0.",
    ],
    "Duel.CheckLocation": ["Checks whether player can use the given sequence in location."],
    "Card.GetRank": [
        "Returns c's current Rank.",
        "Non-Xyz cards return 0. Xyz Monsters outside the Monster Zone return their original Rank; in the Monster Zone, Rank-changing effects are applied and the result is at least 1.",
    ],
    "Card.GetOriginalCode": ["Returns c's original card code from card data."],
    "Card.IsDefense": [
        "Checks whether c is not a Link Monster, is a monster or currently treated as one, and has current DEF equal to any supplied def value.",
        "Nil def arguments are skipped. Unlike the old imported text, the binding does not explicitly require c to be in the Monster Zone.",
    ],
    "Auxiliary.fuslimit": ["Special Summon condition helper that returns true when summon type st contains SUMMON_TYPE_FUSION."],
    "Card.IsAbleToChangeControler": ["Checks only whether c is free of EFFECT_CANNOT_CHANGE_CONTROL."],
    "Group.Sub": ["Removes every card in g2 from g1. g1 is mutated unless it is read-only; g2 is not changed."],
    "Card.IsFusionType": [
        "Checks whether c's type while used as Fusion Material contains type.",
        "For an original Monster Card in the Spell & Trap Zone, the core uses the card-data type while material checks are active; otherwise it uses c's current type.",
    ],
    "Duel.ReturnToField": [
        "Returns a card temporarily removed from the field to its previous controller and previous location.",
        "pos defaults to the previous position and zone defaults to 0xff. If c was not removed for REASON_TEMPORARY, the binding returns no Lua value; otherwise it yields and returns whether the move succeeded.",
    ],
    "Duel.SetChainLimit": [
        "Registers a temporary chain-limit callback for the current Chain window.",
        "The callback is stored with the current reason player and is later called as f(e, chain_player, activating_player). If it returns false, that effect cannot be chained.",
    ],
    "Card.CheckRemoveOverlayCard": [
        "Checks whether player can remove at least count Xyz Materials from c for reason.",
        "Replacement effects with EFFECT_OVERLAY_REMOVE_REPLACE can make this return true even when c itself has too few materials.",
    ],
    "Card.IsDestructable": [
        "Checks whether c can be destroyed.",
        "Without e, the core only rejects Xyz Materials and cards already in the GY or banished. With e, it checks whether c is affected by e and whether effect-destruction protection applies for the current reason player.",
    ],
    "Card.RemoveOverlayCard": [
        "Lets player remove between min and max Xyz Materials from c for reason and returns the number actually removed.",
        "The core also offers applicable EFFECT_OVERLAY_REMOVE_REPLACE effects before selecting materials.",
    ],
    "Auxiliary.IsCodeListed": [
        "Checks whether code is registered in c's card_code_list by Auxiliary.AddCodeList or a related helper.",
        "The Lua helper returns true for a listed code and nil otherwise, so it is normally used as a truthy check.",
    ],
    "Card.IsCanOverlay": [
        "Checks whether c can be used as Xyz Material by player.",
        "player defaults to the current reason player. The core rejects Tokens, forbidden cards in invalid states, and cards controlled by the other player that cannot change control.",
    ],
    "Card.GetReasonPlayer": ["Returns c's current reason player, the player recorded in c's current reason state."],
    "Group.SelectUnselect": [
        "Lets player choose one card from cg to add to the current selection or one card from sg to remove from it, then returns the card that was chosen.",
        "sg may be nil. finishable controls whether the selection can finish at its current size, cancelable allows cancellation, and cancellation returns nil. min and max default to 1.",
    ],
    "Card.GetAttribute": [
        "Returns c's current Attribute bitmask.",
        "Cards treated as having multiple Attributes can return a bitwise combination of ATTRIBUTE_* values.",
    ],
    "Effect.GetOwnerPlayer": ["Returns the player stored as e's owner player."],
    "Card.GetOriginalType": ["Returns c's original card-data type bitmask, not its current modified type."],
    "Card.IsAttack": [
        "Checks whether c is a monster or currently treated as one, and whether its current ATK equals any supplied atk value.",
        "Nil atk arguments are skipped. Non-monsters that are not treated as monsters return false.",
    ],
    "Duel.GetCurrentChain": ["Returns the number of Chain Links currently stored in the active Chain."],
    "Auxiliary.ExceptThisCard": ["Returns e's handler while that card is still related to the current Chain; otherwise returns nil."],
    "Group.CreateGroup": ["Creates and returns a new empty Group."],
    "Card.GetReasonCard": ["Returns c's current reason card, or nil when no reason card is recorded."],
    "Card.GetOverlayGroup": ["Returns a Group containing the cards currently attached to c as Xyz Materials."],
    "Card.IsAttackPos": ["Checks whether c's current position contains POS_ATTACK."],
    "Card.IsCanChangePosition": [
        "Checks the core's effect-specific position-change capability for c.",
        "In this MDPro3/YGOPro core, that helper returns false for Link Monsters and true for other cards; it does not perform the broader manual battle-position-change checks.",
    ],
    "Duel.ConfirmDecktop": [
        "Reveals up to count cards from the top of player's Main Deck to the client.",
        "count is clamped to the remaining Deck size. The function yields for the reveal wait and returns no Lua values.",
    ],
    "Auxiliary.MustMaterialCheck": [
        "Checks whether tp's required-material effects of type code are satisfied.",
        "When v is nil, the helper succeeds only if Duel.GetMustMaterial(tp, code) is empty, except for the hard-coded Xyz and Synchro material exceptions present in the utility script. When v is supplied, it returns Duel.CheckMustMaterial(tp, v, code).",
    ],
    "Effect.IsActivated": ["Checks whether e has one of the EFFECT_TYPES_CHAIN_LINK type bits."],
    "Group.GetSum": ["Calls f for each card in g, forwards any extra arguments, and returns the sum of the integer values produced."],
    "Card.AddCounter": [
        "Attempts to add count counters of countertype to c and returns whether the core accepted the addition.",
        "The card must be affected by the resolving reason effect. The current reason player is used as the player adding the counters. When singly is true, counter-limit checks allow a partial addition up to the remaining limit.",
    ],
    "Duel.MoveSequence": [
        "Moves c to sequence seq within its current controller and location if c is affected by the resolving reason effect.",
        "The core raises EVENT_MOVE for the moved card and returns no Lua values.",
    ],
    "Auxiliary.AddFusionProcFun2": ["Registers a Fusion Summon procedure on c that requires one material satisfying f1 and one material satisfying f2."],
    "Group.RandomSelect": [
        "Returns a new Group containing count randomly chosen cards from g.",
        "count is clamped to g's size. The player argument is written to the random-selection message but does not influence the random choice.",
    ],
    "Card.IsAttackAbove": [
        "Checks whether c is a monster or currently treated as one, and whether its current ATK is at least atk.",
        "Unlike Card.IsAttackBelow, this core does not add a separate guard for unknown ATK before comparing.",
    ],
    "Card.IsLinkRace": ["Checks whether c's Race while used as Link Material for player contains race. player defaults to the current reason player."],
    "Auxiliary.SelectFromOptions": [
        "Filters option tables by their condition, calls Duel.SelectOption with the available option labels, and returns the selected table's custom value or original index.",
        "Each option is {condition, option[, value]}. If no condition is true, the helper returns nil. Its default index return is 1-based, unlike Duel.SelectOption's 0-based return.",
    ],
    "Card.IsCanBeFusionMaterial": [
        "Checks whether c can be used as Fusion Material for fc and summon_type.",
        "fc is optional and summon_type defaults to SUMMON_TYPE_FUSION. The binding has no ignore_mon argument; it delegates to the core Fusion Material legality checks.",
    ],
    "Card.IsLinkType": ["Checks whether c's type while used as Link Material contains type."],
    "Card.IsLinkSetCard": ["Checks whether c can be treated as any supplied setcode while used as Link Material. Nil setcode arguments are skipped."],
    "Auxiliary.AddFusionProcFunRep": ["Registers a Fusion Summon procedure on c that requires cc materials satisfying the same material filter f."],
    "Card.GetFlagEffectLabel": [
        "Returns the first label value from each flag effect with the given code on c.",
        "If c has no matching flag effect, the core returns nil. Matching flag effects with no label return 0 for that slot.",
    ],
    "Card.GetMaterial": ["Returns a Group containing the cards currently stored as c's material cards."],
    "Duel.GetChainMaterial": [
        "Returns the first EFFECT_CHAIN_MATERIAL effect currently applying to player, or nil if none applies.",
        "Fusion-style scripts use the returned effect's target and operation callbacks to handle Chain Material alternatives.",
    ],
    "Duel.NegateRelatedChain": [
        "For each current Chain Link whose triggering effect is handled by c and still related to c, registers a temporary EFFECT_DISABLE_CHAIN effect on c.",
        "The generated disable effect resets with RESET_CHAIN, RESET_EVENT, and the supplied reset flags. The core does nothing if there is no earlier Chain Link to disable or if c is unaffected by the resolving effect.",
    ],
    "Card.IsSummonLocation": ["Checks whether c's recorded Summon location contains loc."],
    "Card.GetFieldID": [
        "Returns c's current field ID, the core timestamp assigned when c moved to its current place.",
        "Smaller values are older. This differs from Card.GetRealFieldID, which tracks the real field ID used by battle-state checks.",
    ],
    "Effect.GetFieldID": ["Returns e's internal field ID."],
    "Effect.IsHasProperty": [
        "Checks whether e contains the requested effect property flags.",
        "prop1 is checked against the first property word and optional prop2 against the second property word. Passing 0 for a word makes that word pass.",
    ],
    "Card.CheckUniqueOnField": [
        "Checks whether c can coexist on check_player's field under the current unique-on-field rules.",
        "check_location defaults to LOCATION_ONFIELD and is masked to on-field locations. icard can be supplied as an ignored card when testing a pending move.",
    ],
    "Duel.GetDecktopGroup": ["Returns a Group containing up to count cards from the top of player's Deck."],
    "Duel.GetFusionMaterial": [
        "Returns two Groups for player: all currently usable Fusion Material candidates, then the base material pool from the requested locations.",
        "location defaults to LOCATION_HAND + LOCATION_MZONE. Extra Fusion Material effects in the Spell & Trap Zone or GY are added to the first returned Group, while the second Group contains only cards from location.",
    ],
    "Card.EnableCounterPermit": [
        "Registers a single-card counter permit effect allowing c to receive counters of countertype in the chosen range.",
        "If location is omitted, monsters default to LOCATION_MZONE and non-monsters default to LOCATION_SZONE + LOCATION_FZONE. An optional condition callback is stored on the permit effect.",
    ],
    "Card.IsCanTurnSet": [
        "Checks whether c can be turned face-down by the current reason player.",
        "The core returns false for Link Monsters, Tokens, already face-down cards, and cards or players affected by EFFECT_CANNOT_TURN_SET.",
    ],
    "Duel.AddCustomActivityCounter": [
        "Registers a custom activity counter with id counter_id for the selected ACTIVITY_* type.",
        "For Summon and attack counters, f is called with a Card and the counter increases when f returns false. For ACTIVITY_CHAIN, f is called with effect, player, chain_id and also counts false results.",
    ],
    "Card.IsAttackBelow": [
        "Checks whether c is a monster, or treated as one, whose current ATK is known and less than or equal to atk.",
        "Cards with unknown ATK return false because the core requires the current ATK to be at least 0.",
    ],
    "Duel.GetCustomActivityCount": [
        "Returns player 0's or player 1's count for the custom counter_id and ACTIVITY_* type.",
        "Counts are reset each turn. In this core, most card-based custom counters only record whether that player has performed a counted activity at least once, while Chain counters can increase and decrease with Chain creation and cancellation.",
    ],
    "Card.IsCanBeSpecialSummoned": [
        "Checks whether c can be Special Summoned by effect e using sumtype, sumplayer, sumpos, target player, and optional zone.",
        "If nocheck is true, c's Summoning condition is skipped. If nolimit is true, c's revive limit or proper-Summon limit is skipped.",
    ],
    "Card.IsCode": ["Checks whether c's current card code, or alternate code if it has one, matches any supplied code."],
    "Duel.GetFirstTarget": [
        "Returns the first target card currently recorded for the resolving Chain.",
        "If multiple target cards were recorded, the remaining target cards are returned as additional values in recorded order.",
    ],
    "Duel.GetMatchingGroup": [
        "Returns a Group containing cards from the specified locations that satisfy filter f and are not excluded by ex.",
        "s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.",
    ],
    "Duel.IsExistingTarget": [
        "Checks whether the specified locations contain at least count cards that satisfy filter f, are not excluded by ex, and can be targeted by the currently handled effect.",
        "Use this in Target callbacks when the card must become an official effect target.",
    ],
    "Duel.SelectTarget": [
        "Lets sel_player choose min to max cards that satisfy filter f, are not excluded by ex, and can be targeted by the currently handled effect.",
        "The selected cards are also registered as the current Chain's target cards.",
    ],
    "Duel.SpecialSummon": [
        "Special Summons targets to target_player's field in position pos and returns the number of cards successfully Summoned.",
        "sumplayer is the player performing the Summon and sumtype records the Summon type. nocheck skips Summoning-condition checks; nolimit skips revive-limit checks.",
    ],
    "Effect.SetCost": [
        "Sets e's cost callback. For activated effects, the callback checks whether the cost can be paid and then pays it.",
        "Cost callbacks should only test legality when chk is 0; irreversible payment belongs in the nonzero chk branch.",
    ],
    "Effect.SetTargetRange": [
        "Sets e's target range fields and clears EFFECT_FLAG_ABSOLUTE_TARGET.",
        "For most field effects, s_range is the affected locations on the handler's controller's side and o_range is the affected locations on the opponent's side. With EFFECT_FLAG_SPSUM_PARAM, they store Special Summon destination player and position.",
    ],
    "Group.Filter": [
        "Returns a new Group containing cards from g that satisfy filter f and are not excluded by ex.",
        "Extra arguments after ex are passed to f after the card argument.",
    ],
    "Group.GetFirst": ["Returns the first card in g and resets g's internal iterator to that card. Returns nil when g is empty."],
    "Group.GetNext": ["Advances g's internal iterator and returns the next card, or nil when there are no more cards."],
    "Group.IsExists": [
        "Checks whether at least count cards in g satisfy filter f and are not excluded by ex.",
        "Extra arguments after ex are passed to f after the card argument.",
    ],
    "Group.Select": ["Lets player choose min to max cards from g, optionally excluding ex, and returns the selected Group."],
    "Auxiliary.Stringid": ["Returns the card-string id for card code and string index id. The index starts at 0 and is commonly passed to Effect.SetDescription, Duel.Hint, or selection prompts."],
    "Card.IsFaceup": ["Checks whether c is in face-up position."],
    "Card.IsLocation": [
        "Checks whether c is currently in location.",
        "Cards treated as not being on the field return false for field locations, including during a Summon before it successfully reaches the Monster Zone.",
    ],
    "Card.IsRelateToEffect": [
        "Checks whether c is still related to effect e.",
        "When an effect enters the Chain, its handler and cards selected with Duel.SetTargetCard or Duel.SelectTarget are related to that effect. That relation is normally lost once the card leaves its expected place.",
    ],
    "Card.IsSetCard": ["Checks whether c belongs to any of the supplied set codes."],
    "Card.IsType": ["Checks whether c has at least one of the type flags in type."],
    "Card.RegisterEffect": [
        "Registers effect e to card c and returns the generated effect field ID.",
        "Registration also makes c the effect handler. If the card is unaffected by the current reason effect, registration can fail unless forced is true.",
    ],
    "Duel.GetLocationCount": [
        "Returns how many zones of location are available on player's field and the corresponding usable zone mask.",
        "location is normally LOCATION_MZONE or LOCATION_SZONE. use_player, reason, and zone are used by effects that restrict where cards can be placed, such as Kaiser Colosseum-style restrictions.",
    ],
    "Duel.Hint": [
        "Sends a hint message of hint_type to player using desc as the message id.",
        "For HINT_SELECTMSG, desc is also stored as that player's last selection hint. HINT_OPSELECTED is displayed to the other player.",
    ],
    "Duel.IsExistingMatchingCard": [
        "Checks whether the specified locations contain at least count cards that satisfy filter f and are not excluded by ex.",
        "s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.",
    ],
    "Duel.SelectMatchingCard": [
        "Lets sel_player choose min to max cards from the specified locations that satisfy filter f and are not excluded by ex.",
        "s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.",
    ],
    "Effect.CreateEffect": ["Creates a new empty Effect object owned by card c."],
    "Effect.GetHandler": ["Returns the card currently handling e, usually the card that registered it with Card.RegisterEffect."],
    "Effect.SetAbsoluteRange": [
        "Sets e's target range from an absolute player viewpoint and marks the effect with EFFECT_FLAG_ABSOLUTE_TARGET.",
        "If playerid is 1, the supplied ranges are swapped internally so the stored ranges still line up with player 0/player 1 absolute handling.",
    ],
    "Effect.SetCategory": [
        "Sets e's operation category flags, such as CATEGORY_DESTROY, CATEGORY_TOHAND, or CATEGORY_SPECIAL_SUMMON.",
        "Categories describe what the effect may do; known operation details should still be recorded with Duel.SetOperationInfo in the Target callback.",
    ],
    "Effect.SetCode": ["Sets e's code. For triggered effects this is usually an event code; for continuous effects it is the effect code being applied."],
    "Effect.SetCondition": ["Sets e's condition callback. The callback decides whether the effect can apply or be activated in the current context."],
    "Effect.SetCountLimit": [
        "Sets how many times e can be used before its count limit is spent.",
        "If count is 0, the core treats it as 1. Effects that share a nonzero code share the same usage count. EFFECT_COUNT_CODE_CHAIN is stored together with EFFECT_COUNT_CODE_SINGLE.",
    ],
    "Effect.SetDescription": ["Sets e's description id, usually produced with Auxiliary.Stringid for card text choices."],
    "Effect.SetOperation": ["Sets e's operation callback. Passing nil clears the operation."],
    "Effect.SetProperty": [
        "Sets e's property flags. prop1 holds the normal effect property flags; prop2 is used for the second property word when needed.",
        "Internal flags are preserved when prop1 is replaced.",
    ],
    "Effect.SetRange": ["Sets the location range where e applies or can be activated."],
    "Effect.SetReset": [
        "Sets when e resets and how many reset checks it can survive.",
        "If reset_count is 0 or omitted, the core stores 1. When a phase reset is used without an explicit turn side, the core applies both RESET_SELF_TURN and RESET_OPPO_TURN.",
    ],
    "Effect.SetTarget": ["Sets e's target callback. For activated effects, this callback performs activation legality checks and records target or operation information."],
    "Effect.SetType": [
        "Sets e's effect type flags.",
        "The core normalizes some type combinations: Spell/Trap activation effects become field activation effects, Flip Effects receive EVENT_FLIP handling, and ignition/Quick Effects gain field behavior.",
    ],
    "Effect.SetValue": ["Sets e's value field. The value can be a number, boolean, or callback function depending on the effect code."],
    "Group.GetCount": ["Returns the number of cards in g."],
    "Card.IsControler": ["Checks whether c's current controller is controler."],
    "Card.IsRace": ["Checks whether c currently has at least one Race flag from race."],
    "Card.IsAbleToHand": [
        "Checks whether c can be returned or added to the hand by the current reason player.",
        "An optional player argument can be passed when a specific player is performing the action.",
    ],
    "Card.EnableReviveLimit": ["Marks c as needing to be properly Summoned before it can be Special Summoned from public locations."],
    "Duel.ConfirmCards": [
        "Reveals a Card or Group to player and waits for the client confirmation.",
        "If skip_panel is true, the client skips the extra confirmation panel when possible.",
    ],
    "Effect.Clone": ["Creates and returns a new Effect object copied from e."],
    "Group.Clone": ["Creates and returns a new Group containing the same cards as g."],
    "Duel.GetChainInfo": [
        "Returns information fields from chainc in the same order as the requested CHAININFO_* constants.",
        "Use chainc=0 for the currently resolving Chain. Unknown requested fields return nil, and no values are returned if the Chain does not exist.",
    ],
    "Duel.RegisterEffect": ["Registers e as a player/global effect for player."],
    "Duel.BreakEffect": [
        "Separates the current resolving effect into a later timing window, then raises EVENT_BREAK_EFFECT.",
        "Use this when card text says to do one action, then do another action afterward, so later triggers do not see both actions as simultaneous.",
    ],
    "Effect.SetHintTiming": ["Sets when the client should offer or highlight e for the handler's controller and, optionally, the opponent."],
    "Effect.SetLabel": ["Stores one or more integer label values on e, replacing any previous labels."],
    "Effect.GetLabel": ["Returns e's stored integer labels. If no label was set, returns 0."],
    "Effect.SetLabelObject": ["Stores a Card, Group, Effect, or nil as e's label object."],
    "Effect.GetLabelObject": ["Returns e's stored label object, or nil if none is stored or the object is no longer valid."],
    "Card.IsAttribute": ["Checks whether c currently has at least one Attribute flag from attribute."],
    "Auxiliary.NecroValleyFilter": ["Returns a wrapper filter that requires f(target, ...) and also rejects cards currently protected by Necrovalley while the Chain is disablable."],
    "Duel.SelectYesNo": ["Asks player a yes/no prompt using description id desc and returns true for Yes."],
    "Card.IsReason": ["Checks whether c's current reason flags include reason."],
    "Card.GetControler": ["Returns c's current controller."],
    "Duel.GetTurnPlayer": ["Returns the current turn player."],
    "Card.IsOnField": ["Checks whether c is currently on the field and is not being treated as off the field."],
    "Effect.IsActiveType": ["Checks whether e's active card type contains at least one flag from type."],
    "Card.IsPreviousLocation": ["Checks whether c's previous location included location."],
    "bit.band": ["Returns the bitwise AND of a and b."],
    "Card.IsFacedown": ["Checks whether c is in face-down position."],
    "Effect.GetHandlerPlayer": ["Returns the current controller of e's handler."],
    "Duel.SetTargetPlayer": ["Stores player as the target player for the currently handled Chain."],
    "Duel.GetFieldGroupCount": ["Returns the number of cards in the specified locations from player's viewpoint."],
    "Duel.SetTargetParam": ["Stores param as the target parameter for the currently handled Chain."],
    "Duel.GetAttacker": ["Returns the monster that is currently attacking, or nil if there is no current attacker."],
    "Auxiliary.FilterBoolFunction": [
        "Returns a filter function that calls f(target, ...) with the extra arguments captured now.",
        "Use this when another API expects a one-argument Card filter but the real filter needs fixed extra values.",
    ],
    "Card.RegisterFlagEffect": [
        "Registers a special single-card flag effect on c and returns the created Effect.",
        "Flag effects are script markers: their code is kept separate from regular effect codes, they cannot be disabled, and count=0 is treated as 1.",
    ],
    "Duel.Draw": [
        "Makes player draw up to count cards for reason and returns the number actually drawn.",
        "When reason includes REASON_RULE, effects that prevent drawing are ignored.",
    ],
    "Duel.GetCurrentPhase": ["Returns the current phase constant."],
    "Duel.Damage": [
        "Deals value effect damage to player for reason and returns the damage actually applied.",
        "If damage is changed into LP recovery or prevented, the return value reflects the final applied damage. With is_step=true, finish the damage/recovery batch with Duel.RDComplete.",
    ],
    "Group.IsContains": ["Checks whether g contains card c."],
    "Card.IsLevelBelow": ["Checks whether c has a Level greater than 0 and less than or equal to level."],
    "Card.IsAbleToRemove": [
        "Checks whether c can be banished by player in position pos for reason.",
        "player defaults to the current reason player, pos defaults to POS_FACEUP, and reason defaults to REASON_EFFECT.",
    ],
    "Card.IsPreviousControler": ["Checks whether c's previous controller was player."],
    "Card.IsLevelAbove": ["Checks whether c has a Level greater than 0 and greater than or equal to level."],
    "Auxiliary.bfgcost": ["Shared cost function that checks whether the handler can be banished as cost, then banishes it face-up as REASON_COST."],
    "Effect.IsHasType": ["Checks whether e's effect type contains at least one flag from type."],
    "Duel.HintSelection": ["Displays the selection animation for g and records those cards as selected for client feedback."],
    "Duel.IsPlayerAffectedByEffect": ["Returns an effect affecting player with code, or nil if no matching effect exists. Some effects may return additional values."],
    "Duel.GetMZoneCount": [
        "Returns the number of usable Monster Zones for player after targets leave, plus the usable zone mask.",
        "use_player, reason, and zone are used by effects that restrict where monsters can be placed.",
    ],
    "Duel.GetAttackTarget": ["Returns the monster currently being attacked, or nil for a direct attack."],
    "Card.GetAttack": ["Returns c's current ATK, with unknown or negative ATK reported as 0."],
    "Duel.SetTargetCard": [
        "Stores targets as the target cards for the currently handled Chain.",
        "This records broad operation targets; it does not by itself check whether the cards are legal effect targets.",
    ],
    "Duel.DiscardHand": [
        "Lets player choose and discard min to max matching cards from their hand for reason, then returns the number discarded.",
        "Cards in ex are excluded. Extra arguments after ex are passed to filter f.",
    ],
    "Group.Merge": ["Adds every card from g2 into g1. g2 itself is not changed."],
    "Card.IsImmuneToEffect": ["Checks whether c is unaffected by effect e."],
    "Duel.GetMatchingGroupCount": [
        "Counts cards in the specified locations that satisfy filter f and are not excluded by ex.",
        "Extra arguments after ex are passed to f after the card argument.",
    ],
    "Auxiliary.AddXyzProcedure": [
        "Registers the standard Xyz Summon procedure for c.",
        "f filters materials, lv is the required Level, ct is the minimum material count, and maxct optionally caps the maximum. alterf/alterdesc/alterop define an alternate one-card Xyz Summon route.",
    ],
    "Card.GetCode": ["Returns c's current card code and, when present, its secondary code."],
    "Card.IsRelateToBattle": ["Checks whether c is still related to the current battle, usually during the Damage Step or shortly after damage calculation."],
    "Card.GetLevel": ["Returns c's current Level."],
    "Auxiliary.NonTuner": [
        "Returns a non-Tuner material filter that also applies f when f is supplied.",
        "Extra arguments are captured now and passed to f after the Card argument.",
    ],
    "Auxiliary.AddSynchroProcedure": [
        "Registers the standard Synchro Summon procedure for c.",
        "f1 filters the Tuner material, f2 filters non-Tuner materials, and minc/maxc set the number of non-Tuner materials required.",
    ],
    "Auxiliary.AddSynchroProcedure2": [
        "Backward-compatible helper for a Synchro Monster that uses exactly 1 Tuner and 1 non-Tuner material.",
        "It calls Auxiliary.AddSynchroProcedure(c, f1, f2, 1, 1).",
    ],
    "Card.IsAbleToExtra": ["Checks whether c can be returned to the Extra Deck by the current reason player."],
    "Card.IsSynchroSummonable": [
        "Checks whether c can be Synchro Summoned with tuner and the available material group mg.",
        "If tuner is nil, this behaves like the regular Special Summon procedure check for c.",
        "min and max restrict the number of non-Tuner Synchro Materials used by the procedure.",
    ],
    "Duel.SynchroSummon": [
        "Performs a Synchro Summon of c for player, optionally requiring tuner and selecting materials from mg.",
        "minc and maxc can restrict the number of non-Tuner materials used by the procedure.",
    ],
    "Duel.SelectSynchroMaterial": [
        "Lets player select Synchro Materials for c and returns the selected Group.",
        "f1 filters the Tuner material, f2 filters non-Tuner materials, min and max restrict the non-Tuner count, smat forces a required material, and mg supplies an optional material pool.",
    ],
    "Duel.SetSynchroMaterial": ["Stores g as the Synchro Material group for the current Summon procedure."],
    "Effect.GetOperation": ["Returns e's operation callback, or nil if no operation callback is set."],
    "Effect.GetTarget": ["Returns e's target callback, or nil if no target callback is set."],
    "Card.GetType": ["Returns c's current type mask, including temporary type changes applied to the card."],
    "Effect.GetType": ["Returns e's effect type mask, such as EFFECT_TYPE_SINGLE, EFFECT_TYPE_FIELD, or EFFECT_TYPE_TRIGGER_O."],
    "Card.CheckFusionMaterial": [
        "Checks whether c's Fusion Material requirements can be satisfied by g, optionally requiring gc to be included.",
        "chkf is forwarded to the Fusion Material condition check, and not_material is used by procedures that check material availability without treating the cards as actual materials yet.",
    ],
    "Duel.CreateToken": [
        "Creates a Token card with card code code for player and returns it.",
        "The returned Token is not placed on the field automatically; scripts normally pass it to Duel.SpecialSummon or another operation afterwards.",
    ],
    "Group.FilterSelect": [
        "Lets player choose min to max cards from g that satisfy filter f, excluding ex, and returns the selected Group.",
        "Extra arguments after ex are passed to f after the Card argument.",
    ],
    "Effect.GetValue": ["Returns e's value field. For function-valued effects this is the stored callback; otherwise it is the stored integer value."],
    "Auxiliary.tgoval": [
        "Shared value function for EFFECT_CANNOT_BE_EFFECT_TARGET effects that protect against the opponent's effects.",
        "It returns true when the reason player rp is the opponent of e's handler player.",
    ],
    "Duel.GetTurnCount": [
        "Returns the current turn count.",
        "With no player argument, this returns the duel-wide turn number; with player 0 or 1, it returns that player's personal turn count.",
    ],
    "Card.IsFusionSetCard": [
        "Checks whether c can be treated as belonging to any supplied set code while used as Fusion Material.",
        "nil set-code arguments are ignored.",
    ],
    "Card.IsPublic": ["Checks whether c is currently public to both players, represented by face-up position in this core."],
    "Card.IsHasEffect": [
        "Returns the effects currently affecting c with effect code code, or nil if none match.",
        "When player is supplied, only effects whose count limit can still be used by that player are returned. Multiple matching effects are returned as multiple Lua return values.",
    ],
    "Card.IsPosition": ["Checks whether c's current battle position includes pos."],
    "Card.GetEquipTarget": ["Returns the card that c is currently equipped to, or nil if c has no equip target."],
    "Duel.SelectFusionMaterial": [
        "Lets player select a valid Fusion Material group for Fusion Monster c from g and returns the selected Group.",
        "gc, when supplied, must be included. The returned Group also contains gc, matching the core selection behavior.",
    ],
    "Group.DeleteGroup": [
        "Releases a Group previously preserved with Group.KeepAlive so Lua can manage it normally again.",
        "Calling this on an ordinary Group has no effect.",
    ],
    "Card.IsLevel": [
        "Checks whether c's current Level equals any supplied level value.",
        "nil level arguments are ignored.",
    ],
    "Card.SetMaterial": ["Sets g as c's material group for a Summon, or clears c's materials when g is nil."],
    "Duel.SelectOption": [
        "Shows player a list of description ids and returns the zero-based index of the selected option.",
        "The selected description id is also announced to the client.",
    ],
    "Effect.GetDescription": ["Returns e's description id."],
    "Card.GetFlagEffect": ["Returns how many flag effects with code are registered on c."],
    "Auxiliary.AddLinkProcedure": [
        "Registers the standard Link Summon procedure for c and returns the created Effect.",
        "f filters materials, min/max constrain the material count, and gf optionally checks the selected material group.",
    ],
    "Card.IsSummonType": ["Checks whether c's recorded Summon type includes every flag in sumtype."],
    "Card.CompleteProcedure": ["Marks c as having completed its proper Summon procedure."],
    "Card.IsStatus": ["Checks whether c currently has at least one status flag from status."],
    "Duel.GetLocationCountFromEx": [
        "Returns the usable Monster Zone count for Special Summoning from the Extra Deck, followed by the usable zone mask.",
        "reason_player defaults to the current reason player. targets are treated as leaving the field before the count is checked.",
    ],
    "Duel.CheckReleaseGroup": [
        "Checks whether player can release at least count cards matching f, excluding ex.",
        "Extra arguments after ex are passed to f after the Card argument. This helper uses REASON_COST.",
    ],
    "Duel.CheckReleaseGroupEx": [
        "Checks whether player can release at least count cards matching f, excluding ex, with an explicit reason and optional hand releases.",
        "Extra arguments after ex are passed to f after the Card argument.",
    ],
    "Card.GetOwner": ["Returns c's original owner player."],
    "Effect.GetOwner": ["Returns the card that owns e."],
    "Card.IsPreviousPosition": ["Checks whether c's previous position included pos."],
    "Duel.SelectReleaseGroup": [
        "Lets player select min to max releasable cards matching f, excluding ex, and returns the selected Group.",
        "Extra arguments after ex are passed to f after the Card argument.",
    ],
    "Group.FilterCount": [
        "Counts cards in g that satisfy f, excluding ex.",
        "Extra arguments after ex are passed to f after the Card argument.",
    ],
    "Group.FromCards": ["Creates and returns a new Group containing the non-nil Card arguments."],
    "Auxiliary.TargetBoolFunction": [
        "Returns an effect target callback that calls f(target, ...) with the extra arguments captured now.",
        "Use this when SetTarget or similar APIs expect a function with parameters (effect, target).",
    ],
    "Duel.GetFieldGroup": ["Returns the cards in the specified locations from player's viewpoint; s is player's side and o is the opponent's side."],
    "Auxiliary.EnablePendulumAttribute": [
        "Registers the Pendulum Summon procedure for Pendulum Monster c.",
        "Unless reg is false, it also registers the Pendulum Card activation effect from the hand.",
    ],
    "Duel.NegateActivation": ["Attempts to negate the activation of chainc and returns true if it succeeds."],
    "Duel.IsChainNegatable": [
        "Compatibility check for whether chainc's activation can be negated.",
        "In this MDPro3 core binding, the function currently returns true for any chain count.",
    ],
    "Duel.IsChainDisablable": [
        "Checks whether chainc's effect can be negated.",
        "While a Chain is resolving, this asks the core whether that Chain link can currently be disabled; outside Chain resolution it returns true.",
    ],
    "Effect.GetCode": ["Returns e's effect code."],
    "Card.GetBattleTarget": ["Returns the monster currently battling c, or nil if c is not the current attacker or attack target."],
    "Duel.GetFlagEffect": ["Returns how many player flag effects with code are registered on player."],
    "Duel.IsPlayerCanSpecialSummonMonster": [
        "Checks whether player can Special Summon a virtual monster with the supplied card data.",
        "Optional arguments override the loaded card data, then pos, target_player, and sumtype describe how and where the monster would be Summoned. This MDPro3 binding does not read a zone argument.",
    ],
    "Duel.RegisterFlagEffect": [
        "Registers a player/global flag effect on player and returns the created Effect.",
        "The flag effect is player-targeted, field-only, cannot be disabled, and count=0 is treated as 1.",
    ],
    "Group.AddCard": ["Adds c to g if g is mutable."],
    "Card.GetBaseAttack": ["Returns c's current base ATK, with unknown or negative ATK reported as 0."],
    "Card.IsCanBeEffectTarget": ["Checks whether c can be targeted by e, or by the current reason effect when e is omitted."],
    "Card.IsMSetable": [
        "Checks whether c can be Normal Set in a Monster Zone for the current reason player.",
        "ignore_count skips the Normal Summon/Set count check. e checks Set legality for that effect, min is the minimum number of releases required, and zone restricts usable Monster Zones.",
    ],
    "Effect.Reset": ["Removes e from its registered card or field effect list when e is still attached to a valid owner and handler."],
    "Duel.GetOperatedGroup": ["Returns the group of cards actually processed by the most recent card operation."],
    "Group.KeepAlive": ["Prevents g from being automatically released by Lua until Group.DeleteGroup is called."],
    "Auxiliary.Next": ["Returns an iterator over g for generic for loops, using Group.GetFirst and Group.GetNext internally."],
    "Duel.Recover": [
        "Gives player LP for reason and returns the amount processed.",
        "Effects can reverse recovery into damage. With is_step=true, finish the damage/recovery batch with Duel.RDComplete.",
    ],
    "Card.IsForbidden": ["Checks whether c currently has STATUS_FORBIDDEN."],
    "Duel.GetLP": ["Returns player's current LP."],
    "Duel.SelectEffectYesNo": ["Asks player whether to use c's effect with description id desc, defaulting to 95."],
    "Duel.NegateEffect": ["Attempts to negate the effect of chainc and returns true if it succeeds. forced requests a forced disable."],
    "Card.IsSummonPlayer": ["Checks whether player was the player who Summoned c."],
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
    "Card.CheckActivateEffect": [
        "Checks whether c has an activation effect that can currently be activated.",
        "If neglect_con is true, condition checks are skipped. If neglect_cost is true, cost checks are skipped.",
        "When copy_info is true, the returned values include the triggering event information: eg, ep, ev, re, r, and rp.",
    ],
    "Card.GetActivateEffect": ["Returns c's activation effect, the effect with type EFFECT_TYPE_ACTIVATE. This is mainly used for Spell/Trap Cards."],
    "Card.GetRace": ["Returns c's current Race value. Cards with multiple Races can return a bitmask containing more than one Race."],
    "Card.GetSequence": [
        "Returns c's sequence within its current location.",
        "For field zones, Main Monster Zones and Spell & Trap Zones use 0-4 from left to right, the Field Zone uses 5, and Pendulum Zones use 6-7.",
        "For other locations, sequence is the card's position in that location, starting from 0.",
    ],
    "Card.IsAbleToDeck": ["Checks whether c can be returned to the Deck."],
    "Card.IsAbleToDeckAsCost": ["Checks whether c can be returned to the Deck as a cost."],
    "Card.IsAbleToDeckOrExtraAsCost": ["Checks whether c can be returned to the Deck or Extra Deck as a cost."],
    "Card.IsAbleToExtraAsCost": ["Checks whether c can be returned to the Extra Deck as a cost."],
    "Card.IsAbleToHandAsCost": [
        "Checks whether c can be returned to the hand as a cost.",
        "This uses c's actual return destination and returns false when the card would go somewhere other than the player's hand, such as the Extra Deck.",
    ],
    "Card.IsAbleToRemoveAsCost": [
        "Checks whether c can be banished as a cost by the current reason player.",
        "pos controls the banished position and defaults to POS_FACEUP.",
    ],
    "Card.IsRelateToChain": [
        "Checks whether c is still related to chainc.",
        "The activating card and cards selected as targets with Duel.SetTargetCard or Duel.SelectTarget automatically become related to that Chain. The relation is lost when the card leaves the expected place.",
    ],
    "Card.IsSSetable": ["Checks whether c can be Set in a Spell & Trap Zone. If ignore_field is true, available zone checks are ignored."],
    "Card.SetUniqueOnField": ["Sets a uniqueness rule for c so only one card with unique_code can exist on the checked field, Monster Zone, or Spell & Trap Zone range."],
    "Debug.SetPlayerInfo": ["Sets a player's LP, starting hand count, and cards drawn each Draw Phase."],
    "Duel.CheckChainTarget": ["Checks whether c is a valid card related to chainc."],
    "Duel.CheckLPCost": ["Checks whether player can pay the specified LP cost."],
    "Duel.ChangePosition": [
        "Changes the battle position of targets and returns the number of cards whose position actually changed.",
        "The position arguments map by current position: au for face-up Attack Position, ad for face-down Attack Position, du for face-up Defense Position, and dd for face-down Defense Position. Omitted values use au.",
    ],
    "Duel.Destroy": [
        "Destroys targets for reason and returns the number of cards actually destroyed.",
        "dest defaults to LOCATION_GRAVE. reason_player defaults to the current Chain's reason player. Use REASON_EFFECT for normal card effects and reserve REASON_RULE for rule/procedure cleanup.",
    ],
    "Duel.Equip": [
        "Equips c1 to c2 for player and returns true if the equip succeeds.",
        "up defaults to true and makes the Equip Card face-up. When is_step is true, call Duel.EquipComplete after all step equips have been created.",
    ],
    "Duel.EquipComplete": [
        "Completes a batch of step equips created with Duel.Equip(..., true) by enabling the equipped cards and raising the equip events.",
    ],
    "Duel.GetControl": [
        "Moves control of targets to player and returns the number of cards whose control actually changed.",
        "Use reset_phase and reset_count for temporary control, such as PHASE_END, 1. To pass only a zone mask, use 0, 0, zone.",
    ],
    "Duel.MoveToField": [
        "Moves c onto target_player's field and returns true if the move succeeds.",
        "dest is normally LOCATION_MZONE or LOCATION_SZONE. LOCATION_FZONE and LOCATION_PZONE are accepted and converted to the matching Spell & Trap Zone handling by the core.",
    ],
    "Duel.Overlay": [
        "Overlays ocard under c as Xyz Material.",
        "By default the field is adjusted after the overlay. Pass adjust=false only when a larger procedure will adjust afterward.",
    ],
    "Duel.Release": [
        "Tributes/Releases targets for reason and returns the number of cards actually released.",
        "Use REASON_COST when paying a cost and REASON_EFFECT or REASON_SPSUMMON when the release is part of an effect or Summon procedure.",
    ],
    "Duel.Remove": [
        "Banishes targets in position pos for reason and returns the number of cards actually banished.",
        "If reason includes REASON_TEMPORARY, the banish is treated as temporary and the card can later be returned with Duel.ReturnToField.",
    ],
    "Duel.SendtoHand": [
        "Sends targets to a hand for reason and returns the number of cards actually moved.",
        "Pass nil for player to use the normal return destination. Pass a specific player only when the effect says the cards go to that player's hand.",
    ],
    "Duel.SpecialSummonComplete": [
        "Completes a batch of successful Duel.SpecialSummonStep calls, raises the Summon events, and returns the number of completed Summons.",
    ],
    "Duel.SpecialSummonStep": [
        "Special Summons one card as part of a multi-step Summon procedure and returns true if that step succeeds.",
        "Every successful step batch must finish with Duel.SpecialSummonComplete.",
    ],
    "Duel.DisableShuffleCheck": [
        "Disables the automatic shuffle check for the next Deck or hand operation.",
        "Use this before operations that intentionally preserve Deck order or hand order.",
    ],
    "Duel.GetOperationCount": ["Returns the number of operation categories recorded for chainc."],
    "Duel.GetOperationInfo": [
        "Returns operation information recorded for category on chainc.",
        "The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.",
    ],
    "Duel.GetReleaseGroup": ["Returns the cards player can Tribute/Release for effect purposes. If use_hand is true, valid cards in the hand are included."],
    "Duel.GetReleaseGroupCount": ["Returns the number of cards player can Tribute/Release for effect purposes. If use_hand is true, valid cards in the hand are included."],
    "Duel.IsPlayerCanDraw": ["Checks whether player can draw count cards."],
    "Duel.PayLPCost": ["Makes player pay the specified LP cost."],
    "Duel.SelectReleaseGroupEx": ["Lets player select min to max cards that can be Tributed/Released for effect purposes, optionally excluding ex and applying filter f."],
    "Duel.SendtoDeck": [
        "Returns targets to the Deck or Extra Deck for reason and returns the number of cards moved.",
        "If player is nil, each card returns to its owner. seq=0 places cards on top of the Deck, seq=1 places them on the bottom, and other values use the default shuffle/return handling.",
    ],
    "Duel.SetOperationInfo": [
        "Records operation information for category on chainc.",
        "Use concrete targets and count when the affected cards are known. For unresolved non-targeting movement effects, pass nil targets with the expected count, target player, and target location.",
        "This information is used by response checks such as Stardust Dragon-style effects.",
    ],
    "Duel.ShuffleDeck": ["Shuffles player's Deck and resets shuffle-check state."],
    "Duel.ShuffleHand": ["Shuffles player's hand and resets shuffle-check state."],
    "Duel.ShuffleSetCard": ["Randomly reorders the Set cards in g, used for effects such as Magical Hats."],
    "Duel.SSet": ["Makes player Set targets to target_player's Spell & Trap Zone. If targets is a Group, returns the number of cards successfully Set."],
    "Group.GetClassCount": ["Counts distinct classes among cards in g according to f. Cards with the same return value from f count as the same class; extra arguments are passed to f."],
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
    "Duel.GetSynchroMaterial": [
        "Gets the group of cards player can use as Synchro Material.",
        "Face-down cards in the Monster Zone are omitted unless facedown is true.",
    ],
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
    "Auxiliary.UrsarcticExCostFilter": ["Replacement-cost filter for the shared Ursarctic Special Summon effect. It accepts cards in the Graveyard that can be banished as cost through effect code 16471775 or 89264428."],
    "Auxiliary.UrsarcticReleaseFilter": ["Cost filter for the shared Ursarctic Special Summon effect. It accepts Level 7 or higher monsters in the hand."],
    "Auxiliary.UrsarcticSpSummonCondition": ["Condition for the shared Ursarctic hand Quick Effect; returns true during either Main Phase."],
    "Auxiliary.UrsarcticSpSummonCost": ["Checks and pays the shared Ursarctic Special Summon cost. The player releases a Level 7 or higher monster from the hand, or banishes a valid Graveyard replacement-cost card and consumes that effect's count limit."],
    "Auxiliary.UrsarcticSpSummonLimit": ["Special Summon restriction target applied after the shared Ursarctic effect resolves; returns true for monsters with Level 0."],
    "Auxiliary.UrsarcticSpSummonOperation": ["Operation for the shared Ursarctic Special Summon effect. It Special Summons the handler, then applies the End Phase Special Summon restriction that blocks Level 0 monsters."],
    "Auxiliary.UrsarcticSpSummonTarget": ["Target function for the shared Ursarctic Special Summon effect. It requires an open Monster Zone and that the handler can be Special Summoned, then sets Special Summon operation info."],
    "Auxiliary.UseExtraReleaseCount": ["Consumes count limits for opponent's cards in g that were released through EFFECT_EXTRA_RELEASE_NONSUM, such as Lair of Darkness-style release effects not selected by Duel.SelectReleaseGroup."],
    "GetID": ["Returns the current script's table, card code, and string offset. The offset is 1 for regular card IDs and 100 for large custom IDs."],
    "Group.CheckSubGroup": ["Checks whether g has a subgroup with size between min and max that satisfies f, while respecting already selected cards from Duel.GrabSelectedCard and Auxiliary.GCheckAdditional."],
    "Group.CheckSubGroupEach": ["Checks whether g can supply one card for each filter in checks. If f is omitted, only the per-position checks are required."],
    "Group.SelectSubGroup": ["Lets tp select a subgroup from g with size between min and max that satisfies f. It respects already selected cards and returns nil if no valid selection is completed."],
    "Group.SelectSubGroupEach": ["Lets tp select one card for each filter in checks, optionally cancelable. If f is omitted, Auxiliary.TRUE is used for the final group check."],
    "bit.bnot": ["Returns the bitwise NOT of a."],
    "bit.extract": ["Extracts width bits from r starting at bit field. width defaults to 1."],
    "bit.replace": ["Returns r with width bits starting at field replaced by the low width bits of v. width defaults to 1."],
    "Auxiliary.AddContactFusionProcedure": ["Registers a Contact Fusion Special Summon procedure on c, using material filter locations and the provided material operation, and returns the created procedure effect."],
    "Auxiliary.AddFusionEffectProc": ["Convenience wrapper for Auxiliary.AddFusionEffectProcUltimate. It builds a params table from the common arguments and returns the created Fusion effect."],
    "Auxiliary.AddRitualProcGreater2": ["Adds a Ritual Summon effect for c that uses the Ritual Monster's current Level and requires materials whose total Level is greater than or equal to it."],
    "Auxiliary.AddRitualProcGreater2Code": ["Registers code1 as listed by c, then adds the Greater2 Ritual procedure restricted to Ritual Monsters with that code."],
    "Auxiliary.AddRitualProcGreater2Code2": ["Registers code1 and code2 as listed by c, then adds the Greater2 Ritual procedure restricted to Ritual Monsters with either code."],
    "Auxiliary.AddRitualProcUltimate": ["Creates the configurable Ritual Summon activation effect for c and returns it. The effect can be paused from registration, can use Graveyard materials, and can run extra target/operation callbacks."],
    "Auxiliary.AssaultModeLimit": ["Special Summon restriction value for /Assault Mode monsters; allows the Assault Mode summon value or effects activated by Assault Mode Activate."],
    "Auxiliary.CheckXyz2XMaterial": ["Checks whether c can be Xyz Summoned using materials from mg while allowing valid EFFECT_DOUBLE_XMATERIAL cards to count as two materials."],
    "Auxiliary.ContactFusionCondition": ["Returns the condition function for Contact Fusion procedures. It collects valid materials from the configured locations and checks c's Fusion Material requirement."],
    "Auxiliary.ContactFusionMaterialFilter": ["Material filter for Contact Fusion procedures. The card must be usable as Fusion Material for fc and must satisfy filter when one is provided."],
    "Auxiliary.ContactFusionOperation": ["Returns the operation function for Contact Fusion procedures. It sets the selected materials on the Fusion Monster, runs mat_operation, and deletes the kept-alive group."],
    "Auxiliary.ContactFusionSendToDeck": ["Returns a Contact Fusion material operation that reveals face-down materials when needed, hints Graveyard/banished materials, and shuffles all materials into the Deck as cost."],
    "Auxiliary.ContactFusionTarget": ["Returns the target function for Contact Fusion procedures. It selects Fusion Materials, keeps the selected group alive, stores it on the effect, and returns whether selection succeeded."],
    "Auxiliary.DarkFusionLimit": ["Special Summon restriction value for Evil HERO/Dark Fusion effects; allows Dark Fusion itself, the Dark Fusion summon value, or Fusion Summons while the player is affected by effect code 72043279."],
    "Auxiliary.FCheckMix": ["Recursive mixed Fusion Material checker. It tests one required material function at a time, tracks selected materials in sg, and consumes the substitute-material allowance when needed."],
    "Auxiliary.FCheckMixGoal": ["Final group check for mixed Fusion Materials. It validates mandatory Fusion Materials, Tune Magician restrictions, Extra Monster Zone availability, and additional Fusion goal hooks."],
    "Auxiliary.FCheckMixRep": ["Checks a selected mixed-repeat Fusion Material group. The repeated material function must cover the variable-count materials, while each remaining function is satisfied once."],
    "Auxiliary.FCheckMixRepFilter": ["Recursive helper for Auxiliary.FCheckMixRep. It temporarily assigns c to one remaining fixed material function and continues checking the rest."],
    "Auxiliary.FCheckMixRepGoal": ["Final goal check for mixed-repeat Fusion Materials. It validates selected count limits, Extra Monster Zone availability, additional Fusion hooks, and fixed/repeated material requirements."],
    "Auxiliary.FCheckMixRepGoalCheck": ["Shared precheck for mixed-repeat Fusion Material goals. It rejects invalid Tune Magician combinations, missing mandatory Fusion Materials, and failed goal hooks."],
    "Auxiliary.FCheckMixRepSelected": ["Selection-recursion helper for mixed-repeat Fusion Materials; it delegates to Auxiliary.FCheckMixRepTemplate using the selected-material condition."],
    "Auxiliary.FCheckMixRepSelectedCond": ["Checks whether the recursive mixed-repeat selection can continue from the currently selected group, or can finish through Auxiliary.FCheckSelectMixRep."],
    "Auxiliary.FCheckMixRepTemplate": ["Generic recursive template for mixed-repeat Fusion Material checks. It tries assigning c to each fixed material function or to the repeated material slot."],
    "Auxiliary.FCheckSelectMixRep": ["Checks whether a mixed-repeat Fusion Material selection can be completed from the current chosen group."],
    "Auxiliary.FCheckSelectMixRepAll": ["Recursive helper for mixed-repeat Fusion selection when field-space constraints are already satisfied or not required."],
    "Auxiliary.FCheckSelectMixRepM": ["Recursive helper for mixed-repeat Fusion selection that requires the next candidate to be controlled by tp in the Monster Zone."],
    "Auxiliary.FConditionFilterMix": ["Material filter used by mixed Fusion procedures. It checks whether c can be used as Fusion Material for fc and satisfies at least one required material function."],
    "Auxiliary.FConditionMix": ["Returns the condition function for fixed mixed Fusion Material procedures."],
    "Auxiliary.FConditionMixRep": ["Returns the condition function for mixed Fusion Material procedures with a repeated material slot."],
    "Auxiliary.FMaterialFilter": ["Default Fusion Material filter for Fusion effects; returns whether c can be used as Fusion Material."],
    "Auxiliary.FMaterialRemove": ["Default operation for banishing Fusion Materials with Fusion reason flags."],
    "Auxiliary.FMaterialRemoveFilter": ["Default Graveyard-material filter for Fusion effects that banish materials; returns whether c can be banished."],
    "Auxiliary.FMaterialToDeck": ["Default operation for returning Fusion Materials to the Deck with Fusion reason flags."],
    "Auxiliary.FMaterialToGrave": ["Default operation for sending Fusion Materials to the Graveyard with Fusion reason flags."],
    "Auxiliary.FMaterialToGraveFilter": ["Default Fusion Material filter for effects that send materials to the Graveyard; returns whether c can be sent to the Graveyard."],
    "Auxiliary.FOperationMix": ["Returns the operation function for fixed mixed Fusion Material procedures; it selects valid materials and stores them with Duel.SetFusionMaterial."],
    "Auxiliary.FOperationMixRep": ["Returns the operation function for mixed Fusion Material procedures with a repeated material slot; it lets the player build a valid material group and stores it."],
    "Auxiliary.FossilFusionLimit": ["Special Summon restriction value for Fossil Fusion effects; allows Fossil Fusion's summon value, Fossil Fusion itself, or non-Extra Deck handlers."],
    "Auxiliary.FSelectMixRep": ["Candidate test for mixed-repeat Fusion selection. It temporarily adds c to sg and returns whether the selection is already valid or can still be completed."],
    "Auxiliary.FShaddollCondition": ["Returns the condition function for Shaddoll Fusion procedures. It checks for one Shaddoll material and one material with the required Attribute, with optional field-spell opponent-material support."],
    "Auxiliary.FShaddollExFilter": ["Opponent-field Shaddoll Fusion Material filter used with effect code 81788994; c must be face-up, affected by the field effect, and pass the standard Shaddoll material filter."],
    "Auxiliary.FShaddollFilter": ["Standard Shaddoll Fusion Material filter. The card must be either a Shaddoll monster or match the required Attribute, be usable as Fusion Material, and not be blocked by effect 6205579."],
    "Auxiliary.FShaddollFilter1": ["Returns true if c belongs to the Shaddoll Fusion set 0x9d."],
    "Auxiliary.FShaddollFilter2": ["Returns true if c has the required Fusion Attribute or effect code 4904633."],
    "Auxiliary.FShaddollOperation": ["Returns the operation function for Shaddoll Fusion procedures; it selects the two required materials, optionally using the opponent-field material effect, and stores them with Duel.SetFusionMaterial."],
    "Auxiliary.FShaddollSpFilter1": ["Checks whether c can be paired with another valid Shaddoll Fusion Material from mg or exg."],
    "Auxiliary.FShaddollSpFilter2": ["Checks whether c and mc form the required Shaddoll Fusion Material pair while respecting mandatory Fusion Material and additional Fusion checks."],
    "Auxiliary.FusionEffectUltimateFilter": ["Checks whether c is a Fusion Monster that can be Fusion Summoned by e using mg and the filters stored in params."],
    "Auxiliary.FusionEffectUltimateMatFilter": ["Fusion effect material filter; rejects materials immune to e and applies the optional material filter f."],
    "Auxiliary.FusionEffectUltimateMatLocFilter": ["Location-specific Fusion material filter; cards outside loc pass, and cards in loc must satisfy f when one is provided."],
    "Auxiliary.FusionEffectUltimateOperation": ["Returns the operation function for configurable Fusion Summon effects. It builds the material pool, handles Chain Material, applies per-location material operations, Special Summons the chosen Fusion Monster, and runs extra callbacks."],
    "Auxiliary.FusionEffectUltimateTarget": ["Returns the target function for configurable Fusion Summon effects. It checks available Fusion Monsters and material pools, handles Chain Material fallback, and registers operation information."],
    "Auxiliary.GetLinkMaterials": ["Returns the available Link Materials for tp, including regular Monster Zone materials and cards allowed by extra Link Material effects."],
    "Auxiliary.GetMinSynchroLevel": ["Returns the smallest Synchro Level value c can provide for syncard, including packed alternative Synchro Levels."],
    "Auxiliary.GetSynchroLevelFlowerCardian": ["Returns the fixed Synchro Level value used by Flower Cardian helpers."],
    "Auxiliary.GetSynMaterials": ["Returns the available Synchro Materials for tp and syncard, including valid hand materials when any field material enables hand Synchro use."],
    "Auxiliary.LCheckGoal": ["Final Link Material group check. It verifies Link Rating total, Extra Monster Zone availability, optional group filter, extra-material compatibility, and required lmat inclusion."],
    "Auxiliary.LCheckOtherMaterial": ["Checks whether c is compatible with the other selected Link Materials through EFFECT_EXTRA_LINK_MATERIAL handlers."],
    "Auxiliary.LConditionFilter": ["Regular Link Material filter. The card must be visible or selectable by e, usable as Link Material for lc, and satisfy f when provided."],
    "Auxiliary.LExtraFilter": ["Extra Link Material filter for hand, Spell & Trap Zone, or opponent-field cards granted by EFFECT_EXTRA_LINK_MATERIAL."],
    "Auxiliary.LExtraMaterialCount": ["Consumes count limits for selected Link Materials that were used through valid EFFECT_EXTRA_LINK_MATERIAL effects."],
    "Auxiliary.LinkCondition": ["Returns the condition function for Link Summon procedures."],
    "Auxiliary.LinkOperation": ["Returns the operation function for Link Summon procedures; it sets the materials, consumes extra-material count limits, and sends the materials to the Graveyard."],
    "Auxiliary.LinkTarget": ["Returns the target function for Link Summon procedures; it selects a valid Link Material subgroup and stores it on the effect."],
    "Auxiliary.LUncompatibilityFilter": ["Returns true when c is not compatible with the other selected Link Materials."],
    "Auxiliary.MaskChangeLimit": ["Special Summon restriction value for Masked HERO/Mask Change effects; allows the Mask Change summon value or effects activated by card code 21143940."],
    "Auxiliary.PConditionExtraFilter": ["Checks whether any extra Pendulum Summon effect in eset allows c for the current scales."],
    "Auxiliary.PConditionExtraFilterSpecific": ["Checks whether one extra Pendulum Summon effect allows c for the current scales."],
    "Auxiliary.PConditionFilter": ["Pendulum Summon candidate filter. It checks location, Level or pendulum_level, scales, Special Summon legality, forbidden state, and extra Pendulum Summon permissions."],
    "Auxiliary.PendCondition": ["Condition function for the shared Pendulum Summon procedure. It checks the two Pendulum Zones, available locations and zones, once-per-turn state, and valid summonable monsters."],
    "Auxiliary.PendOperation": ["Operation function for the shared Pendulum Summon procedure. It chooses the regular or extra Pendulum Summon effect, selects monsters within hand/Extra Deck zone limits, updates the checklist, and merges the selection into sg."],
    "Auxiliary.PendOperationCheck": ["Returns a group check that enforces the hand, Extra Deck, and total zone limits for a Pendulum Summon selection."],
    "Auxiliary.PendulumReset": ["Resets the shared Pendulum Summon checklist at the start of the Draw Phase."],
    "Auxiliary.PendulumSummonableBool": ["Returns true if c has a psummonable_location flag that includes its current location."],
    "Auxiliary.PSSCompleteProcedure": ["Completes the procedure for monsters that were Special Summoned by Pendulum Summon through the revive-limit helper."],
    "Auxiliary.RitualCheckAdditional": ["Returns an additional subgroup check used while selecting Ritual Materials for Equal or Greater Ritual procedures."],
    "Auxiliary.RitualCheckAdditionalLevel": ["Returns the smaller usable Ritual Level value for c when its Ritual Level packs two alternatives."],
    "Auxiliary.RitualCheckEqual": ["Checks whether g's Ritual Levels exactly equal lv for c."],
    "Auxiliary.RitualCheckGreater": ["Checks whether g's Ritual Levels are greater than or equal to lv for c."],
    "Auxiliary.RitualExtraFilter": ["Graveyard Ritual Material filter; c must be a Level monster accepted by f and able to be banished."],
    "Auxiliary.RitualUltimateFilter": ["Checks whether c is a valid Ritual Monster that can be Ritual Summoned with the available material groups and the selected Equal or Greater level rule."],
    "Auxiliary.RitualUltimateOperation": ["Returns the operation function for configurable Ritual Summon effects. It selects the Ritual Monster and materials, releases or banishes the materials, Special Summons the monster, and runs extra callbacks."],
    "Auxiliary.RitualUltimateTarget": ["Returns the target function for configurable Ritual Summon effects. It checks Ritual Monsters and material pools, then registers Special Summon, banish, and extra target information."],
    "Auxiliary.SynCondition": ["Returns the condition function for basic Synchro Summon procedures, including optional fixed tuner material handling."],
    "Auxiliary.SynGroupCheckLevelAddition": ["Returns a group check for Synchro material selection that keeps the sum of the selected materials' minimum Synchro Levels at or below syncard's Level."],
    "Auxiliary.SynLimitFilter": ["Returns true when limiter function f exists and rejects c for syncard."],
    "Auxiliary.SynMaterialFilter": ["Synchro Material filter; c must be face-up or public and usable as Synchro Material for syncard."],
    "Auxiliary.SynMixCheck": ["Checks whether the remaining mixed Synchro Material pool can complete the selected fixed-material group within the variable material count range."],
    "Auxiliary.SynMixCheckGoal": ["Final mixed Synchro Material group check. It validates count, Extra Monster Zone availability, group callback, fixed material, mandatory Synchro Materials, EFFECT_TUNE_MAGICIAN restrictions, Level total, hand-material limits, and tuner limits."],
    "Auxiliary.SynMixCheckPrune": ["Pruning check for mixed Synchro searches; returns true once the selected materials' minimum Synchro Level total reaches syncard's Level."],
    "Auxiliary.SynMixCheckRecursive": ["Recursive mixed Synchro Material search helper. It temporarily adds c, checks the goal, and continues through mg while the branch remains possible."],
    "Auxiliary.SynMixCondition": ["Returns the condition function for mixed Synchro Summon procedures with up to three fixed material filters and a variable material slot."],
    "Auxiliary.SynMixFilter1": ["First fixed-material candidate filter for mixed Synchro procedures."],
    "Auxiliary.SynMixFilter2": ["Second fixed-material candidate filter for mixed Synchro procedures, or the transition into the variable material slot when no second filter is required."],
    "Auxiliary.SynMixFilter3": ["Third fixed-material candidate filter for mixed Synchro procedures, or the transition into the variable material slot when no third filter is required."],
    "Auxiliary.SynMixFilter4": ["Variable-slot candidate filter for mixed Synchro procedures; after adding c it checks whether the remaining material pool can complete the summon."],
    "Auxiliary.SynMixHandCheck": ["Checks whether selected hand Synchro Materials are allowed by a material that grants hand Synchro use, including filter and count limits."],
    "Auxiliary.SynMixHandFilter": ["Returns true for a hand material that is being used because another card enables it, rather than by its own extra Synchro Material effect."],
    "Auxiliary.SynMixOperation": ["Returns the operation function for mixed Synchro Summon procedures; it sets materials, sends them to the Graveyard, and releases the kept group."],
    "Auxiliary.SynMixTarget": ["Returns the target function for mixed Synchro Summon procedures; it guides material selection and stores the selected group on the effect."],
    "Auxiliary.SynOperation": ["Returns the operation function for basic Synchro Summon procedures; it sets materials, sends them to the Graveyard, and releases the kept group."],
    "Auxiliary.SynTarget": ["Returns the target function for basic Synchro Summon procedures; it selects Synchro Materials and stores the selected group on the effect."],
    "Auxiliary.TuneMagicianCheckAdditionalX": ["Deprecated factory that returns a group check rejecting groups with an invalid EFFECT_TUNE_MAGICIAN_* pair for ecode."],
    "Auxiliary.TuneMagicianCheckAdditionalXyz": ["Additional Xyz material group check that rejects invalid EFFECT_TUNE_MAGICIAN_X pairs."],
    "Auxiliary.Xyz2XMaterialEffectFilter": ["Checks whether c has a valid EFFECT_DOUBLE_XMATERIAL effect for xyzc, optionally skipping the normal Xyz Material filter when checked is true."],
    "Auxiliary.Xyz2XMaterialFilter": ["Xyz Material filter for double-material handling; c must be face-up or public, usable as Xyz Material for xyzc, match lv, and satisfy f when provided."],
    "Auxiliary.Xyz2XMaterialGoal": ["Final group check for Xyz Summons that may use EFFECT_DOUBLE_XMATERIAL. It validates Extra Monster Zone availability, EFFECT_XYZ_MIN_COUNT, and whether double-material effects cover minc."],
    "Auxiliary.Xyz2XMaterialOperation": ["Consumes the count limits for selected EFFECT_DOUBLE_XMATERIAL cards needed for the selected group to satisfy the minimum material count."],
    "Auxiliary.XyzAlterFilter": ["Alternate Xyz Summon candidate filter. It checks alterf, Xyz Material legality, Extra Monster Zone availability, mandatory Xyz Materials, EFFECT_XYZ_MIN_COUNT, and optional alterop validation."],
    "Auxiliary.XyzCondition": ["Returns the condition function for standard Xyz Summon procedures, including optional alternate one-card Xyz Summon and EFFECT_DOUBLE_XMATERIAL handling."],
    "Auxiliary.XyzLevelFreeCondition": ["Returns the condition function for Level-free Xyz Summon procedures with optional group filter and alternate one-card Xyz Summon support."],
    "Auxiliary.XyzLevelFreeFilter": ["Level-free Xyz Material filter; c must be face-up if on the field, usable as Xyz Material for xyzc, and satisfy f when provided."],
    "Auxiliary.XyzLevelFreeGoal": ["Final group check for Level-free Xyz Summons. It validates Extra Monster Zone availability, optional group filter gf, and EFFECT_XYZ_MIN_COUNT requirements."],
    "Auxiliary.XyzLevelFreeOperation": ["Returns the operation function for Level-free Xyz Summon procedures; it handles alternate summons, sends old overlay cards to the Graveyard by rule, sets materials, and overlays them."],
    "Auxiliary.XyzLevelFreeTarget": ["Returns the target function for Level-free Xyz Summon procedures; it chooses between alternate material and regular group selection and stores the selected group."],
    "Auxiliary.XyzOperation": ["Returns the operation function for standard Xyz Summon procedures; it handles alternate summons, double-material count limits, sends old overlay cards to the Graveyard by rule, sets materials, and overlays them."],
    "Auxiliary.XyzTarget": ["Returns the target function for standard Xyz Summon procedures; it chooses between alternate material, double-material group selection, and regular Xyz Material selection."],
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
    "Card.CheckFusionSubstitute": ["检查c能否代替融合怪兽fcard所列名的指定融合素材。"],
    "Card.GetPreviousLocation": ["返回c在上一次位置变化前的原位置位掩码。"],
    "Duel.GetFlagEffectLabel": [
        "返回player身上code对应标志效果保存的Label值。",
        "没有对应标志效果时核心返回nil；存在多个对应标志效果时，会按每个效果返回一个Label值。",
    ],
    "Duel.GetOverlayGroup": ["返回player视角下s和o位置中卡片叠放的超量素材Group。"],
    "Duel.IsPlayerCanRelease": [
        "检查player是否能进行解放，或检查player能否以reason解放c。",
        "提供c但省略reason时，核心使用REASON_COST。",
    ],
    "Duel.SetFlagEffectLabel": ["把player身上第一个匹配的标志效果Label设为label，并返回是否找到该效果。"],
    "Duel.SetFusionMaterial": ["把核心当前的融合素材集合替换为g中的卡。"],
    "Auxiliary.AddFusionProcFunRep2": ["登记融合手续，要求minc到maxc只满足f的素材。"],
    "Auxiliary.DragonXyzSpSummonType": ["仅在c是「魂吸收龙」时返回true，用作特殊召唤手续类型辅助函数。"],
    "Auxiliary.GetColumn": ["从玩家p视角返回c所在纵列编号；c没有场上纵列时返回NULL_VALUE。"],
    "Auxiliary.GetValueType": ["普通值返回Lua的type字符串；Card、Group、Effect userdata返回对应名称。"],
    "Auxiliary.IsSelfEquip": ["检查c是否有带标志效果id的装备卡，用于判断由该卡自身效果装备的卡。"],
    "Card.GetAttackableTarget": ["返回c可攻击的卡的Group，以及c能否直接攻击的布尔值。"],
    "Card.GetAttackedCount": ["返回c在当前回合的攻击次数。"],
    "Card.GetLeaveFieldDest": ["返回c因REASON_EFFECT适用离场改去效果时会前往的位置。"],
    "Card.GetPreviousLevelOnField": ["返回c先前在场上时的等级值。"],
    "Card.IsXyzLevel": ["检查c能否为超量怪兽xyzc提供超量用等级lv。"],
    "Duel.DisableSelfDestroyCheck": ["设置是否禁用核心的自毁检查；省略disable时表示禁用检查。"],
    "Effect.GetCondition": ["返回e的Condition回调；没有设置Condition时返回nil。"],
    "Auxiliary.AddRitualProcEqualCode": [
        "为卡号code1的仪式怪兽创建仪式召唤发动效果。",
        "所选素材的仪式等级合计必须等于该仪式怪兽的原本等级；可选的墓地素材筛选、素材筛选和额外回调会传给共用仪式手续。",
    ],
    "Auxiliary.ArcanaCondition": ["「秘仪之力」条件辅助函数，检查处理对象是否保存有秘仪硬币结果标志。"],
    "Auxiliary.dogcon": ["EVENT_TO_GRAVE条件辅助函数，检查处理对象先前由tp控制且被对方破坏。"],
    "Auxiliary.DrytronSpSummonType": ["检查c是否是特殊召唤手续怪兽，供「龙辉巧」特殊召唤辅助函数使用。"],
    "Auxiliary.indsval": ["自身效果破坏保护用Value辅助函数；原因玩家是处理对象玩家时返回true。"],
    "Auxiliary.PhantasmsSpSummonType": ["检查c是否是特殊召唤手续怪兽，供Phantasm特殊召唤辅助函数使用。"],
    "Auxiliary.TriamidSpSummonType": ["检查c是否是特殊召唤手续怪兽，供「三形金字塔」特殊召唤辅助函数使用。"],
    "Card.CancelCardTarget": ["把target从c的持续卡片对象关系中移除。"],
    "Card.GetMutualLinkedGroup": ["返回与c互相连接的卡的Group。"],
    "Card.IsCanBeLinkMaterial": ["检查c能否作为连接素材；可选地指定连接怪兽scard。"],
    "Card.IsLinkMarker": ["检查c是否具有方向dir的连接标记。"],
    "Card.ReleaseEffectRelation": ["解除c与效果e之间的关系。"],
    "Card.ReverseInDeck": [
        "把位于Deck中的c标记为表侧。",
        "如果c是当前主Deck最上方的卡，核心还会向客户端发送Deck顶更新。",
    ],
    "Duel.ChangeBattleDamage": [
        "把当前战斗中player受到的战斗伤害改为value。",
        "check为true或省略时，原本已经是0的战斗伤害不会被改写。",
    ],
    "Duel.GetCoinResult": ["返回当前投掷硬币事件保存的硬币结果；每枚硬币返回一个结果。"],
    "Duel.GetDrawCount": ["返回player当前抽卡阶段规则抽卡数量。"],
    "Effect.IsActivatable": ["检查e当前能否由player发动，并可用可选布尔值忽略位置检查和对象检查。"],
    "Auxiliary.AddFusionProcCode4": ["登记固定四个卡名的融合手续，要求code1、code2、code3、code4作为素材。"],
    "Auxiliary.EnableReviveLimitPendulumSummonable": [
        "给c启用苏生限制处理，同时允许其从loc对应位置进行灵摆召唤。",
        "该辅助函数会把loc保存到c的metatable，并在c成功灵摆召唤时完成正规手续。",
    ],
    "Auxiliary.FilterEqualFunction": ["返回卡片筛选函数：对该卡和额外参数调用f，并检查结果是否等于value。"],
    "Auxiliary.penlimit": ["特殊召唤条件辅助函数：仅当st包含SUMMON_TYPE_PENDULUM时返回true。"],
    "Auxiliary.TargetEqualFunction": ["返回效果对象Value函数：对对象卡和额外参数调用f，并检查结果是否等于value。"],
    "Auxiliary.tgsval": ["自身对象保护用Value辅助函数；原因玩家是处理对象玩家时返回true。"],
    "Card.AssumeProperty": [
        "临时假定c的一个属性供核心检查使用。",
        "assume_type可为ASSUME_CODE、ASSUME_TYPE、ASSUME_LEVEL、ASSUME_RANK、ASSUME_ATTRIBUTE、ASSUME_RACE、ASSUME_ATTACK或ASSUME_DEFENSE。",
    ],
    "Card.GetAttributeInGrave": ["返回c在墓地中对player视为具有的属性；player省略时使用当前原因玩家。"],
    "Card.GetPreviousDefenseOnField": ["返回c先前在场上时的DEF值。"],
    "Card.GetSummonLocation": ["返回c是从哪个位置被召唤的，该值从召唤信息中解析。"],
    "Card.ReplaceEffect": [
        "用卡号code的效果替换c的效果，使用给定reset标志，并返回替换效果id。",
        "count默认1；RESET_PHASE未指定自己/对方回合时会自动补上双方回合。",
    ],
    "Duel.GetDiceResult": ["返回当前掷骰事件保存的5个骰子结果槽位。"],
    "Duel.IsPlayerCanSSet": ["检查player是否能盖放魔法/陷阱，或检查player能否把c作为魔法/陷阱盖放。"],
    "Duel.SetDiceResult": ["设置5个骰子结果槽位；缺少或超出范围的值会被保存为1。"],
    "Card.IsCanBeSynchroMaterial": ["检查c能否作为scard的同调素材；核心需要配对调整时可提供tuner。"],
    "Duel.GetCounter": ["返回player视角下s和o位置中countertype类型指示物的总数。"],
    "Duel.GetUsableMZoneCount": [
        "返回player可用于怪兽进场的怪兽区域数量。",
        "use_player省略时使用当前原因玩家，并用于涉及行动玩家的区域限制检查。",
    ],
    "Effect.GetCategory": ["返回e的Category位掩码。"],
    "Auxiliary.AddFusionProcCodeRep": ["登记固定数量融合素材手续，要求cc只卡号为code1的怪兽。"],
    "Auxiliary.EnableArcanaCoin": [
        "为c在event1以及额外事件上登记「秘仪之力」式强制投掷硬币触发效果。",
        "共用操作会把硬币结果记录为FLAG_ID_ARCANA_COIN；受「逆转命运」影响时改为由玩家选择结果。",
    ],
    "Auxiliary.MZoneSequence": ["从控制者视角返回怪兽区域序号seq对应的本地纵列编号。"],
    "Auxiliary.AddBanishRedirect": ["登记EFFECT_LEAVE_FIELD_REDIRECT效果，使condition为真时离场的c改为除外；默认条件为c表侧表示。"],
    "Auxiliary.AddEquipSpellEffect": [
        "为c创建装备魔法发动效果，并登记对应的EFFECT_EQUIP_LIMIT。",
        "返回创建的发动效果；pause为true时只创建该效果，不立即登记到c上。",
    ],
    "Auxiliary.AddFusionProcCodeFunRep": ["登记融合手续，要求code1以及minc到maxc只满足f的素材。"],
    "Auxiliary.AddFusionProcFunFunRep": ["登记融合手续，要求1只满足f1的素材以及minc到maxc只满足f2的素材。"],
    "Card.GetBattledGroupCount": ["返回c当前记录的已战斗卡集合数量。"],
    "Card.GetLinkAttribute": ["返回c作为连接素材使用时对player使用的属性；player省略时使用当前原因玩家。"],
    "Card.IsNotTuner": ["检查c对同调怪兽scard而言是否被视为非调整。"],
    "Duel.GetOverlayCount": ["返回player视角下s和o位置中的超量素材数量。"],
    "Duel.Readjust": [
        "为当前原因效果的处理对象请求场地重新调整。",
        "同一处理对象在当前追踪表中请求超过3次时，核心会把它因规则送去墓地。",
    ],
    "Auxiliary.IsMaterialListSetCard": ["检查c的material_setcode元数据是否列有setcode，并支持打包子系列匹配。"],
    "Auxiliary.qlifilter": [
        "机壳免疫用Value辅助函数。",
        "接受由原本等级或阶级低于处理对象当前等级的怪兽发动的怪兽效果，并拒绝连接怪兽。",
    ],
    "Card.GetOriginalRank": ["返回c卡片数据中的原本阶级；c不是超量怪兽时返回0。"],
    "Card.GetRightScale": ["返回c当前的右灵摆刻度数值。"],
    "Card.GetSynchroLevel": ["返回c为同调怪兽scard提供的同调等级数值。"],
    "Card.IsCanHaveCounter": ["检查c能否持有countertype类型的指示物。"],
    "Card.IsDualState": ["检查c当前是否受EFFECT_DUAL_STATUS影响。"],
    "Card.IsRelateToCard": ["检查c1当前是否与c2保持关系。"],
    "Auxiliary.AddFusionProcMix": [
        "给fcard登记固定数量的混合融合素材手续。",
        "每个额外参数都是一个必需素材槽，可以是卡号、筛选函数或替代项table。数字素材槽会更新列名素材元数据。",
    ],
    "Auxiliary.CheckUnionEquip": ["检查同盟怪兽uc与对象tc之间的同盟装备数量兼容性，可选择忽略部分新式同盟数量。"],
    "Auxiliary.linklimit": ["特殊召唤条件辅助函数：仅当st包含SUMMON_TYPE_LINK时返回true。"],
    "bit.bxor": ["返回a与b的按位异或结果。"],
    "bit.rshift": ["返回a右移b位后的结果。"],
    "Card.CheckUnionTarget": [
        "检查target是否是在EFFECT_UNION_LIMIT下c的合法同盟装备对象。",
        "核心还会检查c与target之间的新式/旧式同盟数量兼容性。",
    ],
    "Card.EnableDualState": ["给c登记带客户端提示的EFFECT_DUAL_STATUS效果。"],
    "Card.GetColumnGroupCount": ["返回与c所在纵列重叠的卡数量。"],
    "Card.GetHandSynchro": [
        "返回c上的手牌同调启用效果、其Target函数，以及手牌素材数量min/max。",
        "只检查怪兽区域中的卡。优先检查EFFECT_HAND_SYNCHRO，其次检查带LOCATION_HAND的EFFECT_TUNER_MATERIAL_LIMIT。",
    ],
    "Card.GetTributeRequirement": ["返回通常召唤c所需的最小和最大解放数量。"],
    "Card.SetHint": ["向客户端发送c的卡片提示消息，内容为提示type和值value；type大于等于CHINT_DESC_ADD时会被忽略。"],
    "Duel.CheckChainUniqueness": ["检查当前全部连锁环的处理对象卡号是否互不相同。"],
    "Duel.SelectField": [
        "让player从location1/location2对应的场地区域中选择count个区域，并把filter视为不可选择区域。",
        "提供desc时，核心会显示该选择提示。返回值是从player视角表示已选区域的位掩码。",
    ],
    "Group.Remove": ["从可修改的Group g中移除满足f且不等于ex的卡，并把额外参数传给f。"],
    "Auxiliary.AddFusionProcShaddoll": ["登记影依融合素材手续，要求1只影依素材以及1只把attr作为融合素材属性的素材。"],
    "Auxiliary.evospcon": ["进化龙式效果以及0x304e系列怪兽特殊召唤用的特殊召唤条件辅助函数。"],
    "Card.GetDestination": ["返回c当前送去参数中保存的目标位置。"],
    "Card.GetPreviousAttackOnField": ["返回c之前场上状态记录的攻击力数值。"],
    "Card.GetRitualLevel": ["返回c为仪式怪兽rc提供的仪式等级数值。"],
    "Duel.SwapSequence": [
        "当c1和c2由同一玩家控制、都在怪兽区域且都受当前原因效果影响时，交换它们的怪兽区域序号。",
        "交换成功时，核心会为这两张卡引发移动事件。",
    ],
    "Auxiliary.AddFusionProcFunFun": ["登记融合手续，要求1只满足f1的素材以及cc只满足f2的素材。"],
    "Auxiliary.nzdef": ["表侧表示且当前守备力大于0的卡返回true。"],
    "bit.lshift": ["返回a左移b位后的结果。"],
    "Duel.GetLinkedGroup": ["返回player视角下s和o位置中处于连接状态区域的卡组成的Group。"],
    "Auxiliary.SelectSameCount": [
        "让tp构建一个从g1和g2中选取相同数量卡的选择结果。",
        "except会先从两个Group中移除。若min大于计算出的max，结果可以为nil。",
    ],
    "Auxiliary.TuneMagicianCheckX": ["检查c是否具有ecode效果，且该效果的Value会拒绝已选Group sg中的至少另一张卡。"],
    "Auxiliary.IsUnionState": [
        "当effect的处理对象具有EFFECT_UNION_STATUS且正在装备时，返回其装备对象。",
        "该Lua表达式成功时返回可作为真值使用的Card；没有同盟状态效果时返回false；没有装备对象时返回nil。",
    ],
    "Card.IsLinkCode": [
        "检查c作为连接素材使用时是否匹配任意给定卡号。",
        "会检查c当前卡号、第二卡号以及EFFECT_ADD_LINK_CODE追加的卡号。没有连接卡号追加效果时，该绑定退回使用Card.IsCode。",
    ],
    "Duel.ChangeChainOperation": ["把chainc连锁环的Operation函数替换为f。"],
    "Group.Clear": ["清空g；若g为只读Group则不会清空。"],
    "Auxiliary.sumreg": ["对eg中原本卡号等于e的Label的每张卡登记同卡号的标志效果，持续到结束阶段/重置。"],
    "Card.GetEffectCount": ["返回c的效果筛选中当前找到的code效果数量。"],
    "Card.GetPreviousPosition": ["返回c之前记录的表示形式数值。"],
    "Card.IsCanRemoveCounter": ["检查player能否因reason从c上取除count个countertype类型的指示物。"],
    "Card.IsLinkSummonable": [
        "检查连接怪兽c能否由当前原因玩家进行连接召唤。",
        "可选的materials、lcard、minc、maxc会限制核心检查使用的连接素材池和素材数量。",
    ],
    "Card.IsRankBelow": ["检查c是否具有非0阶级，且阶级小于等于rank。"],
    "Duel.ClearTargetCard": ["清空当前连锁环记录的取对象卡组；没有记录时不处理。"],
    "Duel.LinkSummon": [
        "为player开始对c进行规则连接召唤。",
        "materials、lcard、minc、maxc会成为临时连接召唤限制；该绑定交给核心处理并且不返回Lua值。",
    ],
    "Duel.Win": ["把player设置为因reason获得决斗胜利；如果核心已经记录胜者，则不会覆盖。"],
    "Auxiliary.AddFusionProcCode3": ["登记需要卡号code1、code2、code3的怪兽作为固定融合素材的融合素材手续。"],
    "Auxiliary.SameValueCheck": ["检查g中的所有卡是否共享f返回值中的至少一个位；0张或1张卡的Group返回true。"],
    "Card.GetLinkCode": ["返回c作为连接素材使用时的卡号：当前卡号、存在时的第二卡号，以及EFFECT_ADD_LINK_CODE的追加值。"],
    "Card.GetUnionCount": ["返回c当前的新式同盟数量和旧式同盟数量。"],
    "Duel.CheckEvent": [
        "不传get_info时，返回当前事件状态中是否存在event。",
        "get_info为true且找到事件时，返回true以及事件卡组、事件玩家、事件值、原因效果、原因、原因玩家；没有找到时只返回false。",
    ],
    "Duel.SetSelectedCard": ["把核心必须选择列表设置为一张Card，或设置为Group中的全部卡，供之后的选择辅助函数使用。"],
    "Duel.SwapControl": [
        "交换两张Card或两组Group的控制权，并返回交换处理器是否成功。",
        "reset_phase和reset_count是可选的临时控制权重置设置。",
    ],
    "Group.SelectWithSumEqual": [
        "让player从g中选择若干卡，使f的合计值等于acc，选择数量在min到max之间。",
        "先前用Duel.SetSelectedCard设置的卡会强制计入合计、从可选池移除、处理后清空，且不会包含在返回的Group中。",
    ],
    "Auxiliary.bdcon": ["战斗破坏条件辅助函数：处理对象仍与战斗相关时返回true。"],
    "Card.GetAttackAnnouncedCount": ["返回c的攻击宣言次数。"],
    "Card.GetTextDefense": ["返回c卡片数据中记载/保存的守备力数值；c处于无等级状态时返回0。"],
    "Card.ResetEffect": ["手动重置c上匹配code和reset_type的效果。"],
    "Card.GetCardTargetCount": ["返回c当前记录的持续取对象卡数量。"],
    "Card.GetFusionAttribute": ["返回c作为融合素材使用时对player使用的属性；player省略时使用当前原因玩家。"],
    "Card.GetSummonPlayer": ["返回记录为召唤c的玩家。"],
    "Auxiliary.gbspcon": ["剑斗兽式返回以及0x1019系列怪兽特殊召唤用的特殊召唤条件辅助函数。"],
    "Card.CreateRelation": ["建立从c1到c2的关系，并按reset清除。"],
    "Card.GetMutualLinkedGroupCount": ["返回与c互相连接的卡数量。"],
    "Card.IsExtraDeckMonster": ["检查c是否属于核心视为额外卡组怪兽的卡种。"],
    "Duel.AnnounceCoin": ["让player从内置硬币面选项中选择一个，并返回从0开始的选项索引。"],
    "Auxiliary.synlimit": ["特殊召唤条件辅助函数：仅当st包含SUMMON_TYPE_SYNCHRO时返回true。"],
    "Card.GetCardTarget": ["返回包含c当前记录的全部持续取对象卡的Group。"],
    "Card.GetLinkRace": ["返回c作为连接素材使用时对player使用的种族；player省略时使用当前原因玩家。"],
    "Card.IsLinkBelow": ["检查c是否具有非0连接值，且连接值小于等于link。"],
    "Card.IsLinkState": ["检查c当前是否处于连接状态。"],
    "Auxiliary.AddXyzProcedureLevelFree": [
        "给c登记不检查等级的超量召唤手续。",
        "该辅助函数使用f、gf、minc、maxc以及可选的替代召唤设置，且没有显式返回值。",
    ],
    "Auxiliary.IsCanBeQuickEffect": ["检查玩家tp是否受code影响、code是否登记了快速效果筛选，并且该筛选是否接受c。"],
    "Card.GetColumnZone": [
        "返回loc范围内与c所在纵列重叠的区域位掩码。",
        "提供player且视角为对方时，核心会交换掩码中的双方区域部分。",
    ],
    "Card.GetFusionCode": [
        "返回c作为融合素材使用时的卡号：当前卡号、存在时的第二卡号，以及EFFECT_ADD_FUSION_CODE的追加值。",
        "核心以not_material状态检查时，只返回当前卡号和第二卡号。",
    ],
    "Card.IsOriginalSetCard": ["检查c的原本系列数据是否匹配任意给定系列代码。"],
    "Card.SetFlagEffectLabel": ["把c上code对应的第一个标志效果Label设置为label，并返回是否找到标志效果。"],
    "Group.CheckWithSumGreater": [
        "检查g是否能满足f的合计值至少为acc。",
        "先前用Duel.SetSelectedCard设置的卡会强制计入合计，且必须选择列表会在返回前清空。",
    ],
    "Auxiliary.AddRitualProcEqual2": ["使用Card.GetLevel登记等级正好相等的仪式召唤手续，并返回创建的Effect。"],
    "Auxiliary.bdgcon": ["战斗破坏条件辅助函数：处理对象的战斗对象是墓地中的怪兽时返回true。"],
    "Card.GetLinkedGroupCount": ["返回位于c所连接区域中的卡数量。"],
    "Card.GetPosition": ["返回c当前的表示形式数值。"],
    "Card.GetRealFieldID": ["返回c的真实field ID，即核心用于关系追踪的场上识别值。"],
    "Duel.ChangeTargetCard": ["把chainc连锁环记录的取对象卡组替换为g。"],
    "Card.RemoveCounter": [
        "由player因reason从c上取除count个countertype类型的指示物。",
        "countertype为0时，核心会清除c上的全部指示物且不返回Lua值。否则会让处理器取除指定指示物，并返回是否成功。",
    ],
    "Duel.CalculateDamage": [
        "开始attacker与attack_target之间的伤害计算；attack_target为nil时表示直接攻击。",
        "new_attack为可选参数，会传给伤害步骤处理器。attacker和attack_target是同一张卡时，该绑定不开始伤害计算且不返回值。",
    ],
    "Effect.GetProperty": ["返回e的两个属性标志字段flag1和flag2。"],
    "Auxiliary.SetUnionState": [
        "在c成为装备卡后，为其适用已装备的同盟状态。",
        "若c具有EFFECT_UNION_LIMIT效果，则登记对应的EFFECT_EQUIP_LIMIT和EFFECT_UNION_STATUS重置效果。旧式同盟卡还会获得EFFECT_OLDUNION_STATUS。",
    ],
    "Card.IsLinkAbove": ["检查c是否具有非0连接值，且连接值大于等于link。"],
    "Card.IsSummonableCard": [
        "检查c的卡片数据是否属于按卡种可以通常召唤或盖放的怪兽。",
        "非怪兽、额外卡组怪兽、仪式怪兽、特殊召唤怪兽和衍生物会返回false。该函数不检查当前费用、召唤次数、位置或玩家限制。",
    ],
    "Duel.AnnounceRace": ["让player从available中宣言count个种族，并返回所选RACE_*位掩码。"],
    "Duel.ChangeAttackTarget": [
        "把当前攻击对象改为target；target为nil时改为直接攻击。返回是否成功变更。",
        "当前攻击怪兽必须存在、可以攻击，且攻击未被取消。卡片对象必须是当前合法攻击对象之一；直接攻击要求攻击怪兽未被禁止直接攻击。",
    ],
    "Duel.IsPlayerCanSpecialSummon": [
        "只提供player时，检查player是否允许进行特殊召唤，且仍有可用的特殊召唤次数。",
        "提供可选的卡片相关参数时，使用当前原因效果检查player能否以sumtype和sumpos把c特殊召唤到target_player场上。",
    ],
    "Duel.ResetFlagEffect": ["重置player持有的code对应全部玩家标志效果。"],
    "Duel.SelectPosition": ["让player为c从允许的表示形式中选择一个，并返回所选POS_*数值。"],
    "Effect.GetCost": ["返回e的费用函数；未设置费用函数时返回nil。"],
    "Card.GetLeftScale": ["返回c当前的左灵摆刻度数值。"],
    "Card.GetPreviousAttributeOnField": ["返回c之前场上状态记录的属性数值。"],
    "Card.GetSummonType": ["返回c记录的召唤类型位，并按默认召唤类型字段进行掩码。"],
    "Duel.IsPlayerCanSummon": [
        "只提供player时，检查player是否未被无目标的EFFECT_CANNOT_SUMMON禁止通常召唤。",
        "提供sumtype和c时，检查player对c以该sumtype通常召唤时受到的EFFECT_CANNOT_SUMMON限制。该绑定不检查召唤次数、费用、解放可用性或区域可用性。",
    ],
    "Card.CopyEffect": [
        "把卡号code的initial_effect复制到c上，并返回生成的复制id；code对应通常怪兽时返回-1。",
        "reset为0时默认RESETS_STANDARD。count默认1；带阶段重置但未指定自己/对方回合时，会规范为双方回合。若c是非效果怪兽，核心还会以同样重置条件追加TYPE_EFFECT。",
    ],
    "Card.GetMaterialCount": ["返回当前记录为c素材的卡数量。"],
    "Card.IsRankAbove": ["检查c是否具有非0阶级，且阶级大于等于rank。"],
    "Duel.CheckPhaseActivity": ["返回当前阶段是否已经记录过行动。"],
    "Auxiliary.Tuner": ["返回一个素材筛选函数：接受对syncard来说是调整，且在提供f时满足f(target, ...)的卡。"],
    "Card.GetBattlePosition": ["返回c的临时战斗表示形式快照。"],
    "Card.IsXyzType": ["检查c作为超量素材使用时的类型是否包含type。"],
    "Duel.AnnounceLevel": [
        "让player宣言等级，并返回宣言的等级以及从0开始的选项索引。",
        "min和max默认1与12；min大于max时会交换。额外的等级参数会从选项中排除；没有剩余等级时，该绑定不返回值。",
    ],
    "Duel.GetTargetCount": ["统计给定场上位置中匹配filter且可作为效果对象的卡数量；提供exception时将其排除。"],
    "Duel.IsCanAddCounter": [
        "只提供player时，检查player是否未被禁止放置指示物。",
        "提供countertype、count和c时，检查player能否在c上放置该数量的countertype指示物。",
    ],
    "Duel.SendtoExtraP": ["因reason把卡以表侧送去player方额外卡组，并返回实际移动的卡数量。"],
    "Auxiliary.ritlimit": ["特殊召唤条件辅助函数：仅当召唤类型包含SUMMON_TYPE_RITUAL时返回true。"],
    "Card.GetCurrentScale": [
        "返回c当前使用的灵摆刻度。",
        "在灵摆区域时，会按c所在区域序号返回当前左/右刻度；不在灵摆区域时，返回c记载的左刻度数值。",
    ],
    "Card.GetLocation": ["返回c当前所在位置；c当前被当作不在场上时返回0。"],
    "Duel.AnnounceType": [
        "让player从核心内置的怪兽/魔法/陷阱类型选项中选择，并返回从0开始的选项索引。",
        "返回值是所选选项索引，不是TYPE_*位掩码。",
    ],
    "Duel.IsPlayerCanAdditionalSummon": ["当player在core.extra_summon中没有待处理的额外通常召唤标记时返回true。"],
    "Group.GetMinGroup": [
        "对g中的每张卡调用f，转发额外参数，并返回所有最小值并列卡组成的Group。",
        "第二个返回值是最小整数值。g为空时，该绑定不返回Lua值。",
    ],
    "Card.GetPreviousCodeOnField": [
        "返回c之前场上状态记录的卡号。",
        "若之前状态有第二卡号，则第二卡号作为第2个返回值返回。",
    ],
    "Card.IsHasCardTarget": ["检查c1当前是否把c2作为持续取对象卡。"],
    "Duel.GetBattleDamage": ["返回当前为player记录的战斗伤害。"],
    "Duel.GetLinkedZone": ["返回从player视角看当前被连接标记指向的区域位掩码。"],
    "Auxiliary.damcon1": [
        "用于判断玩家tp是否会受到效果伤害的条件辅助函数。",
        "它检查操作信息中对tp造成的伤害，或被反转成伤害的对tp恢复，并会考虑EFFECT_REVERSE_DAMAGE、EFFECT_REVERSE_RECOVER和EFFECT_NO_EFFECT_DAMAGE。",
    ],
    "Auxiliary.EnableUnionAttribute": [
        "为c登记标准现代同盟怪兽组件。",
        "该辅助函数会添加装备卡破坏代替、使用filter的EFFECT_UNION_LIMIT、从怪兽区域把c装备给合法怪兽的起动效果，以及从魔法与陷阱区域特殊召唤c的起动效果。",
    ],
    "Card.GetReason": [
        "返回c当前记录的原因位掩码/数值。",
        "这是c当前状态中记录的原因，例如REASON_EFFECT、REASON_COST或REASON_BATTLE；并不只用于表示形式变更。",
    ],
    "Card.IsDefenseBelow": [
        "检查c已知的当前守备力是否小于等于def。",
        "连接怪兽和非怪兽返回false；未知或负数守备力也返回false。",
    ],
    "Card.IsFusionCode": [
        "检查c作为融合素材使用时，是否能当作任意给定code。",
        "核心会计入c当前卡号、第二卡号以及EFFECT_ADD_FUSION_CODE数值。没有适用的融合专用追加卡号，或素材卡号检查被禁用时，退回Card.IsCode检查。",
    ],
    "Auxiliary.EnableDualAttribute": [
        "为c登记标准二重怪兽处理。",
        "该卡可以再次通常召唤；并且在怪兽区域或墓地表侧表示且不处于二重状态时，当作通常怪兽而不是效果怪兽。",
    ],
    "Card.GetPreviousEquipTarget": ["返回c之前的装备对象；没有时返回nil。"],
    "Duel.CheckRemoveOverlayCard": [
        "检查player能否因reason从指定的己方/对方场上位置取除至少count个超量素材。",
        "s表示从player视角看的己方场上位置，o表示对方场上位置。可适用的替代效果也能满足该检查。",
    ],
    "Auxiliary.IsMaterialListCode": ["检查code是否存在于c.material中；该表通常由AddMaterialCodeList填充。返回true或nil。"],
    "Card.IsChainAttackable": [
        "检查当前攻击怪兽能否按连续攻击规则再次攻击。",
        "这个核心绑定会校验c，但实际检查决斗中的当前攻击怪兽。ac默认2，monsteronly要求必须有攻击对象，不能直接攻击。",
    ],
    "Auxiliary.IsDualState": ["条件辅助函数：e的处理对象未被无效且处于二重状态时返回true。"],
    "Auxiliary.mzctcheckrel": ["检查因reason解放g后是否留下怪兽区域，并且g是否是tp可用的有效解放组。"],
    "Duel.SetChainLimitTillChainEnd": ["登记持续到当前连锁结束的连锁限制回调。"],
    "Duel.IsDamageCalculated": ["返回当前战斗/伤害步骤状态中是否已经进行过伤害计算。"],
    "Duel.RDComplete": ["在Duel.Damage或Duel.Recover以is_step=true调用后，完成保留的分步伤害/恢复处理。"],
    "Card.IsReleasableByEffect": ["使用当前原因玩家和原因效果，检查c是否能被当前处理中的效果解放。"],
    "Duel.AdjustInstantly": [
        "立即进行场上调整。",
        "提供c时，核心会先刷新与c相关卡的无效关联，再调整场上状态。",
    ],
    "Auxiliary.EnableSpiritReturn": [
        "为c登记灵魂怪兽回手设置。",
        "任意列出的事件发生时，会在怪兽区域创建结束阶段回到手牌的效果，并遵守EFFECT_SPIRIT_DONOT_RETURN和EFFECT_SPIRIT_MAYNOT_RETURN。",
    ],
    "Card.ResetFlagEffect": ["重置c上code对应的全部标志效果。"],
    "Duel.RemoveOverlayCard": [
        "让player因reason从指定的己方/对方场上位置取除min到max个超量素材。",
        "s表示从player视角看的己方场上位置，o表示对方场上位置。返回值为实际取除的素材数量。",
    ],
    "Effect.IsHasCategory": ["检查e的category位掩码是否包含cate。"],
    "Card.GetTurnCounter": ["返回c的回合计数器。"],
    "Card.IsLink": ["检查c:GetLink()是否等于任意给定link值。nil的link参数会被跳过；非连接怪兽按0比较。"],
    "Card.IsSynchroType": ["检查c作为同调素材使用时的类型是否包含type。"],
    "Duel.ClearOperationInfo": ["清除连锁ct的操作信息；该连锁环不存在时不做处理。"],
    "Duel.ShuffleExtra": ["洗切player的额外卡组。"],
    "Auxiliary.AddRitualProcGreaterCode": [
        "为仪式怪兽code1登记仪式召唤手续，允许素材仪式等级合计大于等于仪式怪兽原本等级。",
        "该辅助函数还会把code1加入c的卡号/素材列表，并返回创建的手续效果。",
    ],
    "Card.SetTurnCounter": ["设置c的回合计数器。"],
    "Auxiliary.AddSynchroMixProcedure": [
        "登记混合同调召唤手续：最多3个固定素材筛选条件，加上f4重复minc到maxc次。",
        "最大数量会按c的等级扣除必要固定素材后进行上限限制。",
    ],
    "Auxiliary.nzatk": ["筛选辅助函数：表侧表示且当前攻击力大于0的卡返回true。"],
    "Card.SetCounterLimit": ["为c添加countertype对应的EFFECT_COUNTER_LIMIT，数值为limit。"],
    "Group.CheckWithSumEqual": ["检查g的某个子集（包括所有必须选择的卡）能否用min到max张卡使f的合计正好等于acc。"],
    "Duel.IsPlayerCanRemove": [
        "只提供player时，检查player是否未被禁止除外。",
        "提供c时，检查player能否因reason除外c；reason默认REASON_EFFECT。",
    ],
    "Duel.AnnounceCard": ["让player宣言一个匹配可选opcode/filter表达式的卡号，并返回所选卡号。"],
    "Duel.RaiseSingleEvent": ["以code、re、r、rp、ep、ev为ec引发单卡事件，然后处理单卡事件。"],
    "Auxiliary.CreateChecks": ["返回一组单卡检查函数；每个函数调用f(c, list[i])。"],
    "Auxiliary.RitualCheck": ["仪式素材组判定：检查区域可用性、指定的Greater/Equal等级规则、自定义mat_group_check以及RCheckAdditional。"],
    "Card.IsXyzSummonable": ["检查超量怪兽c能否由当前原因玩家用可选素材组和min/max限制进行超量召唤。"],
    "Duel.XyzSummon": ["为player和c执行规则超量召唤，可使用可选素材组和min/max限制。"],
    "Auxiliary.bdogcon": ["战斗破坏用条件辅助函数：处理对象仍与战斗相关，和对方怪兽进行过战斗，且该战斗对象是墓地中的怪兽。"],
    "Card.GetEquipCount": ["返回当前装备给c的装备卡数量。"],
    "Card.GetFirstCardTarget": ["返回c的第1个持续取对象卡；没有时返回nil。"],
    "Duel.SortDecktop": [
        "让sort_player重新排列target_player主卡组最上方count张卡。",
        "两名玩家都必须有效，且count至少为1。count大于剩余卡组数量时，处理器只排列实际存在的最上方卡。",
    ],
    "Duel.RemoveCounter": [
        "让player因reason从指定场上位置取除count个countertype类型的指示物，并返回是否成功取除。",
        "s表示从player视角看的己方场上位置，o表示对方场上位置。核心会在取除指示物前提供可适用的指示物取除替代效果。",
    ],
    "Duel.TossDice": [
        "为player投掷count1个骰子；提供count2时，为对方再投掷count2个骰子。",
        "有效骰子结果为1到6的整数。通常脚本用法应保持count1 + count2不超过5；核心会拒绝count1 <= 0和count2 < 0。",
    ],
    "Card.IsLinkAttribute": [
        "检查c作为连接素材使用时的属性是否包含attribute。",
        "player默认当前原因玩家。核心使用c:GetLinkAttribute(player)，因此会计入连接素材用属性变更效果。",
    ],
    "Card.IsOriginalCodeRule": [
        "检查c按规则使用的原本卡号是否匹配任意给定code。",
        "nil的code参数会被跳过。双卡号卡会检查两个规则原本卡号；其他卡检查核心使用的决斗卡号。",
    ],
    "Duel.GetBattleMonster": [
        "返回当前战斗中由player控制的怪兽，然后返回当前战斗中由对方控制的怪兽。",
        "若对应控制者没有攻击怪兽或攻击对象，则对应返回值为nil。",
    ],
    "Duel.SkipPhase": [
        "适用一个临时场上效果，使player跳过phase阶段。",
        "phase必须是PHASE_DRAW、PHASE_STANDBY、PHASE_MAIN1、PHASE_BATTLE、PHASE_MAIN2或PHASE_END之一。reset_count小于等于0时按1处理，value会保存在生成的跳过阶段效果上。",
    ],
    "Card.GetPreviousRaceOnField": ["返回c之前场上状态记录的种族数值。"],
    "Card.CreateEffectRelation": [
        "在c与效果e之间建立关联。",
        "若e是当前连锁中某个连锁环的发动效果，该关联会绑定到该连锁环；否则核心会保存直接的效果关联。",
    ],
    "Card.GetLink": ["返回c的连接值；c不是连接怪兽时返回0。"],
    "Card.IsAttackable": [
        "检查c当前是否满足核心的基础可攻击条件。",
        "该卡必须是表侧攻击表示，或带EFFECT_DEFENSE_ATTACK的表侧守备表示，并且不能处于禁止状态、不能攻击、攻击被无效，或回合玩家被跳过战斗阶段。该函数不检查攻击宣言费用。",
    ],
    "Card.SetStatus": [
        "设置或清除c上的status状态位。",
        "这是内部状态辅助函数。c正在复制其他卡效果时，该绑定不做处理。",
    ],
    "Duel.AnnounceAttribute": [
        "让player从available属性位掩码中宣言count个属性，并返回所选属性位掩码。",
        "available应为ATTRIBUTE_*常量的按位组合。",
    ],
    "Group.GetMaxGroup": [
        "对g中的每张卡调用f，转发额外参数，并返回所有最大值并列卡组成的Group。",
        "第二个返回值是最大整数值。g为空时，该绑定不返回Lua值。",
    ],
    "bit.bor": ["返回a与b的按位或结果。"],
    "Card.IsDefenseAbove": [
        "检查c当前守备力是否大于等于def。",
        "连接怪兽，以及不是怪兽且当前未被当作怪兽的卡，返回false。",
    ],
    "Effect.SetOwnerPlayer": [
        "将效果e的拥有者玩家设为player。",
        "只接受0和1作为player；其他值不会改变该效果。",
    ],
    "Auxiliary.imval1": ["EFFECT_CANNOT_BE_BATTLE_TARGET默认Value辅助函数；c不免疫e时返回true。"],
    "Card.GetReasonEffect": ["返回c当前记录的原因效果；没有记录原因效果时返回nil。"],
    "Card.GetTurnID": [
        "返回c保存的回合ID。",
        "核心在卡加入某个位置时更新该值，因此脚本常用它与Duel.GetTurnCount()比较来判断同回合时点。",
    ],
    "Card.IsDisabled": ["检查c当前是否带STATUS_DISABLED。"],
    "Duel.NegateSummon": [
        "无效targets正在进行的通常召唤、反转召唤或特殊召唤。",
        "targets可以是Card或Group。通常召唤与反转召唤的无效要求只有1张卡；特殊召唤无效可以处理Group，并且只无效当前原因效果可以无效其召唤的卡。核心会引发对应的*_SUMMON_NEGATED事件，且不返回Lua值。",
    ],
    "Duel.SelectDisableField": [
        "让player从请求的己方与对方位置中选择count个可用场地区域，并返回所选区域位掩码。",
        "location1应用于player场上，location2应用于对方场上。核心会把count限制为可用区域数量；没有可选区域时不返回值。",
    ],
    "Duel.IsPlayerCanSpecialSummonCount": [
        "检查player在当前剩余特殊召唤次数限制下，能否进行count次特殊召唤。",
        "核心会检查EFFECT_LEFT_SPSUMMON_COUNT效果以及该玩家的特殊召唤计数器。",
    ],
    "Card.CheckEquipTarget": [
        "检查c2是否是c1的合法装备对象。",
        "核心要求c1受到接受c2的EFFECT_EQUIP_LIMIT影响，并且还会检查旧式和现代同盟怪兽的装备数量限制。",
    ],
    "Card.GetOriginalCodeRule": [
        "返回c按规则使用的原本卡号。",
        "双卡号卡返回两个卡号：记载的原本卡号和第二规则卡号。其他卡只返回核心使用的决斗卡号。",
    ],
    "Auxiliary.chainreg": [
        "若效果e的处理者还没有FLAG_ID_CHAINING，则给其登记该标记效果。",
        "该标记按标准事件重置，但不因回合盖放重置，并会在连锁结束时重置。",
    ],
    "Duel.EnableGlobalFlag": ["启用决斗中的指定core global_flag位，且不返回Lua值。"],
    "Duel.TossCoin": [
        "为player投掷count枚硬币，并为每次投掷返回1个整数结果。",
        "结果为0或1。通常脚本用法传入正数count且不超过MAX_COIN_COUNT；该绑定拒绝0和小于-1的值，并将过大的正数限制为核心最大值。",
    ],
    "Card.GetColumnGroup": [
        "返回与c位于同一纵列的卡组成的Group。",
        "此MDPro3/YGOPro绑定只接收c。它使用c当前场上的纵列，包含相关怪兽区域、魔法与陷阱区域以及额外怪兽区域的纵列关系；若c不在场上，返回的Group为空。",
    ],
    "Duel.GetFirstMatchingCard": [
        "返回指定位置中第一张满足f且未被ex排除的卡。",
        "f可以为nil。ex可以是Card、Group或nil，ex之后的额外参数会传给f。没有匹配卡时返回nil。",
    ],
    "Card.IsFusionAttribute": [
        "检查c作为融合素材使用时的属性是否包含attribute。",
        "player默认当前原因玩家。核心使用c:GetFusionAttribute(player)，因此会计入融合素材用属性变更效果。",
    ],
    "Duel.GetActivityCount": [
        "按传入的activity_type顺序返回player的行动次数。",
        "内置支持ACTIVITY_SUMMON、ACTIVITY_NORMALSUMMON、ACTIVITY_SPSUMMON、ACTIVITY_FLIPSUMMON、ACTIVITY_ATTACK和ACTIVITY_BATTLE_PHASE。其他值在该绑定中返回0，包括ACTIVITY_CHAIN。",
    ],
    "Effect.UseCountLimit": [
        "手动消耗玩家p对效果e的count次次数限制。",
        "count默认1。oath_only为true时，只有e的次数代码包含EFFECT_COUNT_CODE_OATH才会消耗次数；否则该绑定会直接减少次数限制。",
    ],
    "Card.GetOriginalRace": ["返回c卡片数据中的原本种族；c带STATUS_NO_LEVEL时返回0。"],
    "Card.GetOverlayCount": ["返回c当前叠放的超量素材数量。"],
    "Card.IsCanAddCounter": [
        "检查当前原因玩家能否在c上放置count个countertype类型的指示物。",
        "loc为0时，c必须当前表侧表示存在于场上。loc不为0时，改为用loc检查指示物许可效果的范围。singly为true时，指示物上限按当前数量+1检查，而不是按当前数量+count检查。",
    ],
    "Duel.SetLP": ["将player的LP设为lp；lp为负数时限制为0，并发送LP更新消息。"],
    "Auxiliary.AddFusionProcCodeFun": [
        "给c登记需要code1以及cc个满足f的额外融合素材的融合召唤手续。",
        "该辅助函数会构造cc份f，并连同sub和insf转交给Auxiliary.AddFusionProcMix。",
    ],
    "Duel.AnnounceNumber": [
        "让player从给定数字中选择1个。",
        "返回被选择的数字，以及该数字在核心选项列表中的0基序号。",
    ],
    "Card.GetBaseDefense": ["返回c当前的基础守备力。未知或负数基础守备力会被该绑定限制为0。"],
    "Card.SetSPSummonOnce": [
        "将c标记为按spsummon_code共享每回合1次的特殊召唤限制。",
        "具有相同非零spsummon_code的卡对每名玩家共享该限制。c正在复制其他卡效果时，该绑定不做处理。",
    ],
    "Card.IsPreviousSetCard": [
        "检查c之前记录的卡号或附加系列数据是否匹配任意给定setcode。",
        "nil的setcode参数会被跳过。该函数使用最近相关场上状态或表示形式更新前记录的状态，不检查c当前的系列。",
    ],
    "Duel.IsAbleToEnterBP": [
        "检查当前回合玩家是否仍能进入战斗阶段。",
        "核心要求决斗允许先攻攻击或当前不是第1回合，当前阶段早于PHASE_BATTLE_START，并且回合玩家不受EFFECT_CANNOT_BP影响。",
    ],
    "Duel.CheckTribute": [
        "检查是否存在可用于通常召唤或盖放c的合法祭品组合。",
        "max默认等于min，mg可以限制候选素材池，toplayer默认c当前控制者，zone默认当前额外召唤区域限制，若没有限制则为0x1f。",
    ],
    "Effect.GetActivateLocation": ["返回效果e发动时所在的位置。"],
    "Card.AddMonsterAttribute": [
        "通过效果给c追加临时怪兽属性。",
        "该绑定会清除STATUS_NO_LEVEL，用type适用EFFECT_PRE_MONSTER，并对非零的属性、种族、等级、基础攻击力和基础守备力数值适用对应变更效果。",
    ],
    "Card.GetPreviousTypeOnField": ["返回c之前场上状态记录的种类数值。"],
    "Duel.GetFieldCard": [
        "返回player的location中sequence位置的卡；该位置为空或无效时返回nil。",
        "若该位置的卡正在召唤或处于特殊召唤步骤状态，该绑定也返回nil。场地区域使用sequence 0，灵摆区域只在sequence 0和1且该卡当前标记为灵摆区域卡时返回。",
    ],
    "Card.GetOriginalAttribute": ["返回c卡片数据中的原本属性；c带STATUS_NO_LEVEL时返回0。"],
    "Duel.SelectTribute": [
        "让player为通常召唤或盖放c选择min到max只祭品，并返回选择的Group。",
        "mg可以限制候选素材池。toplayer默认player；toplayer不同于player时，核心会构建用于向该玩家场上解放的额外候选列表。",
    ],
    "Auxiliary.bdocon": ["EVENT_BATTLE_DESTROYING效果常用的条件辅助函数；处理者仍与战斗关联并且和对方怪兽战斗时返回true。"],
    "Card.IsCanBeXyzMaterial": [
        "检查c能否作为超量素材使用，可选指定要召唤的sc。",
        "核心会拒绝衍生物、超量素材用种类不是怪兽的卡、带STATUS_FORBIDDEN的卡，以及适用的EFFECT_CANNOT_BE_XYZ_MATERIAL效果。",
    ],
    "Card.GetPreviousControler": ["返回c之前记录的控制者。"],
    "Card.GetEquipGroup": ["以Group返回当前装备给c的装备卡。"],
    "Card.GetLinkedGroup": ["返回当前位于c连接区域中的卡。"],
    "Card.GetLinkedZone": [
        "返回c产生的连接区域位掩码。",
        "默认从c控制者视角返回。传入对方玩家作为player时，会交换自己/对方两部分位掩码，转换为该玩家视角。",
    ],
    "Card.GetPreviousSequence": ["返回c之前记录的位置序号。"],
    "Duel.ChainAttack": [
        "标记当前攻击怪兽，使其可以再次攻击；可选将攻击对象限制为卡c。",
        "该绑定只设置连续攻击状态，不返回Lua值。没有当前攻击怪兽，或攻击怪兽不受当前处理效果影响时，不做处理。",
    ],
    "Duel.IsCanRemoveCounter": [
        "检查player能否因reason从指定场上位置取除count个countertype类型的指示物。",
        "s表示从player视角看的己方场上位置，o表示对方场上位置。",
    ],
    "Card.IsControlerCanBeChanged": [
        "检查c的控制权当前能否转移给另一名玩家。",
        "c必须在怪兽区域，且不受EFFECT_CANNOT_CHANGE_CONTROL影响。ignore_mzone不为true时，对方还必须在zone指定范围内有可用的怪兽区域。",
    ],
    "Duel.NegateAttack": [
        "尝试无效当前攻击，并返回是否成功无效该次攻击。",
        "没有有效攻击怪兽、攻击怪兽离场或field ID变化、攻击怪兽不能攻击、伤害步骤状态不允许无效攻击，或攻击怪兽不受当前处理效果影响时，核心返回false。",
    ],
    "Card.GetCounter": [
        "返回c上的countertype类型指示物信息。",
        "countertype为0时，此核心返回c当前拥有的不同指示物类型数量，而不是全部指示物的总数。",
    ],
    "Card.GetDefense": ["返回c当前的守备力。未知或负数守备力会被该绑定限制为0。"],
    "Card.IsDefensePos": ["检查c当前表示形式是否包含POS_DEFENSE。"],
    "Card.IsReleasable": [
        "检查c能否由当前原因玩家作为非召唤用途被解放。",
        "reason默认REASON_COST。正在召唤中的卡、超量素材、墓地或除外的卡、手牌中的魔法/陷阱卡、玩家不能解放的卡，以及受EFFECT_UNRELEASABLE_NONSUM影响的卡会返回false。",
    ],
    "Card.SetCardTarget": [
        "把c2登记为c1的持续卡片对象。",
        "该函数保存的是供Card.GetCardTarget等函数以及相关卡无效检查使用的卡片对象关系，不是Duel.SelectTarget登记的连锁对象列表。",
    ],
    "Auxiliary.exccon": ["用于“送去墓地的当回合不能发动”类效果的条件辅助函数；处理者不是本回合送去墓地，或处理者因返回而记录原因时返回true。"],
    "Card.GetOriginalLevel": ["返回c卡片数据中的原本等级；超量怪兽、连接怪兽以及带STATUS_NO_LEVEL的卡返回0。"],
    "Group.RemoveCard": ["从g中移除c。除非g为只读Group，否则会直接修改g；不返回Lua值。"],
    "Auxiliary.AddFusionProcCode2": [
        "给c登记需要卡号为code1和code2的素材的融合召唤手续。",
        "该辅助函数会把sub和insf原样转交给Auxiliary.AddFusionProcMix。",
    ],
    "Duel.IsEnvironment": [
        "检查code当前是否被视为环境卡，或是否在请求的位置中存在匹配的表侧表示卡。",
        "player默认PLAYER_ALL，loc默认LOCATION_ONFIELD。核心会先检查场地区域；若没有表侧场地区域卡，也可以匹配最新的EFFECT_CHANGE_ENVIRONMENT效果。",
    ],
    "Auxiliary.indoval": ["对方效果破坏耐性使用的Value辅助函数；当rp是效果e处理者玩家的对方时返回true。"],
    "Duel.RaiseEvent": [
        "以给定效果、原因、原因玩家、事件玩家和事件值，对Card或Group引发事件code。",
        "核心在引发事件后处理即时事件并yield，不返回Lua值。",
    ],
    "Auxiliary.GCheckAdditional": [
        "Group.CheckSubGroup及相关选择辅助函数使用的全局额外子组检查钩子。",
        "默认实现返回true。召唤和选择手续会临时替换该函数以施加额外组限制，之后再恢复。",
    ],
    "Card.IsRank": [
        "检查c:GetRank()是否等于任意给定rank值。",
        "nil的rank参数会被跳过。该绑定直接比较数值阶级，不会额外要求c必须是超量怪兽，因此非超量卡会按阶级0参与比较。",
    ],
    "Card.GetTextAttack": [
        "返回c卡片数据中记录的攻击力。",
        "这是记载/数据库数值，不是当前攻击力。不同于Card.GetAttack，该绑定不会把未知攻击力限制为0；但带STATUS_NO_LEVEL的卡返回0。",
    ],
    "Duel.CheckLocation": ["检查player能否使用location中的sequence位置。"],
    "Card.GetRank": [
        "返回c当前的阶级。",
        "非超量卡返回0。超量怪兽不在怪兽区域时返回原本阶级；在怪兽区域时会应用阶级变更效果，结果最低为1。",
    ],
    "Card.GetOriginalCode": ["返回c卡片数据中的原本卡号。"],
    "Card.IsDefense": [
        "检查c不是连接怪兽、是怪兽或当前被当作怪兽，并且当前守备力是否等于任意给定def值。",
        "nil的def参数会被跳过。不同于旧导入文本，该绑定不会明确要求c位于怪兽区域。",
    ],
    "Auxiliary.fuslimit": ["特殊召唤条件辅助函数；当召唤类型st包含SUMMON_TYPE_FUSION时返回true。"],
    "Card.IsAbleToChangeControler": ["只检查c是否不受EFFECT_CANNOT_CHANGE_CONTROL影响。"],
    "Group.Sub": ["从g1中移除g2包含的每张卡。除非g1只读，否则会直接修改g1；g2不会改变。"],
    "Card.IsFusionType": [
        "检查c作为融合素材使用时的种类是否包含type。",
        "原本为怪兽的卡位于魔法与陷阱区域，且正在素材检查时，核心使用卡片数据中的种类；其他情况使用c当前种类。",
    ],
    "Duel.ReturnToField": [
        "把临时离场的卡返回到其之前的控制者和之前的位置。",
        "pos默认之前的表示形式，zone默认0xff。若c不是因REASON_TEMPORARY离场，该绑定不返回Lua值；否则会yield并返回移动是否成功。",
    ],
    "Duel.SetChainLimit": [
        "为当前连锁窗口登记临时连锁限制回调。",
        "该回调会与当前原因玩家一起保存，之后以f(e, chain_player, activating_player)调用；返回false时，该效果不能连锁。",
    ],
    "Card.CheckRemoveOverlayCard": [
        "检查player能否为了reason从c上取除至少count个超量素材。",
        "即使c本身素材不足，可适用的EFFECT_OVERLAY_REMOVE_REPLACE替代效果也可能使该函数返回true。",
    ],
    "Card.IsDestructable": [
        "检查c能否被破坏。",
        "不传e时，核心只排除超量素材以及已经在墓地或除外的卡。传入e时，会检查c是否受e影响，以及按当前原因玩家判断的效果破坏耐性。",
    ],
    "Card.RemoveOverlayCard": [
        "让player为了reason从c上取除min到max个超量素材，并返回实际取除数量。",
        "核心会在选择素材前提供可适用的EFFECT_OVERLAY_REMOVE_REPLACE替代效果。",
    ],
    "Auxiliary.IsCodeListed": [
        "检查code是否已通过Auxiliary.AddCodeList或相关辅助函数登记在c的card_code_list中。",
        "该Lua辅助函数在列名时返回true，否则返回nil，通常作为真假判断使用。",
    ],
    "Card.IsCanOverlay": [
        "检查c能否由player作为超量素材使用。",
        "player省略时使用当前原因玩家。核心会排除衍生物、处于非法状态的禁止使用卡，以及由对方控制且不能变更控制权的卡。",
    ],
    "Card.GetReasonPlayer": ["返回c当前记录的原因玩家，即c当前原因状态中的玩家。"],
    "Group.SelectUnselect": [
        "让player从cg中选择1张卡加入当前选择，或从sg中选择1张卡移出当前选择，并返回被选择的那张卡。",
        "sg可以为nil。finishable控制当前数量下能否结束选择，cancelable允许取消；取消时返回nil。min和max默认均为1。",
    ],
    "Card.GetAttribute": [
        "返回c当前的属性位掩码。",
        "被视为具有多个属性的卡可能返回多个ATTRIBUTE_*值的按位组合。",
    ],
    "Effect.GetOwnerPlayer": ["返回效果e记录的拥有者玩家。"],
    "Card.GetOriginalType": ["返回c原本卡片数据中的种类位掩码，而不是当前被修改后的种类。"],
    "Card.IsAttack": [
        "检查c是否为怪兽或当前被当作怪兽，并且当前攻击力是否等于任意给定的atk值。",
        "nil的atk参数会被跳过。不是怪兽且未被当作怪兽的卡返回false。",
    ],
    "Duel.GetCurrentChain": ["返回当前连锁中已记录的连锁环数量。"],
    "Auxiliary.ExceptThisCard": ["当效果e的处理者仍与当前连锁保持关联时返回该卡；否则返回nil。"],
    "Group.CreateGroup": ["新建并返回一个空Group。"],
    "Card.GetReasonCard": ["返回c当前记录的原因卡；没有记录原因卡时返回nil。"],
    "Card.GetOverlayGroup": ["返回当前叠放在c下面作为超量素材的卡组成的Group。"],
    "Card.IsAttackPos": ["检查c当前表示形式是否包含POS_ATTACK。"],
    "Card.IsCanChangePosition": [
        "检查核心中供效果改变表示形式使用的能力判断。",
        "在此MDPro3/YGOPro核心中，该底层辅助函数对连接怪兽返回false，对其他卡返回true；它不会执行更完整的手动改变战斗表示形式检查。",
    ],
    "Duel.ConfirmDecktop": [
        "向客户端公开player卡组最上方最多count张卡。",
        "count会被限制为剩余主卡组数量。函数会为公开等待而yield，不返回Lua值。",
    ],
    "Auxiliary.MustMaterialCheck": [
        "检查tp受到的code类型必须素材效果是否已经满足。",
        "v为nil时，只有Duel.GetMustMaterial(tp, code)为空才成功，但utility脚本中存在硬编码的超量和同调素材例外。v提供时，返回Duel.CheckMustMaterial(tp, v, code)的结果。",
    ],
    "Effect.IsActivated": ["检查效果e是否具有EFFECT_TYPES_CHAIN_LINK中的类型位。"],
    "Group.GetSum": ["对g中的每张卡调用f，转发额外参数，并返回各次整数结果的总和。"],
    "Card.AddCounter": [
        "尝试给c放置count个countertype类型的指示物，并返回核心是否接受该次放置。",
        "c必须受当前处理中的原因效果影响。放置指示物的玩家使用当前原因玩家。singly为true时，指示物上限检查允许只放置到剩余上限为止。",
    ],
    "Duel.MoveSequence": [
        "若c受当前处理中的原因效果影响，将c在其当前控制者与当前位置内移动到序号seq。",
        "核心会对移动的卡引发EVENT_MOVE，且不返回Lua值。",
    ],
    "Auxiliary.AddFusionProcFun2": ["给c登记需要1个满足f1和1个满足f2的素材的融合召唤手续。"],
    "Group.RandomSelect": [
        "返回一个新Group，包含从g中随机选出的count张卡。",
        "count会被限制为g的数量。player参数会写入随机选择消息，但不影响随机结果。",
    ],
    "Card.IsAttackAbove": [
        "检查c是否为怪兽或当前被当作怪兽，并且当前攻击力是否大于等于atk。",
        "不同于Card.IsAttackBelow，此核心在比较前不会额外检查攻击力未知的情况。",
    ],
    "Card.IsLinkRace": ["检查c作为player的连接素材使用时的种族是否包含race。player省略时使用当前原因玩家。"],
    "Auxiliary.SelectFromOptions": [
        "按条件筛选选项表，用可用选项文本调用Duel.SelectOption，并返回所选表的自定义值或原始序号。",
        "每个选项为{condition, option[, value]}。没有条件成立时返回nil。默认返回的序号从1开始，不同于Duel.SelectOption从0开始。",
    ],
    "Card.IsCanBeFusionMaterial": [
        "检查c能否作为fc和summon_type的融合素材使用。",
        "fc可省略，summon_type默认SUMMON_TYPE_FUSION。该绑定没有ignore_mon参数，而是交给核心的融合素材合法性检查处理。",
    ],
    "Card.IsLinkType": ["检查c作为连接素材使用时的种类是否包含type。"],
    "Card.IsLinkSetCard": ["检查c作为连接素材使用时能否视为任意给定setcode的系列卡。nil的setcode参数会被跳过。"],
    "Auxiliary.AddFusionProcFunRep": ["给c登记需要cc个满足同一素材筛选函数f的素材的融合召唤手续。"],
    "Card.GetFlagEffectLabel": [
        "返回c上编号为code的每个标记效果的第1个Label值。",
        "没有匹配的标记效果时返回nil；匹配的标记效果没有Label时，该位置返回0。",
    ],
    "Card.GetMaterial": ["返回c当前记录的素材卡Group。"],
    "Duel.GetChainMaterial": [
        "返回当前适用于player的第1个EFFECT_CHAIN_MATERIAL效果；没有时返回nil。",
        "融合类脚本通常读取该效果的Target和Operation回调，用于处理连锁素材替代流程。",
    ],
    "Duel.NegateRelatedChain": [
        "对当前连锁中由c发动且仍与c保持关联的连锁，给c登记临时的EFFECT_DISABLE_CHAIN效果。",
        "该无效效果以RESET_CHAIN、RESET_EVENT和传入的reset标志重置；若没有可处理的早前连锁，或c不受当前处理效果影响，核心不做处理。",
    ],
    "Card.IsSummonLocation": ["检查c记录的召唤位置是否包含loc。"],
    "Card.GetFieldID": [
        "返回c当前的field ID，即核心在c移动到当前位置时分配的时间标识。",
        "数值越小表示越早进入当前位置。此值不同于Card.GetRealFieldID，后者用于战斗状态等真实位置检查。",
    ],
    "Effect.GetFieldID": ["返回效果e的内部field ID。"],
    "Effect.IsHasProperty": [
        "检查效果e是否包含指定的效果Property标志。",
        "prop1检查第1个Property字段，可选的prop2检查第2个Property字段；某个字段传0时该字段视为通过。",
    ],
    "Card.CheckUniqueOnField": [
        "检查c在check_player场上是否满足当前唯一性规则，可以与已存在的卡共存。",
        "check_location默认LOCATION_ONFIELD，并会被限制为场上位置；测试即将移动的卡时，可用icard指定一张忽略的卡。",
    ],
    "Duel.GetDecktopGroup": ["返回玩家player卡组最上方最多count张卡组成的Group。"],
    "Duel.GetFusionMaterial": [
        "返回player的两个Group：当前可用的全部融合素材候选，以及来自指定位置的基础素材池。",
        "location默认LOCATION_HAND + LOCATION_MZONE。魔法与陷阱区域或墓地中受EFFECT_EXTRA_FUSION_MATERIAL影响的卡只加入第1个返回Group；第2个Group只包含location指定位置的卡。",
    ],
    "Card.EnableCounterPermit": [
        "给c登记单卡的指示物许可效果，使其可以在指定范围放置countertype类型的指示物。",
        "省略location时，怪兽默认LOCATION_MZONE，非怪兽默认LOCATION_SZONE + LOCATION_FZONE。提供condition时会作为该许可效果的条件回调保存。",
    ],
    "Card.IsCanTurnSet": [
        "检查c能否被当前原因玩家变成里侧表示。",
        "连接怪兽、衍生物、已经里侧表示的卡，以及受到EFFECT_CANNOT_TURN_SET影响的卡或玩家会返回false。",
    ],
    "Duel.AddCustomActivityCounter": [
        "为指定ACTIVITY_*类型登记编号为counter_id的自定义行动计数器。",
        "召唤和攻击类计数器会以Card调用f，f返回false时计数增加。ACTIVITY_CHAIN会以effect, player, chain_id调用f，同样在返回false时计数。",
    ],
    "Card.IsAttackBelow": [
        "检查c是否为怪兽或被当作怪兽，并且当前攻击力已确定且小于等于atk。",
        "攻击力未知的卡返回false，因为核心要求当前攻击力至少为0。",
    ],
    "Duel.GetCustomActivityCount": [
        "返回counter_id和指定ACTIVITY_*类型下，player对应的自定义计数。",
        "计数每回合重置。在此核心中，多数以卡为对象的自定义计数器只记录该玩家是否至少进行过1次被计数行动；连锁计数器会随连锁建立和取消而增减。",
    ],
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
    "Auxiliary.UrsarcticExCostFilter": ["「北极天熊」共通特殊召唤效果的代替费用筛选；匹配墓地中可作为费用除外，且具有编号16471775或89264428效果的卡。"],
    "Auxiliary.UrsarcticReleaseFilter": ["「北极天熊」共通特殊召唤效果的费用筛选；匹配手牌中7星以上的怪兽。"],
    "Auxiliary.UrsarcticSpSummonCondition": ["「北极天熊」共通手牌快速效果的条件；当前为任一主要阶段时返回true。"],
    "Auxiliary.UrsarcticSpSummonCost": ["检查并支付「北极天熊」共通特殊召唤费用。玩家解放手牌中1只7星以上怪兽，或除外1张可用的墓地代替费用卡并使用对应效果的次数限制。"],
    "Auxiliary.UrsarcticSpSummonLimit": ["「北极天熊」共通效果处理后登记的特殊召唤限制目标；对等级为0的怪兽返回true。"],
    "Auxiliary.UrsarcticSpSummonOperation": ["「北极天熊」共通特殊召唤效果的操作；特殊召唤处理对象后，登记直到结束阶段的特殊召唤限制，阻止等级为0的怪兽特殊召唤。"],
    "Auxiliary.UrsarcticSpSummonTarget": ["「北极天熊」共通特殊召唤效果的目标处理；要求有可用怪兽区域且处理对象可以特殊召唤，然后登记特殊召唤信息。"],
    "Auxiliary.UseExtraReleaseCount": ["对g中通过EFFECT_EXTRA_RELEASE_NONSUM被解放的对方卡使用次数限制，用于未通过Duel.SelectReleaseGroup选择的额外解放效果。"],
    "GetID": ["返回当前脚本的表、卡名编号以及字符串偏移值。普通卡编号的偏移值为1，大型自定义编号的偏移值为100。"],
    "Group.CheckSubGroup": ["检查g是否存在数量在min到max之间且满足f的子组，同时考虑Duel.GrabSelectedCard已有选择和Auxiliary.GCheckAdditional。"],
    "Group.CheckSubGroupEach": ["检查g是否能为checks中的每个筛选各提供1张卡。省略f时，只要求每个位置的筛选成立。"],
    "Group.SelectSubGroup": ["让tp从g中选择数量在min到max之间且满足f的子组。会考虑已有选择；若不能完成有效选择则返回nil。"],
    "Group.SelectSubGroupEach": ["让tp为checks中的每个筛选各选择1张卡，可选择是否允许取消。省略f时，最终组检查使用Auxiliary.TRUE。"],
    "bit.band": ["返回a和b的按位与结果。"],
    "bit.bnot": ["返回a的按位取反结果。"],
    "bit.extract": ["从r中提取从field位开始的width位。width省略时为1。"],
    "bit.replace": ["返回把r中从field位开始的width位替换为v的低width位后的结果。width省略时为1。"],
    "Auxiliary.AddContactFusionProcedure": ["为c登记接触融合特殊召唤手续，使用指定素材筛选位置和素材操作，并返回创建的手续效果。"],
    "Auxiliary.AddFusionEffectProc": ["Auxiliary.AddFusionEffectProcUltimate的便捷包装；用常用参数构造params表，并返回创建的融合效果。"],
    "Auxiliary.AddSynchroProcedure2": [
        "为c登记旧式同调召唤手续，要求1只调整和1只非调整怪兽作为素材。",
        "等价于Auxiliary.AddSynchroProcedure(c, f1, f2, 1, 1)。",
    ],
    "Card.IsAbleToExtra": ["判断c能否由当前原因玩家返回额外卡组。"],
    "Card.IsAbleToHand": [
        "判断c能否由player送去或返回手牌。",
        "player省略时使用当前原因玩家。",
    ],
    "Card.IsAbleToRemoveAsCost": [
        "判断c能否由当前原因玩家作为cost除外。",
        "pos指定除外时的表示形式，省略时为POS_FACEUP。",
    ],
    "Card.IsSynchroSummonable": [
        "判断c能否使用tuner以及可用素材组mg进行同调召唤。",
        "tuner为nil时，相当于检查c通常的特殊召唤手续。",
        "min和max限制该手续使用的非调整同调素材数量。",
    ],
    "Duel.GetSynchroMaterial": [
        "返回player可作为同调素材使用的卡组。",
        "怪兽区域中里侧表示的卡只有在facedown为true时才包含。",
    ],
    "Duel.SynchroSummon": [
        "为player进行c的同调召唤；可以指定必须使用的tuner，并可从mg中选择素材。",
        "minc和maxc可以限制该手续使用的非调整素材数量。",
    ],
    "Duel.SelectSynchroMaterial": [
        "让player为c选择同调素材，并返回选中的Group。",
        "f1筛选调整素材，f2筛选非调整素材，min和max限制非调整数量，smat指定必须包含的素材，mg提供可选的素材范围。",
    ],
    "Duel.SetSynchroMaterial": ["把g保存为当前召唤手续使用的同调素材组。"],
    "Effect.GetOperation": ["返回e的Operation回调函数；未设置时返回nil。"],
    "Effect.GetTarget": ["返回e的Target回调函数；未设置时返回nil。"],
    "Card.GetType": ["返回c当前的类型掩码，包含卡片当前受到的临时类型变更。"],
    "Effect.GetType": ["返回e的效果类型掩码，例如EFFECT_TYPE_SINGLE、EFFECT_TYPE_FIELD或EFFECT_TYPE_TRIGGER_O。"],
    "Card.CheckFusionMaterial": [
        "检查c的融合素材要求是否可以由g满足，并可要求必须包含gc。",
        "chkf会传给融合素材条件检查；not_material用于只检查素材可用性、但暂不把卡视为实际素材的手续。",
    ],
    "Duel.CreateToken": [
        "为player创建卡号为code的衍生物并返回该Card。",
        "返回的衍生物不会自动放到场上；脚本通常会随后把它传给Duel.SpecialSummon或其他处理。",
    ],
    "Group.FilterSelect": [
        "让player从g中选择min到max张满足筛选函数f且不在ex中的卡，并返回选中的Group。",
        "ex之后的额外参数会在Card参数之后传给f。",
    ],
    "Effect.GetValue": ["返回e的Value字段。函数值效果返回保存的回调函数；否则返回保存的整数值。"],
    "Auxiliary.tgoval": [
        "EFFECT_CANNOT_BE_EFFECT_TARGET常用的Value函数，用于防止成为对方效果的对象。",
        "当原因玩家rp是e处理对象玩家的对方时返回true。",
    ],
    "Duel.GetTurnCount": [
        "返回当前回合数。",
        "不传player时返回整场决斗的回合数；传入player 0或1时返回该玩家经过的个人回合数。",
    ],
    "Card.IsFusionSetCard": [
        "判断c作为融合素材时是否可以视为属于任一传入的系列编号。",
        "nil系列编号参数会被忽略。",
    ],
    "Card.IsPublic": ["判断c当前是否为双方公开状态；在当前核心中表现为表侧表示。"],
    "Card.IsHasEffect": [
        "返回当前影响c且效果编号为code的效果；没有匹配效果时返回nil。",
        "提供player时，只返回该玩家仍可使用次数限制的效果。多个匹配效果会作为多个Lua返回值返回。",
    ],
    "Card.IsPosition": ["判断c当前表示形式是否包含pos。"],
    "Card.GetEquipTarget": ["返回c当前装备到的卡；如果c没有装备对象则返回nil。"],
    "Duel.SelectFusionMaterial": [
        "让player从g中为融合怪兽c选择有效的融合素材组，并返回选中的Group。",
        "提供gc时，所选素材必须包含gc；返回的Group也会包含gc，与核心选择行为一致。",
    ],
    "Group.DeleteGroup": [
        "释放之前通过Group.KeepAlive保留的Group，使其重新交由Lua正常管理。",
        "对普通Group调用此函数没有效果。",
    ],
    "Card.GetAttack": ["返回c当前的攻击力；未知或负数攻击力按0返回。"],
    "Card.IsLevel": [
        "判断c当前等级是否等于任一传入的等级值。",
        "nil等级参数会被忽略。",
    ],
    "Card.SetMaterial": ["把g设置为c本次召唤使用的素材组；g为nil时清除素材记录。"],
    "Duel.SelectOption": [
        "让player从一组描述编号中选择1项，并返回所选项从0开始的序号。",
        "所选描述编号也会作为客户端提示显示。",
    ],
    "Effect.GetDescription": ["返回e的描述编号。"],
    "Card.GetFlagEffect": ["返回c上编号为code的标记效果数量。"],
    "Auxiliary.AddLinkProcedure": [
        "为c登记标准连接召唤手续，并返回创建的Effect。",
        "f筛选素材，min/max限制素材数量，gf可额外检查选中的素材组。",
    ],
    "Card.IsSummonType": ["判断c记录的召唤类型是否包含sumtype中的全部标志。"],
    "Card.CompleteProcedure": ["把c标记为已经完成正规召唤手续。"],
    "Card.IsStatus": ["判断c当前状态是否包含status中的至少一个标志。"],
    "Duel.GetLocationCountFromEx": [
        "返回从额外卡组特殊召唤时可用的怪兽区域数量，并额外返回可用区域掩码。",
        "reason_player省略时使用当前原因玩家。targets会在检查数量前视为将离场。",
    ],
    "Duel.CheckReleaseGroup": [
        "检查player是否能解放至少count张满足f且不在ex中的卡。",
        "ex之后的额外参数会传给f。此辅助函数使用REASON_COST。",
    ],
    "Duel.CheckReleaseGroupEx": [
        "检查player是否能以指定reason解放至少count张满足f且不在ex中的卡，并可选择是否允许从手牌解放。",
        "ex之后的额外参数会传给f。",
    ],
    "Card.GetOwner": ["返回c的原本持有者玩家。"],
    "Effect.GetOwner": ["返回持有e的卡。"],
    "Card.IsPreviousPosition": ["判断c之前的表示形式是否包含pos。"],
    "Duel.SelectReleaseGroup": [
        "让player选择min到max张满足f且不在ex中的可解放卡，并返回选中的Group。",
        "ex之后的额外参数会传给f。",
    ],
    "Group.FilterCount": [
        "统计g中满足f且不在ex中的卡数量。",
        "ex之后的额外参数会传给f。",
    ],
    "Group.FromCards": ["创建并返回包含所有非nil Card参数的新Group。"],
    "Auxiliary.TargetBoolFunction": [
        "返回效果目标回调函数；调用时会执行f(target, ...)并使用当前捕获的额外参数。",
        "适用于SetTarget等需要(effect, target)形式函数的API。",
    ],
    "Duel.GetFieldGroup": ["从player视角返回指定位置的卡组；s为自己一侧位置，o为对方一侧位置。"],
    "Auxiliary.EnablePendulumAttribute": [
        "为灵摆怪兽c登记灵摆召唤手续。",
        "除非reg为false，否则也会登记从手牌发动该灵摆卡的效果。",
    ],
    "Duel.NegateActivation": ["尝试把chainc的发动无效，并返回是否成功。"],
    "Duel.IsChainNegatable": [
        "用于兼容的连锁发动可否被无效检查。",
        "在当前MDPro3核心绑定中，此函数对任意连锁序号都会返回true。",
    ],
    "Duel.IsChainDisablable": [
        "检查chainc的效果能否被无效。",
        "连锁处理中会询问核心该连锁环节当前能否被无效；不在连锁处理中时返回true。",
    ],
    "Effect.GetCode": ["返回e的效果编号。"],
    "Card.GetBattleTarget": ["返回当前正在与c战斗的怪兽；若c不是当前攻击怪兽或攻击对象则返回nil。"],
    "Duel.GetFlagEffect": ["返回player上编号为code的玩家标记效果数量。"],
    "Duel.IsPlayerCanSpecialSummonMonster": [
        "检查player能否特殊召唤一只由传入卡片数据构造的虚拟怪兽。",
        "可选参数会覆盖读取到的卡片数据，之后用pos、target_player和sumtype描述召唤方式与位置。当前MDPro3绑定不会读取zone参数。",
    ],
    "Duel.RegisterFlagEffect": [
        "为player登记玩家/全局标记效果，并返回创建的Effect。",
        "该标记效果以玩家为对象、只作为场地效果存在、不能被无效，且count=0会按1处理。",
    ],
    "Group.AddCard": ["若g可修改，则把c加入g。"],
    "Card.GetBaseAttack": ["返回c当前的基础攻击力；未知或负数攻击力按0返回。"],
    "Card.IsCanBeEffectTarget": ["判断c能否成为e的效果对象；省略e时使用当前原因效果。"],
    "Card.IsMSetable": [
        "判断c能否由当前原因玩家在怪兽区域通常盖放。",
        "ignore_count会跳过通常召唤/盖放次数检查。e用于检查由该效果进行的盖放，min为要求的最少解放数量，zone限制可用怪兽区域。",
    ],
    "Effect.Reset": ["当e仍附着在有效持有者和处理对象上时，将其从对应卡片或场地效果列表中移除。"],
    "Duel.GetOperatedGroup": ["返回最近一次卡片操作实际处理过的卡组。"],
    "Group.KeepAlive": ["阻止g被Lua自动释放，直到调用Group.DeleteGroup。"],
    "Auxiliary.Next": ["返回用于generic for循环遍历g的迭代器，内部使用Group.GetFirst和Group.GetNext。"],
    "Duel.Recover": [
        "为player恢复LP并返回处理的数值。",
        "效果可以把恢复反转为伤害。is_step=true时，需要用Duel.RDComplete完成本批伤害/恢复处理。",
    ],
    "Card.IsForbidden": ["判断c当前是否具有STATUS_FORBIDDEN状态。"],
    "Duel.GetLP": ["返回player当前LP。"],
    "Duel.SelectEffectYesNo": ["询问player是否使用c的效果，提示描述编号为desc，省略时默认为95。"],
    "Duel.NegateEffect": ["尝试把chainc的效果无效，并返回是否成功。forced表示请求强制无效。"],
    "Card.IsSummonPlayer": ["判断player是否为召唤c的玩家。"],
    "Auxiliary.AddRitualProcGreater2": ["为c添加仪式召唤效果，使用仪式怪兽的当前等级，并要求素材等级合计大于等于该等级。"],
    "Auxiliary.AddRitualProcGreater2Code": ["把code1登记为c列名的编号，然后添加只适用于该编号仪式怪兽的Greater2仪式手续。"],
    "Auxiliary.AddRitualProcGreater2Code2": ["把code1和code2登记为c列名的编号，然后添加只适用于任一编号仪式怪兽的Greater2仪式手续。"],
    "Auxiliary.AddRitualProcUltimate": ["为c创建可配置的仪式召唤发动效果并返回它。该效果可选择不立即登记，可使用墓地素材，并可执行额外的目标/操作回调。"],
    "Auxiliary.AssaultModeLimit": ["「/爆裂体」怪兽的特殊召唤限制Value函数；允许/爆裂体召唤值，或由「爆裂模式」发动的效果。"],
    "Auxiliary.CheckXyz2XMaterial": ["检查c是否可以用mg中的素材进行超量召唤，并允许有效的EFFECT_DOUBLE_XMATERIAL卡按2个素材计数。"],
    "Auxiliary.ContactFusionCondition": ["返回接触融合手续的条件函数；从指定位置收集有效素材，并检查c的融合素材要求。"],
    "Auxiliary.ContactFusionMaterialFilter": ["接触融合手续的素材筛选；该卡必须能作为fc的融合素材，且提供filter时也必须满足filter。"],
    "Auxiliary.ContactFusionOperation": ["返回接触融合手续的操作函数；把已选择素材设置给融合怪兽，执行mat_operation，并删除保留的Group。"],
    "Auxiliary.ContactFusionSendToDeck": ["返回接触融合素材操作函数；必要时公开里侧素材，提示墓地/除外素材，并把全部素材作为费用洗回卡组。"],
    "Auxiliary.ContactFusionTarget": ["返回接触融合手续的目标函数；选择融合素材，保留选择的Group并保存到效果上，返回是否选择成功。"],
    "Auxiliary.DarkFusionLimit": ["「邪心英雄」/「暗黑融合」类效果的特殊召唤限制Value函数；允许「暗黑融合」本身、暗黑融合召唤值，或玩家受编号72043279效果影响时的融合召唤。"],
    "Auxiliary.FCheckMix": ["混合融合素材递归检查；按顺序检查每个必需素材函数，把已选素材记录在sg中，并在需要时消耗代替融合素材许可。"],
    "Auxiliary.FCheckMixGoal": ["混合融合素材的最终组检查；验证必须使用的融合素材、EFFECT_TUNE_MAGICIAN_F限制、额外怪兽区域可用性以及额外融合目标检查。"],
    "Auxiliary.FCheckMixRep": ["检查已选择的重复混合融合素材组；可重复素材函数负责可变数量素材，其余每个素材函数各满足1次。"],
    "Auxiliary.FCheckMixRepFilter": ["Auxiliary.FCheckMixRep使用的递归辅助函数；临时把c分配给剩余的一个固定素材函数，并继续检查其余要求。"],
    "Auxiliary.FCheckMixRepGoal": ["重复混合融合素材的最终目标检查；验证已选数量限制、额外怪兽区域可用性、额外融合检查以及固定/重复素材要求。"],
    "Auxiliary.FCheckMixRepGoalCheck": ["重复混合融合素材目标的共通预检查；排除无效的EFFECT_TUNE_MAGICIAN_F组合、缺少必须融合素材以及额外目标检查失败的情况。"],
    "Auxiliary.FCheckMixRepSelected": ["重复混合融合素材选择递归辅助函数；使用已选择素材条件转交Auxiliary.FCheckMixRepTemplate处理。"],
    "Auxiliary.FCheckMixRepSelectedCond": ["判断当前重复混合融合素材选择是否可以继续递归，或是否可以通过Auxiliary.FCheckSelectMixRep完成。"],
    "Auxiliary.FCheckMixRepTemplate": ["重复混合融合素材检查的通用递归模板；尝试把c分配给每个固定素材函数，或分配给可重复素材位置。"],
    "Auxiliary.FCheckSelectMixRep": ["检查当前重复混合融合素材选择是否可以从已选Group继续完成。"],
    "Auxiliary.FCheckSelectMixRepAll": ["重复混合融合选择使用的递归辅助函数；用于场地空间限制已经满足或不需要检查的情况。"],
    "Auxiliary.FCheckSelectMixRepM": ["重复混合融合选择使用的递归辅助函数；要求下一个候选素材由tp控制且位于怪兽区域。"],
    "Auxiliary.FConditionFilterMix": ["混合融合手续使用的素材筛选；检查c是否可以作为fc的融合素材，并满足至少1个必需素材函数。"],
    "Auxiliary.FConditionMix": ["返回固定混合融合素材手续的条件函数。"],
    "Auxiliary.FConditionMixRep": ["返回带可重复素材位置的混合融合素材手续的条件函数。"],
    "Auxiliary.FMaterialFilter": ["融合效果的默认融合素材筛选；判断c是否可以作为融合素材。"],
    "Auxiliary.FMaterialRemove": ["把融合素材以融合相关原因标记除外的默认操作。"],
    "Auxiliary.FMaterialRemoveFilter": ["会除外素材的融合效果使用的默认墓地素材筛选；判断c是否可以除外。"],
    "Auxiliary.FMaterialToDeck": ["把融合素材以融合相关原因标记回到卡组的默认操作。"],
    "Auxiliary.FMaterialToGrave": ["把融合素材以融合相关原因标记送去墓地的默认操作。"],
    "Auxiliary.FMaterialToGraveFilter": ["会把素材送去墓地的融合效果使用的默认素材筛选；判断c是否可以送去墓地。"],
    "Auxiliary.FOperationMix": ["返回固定混合融合素材手续的操作函数；选择有效融合素材并通过Duel.SetFusionMaterial保存。"],
    "Auxiliary.FOperationMixRep": ["返回带可重复素材位置的混合融合素材手续的操作函数；让玩家构建有效素材组并保存。"],
    "Auxiliary.FossilFusionLimit": ["化石融合类效果的特殊召唤限制Value函数；允许化石融合召唤值、「化石融合」本身，或处理对象不在额外卡组。"],
    "Auxiliary.FSelectMixRep": ["重复混合融合选择的候选检查；临时把c加入sg，并返回当前选择是否已经有效或仍可完成。"],
    "Auxiliary.FShaddollCondition": ["返回「影依」融合手续的条件函数；检查1个「影依」素材和1个指定属性素材，并支持场地效果使用对方怪兽作为素材。"],
    "Auxiliary.FShaddollExFilter": ["配合编号81788994效果使用的对方场上「影依」融合素材筛选；c必须表侧表示、受该场地效果影响，并满足标准「影依」素材筛选。"],
    "Auxiliary.FShaddollFilter": ["标准「影依」融合素材筛选；该卡必须是「影依」怪兽或匹配指定属性，可以作为融合素材，且未被编号6205579效果阻止。"],
    "Auxiliary.FShaddollFilter1": ["c属于「影依」融合系列0x9d时返回true。"],
    "Auxiliary.FShaddollFilter2": ["c具有指定融合属性，或具有编号4904633效果时返回true。"],
    "Auxiliary.FShaddollOperation": ["返回「影依」融合手续的操作函数；选择2张必需融合素材，必要时使用对方场上素材效果，并通过Duel.SetFusionMaterial保存。"],
    "Auxiliary.FShaddollSpFilter1": ["检查c是否可以和mg或exg中的另一张有效「影依」融合素材配对。"],
    "Auxiliary.FShaddollSpFilter2": ["检查c和mc是否组成所需的「影依」融合素材组合，并同时遵守必须融合素材和额外融合检查。"],
    "Auxiliary.FusionEffectUltimateFilter": ["检查c是否为可由e使用mg和params中筛选条件进行融合召唤的融合怪兽。"],
    "Auxiliary.FusionEffectUltimateMatFilter": ["融合效果素材筛选；排除不受e影响的素材，并在提供f时套用该素材筛选。"],
    "Auxiliary.FusionEffectUltimateMatLocFilter": ["按位置使用的融合素材筛选；不在loc的卡直接通过，在loc的卡则需要在提供f时满足f。"],
    "Auxiliary.FusionEffectUltimateOperation": ["返回可配置融合召唤效果的操作函数；构建素材池，处理连锁素材，按位置执行素材操作，特殊召唤选择的融合怪兽，并执行额外回调。"],
    "Auxiliary.FusionEffectUltimateTarget": ["返回可配置融合召唤效果的目标函数；检查可召唤融合怪兽和素材池，处理连锁素材的备用检查，并登记操作信息。"],
    "Auxiliary.GetLinkMaterials": ["返回tp可用的连接素材，包括通常怪兽区域素材，以及由额外连接素材效果允许使用的卡。"],
    "Auxiliary.GetMinSynchroLevel": ["返回c可为syncard提供的最小同调等级，包括打包保存的可选同调等级。"],
    "Auxiliary.GetSynchroLevelFlowerCardian": ["返回「花札卫」辅助函数使用的固定同调等级。"],
    "Auxiliary.GetSynMaterials": ["返回tp对syncard可用的同调素材；若场上素材允许使用手牌同调素材，也会合并有效手牌素材。"],
    "Auxiliary.LCheckGoal": ["连接素材组的最终检查；验证连接数值合计、额外怪兽区域可用性、可选组筛选、额外素材兼容性，以及是否包含指定lmat。"],
    "Auxiliary.LCheckOtherMaterial": ["通过EFFECT_EXTRA_LINK_MATERIAL处理函数检查c是否与其他已选连接素材兼容。"],
    "Auxiliary.LConditionFilter": ["通常连接素材筛选；该卡必须可见或可被e选择，可以作为lc的连接素材，并在提供f时满足f。"],
    "Auxiliary.LExtraFilter": ["由EFFECT_EXTRA_LINK_MATERIAL允许的额外连接素材筛选，用于手牌、魔法/陷阱区域或对方场上的卡。"],
    "Auxiliary.LExtraMaterialCount": ["对通过有效EFFECT_EXTRA_LINK_MATERIAL效果使用的已选连接素材消耗次数限制。"],
    "Auxiliary.LinkCondition": ["返回连接召唤手续的条件函数。"],
    "Auxiliary.LinkOperation": ["返回连接召唤手续的操作函数；设置素材，消耗额外素材次数限制，并把素材送去墓地。"],
    "Auxiliary.LinkTarget": ["返回连接召唤手续的目标函数；选择有效连接素材子组并保存在效果上。"],
    "Auxiliary.LUncompatibilityFilter": ["c与其他已选连接素材不兼容时返回true。"],
    "Auxiliary.MaskChangeLimit": ["Masked HERO/Mask Change类效果的特殊召唤限制Value函数；允许Mask Change召唤值，或由编号21143940的卡发动的效果。"],
    "Auxiliary.PConditionExtraFilter": ["检查eset中的任意额外灵摆召唤效果是否允许c在当前刻度下使用。"],
    "Auxiliary.PConditionExtraFilterSpecific": ["检查1个额外灵摆召唤效果是否允许c在当前刻度下使用。"],
    "Auxiliary.PConditionFilter": ["灵摆召唤候选筛选；检查位置、等级或pendulum_level、刻度、特殊召唤合法性、禁止状态，以及额外灵摆召唤许可。"],
    "Auxiliary.PendCondition": ["共通灵摆召唤手续的条件函数；检查2个灵摆区域、可用位置和区域、每回合状态，以及可召唤怪兽。"],
    "Auxiliary.PendOperation": ["共通灵摆召唤手续的操作函数；选择通常或额外灵摆召唤效果，在手牌/额外卡组区域限制内选择怪兽，更新检查标记，并把选择合并到sg。"],
    "Auxiliary.PendOperationCheck": ["返回组检查函数，用于限制一次灵摆召唤选择中的手牌数量、额外卡组数量和总区域数量。"],
    "Auxiliary.PendulumReset": ["在抽卡阶段开始时重置共通灵摆召唤检查标记。"],
    "Auxiliary.PendulumSummonableBool": ["c具有psummonable_location标记且当前位置包含在其中时返回true。"],
    "Auxiliary.PSSCompleteProcedure": ["对通过复活限制辅助函数设置、并以灵摆召唤特殊召唤的怪兽完成正规手续。"],
    "Auxiliary.RitualCheckAdditional": ["返回仪式素材选择时使用的额外子组检查函数，支持Equal或Greater仪式手续。"],
    "Auxiliary.RitualCheckAdditionalLevel": ["当c的仪式等级打包了2个可选数值时，返回较小的可用仪式等级。"],
    "Auxiliary.RitualCheckEqual": ["检查g中仪式等级合计是否正好等于c所需的lv。"],
    "Auxiliary.RitualCheckGreater": ["检查g中仪式等级合计是否大于或等于c所需的lv。"],
    "Auxiliary.RitualExtraFilter": ["墓地仪式素材筛选；c必须是f接受的有等级怪兽，并且可以被除外。"],
    "Auxiliary.RitualUltimateFilter": ["检查c是否为可用现有素材组以及所选Equal或Greater等级规则进行仪式召唤的有效仪式怪兽。"],
    "Auxiliary.RitualUltimateOperation": ["返回可配置仪式召唤效果的操作函数；选择仪式怪兽和素材，解放或除外素材，特殊召唤该怪兽，并执行额外回调。"],
    "Auxiliary.RitualUltimateTarget": ["返回可配置仪式召唤效果的目标函数；检查仪式怪兽和素材池，并登记特殊召唤、除外及额外目标信息。"],
    "Auxiliary.SynCondition": ["返回基础同调召唤手续的条件函数，并支持可选的固定调整素材处理。"],
    "Auxiliary.SynGroupCheckLevelAddition": ["返回同调素材选择使用的组检查函数；要求已选素材的最小同调等级合计不超过syncard的等级。"],
    "Auxiliary.SynLimitFilter": ["限制函数f存在且拒绝c作为syncard的素材时返回true。"],
    "Auxiliary.SynMaterialFilter": ["同调素材筛选；c必须表侧表示或公开，并且可以作为syncard的同调素材。"],
    "Auxiliary.SynMixCheck": ["检查剩余混合同调素材池是否能在可变素材数量范围内，完成当前已选固定素材组。"],
    "Auxiliary.SynMixCheckGoal": ["混合同调素材组的最终检查；验证数量、额外怪兽区域、组回调、指定素材、必须同调素材、EFFECT_TUNE_MAGICIAN限制、等级合计、手牌素材限制以及调整限制。"],
    "Auxiliary.SynMixCheckPrune": ["混合同调搜索的剪枝检查；当已选素材的最小同调等级合计达到syncard等级时返回true。"],
    "Auxiliary.SynMixCheckRecursive": ["混合同调素材搜索的递归辅助函数；临时加入c，检查目标，并在分支仍可能成立时继续搜索mg。"],
    "Auxiliary.SynMixCondition": ["返回混合同调召唤手续的条件函数；支持最多3个固定素材筛选和1个可变素材位置。"],
    "Auxiliary.SynMixFilter1": ["混合同调手续的第1个固定素材候选筛选。"],
    "Auxiliary.SynMixFilter2": ["混合同调手续的第2个固定素材候选筛选；若不需要第2个筛选，则转入可变素材位置。"],
    "Auxiliary.SynMixFilter3": ["混合同调手续的第3个固定素材候选筛选；若不需要第3个筛选，则转入可变素材位置。"],
    "Auxiliary.SynMixFilter4": ["混合同调手续的可变素材候选筛选；加入c后检查剩余素材池是否还能完成召唤。"],
    "Auxiliary.SynMixHandCheck": ["检查已选手牌同调素材是否由允许使用手牌同调素材的卡支持，并验证筛选和数量限制。"],
    "Auxiliary.SynMixHandFilter": ["当手牌素材是因为其他卡允许而被使用、不是依靠自身额外同调素材效果时返回true。"],
    "Auxiliary.SynMixOperation": ["返回混合同调召唤手续的操作函数；设置素材，把素材送去墓地，并释放保留的Group。"],
    "Auxiliary.SynMixTarget": ["返回混合同调召唤手续的目标函数；引导素材选择，并把选择的Group保存在效果上。"],
    "Auxiliary.SynOperation": ["返回基础同调召唤手续的操作函数；设置素材，把素材送去墓地，并释放保留的Group。"],
    "Auxiliary.SynTarget": ["返回基础同调召唤手续的目标函数；选择同调素材并把选择的Group保存在效果上。"],
    "Auxiliary.TuneMagicianCheckAdditionalX": ["已废弃的工厂函数；返回组检查函数，用于排除含有对ecode无效的EFFECT_TUNE_MAGICIAN_*组合的素材组。"],
    "Auxiliary.TuneMagicianCheckAdditionalXyz": ["超量素材组的额外检查；排除无效的EFFECT_TUNE_MAGICIAN_X组合。"],
    "Auxiliary.Xyz2XMaterialEffectFilter": ["检查c是否具有对xyzc有效的EFFECT_DOUBLE_XMATERIAL效果；checked为true时可跳过通常超量素材筛选。"],
    "Auxiliary.Xyz2XMaterialFilter": ["双重素材处理用的超量素材筛选；c必须表侧表示或公开，可以作为xyzc的超量素材，匹配lv，并在提供f时满足f。"],
    "Auxiliary.Xyz2XMaterialGoal": ["可能使用EFFECT_DOUBLE_XMATERIAL的超量召唤最终组检查；验证额外怪兽区域、EFFECT_XYZ_MIN_COUNT，以及双重素材效果是否足以满足minc。"],
    "Auxiliary.Xyz2XMaterialOperation": ["为已选素材组中需要用于满足最小素材数量的EFFECT_DOUBLE_XMATERIAL卡消耗次数限制。"],
    "Auxiliary.XyzAlterFilter": ["替代超量召唤候选筛选；检查alterf、超量素材合法性、额外怪兽区域、必须超量素材、EFFECT_XYZ_MIN_COUNT以及可选alterop验证。"],
    "Auxiliary.XyzCondition": ["返回标准超量召唤手续的条件函数，支持可选的1张素材替代超量召唤以及EFFECT_DOUBLE_XMATERIAL处理。"],
    "Auxiliary.XyzLevelFreeCondition": ["返回不检查等级的超量召唤手续的条件函数，支持可选组筛选和1张素材替代超量召唤。"],
    "Auxiliary.XyzLevelFreeFilter": ["不检查等级的超量素材筛选；c在场上时必须表侧表示，可以作为xyzc的超量素材，并在提供f时满足f。"],
    "Auxiliary.XyzLevelFreeGoal": ["不检查等级的超量召唤最终组检查；验证额外怪兽区域、可选组筛选gf以及EFFECT_XYZ_MIN_COUNT要求。"],
    "Auxiliary.XyzLevelFreeOperation": ["返回不检查等级的超量召唤手续操作函数；处理替代召唤，把原本叠放素材因规则送去墓地，设置素材并叠放。"],
    "Auxiliary.XyzLevelFreeTarget": ["返回不检查等级的超量召唤手续目标函数；在替代素材和通常组选素材之间选择，并保存所选Group。"],
    "Auxiliary.XyzOperation": ["返回标准超量召唤手续的操作函数；处理替代召唤、双重素材次数限制，把原本叠放素材因规则送去墓地，设置素材并叠放。"],
    "Auxiliary.XyzTarget": ["返回标准超量召唤手续的目标函数；在替代素材、双重素材组选取以及通常超量素材选择之间进行处理。"],
}


CORE_DOC_OVERRIDES = {
    "Card.CheckFusionSubstitute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fcard", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Fusion substitute validity."],
        "description_zh": ["检查融合素材代用是否合法。"],
    },
    "Card.GetPreviousLocation": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns previous location."],
        "description_zh": ["返回先前位置。"],
    },
    "Duel.GetFlagEffectLabel": {
        "params": [ParamDoc("player", "int"), ParamDoc("code", "int")],
        "returns": [
            ReturnDoc("int|nil", "First matching label, or nil if no matching flag effect exists."),
            ReturnDoc("int...", "Additional matching labels."),
        ],
        "description": ["Returns player flag-effect labels."],
        "description_zh": ["返回玩家标志效果Label。"],
    },
    "Duel.GetOverlayGroup": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int")],
        "returns": [ReturnDoc("Group|nil", "Overlay group, or nil if player is invalid.")],
        "description": ["Returns overlay cards in locations."],
        "description_zh": ["返回位置中的超量素材。"],
    },
    "Duel.IsPlayerCanRelease": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card", True), ParamDoc("reason", "int", True, "default: REASON_COST")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether a player can release."],
        "description_zh": ["检查玩家能否解放。"],
    },
    "Duel.SetFlagEffectLabel": {
        "params": [ParamDoc("player", "int"), ParamDoc("code", "int"), ParamDoc("label", "int")],
        "returns": [ReturnDoc("bool|nil", "True if a matching flag effect was updated; false if none exists; nil if player is invalid.")],
        "description": ["Updates a player flag-effect label."],
        "description_zh": ["更新玩家标志效果Label。"],
    },
    "Duel.SetFusionMaterial": {
        "params": [ParamDoc("g", "Group")],
        "returns": [],
        "description": ["Sets current Fusion Materials."],
        "description_zh": ["设置当前融合素材。"],
    },
    "Auxiliary.AddFusionProcFunRep2": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function|table"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers repeated-filter Fusion materials."],
        "description_zh": ["登记重复筛选融合素材。"],
    },
    "Auxiliary.DragonXyzSpSummonType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Soul Drain Dragon procedure type."],
        "description_zh": ["检查魂吸收龙手续类型。"],
    },
    "Auxiliary.GetColumn": {
        "params": [ParamDoc("c", "Card"), ParamDoc("p", "int", True, "default: 0")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns field column."],
        "description_zh": ["返回场上纵列。"],
    },
    "Auxiliary.GetValueType": {
        "params": [ParamDoc("v", "any")],
        "returns": [ReturnDoc("string")],
        "description": ["Returns normalized Lua value type."],
        "description_zh": ["返回规范化Lua值类型。"],
    },
    "Auxiliary.IsSelfEquip": {
        "params": [ParamDoc("c", "Card"), ParamDoc("id", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks self-equipped cards."],
        "description_zh": ["检查自身效果装备卡。"],
    },
    "Card.GetAttackableTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group", "Attackable monsters."), ReturnDoc("bool", "Whether c can attack directly.")],
        "description": ["Returns attackable targets and direct-attack flag."],
        "description_zh": ["返回可攻击对象和直接攻击标志。"],
    },
    "Card.GetAttackedCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns attack count."],
        "description_zh": ["返回攻击次数。"],
    },
    "Card.GetLeaveFieldDest": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns leave-field redirect destination."],
        "description_zh": ["返回离场改去目的地。"],
    },
    "Card.GetPreviousLevelOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns previous on-field Level."],
        "description_zh": ["返回先前场上等级。"],
    },
    "Card.IsXyzLevel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("xyzc", "Card"), ParamDoc("lv", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Xyz Level value."],
        "description_zh": ["检查超量用等级。"],
    },
    "Duel.DisableSelfDestroyCheck": {
        "params": [ParamDoc("disable", "bool", True, "default: true")],
        "returns": [],
        "description": ["Toggles self-destruction checks."],
        "description_zh": ["切换自毁检查。"],
    },
    "Effect.GetCondition": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("function|nil")],
        "description": ["Returns condition callback."],
        "description_zh": ["返回Condition回调。"],
    },
    "Auxiliary.AddRitualProcEqualCode": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("summon_location", "int", True, "default: LOCATION_HAND"),
            ParamDoc("grave_filter", "function", True), ParamDoc("mat_filter", "function", True), ParamDoc("pause", "bool", True),
            ParamDoc("extra_operation", "function", True), ParamDoc("extra_target", "function", True),
        ],
        "returns": [ReturnDoc("Effect", "Created Ritual Summon activation effect.")],
        "description": ["Creates equal-Level Ritual procedure for a card code."],
        "description_zh": ["创建指定卡号的等等级仪式手续。"],
    },
    "Auxiliary.ArcanaCondition": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Arcana coin flag."],
        "description_zh": ["检查秘仪硬币标志。"],
    },
    "Auxiliary.dogcon": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "int"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Destroyed-by-opponent EVENT_TO_GRAVE condition."],
        "description_zh": ["被对方破坏送去墓地条件。"],
    },
    "Auxiliary.DrytronSpSummonType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Special Summon procedure type."],
        "description_zh": ["检查特殊召唤手续类型。"],
    },
    "Auxiliary.indsval": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("re", "Effect"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Self effect-destruction protection value."],
        "description_zh": ["自身效果破坏保护Value。"],
    },
    "Auxiliary.PhantasmsSpSummonType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Special Summon procedure type."],
        "description_zh": ["检查特殊召唤手续类型。"],
    },
    "Auxiliary.TriamidSpSummonType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Special Summon procedure type."],
        "description_zh": ["检查特殊召唤手续类型。"],
    },
    "Card.CancelCardTarget": {
        "params": [ParamDoc("c", "Card"), ParamDoc("target", "Card")],
        "returns": [],
        "description": ["Cancels persistent card target."],
        "description_zh": ["取消持续卡片对象。"],
    },
    "Card.GetMutualLinkedGroup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns mutually linked cards."],
        "description_zh": ["返回互相连接的卡。"],
    },
    "Card.IsCanBeLinkMaterial": {
        "params": [ParamDoc("c", "Card"), ParamDoc("scard", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Link Material usability."],
        "description_zh": ["检查能否作为连接素材。"],
    },
    "Card.IsLinkMarker": {
        "params": [ParamDoc("c", "Card"), ParamDoc("dir", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Link Marker direction."],
        "description_zh": ["检查连接标记方向。"],
    },
    "Card.ReleaseEffectRelation": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect")],
        "returns": [],
        "description": ["Releases effect relation."],
        "description_zh": ["解除效果关系。"],
    },
    "Card.ReverseInDeck": {
        "params": [ParamDoc("c", "Card")],
        "returns": [],
        "description": ["Marks card face-up in Deck."],
        "description_zh": ["把Deck中的卡标记为表侧。"],
    },
    "Duel.ChangeBattleDamage": {
        "params": [ParamDoc("player", "int"), ParamDoc("value", "int"), ParamDoc("check", "bool", True, "default: true")],
        "returns": [],
        "description": ["Changes current battle damage."],
        "description_zh": ["改变当前战斗伤害。"],
    },
    "Duel.GetCoinResult": {
        "params": [],
        "returns": [ReturnDoc("int...", "One value per stored coin result.")],
        "description": ["Returns coin results."],
        "description_zh": ["返回硬币结果。"],
    },
    "Duel.GetDrawCount": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("int|nil", "Draw count, or nil if player is invalid.")],
        "description": ["Returns rule draw count."],
        "description_zh": ["返回规则抽卡数量。"],
    },
    "Effect.IsActivatable": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("player", "int"), ParamDoc("neglect_loc", "bool", True), ParamDoc("neglect_target", "bool", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks effect activation legality."],
        "description_zh": ["检查效果能否发动。"],
    },
    "Auxiliary.AddFusionProcCode4": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int"), ParamDoc("code3", "int"), ParamDoc("code4", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers four-code Fusion materials."],
        "description_zh": ["登记四卡号融合素材。"],
    },
    "Auxiliary.EnableReviveLimitPendulumSummonable": {
        "params": [ParamDoc("c", "Card"), ParamDoc("loc", "int", True, "default: 0xff")],
        "returns": [],
        "description": ["Enables revive-limit Pendulum Summon handling."],
        "description_zh": ["启用苏生限制灵摆召唤处理。"],
    },
    "Auxiliary.FilterEqualFunction": {
        "params": [ParamDoc("f", "function"), ParamDoc("value", "any"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("function")],
        "description": ["Builds equality card filter."],
        "description_zh": ["生成等值卡片筛选。"],
    },
    "Auxiliary.penlimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Pendulum Summon type."],
        "description_zh": ["检查灵摆召唤类型。"],
    },
    "Auxiliary.TargetEqualFunction": {
        "params": [ParamDoc("f", "function"), ParamDoc("value", "any"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("function")],
        "description": ["Builds equality target-value function."],
        "description_zh": ["生成等值对象Value函数。"],
    },
    "Auxiliary.tgsval": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("re", "Effect"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Self effect-target protection value."],
        "description_zh": ["自身效果对象保护Value。"],
    },
    "Card.AssumeProperty": {
        "params": [ParamDoc("c", "Card"), ParamDoc("assume_type", "int"), ParamDoc("assume_value", "int")],
        "returns": [],
        "description": ["Sets assumed property for core checks."],
        "description_zh": ["设置核心检查用假定属性。"],
    },
    "Card.GetAttributeInGrave": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Graveyard Attribute."],
        "description_zh": ["返回墓地属性。"],
    },
    "Card.GetPreviousDefenseOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns previous on-field DEF."],
        "description_zh": ["返回先前场上DEF。"],
    },
    "Card.GetSummonLocation": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns summon source location."],
        "description_zh": ["返回召唤来源位置。"],
    },
    "Card.ReplaceEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("reset", "int"), ParamDoc("count", "int", True, "default: 1")],
        "returns": [ReturnDoc("int")],
        "description": ["Replaces copied effects."],
        "description_zh": ["替换复制效果。"],
    },
    "Duel.GetDiceResult": {
        "params": [],
        "returns": [
            ReturnDoc("int", "First dice result."), ReturnDoc("int", "Second dice result."), ReturnDoc("int", "Third dice result."),
            ReturnDoc("int", "Fourth dice result."), ReturnDoc("int", "Fifth dice result."),
        ],
        "description": ["Returns dice result slots."],
        "description_zh": ["返回骰子结果槽位。"],
    },
    "Duel.IsPlayerCanSSet": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Spell/Trap Set permission."],
        "description_zh": ["检查魔法/陷阱盖放权限。"],
    },
    "Duel.SetDiceResult": {
        "params": [
            ParamDoc("res1", "int", True), ParamDoc("res2", "int", True), ParamDoc("res3", "int", True),
            ParamDoc("res4", "int", True), ParamDoc("res5", "int", True),
        ],
        "returns": [],
        "description": ["Sets dice result slots."],
        "description_zh": ["设置骰子结果槽位。"],
    },
    "Card.IsCanBeSynchroMaterial": {
        "params": [ParamDoc("c", "Card"), ParamDoc("scard", "Card", True), ParamDoc("tuner", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Synchro Material usability."],
        "description_zh": ["检查能否作为同调素材。"],
    },
    "Duel.GetCounter": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("countertype", "int")],
        "returns": [ReturnDoc("int|nil", "Counter count, or nil if player is invalid.")],
        "description": ["Counts counters in field locations."],
        "description_zh": ["统计场上位置中的指示物。"],
    },
    "Duel.GetUsableMZoneCount": {
        "params": [ParamDoc("player", "int"), ParamDoc("use_player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("int|nil", "Usable Monster Zone count, or nil if player is invalid.")],
        "description": ["Returns usable Monster Zone count."],
        "description_zh": ["返回可用怪兽区域数量。"],
    },
    "Effect.GetCategory": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns effect category bits."],
        "description_zh": ["返回效果Category位。"],
    },
    "Auxiliary.AddFusionProcCodeRep": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("cc", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers repeated-code Fusion materials."],
        "description_zh": ["登记重复卡号融合素材。"],
    },
    "Auxiliary.EnableArcanaCoin": {
        "params": [ParamDoc("c", "Card"), ParamDoc("event1", "int"), ParamDoc("...", "int", True)],
        "returns": [],
        "description": ["Enables Arcana Force coin effects."],
        "description_zh": ["启用秘仪之力硬币效果。"],
    },
    "Auxiliary.MZoneSequence": {
        "params": [ParamDoc("seq", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Converts Monster Zone sequence to local column."],
        "description_zh": ["把怪兽区域序号转换为本地纵列。"],
    },
    "Auxiliary.AddBanishRedirect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("condition", "function", True, "default: face-up condition")],
        "returns": [],
        "description": ["Registers leave-field banish redirect."],
        "description_zh": ["登记离场除外替换。"],
    },
    "Auxiliary.AddEquipSpellEffect": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("is_self", "bool"), ParamDoc("is_opponent", "bool"),
            ParamDoc("filter", "function"), ParamDoc("eqlimit", "function|nil"), ParamDoc("pause", "bool", True, "default: false"),
            ParamDoc("skip_target", "bool", True, "default: false"),
        ],
        "returns": [ReturnDoc("Effect", "Created activation effect.")],
        "description": ["Creates an Equip Spell activation helper."],
        "description_zh": ["创建装备魔法发动辅助效果。"],
    },
    "Auxiliary.AddFusionProcCodeFunRep": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("code1", "int|table"), ParamDoc("f", "function|table"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool"),
        ],
        "returns": [],
        "description": ["Registers code plus repeated-filter Fusion materials."],
        "description_zh": ["登记卡号加重复筛选融合素材。"],
    },
    "Auxiliary.AddFusionProcFunFunRep": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f1", "function|table"), ParamDoc("f2", "function|table"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers one filter plus repeated-filter Fusion materials."],
        "description_zh": ["登记一个筛选加重复筛选融合素材。"],
    },
    "Card.GetBattledGroupCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts cards battled by c."],
        "description_zh": ["统计c已战斗的卡。"],
    },
    "Card.GetLinkAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Link Material Attribute."],
        "description_zh": ["返回连接素材属性。"],
    },
    "Card.IsNotTuner": {
        "params": [ParamDoc("c", "Card"), ParamDoc("scard", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks non-Tuner status for Synchro Material use."],
        "description_zh": ["检查同调素材用非调整状态。"],
    },
    "Duel.GetOverlayCount": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int")],
        "returns": [ReturnDoc("int|nil", "Overlay count, or nil if player is invalid.")],
        "description": ["Counts Xyz Materials in field locations."],
        "description_zh": ["统计场上位置中的超量素材。"],
    },
    "Duel.Readjust": {
        "params": [],
        "returns": [],
        "description": ["Requests field readjustment."],
        "description_zh": ["请求场地重新调整。"],
    },
    "Auxiliary.IsMaterialListSetCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("setcode", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks listed material set codes."],
        "description_zh": ["检查列名素材系列代码。"],
    },
    "Auxiliary.qlifilter": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("te", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Qli monster immunity filter."],
        "description_zh": ["机壳怪兽免疫筛选。"],
    },
    "Card.GetOriginalRank": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns printed Rank."],
        "description_zh": ["返回原本阶级。"],
    },
    "Card.GetRightScale": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns right Pendulum Scale."],
        "description_zh": ["返回右灵摆刻度。"],
    },
    "Card.GetSynchroLevel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("scard", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Synchro Material Level value."],
        "description_zh": ["返回同调素材等级值。"],
    },
    "Card.IsCanHaveCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("countertype", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks counter compatibility."],
        "description_zh": ["检查指示物兼容性。"],
    },
    "Card.IsDualState": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Gemini/Dual state."],
        "description_zh": ["检查二重状态。"],
    },
    "Card.IsRelateToCard": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks relation between two cards."],
        "description_zh": ["检查两张卡之间的关系。"],
    },
    "Auxiliary.AddFusionProcMix": {
        "params": [ParamDoc("fcard", "Card"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool"), ParamDoc("...", "int|function|table")],
        "returns": [],
        "description": ["Registers mixed fixed-count Fusion materials."],
        "description_zh": ["登记固定数量混合融合素材。"],
    },
    "Auxiliary.CheckUnionEquip": {
        "params": [ParamDoc("uc", "Card"), ParamDoc("tc", "Card"), ParamDoc("exclude_modern_count", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Union equip-count limits."],
        "description_zh": ["检查同盟装备数量限制。"],
    },
    "Auxiliary.linklimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Link Summon type."],
        "description_zh": ["检查连接召唤类型。"],
    },
    "bit.bxor": {
        "params": [ParamDoc("a", "int"), ParamDoc("b", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Bitwise XOR."],
        "description_zh": ["按位异或。"],
    },
    "bit.rshift": {
        "params": [ParamDoc("a", "int"), ParamDoc("b", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Bitwise right shift."],
        "description_zh": ["按位右移。"],
    },
    "Card.CheckUnionTarget": {
        "params": [ParamDoc("c", "Card"), ParamDoc("target", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Union equip target legality."],
        "description_zh": ["检查同盟装备对象合法性。"],
    },
    "Card.EnableDualState": {
        "params": [ParamDoc("c", "Card")],
        "returns": [],
        "description": ["Enables Gemini/Dual state."],
        "description_zh": ["启用二重状态。"],
    },
    "Card.GetColumnGroupCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts cards in c's columns."],
        "description_zh": ["统计c纵列中的卡。"],
    },
    "Card.GetHandSynchro": {
        "params": [ParamDoc("c", "Card")],
        "returns": [
            ReturnDoc("Effect|nil", "Hand Synchro enabling effect."),
            ReturnDoc("function|nil", "Effect target function."),
            ReturnDoc("int|nil", "Minimum hand-material count."),
            ReturnDoc("int|nil", "Maximum hand-material count."),
        ],
        "description": ["Returns hand Synchro parameters."],
        "description_zh": ["返回手牌同调参数。"],
    },
    "Card.GetTributeRequirement": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Minimum Tribute count."), ReturnDoc("int", "Maximum Tribute count.")],
        "description": ["Returns Normal Summon Tribute requirements."],
        "description_zh": ["返回通常召唤解放需求。"],
    },
    "Card.SetHint": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int"), ParamDoc("value", "int")],
        "returns": [],
        "description": ["Sends a card hint."],
        "description_zh": ["发送卡片提示。"],
    },
    "Duel.CheckChainUniqueness": {
        "params": [],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks current Chain handler uniqueness."],
        "description_zh": ["检查当前连锁处理对象唯一性。"],
    },
    "Duel.SelectField": {
        "params": [
            ParamDoc("player", "int"), ParamDoc("count", "int"), ParamDoc("location1", "int"),
            ParamDoc("location2", "int"), ParamDoc("filter", "int"), ParamDoc("desc", "int", True),
        ],
        "returns": [ReturnDoc("int|nil", "Selected zone bitmask, or nil if player is invalid.")],
        "description": ["Lets player select field zones."],
        "description_zh": ["让玩家选择场地区域。"],
    },
    "Group.Remove": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("ex", "Card|nil"), ParamDoc("...", "any", True)],
        "returns": [],
        "description": ["Removes matching cards from a mutable Group."],
        "description_zh": ["从可修改Group中移除匹配卡。"],
    },
    "Auxiliary.AddFusionProcShaddoll": {
        "params": [ParamDoc("c", "Card"), ParamDoc("attr", "int")],
        "returns": [],
        "description": ["Registers Shaddoll Fusion materials."],
        "description_zh": ["登记影依融合素材。"],
    },
    "Auxiliary.evospcon": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"),
            ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Evolsaur-style Special Summon state."],
        "description_zh": ["检查进化龙式特殊召唤状态。"],
    },
    "Card.GetDestination": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns stored destination location."],
        "description_zh": ["返回保存的目标位置。"],
    },
    "Card.GetPreviousAttackOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns previous on-field ATK."],
        "description_zh": ["返回之前场上攻击力。"],
    },
    "Card.GetRitualLevel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("rc", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Ritual Material Level value."],
        "description_zh": ["返回仪式素材等级值。"],
    },
    "Duel.SwapSequence": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card")],
        "returns": [],
        "description": ["Swaps Monster Zone sequences."],
        "description_zh": ["交换怪兽区域序号。"],
    },
    "Auxiliary.AddFusionProcFunFun": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f1", "function|table"), ParamDoc("f2", "function|table"), ParamDoc("cc", "int"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers one filter plus fixed repeated-filter Fusion materials."],
        "description_zh": ["登记一个筛选加固定重复筛选融合素材。"],
    },
    "Auxiliary.nzdef": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks face-up nonzero DEF."],
        "description_zh": ["检查表侧非0守备力。"],
    },
    "bit.lshift": {
        "params": [ParamDoc("a", "int"), ParamDoc("b", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Bitwise left shift."],
        "description_zh": ["按位左移。"],
    },
    "Duel.GetLinkedGroup": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int")],
        "returns": [ReturnDoc("Group|nil", "Linked cards, or nil if player is invalid.")],
        "description": ["Returns linked cards in field locations."],
        "description_zh": ["返回场上位置中的连接卡。"],
    },
    "Auxiliary.SelectSameCount": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("g1", "Group"), ParamDoc("g2", "Group"),
            ParamDoc("min", "int", True, "default: 1"), ParamDoc("max", "int", True, "default: min(#g1, #g2, 127)"),
            ParamDoc("except", "Card|Group|nil", True),
        ],
        "returns": [ReturnDoc("Group|nil")],
        "description": ["Selects equal counts from two Groups."],
        "description_zh": ["从两个Group中选择相同数量。"],
    },
    "Auxiliary.TuneMagicianCheckX": {
        "params": [ParamDoc("c", "Card"), ParamDoc("sg", "Group"), ParamDoc("ecode", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Tune Magician material restrictions."],
        "description_zh": ["检查Tune Magician素材限制。"],
    },
    "Auxiliary.IsUnionState": {
        "params": [ParamDoc("effect", "Effect")],
        "returns": [ReturnDoc("Card|false|nil", "Equipped target when truthy.")],
        "description": ["Checks equipped Union state."],
        "description_zh": ["检查已装备同盟状态。"],
    },
    "Card.IsLinkCode": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Link Material card codes."],
        "description_zh": ["检查连接素材卡号。"],
    },
    "Duel.ChangeChainOperation": {
        "params": [ParamDoc("chainc", "int"), ParamDoc("f", "function")],
        "returns": [],
        "description": ["Changes a Chain Link operation."],
        "description_zh": ["变更连锁环操作函数。"],
    },
    "Group.Clear": {
        "params": [ParamDoc("g", "Group")],
        "returns": [],
        "description": ["Clears a Group."],
        "description_zh": ["清空Group。"],
    },
    "Auxiliary.sumreg": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"),
            ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Registers same-code summon flags."],
        "description_zh": ["登记同卡号召唤标志。"],
    },
    "Card.GetEffectCount": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts matching effects on c."],
        "description_zh": ["统计c上的匹配效果数量。"],
    },
    "Card.GetPreviousPosition": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns previous position."],
        "description_zh": ["返回之前表示形式。"],
    },
    "Card.IsCanRemoveCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int"), ParamDoc("countertype", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool|nil", "nil if player is invalid.")],
        "description": ["Checks counter removal permission."],
        "description_zh": ["检查能否取除指示物。"],
    },
    "Card.IsLinkSummonable": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("materials", "Group|nil"),
            ParamDoc("lcard", "Card|nil", True), ParamDoc("minc", "int", True, "default: 0"),
            ParamDoc("maxc", "int", True, "default: 0"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Link Summon availability."],
        "description_zh": ["检查能否连接召唤。"],
    },
    "Card.IsRankBelow": {
        "params": [ParamDoc("c", "Card"), ParamDoc("rank", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Rank upper bound."],
        "description_zh": ["检查c的阶级上限。"],
    },
    "Duel.ClearTargetCard": {
        "params": [],
        "returns": [],
        "description": ["Clears current Chain targets."],
        "description_zh": ["清空当前连锁对象。"],
    },
    "Duel.LinkSummon": {
        "params": [
            ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("materials", "Group|nil"),
            ParamDoc("lcard", "Card|nil", True), ParamDoc("minc", "int", True, "default: 0"),
            ParamDoc("maxc", "int", True, "default: 0"),
        ],
        "returns": [],
        "description": ["Performs a rule Link Summon."],
        "description_zh": ["进行规则连接召唤。"],
    },
    "Duel.Win": {
        "params": [ParamDoc("player", "int"), ParamDoc("reason", "int")],
        "returns": [],
        "description": ["Sets the duel winner."],
        "description_zh": ["设置决斗胜者。"],
    },
    "Auxiliary.AddFusionProcCode3": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int"),
            ParamDoc("code3", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool"),
        ],
        "returns": [],
        "description": ["Registers a three-code Fusion procedure."],
        "description_zh": ["登记三卡号融合手续。"],
    },
    "Auxiliary.SameValueCheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks shared bit values across a Group."],
        "description_zh": ["检查Group是否共享位值。"],
    },
    "Card.GetLinkCode": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Current code."), ReturnDoc("...?", "Additional Link Material code values, if any.")],
        "description": ["Returns Link Material codes."],
        "description_zh": ["返回连接素材卡号。"],
    },
    "Card.GetUnionCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Modern Union count."), ReturnDoc("int", "Old Union count.")],
        "description": ["Returns Union equip counts."],
        "description_zh": ["返回同盟装备数量。"],
    },
    "Duel.CheckEvent": {
        "params": [ParamDoc("event", "int"), ParamDoc("get_info", "bool", True, "default: false")],
        "returns": [
            ReturnDoc("bool"),
            ReturnDoc("Group|nil", "Event cards when get_info succeeds."),
            ReturnDoc("int|nil", "Event player."),
            ReturnDoc("int|nil", "Event value."),
            ReturnDoc("Effect|nil", "Reason effect."),
            ReturnDoc("int|nil", "Reason."),
            ReturnDoc("int|nil", "Reason player."),
        ],
        "description": ["Checks current event state."],
        "description_zh": ["检查当前事件状态。"],
    },
    "Duel.SetSelectedCard": {
        "params": [ParamDoc("targets", "Card|Group")],
        "returns": [],
        "description": ["Sets cards that must be selected."],
        "description_zh": ["设置必须选择的卡。"],
    },
    "Duel.SwapControl": {
        "params": [
            ParamDoc("targets1", "Card|Group"), ParamDoc("targets2", "Card|Group"),
            ParamDoc("reset_phase", "int", True, "default: 0"), ParamDoc("reset_count", "int", True, "default: 0"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Swaps control of cards."],
        "description_zh": ["交换卡的控制权。"],
    },
    "Group.SelectWithSumEqual": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("player", "int"), ParamDoc("f", "function"),
            ParamDoc("acc", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"),
            ParamDoc("...", "any", True),
        ],
        "returns": [ReturnDoc("Group|nil", "Selected optional cards, or nil for invalid player.")],
        "description": ["Selects cards with an exact sum."],
        "description_zh": ["选择合计值正好相等的卡。"],
    },
    "Auxiliary.bdcon": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"),
            ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks battle relation."],
        "description_zh": ["检查战斗关系。"],
    },
    "Card.GetAttackAnnouncedCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns attack declaration count."],
        "description_zh": ["返回攻击宣言次数。"],
    },
    "Card.GetTextDefense": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns printed/stored DEF."],
        "description_zh": ["返回记载守备力。"],
    },
    "Card.ResetEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("reset_type", "int")],
        "returns": [],
        "description": ["Resets matching effects."],
        "description_zh": ["重置匹配效果。"],
    },
    "Card.GetCardTargetCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts persistent card targets."],
        "description_zh": ["统计持续取对象卡数量。"],
    },
    "Card.GetFusionAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Fusion Material Attribute."],
        "description_zh": ["返回融合素材属性。"],
    },
    "Card.GetSummonPlayer": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Summon player."],
        "description_zh": ["返回召唤玩家。"],
    },
    "Auxiliary.gbspcon": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"),
            ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Gladiator Beast-style Special Summon state."],
        "description_zh": ["检查剑斗兽式特殊召唤状态。"],
    },
    "Card.CreateRelation": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card"), ParamDoc("reset", "int")],
        "returns": [],
        "description": ["Creates a resettable card relation."],
        "description_zh": ["建立可重置的卡片关系。"],
    },
    "Card.GetMutualLinkedGroupCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts mutually linked cards."],
        "description_zh": ["统计互相连接的卡。"],
    },
    "Card.IsExtraDeckMonster": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Extra Deck monster kind."],
        "description_zh": ["检查额外卡组怪兽卡种。"],
    },
    "Duel.AnnounceCoin": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("int", "Zero-based option index.")],
        "description": ["Lets player announce a coin side."],
        "description_zh": ["让玩家宣言硬币面。"],
    },
    "Auxiliary.synlimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Synchro Summon type."],
        "description_zh": ["检查同调召唤类型。"],
    },
    "Card.GetCardTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns persistent card targets."],
        "description_zh": ["返回持续取对象卡。"],
    },
    "Card.GetLinkRace": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns Link Material Race."],
        "description_zh": ["返回连接素材种族。"],
    },
    "Card.IsLinkBelow": {
        "params": [ParamDoc("c", "Card"), ParamDoc("link", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Link Rating upper bound."],
        "description_zh": ["检查c的连接值上限。"],
    },
    "Card.IsLinkState": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks linked state."],
        "description_zh": ["检查连接状态。"],
    },
    "Auxiliary.AddXyzProcedureLevelFree": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f", "function|nil"), ParamDoc("gf", "function|nil"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"),
            ParamDoc("alterf", "function|nil", True), ParamDoc("alterdesc", "int", True),
            ParamDoc("alterop", "function|nil", True),
        ],
        "returns": [],
        "description": ["Registers a Level-free Xyz procedure."],
        "description_zh": ["登记不检查等级的超量手续。"],
    },
    "Auxiliary.IsCanBeQuickEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks quick-effect filter availability."],
        "description_zh": ["检查快速效果筛选可用性。"],
    },
    "Card.GetColumnZone": {
        "params": [ParamDoc("c", "Card"), ParamDoc("loc", "int"), ParamDoc("player", "int", True)],
        "returns": [ReturnDoc("int")],
        "description": ["Returns overlapping column zones."],
        "description_zh": ["返回重叠纵列区域。"],
    },
    "Card.GetFusionCode": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Current code."), ReturnDoc("...?", "Additional Fusion Material code values, if any.")],
        "description": ["Returns Fusion Material codes."],
        "description_zh": ["返回融合素材卡号。"],
    },
    "Card.IsOriginalSetCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("setcode1", "int"), ParamDoc("setcode2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks original set codes."],
        "description_zh": ["检查原本系列代码。"],
    },
    "Card.SetFlagEffectLabel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("label", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Sets a flag effect label."],
        "description_zh": ["设置标志效果Label。"],
    },
    "Group.CheckWithSumGreater": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("acc", "int"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks a greater-or-equal sum."],
        "description_zh": ["检查大于等于的合计值。"],
    },
    "Auxiliary.AddRitualProcEqual2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function"), ParamDoc("summon_location", "int"),
            ParamDoc("grave_filter", "function|nil", True), ParamDoc("mat_filter", "function|nil", True),
            ParamDoc("pause", "bool", True), ParamDoc("extra_operation", "function|nil", True),
            ParamDoc("extra_target", "function|nil", True),
        ],
        "returns": [ReturnDoc("Effect")],
        "description": ["Registers an exact-Level Ritual procedure."],
        "description_zh": ["登记等级正好相等的仪式手续。"],
    },
    "Auxiliary.bdgcon": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"),
            ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"),
            ParamDoc("r", "int"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks battle destruction to the Graveyard."],
        "description_zh": ["检查战斗破坏送去墓地。"],
    },
    "Card.GetLinkedGroupCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Counts linked-zone cards."],
        "description_zh": ["统计连接区域中的卡。"],
    },
    "Card.GetPosition": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns current position."],
        "description_zh": ["返回当前表示形式。"],
    },
    "Card.GetRealFieldID": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns real field ID."],
        "description_zh": ["返回真实field ID。"],
    },
    "Duel.ChangeTargetCard": {
        "params": [ParamDoc("chainc", "int"), ParamDoc("g", "Group")],
        "returns": [],
        "description": ["Changes a Chain Link's target card group."],
        "description_zh": ["变更连锁环的取对象卡组。"],
    },
    "Card.RemoveCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int"), ParamDoc("countertype", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool|nil")],
        "description": ["Removes counters from c."],
        "description_zh": ["从c上取除指示物。"],
    },
    "Duel.CalculateDamage": {
        "params": [ParamDoc("attacker", "Card"), ParamDoc("attack_target", "Card|nil"), ParamDoc("new_attack", "bool", True, "default: false")],
        "returns": [],
        "description": ["Starts damage calculation."],
        "description_zh": ["开始伤害计算。"],
    },
    "Effect.GetProperty": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("int", "flag1."), ReturnDoc("int", "flag2.")],
        "description": ["Returns effect property flags."],
        "description_zh": ["返回效果属性标志。"],
    },
    "Auxiliary.SetUnionState": {
        "params": [ParamDoc("c", "Card")],
        "returns": [],
        "description": ["Sets equipped Union state."],
        "description_zh": ["设置已装备同盟状态。"],
    },
    "Card.IsLinkAbove": {
        "params": [ParamDoc("c", "Card"), ParamDoc("link", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Link Rating lower bound."],
        "description_zh": ["检查c的连接值下限。"],
    },
    "Card.IsSummonableCard": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is a Normal Summonable card kind."],
        "description_zh": ["检查c是否属于可通常召唤的卡种。"],
    },
    "Duel.AnnounceRace": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int"), ParamDoc("available", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Lets player declare Race values."],
        "description_zh": ["让player宣言种族。"],
    },
    "Duel.ChangeAttackTarget": {
        "params": [ParamDoc("target", "Card|nil")],
        "returns": [ReturnDoc("bool")],
        "description": ["Changes the current attack target."],
        "description_zh": ["变更当前攻击对象。"],
    },
    "Duel.IsPlayerCanSpecialSummon": {
        "params": [ParamDoc("player", "int"), ParamDoc("sumtype", "int", True), ParamDoc("sumpos", "int", True), ParamDoc("target_player", "int", True), ParamDoc("c", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can Special Summon."],
        "description_zh": ["检查player能否特殊召唤。"],
    },
    "Duel.ResetFlagEffect": {
        "params": [ParamDoc("player", "int"), ParamDoc("code", "int")],
        "returns": [],
        "description": ["Resets player flag effects."],
        "description_zh": ["重置玩家标志效果。"],
    },
    "Duel.SelectPosition": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("positions", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Lets player select a position."],
        "description_zh": ["让player选择表示形式。"],
    },
    "Effect.GetCost": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("function|nil")],
        "description": ["Returns e's cost function."],
        "description_zh": ["返回e的费用函数。"],
    },
    "Card.GetLeftScale": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's left Pendulum Scale."],
        "description_zh": ["返回c的左灵摆刻度。"],
    },
    "Card.GetPreviousAttributeOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's previous on-field Attribute."],
        "description_zh": ["返回c之前场上属性。"],
    },
    "Card.GetSummonType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's Summon Type bits."],
        "description_zh": ["返回c的召唤类型位。"],
    },
    "Duel.IsPlayerCanSummon": {
        "params": [ParamDoc("player", "int"), ParamDoc("sumtype", "int", True), ParamDoc("c", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can Normal Summon."],
        "description_zh": ["检查player能否通常召唤。"],
    },
    "Card.CopyEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("reset", "int"), ParamDoc("count", "int", True, "default: 1")],
        "returns": [ReturnDoc("int")],
        "description": ["Copies another card's initial_effect."],
        "description_zh": ["复制另一张卡的initial_effect。"],
    },
    "Card.GetMaterialCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns material count."],
        "description_zh": ["返回素材数量。"],
    },
    "Card.IsRankAbove": {
        "params": [ParamDoc("c", "Card"), ParamDoc("rank", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Rank lower bound."],
        "description_zh": ["检查c的阶级下限。"],
    },
    "Duel.CheckPhaseActivity": {
        "params": [],
        "returns": [ReturnDoc("bool")],
        "description": ["Returns phase action state."],
        "description_zh": ["返回阶段行动状态。"],
    },
    "Auxiliary.Tuner": {
        "params": [ParamDoc("f", "function|nil"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("function")],
        "description": ["Creates a Tuner material filter."],
        "description_zh": ["创建调整素材筛选函数。"],
    },
    "Card.GetBattlePosition": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's battle position snapshot."],
        "description_zh": ["返回c的战斗表示形式快照。"],
    },
    "Card.IsXyzType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Xyz Material type."],
        "description_zh": ["检查c的超量素材用类型。"],
    },
    "Duel.AnnounceLevel": {
        "params": [ParamDoc("player", "int"), ParamDoc("min", "int", True, "default: 1"), ParamDoc("max", "int", True, "default: 12"), ParamDoc("excluded_level1", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("int|nil", "Declared Level."), ReturnDoc("int|nil", "Zero-based option index.")],
        "description": ["Lets player declare a Level."],
        "description_zh": ["让player宣言等级。"],
    },
    "Duel.GetTargetCount": {
        "params": [ParamDoc("filter", "function|nil"), ParamDoc("player", "int"), ParamDoc("location1", "int"), ParamDoc("location2", "int"), ParamDoc("exception", "Card|Group|nil"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("int")],
        "description": ["Counts targetable matching cards."],
        "description_zh": ["统计可取对象的匹配卡。"],
    },
    "Duel.IsCanAddCounter": {
        "params": [ParamDoc("player", "int"), ParamDoc("countertype", "int", True), ParamDoc("count", "int", True), ParamDoc("c", "Card", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether counters can be placed."],
        "description_zh": ["检查是否能放置指示物。"],
    },
    "Duel.SendtoExtraP": {
        "params": [ParamDoc("targets", "Card|Group"), ParamDoc("player", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Sends cards to the Extra Deck face-up."],
        "description_zh": ["把卡以表侧送去额外卡组。"],
    },
    "Auxiliary.ritlimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks for Ritual Summon type."],
        "description_zh": ["检查是否为仪式召唤类型。"],
    },
    "Card.GetCurrentScale": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current Pendulum Scale."],
        "description_zh": ["返回c当前灵摆刻度。"],
    },
    "Card.GetLocation": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current location."],
        "description_zh": ["返回c当前位置。"],
    },
    "Duel.AnnounceType": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Lets player choose Monster/Spell/Trap."],
        "description_zh": ["让player选择怪兽/魔法/陷阱。"],
    },
    "Duel.IsPlayerCanAdditionalSummon": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks extra Normal Summon availability."],
        "description_zh": ["检查额外通常召唤可用性。"],
    },
    "Group.GetMinGroup": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("Group|nil", "Cards tied for the minimum value."), ReturnDoc("int|nil", "Minimum value.")],
        "description": ["Returns cards tied for minimum function value."],
        "description_zh": ["返回函数值最小的并列卡。"],
    },
    "Card.GetPreviousCodeOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int"), ReturnDoc("int|nil", "Second previous code, when present.")],
        "description": ["Returns c's previous on-field code."],
        "description_zh": ["返回c之前场上卡号。"],
    },
    "Card.IsHasCardTarget": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks persistent card targeting."],
        "description_zh": ["检查持续取对象卡。"],
    },
    "Duel.GetBattleDamage": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns recorded battle damage."],
        "description_zh": ["返回记录的战斗伤害。"],
    },
    "Duel.GetLinkedZone": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns linked-zone bitmask."],
        "description_zh": ["返回连接区域位掩码。"],
    },
    "Auxiliary.damcon1": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Condition helper for taking effect damage."],
        "description_zh": ["受到效果伤害的条件辅助函数。"],
    },
    "Auxiliary.EnableUnionAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("filter", "function")],
        "returns": [],
        "description": ["Registers modern Union effects."],
        "description_zh": ["登记现代同盟效果。"],
    },
    "Card.GetReason": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current reason value."],
        "description_zh": ["返回c当前记录的原因数值。"],
    },
    "Card.IsDefenseBelow": {
        "params": [ParamDoc("c", "Card"), ParamDoc("def", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's DEF is at most def."],
        "description_zh": ["检查c的守备力是否最多为def。"],
    },
    "Card.IsFusionCode": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Fusion Material codes."],
        "description_zh": ["检查融合素材用卡号。"],
    },
    "Auxiliary.EnableDualAttribute": {
        "params": [ParamDoc("c", "Card")],
        "returns": [],
        "description": ["Registers Gemini Monster handling."],
        "description_zh": ["登记二重怪兽处理。"],
    },
    "Card.GetPreviousEquipTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the previous Equip target."],
        "description_zh": ["返回之前的装备对象。"],
    },
    "Duel.CheckRemoveOverlayCard": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether Xyz Materials can be removed."],
        "description_zh": ["检查是否能取除超量素材。"],
    },
    "Auxiliary.IsMaterialListCode": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("bool|nil")],
        "description": ["Checks c.material for code."],
        "description_zh": ["检查c.material中是否存在code。"],
    },
    "Card.IsChainAttackable": {
        "params": [ParamDoc("c", "Card"), ParamDoc("ac", "int", True, "default: 2"), ParamDoc("monsteronly", "bool", True, "default: false")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether the current attacker can attack again."],
        "description_zh": ["检查当前攻击怪兽是否能再次攻击。"],
    },
    "Auxiliary.IsDualState": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether e's handler is in Dual State."],
        "description_zh": ["检查e的处理对象是否处于二重状态。"],
    },
    "Auxiliary.mzctcheckrel": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("reason", "int", True, "default: REASON_COST")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Monster Zone count after releasing g."],
        "description_zh": ["检查解放g后的怪兽区域数量。"],
    },
    "Duel.SetChainLimitTillChainEnd": {
        "params": [ParamDoc("f", "function", False, "callback: f(e, chain_player, activating_player)")],
        "returns": [],
        "description": ["Sets a chain limit until chain end."],
        "description_zh": ["设置持续到连锁结束的连锁限制。"],
    },
    "Duel.IsDamageCalculated": {
        "params": [],
        "returns": [ReturnDoc("bool")],
        "description": ["Returns whether damage calculation is complete."],
        "description_zh": ["返回是否已进行伤害计算。"],
    },
    "Duel.RDComplete": {
        "params": [],
        "returns": [],
        "description": ["Completes reserved step damage/recover processing."],
        "description_zh": ["完成保留的分步伤害/恢复处理。"],
    },
    "Card.IsReleasableByEffect": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be Released by effect."],
        "description_zh": ["检查c是否能被效果解放。"],
    },
    "Duel.AdjustInstantly": {
        "params": [ParamDoc("c", "Card", True)],
        "returns": [],
        "description": ["Runs immediate field adjustment."],
        "description_zh": ["立即进行场上调整。"],
    },
    "Auxiliary.EnableSpiritReturn": {
        "params": [ParamDoc("c", "Card"), ParamDoc("event1", "int"), ParamDoc("...", "int", True)],
        "returns": [],
        "description": ["Registers Spirit return setup."],
        "description_zh": ["登记灵魂怪兽回手设置。"],
    },
    "Card.ResetFlagEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [],
        "description": ["Resets flag effects by code."],
        "description_zh": ["按code重置标志效果。"],
    },
    "Duel.RemoveOverlayCard": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Removes Xyz Materials."],
        "description_zh": ["取除超量素材。"],
    },
    "Effect.IsHasCategory": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("cate", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks effect category bits."],
        "description_zh": ["检查效果category位。"],
    },
    "Card.GetTurnCounter": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's turn counter."],
        "description_zh": ["返回c的回合计数器。"],
    },
    "Card.IsLink": {
        "params": [ParamDoc("c", "Card"), ParamDoc("link1", "int"), ParamDoc("link2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Link Rating."],
        "description_zh": ["检查c的连接值。"],
    },
    "Card.IsSynchroType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Synchro Material type."],
        "description_zh": ["检查c的同调素材用类型。"],
    },
    "Duel.ClearOperationInfo": {
        "params": [ParamDoc("ct", "int")],
        "returns": [],
        "description": ["Clears operation info for a Chain Link."],
        "description_zh": ["清除连锁环的操作信息。"],
    },
    "Duel.ShuffleExtra": {
        "params": [ParamDoc("player", "int")],
        "returns": [],
        "description": ["Shuffles the Extra Deck."],
        "description_zh": ["洗切额外卡组。"],
    },
    "Auxiliary.AddRitualProcGreaterCode": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("summon_location", "int", True, "default: LOCATION_HAND"), ParamDoc("grave_filter", "function", True), ParamDoc("mat_filter", "function", True), ParamDoc("pause", "bool", True), ParamDoc("extra_operation", "function", True), ParamDoc("extra_target", "function", True)],
        "returns": [ReturnDoc("Effect")],
        "description": ["Adds a Greater Ritual procedure by code."],
        "description_zh": ["按卡号添加Greater仪式手续。"],
    },
    "Card.SetTurnCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("ct", "int")],
        "returns": [],
        "description": ["Sets c's turn counter."],
        "description_zh": ["设置c的回合计数器。"],
    },
    "Auxiliary.AddSynchroMixProcedure": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"), ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("gc", "function", True)],
        "returns": [],
        "description": ["Adds a mixed Synchro procedure."],
        "description_zh": ["添加混合同调手续。"],
    },
    "Auxiliary.nzatk": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is face-up with positive ATK."],
        "description_zh": ["检查c是否表侧表示且攻击力大于0。"],
    },
    "Card.SetCounterLimit": {
        "params": [ParamDoc("c", "Card"), ParamDoc("countertype", "int"), ParamDoc("limit", "int")],
        "returns": [],
        "description": ["Sets a counter limit effect."],
        "description_zh": ["设置指示物上限效果。"],
    },
    "Group.CheckWithSumEqual": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("acc", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks exact sum selection."],
        "description_zh": ["检查正好合计的选择。"],
    },
    "Duel.IsPlayerCanRemove": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card", True), ParamDoc("reason", "int", True, "default: REASON_EFFECT")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can banish."],
        "description_zh": ["检查player能否除外。"],
    },
    "Duel.AnnounceCard": {
        "params": [ParamDoc("player", "int"), ParamDoc("opcode1", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("int")],
        "description": ["Lets player declare a card code."],
        "description_zh": ["让player宣言卡号。"],
    },
    "Duel.RaiseSingleEvent": {
        "params": [ParamDoc("ec", "Card"), ParamDoc("code", "int"), ParamDoc("re", "Effect|nil"), ParamDoc("r", "int"), ParamDoc("rp", "int"), ParamDoc("ep", "int"), ParamDoc("ev", "int")],
        "returns": [],
        "description": ["Raises a single-card event."],
        "description_zh": ["引发单卡事件。"],
    },
    "Auxiliary.CreateChecks": {
        "params": [ParamDoc("f", "function"), ParamDoc("list", "table")],
        "returns": [ReturnDoc("table")],
        "description": ["Creates check functions from a list."],
        "description_zh": ["由列表创建检查函数。"],
    },
    "Auxiliary.RitualCheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("c", "Card"), ParamDoc("lv", "int"), ParamDoc("greater_or_equal", "string")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks Ritual Material groups."],
        "description_zh": ["检查仪式素材组。"],
    },
    "Card.IsXyzSummonable": {
        "params": [ParamDoc("c", "Card"), ParamDoc("materials", "Group|nil", True), ParamDoc("minc", "int", True), ParamDoc("maxc", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be Xyz Summoned."],
        "description_zh": ["检查c是否能超量召唤。"],
    },
    "Duel.XyzSummon": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("materials", "Group|nil", True), ParamDoc("minc", "int", True), ParamDoc("maxc", "int", True)],
        "returns": [],
        "description": ["Performs a rule Xyz Summon."],
        "description_zh": ["执行规则超量召唤。"],
    },
    "Auxiliary.bdogcon": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Condition helper for battle-destroying effects."],
        "description_zh": ["战斗破坏效果用条件辅助函数。"],
    },
    "Card.GetEquipCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns equipped-card count."],
        "description_zh": ["返回装备卡数量。"],
    },
    "Card.GetFirstCardTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the first persistent card target."],
        "description_zh": ["返回第1个持续取对象卡。"],
    },
    "Duel.SortDecktop": {
        "params": [ParamDoc("sort_player", "int"), ParamDoc("target_player", "int"), ParamDoc("count", "int")],
        "returns": [],
        "description": ["Lets one player sort cards on top of a Main Deck."],
        "description_zh": ["让一名玩家排列主卡组最上方的卡。"],
    },
    "Duel.RemoveCounter": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("countertype", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Removes counters from selected field locations."],
        "description_zh": ["从指定场上位置取除指示物。"],
    },
    "Duel.TossDice": {
        "params": [ParamDoc("player", "int"), ParamDoc("count1", "int"), ParamDoc("count2", "int", True, "default: 0")],
        "returns": [ReturnDoc("int", "First die result."), ReturnDoc("...?", "Additional die results.")],
        "description": ["Tosses dice and returns their results."],
        "description_zh": ["投掷骰子并返回结果。"],
    },
    "Card.IsLinkAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("attribute", "int"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Attribute while used as Link Material."],
        "description_zh": ["检查c作为连接素材使用时的属性。"],
    },
    "Card.IsOriginalCodeRule": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's rule-original card code."],
        "description_zh": ["检查c按规则使用的原本卡号。"],
    },
    "Duel.GetBattleMonster": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("Card|nil", "Monster controlled by player."), ReturnDoc("Card|nil", "Monster controlled by the opponent.")],
        "description": ["Returns the battling monsters for player and the opponent."],
        "description_zh": ["返回player与对方当前战斗中的怪兽。"],
    },
    "Duel.SkipPhase": {
        "params": [ParamDoc("player", "int"), ParamDoc("phase", "int"), ParamDoc("reset_flag", "int"), ParamDoc("reset_count", "int"), ParamDoc("value", "int", True, "default: 0")],
        "returns": [],
        "description": ["Makes player skip a phase."],
        "description_zh": ["使player跳过指定阶段。"],
    },
    "Card.GetPreviousRaceOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's previously recorded on-field Race."],
        "description_zh": ["返回c之前记录的场上种族。"],
    },
    "Card.CreateEffectRelation": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect")],
        "returns": [],
        "description": ["Creates an effect relation for c."],
        "description_zh": ["为c建立效果关联。"],
    },
    "Card.GetLink": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's Link Rating."],
        "description_zh": ["返回c的连接值。"],
    },
    "Card.IsAttackable": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is currently attack-capable."],
        "description_zh": ["检查c当前是否可攻击。"],
    },
    "Card.SetStatus": {
        "params": [ParamDoc("c", "Card"), ParamDoc("status", "int"), ParamDoc("enable", "bool")],
        "returns": [],
        "description": ["Sets or clears a status bit on c."],
        "description_zh": ["设置或清除c的状态位。"],
    },
    "Duel.AnnounceAttribute": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int"), ParamDoc("available", "int")],
        "returns": [ReturnDoc("int", "Selected Attribute bitmask.")],
        "description": ["Lets player declare Attributes."],
        "description_zh": ["让player宣言属性。"],
    },
    "Group.GetMaxGroup": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("...", "any", True)],
        "returns": [ReturnDoc("Group|nil", "Cards tied for maximum value."), ReturnDoc("int|nil", "Maximum value.")],
        "description": ["Returns cards with the maximum value produced by f."],
        "description_zh": ["返回使f取得最大值的卡。"],
    },
    "bit.bor": {
        "params": [ParamDoc("a", "int"), ParamDoc("b", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns the bitwise OR of a and b."],
        "description_zh": ["返回a与b的按位或。"],
    },
    "Card.IsDefenseAbove": {
        "params": [ParamDoc("c", "Card"), ParamDoc("def", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's current DEF is at least def."],
        "description_zh": ["检查c当前守备力是否大于等于def。"],
    },
    "Effect.SetOwnerPlayer": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("player", "int")],
        "returns": [],
        "description": ["Sets e's owner player."],
        "description_zh": ["设置效果e的拥有者玩家。"],
    },
    "Auxiliary.imval1": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Default battle-target immunity value helper."],
        "description_zh": ["战斗对象免疫检查用默认Value辅助函数。"],
    },
    "Card.GetReasonEffect": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Effect|nil")],
        "description": ["Returns c's current reason effect."],
        "description_zh": ["返回c当前的原因效果。"],
    },
    "Card.GetTurnID": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's stored turn ID."],
        "description_zh": ["返回c保存的回合ID。"],
    },
    "Card.IsDisabled": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c has STATUS_DISABLED."],
        "description_zh": ["检查c是否带STATUS_DISABLED。"],
    },
    "Duel.NegateSummon": {
        "params": [ParamDoc("targets", "Card|Group")],
        "returns": [],
        "description": ["Negates the current Summon for targets."],
        "description_zh": ["无效targets当前正在进行的召唤。"],
    },
    "Duel.SelectDisableField": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int"), ParamDoc("location1", "int"), ParamDoc("location2", "int"), ParamDoc("filter", "int")],
        "returns": [ReturnDoc("int", "Selected zone bitmask.")],
        "description": ["Lets player select field zones to disable."],
        "description_zh": ["让player选择要禁用的场地区域。"],
    },
    "Duel.IsPlayerCanSpecialSummonCount": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can perform count Special Summons."],
        "description_zh": ["检查player能否进行count次特殊召唤。"],
    },
    "Card.CheckEquipTarget": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c2 is a valid Equip target for c1."],
        "description_zh": ["检查c2是否是c1的合法装备对象。"],
    },
    "Card.GetOriginalCodeRule": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Primary rule-original code."), ReturnDoc("int|nil", "Second rule code, when present.")],
        "description": ["Returns c's rule-original card code."],
        "description_zh": ["返回c按规则使用的原本卡号。"],
    },
    "Auxiliary.chainreg": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int")],
        "returns": [],
        "description": ["Registers the chaining flag on e's handler."],
        "description_zh": ["给效果e的处理者登记连锁标记。"],
    },
    "Duel.EnableGlobalFlag": {
        "params": [ParamDoc("global_flag", "int")],
        "returns": [],
        "description": ["Enables a Duel global flag bit."],
        "description_zh": ["启用决斗全局标记位。"],
    },
    "Duel.TossCoin": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int")],
        "returns": [ReturnDoc("int", "First coin result, 0 or 1."), ReturnDoc("...?", "Additional coin results.")],
        "description": ["Tosses coins and returns their results."],
        "description_zh": ["投掷硬币并返回结果。"],
    },
    "Card.GetColumnGroup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns cards in c's column."],
        "description_zh": ["返回与c同纵列的卡。"],
    },
    "Duel.GetFirstMatchingCard": {
        "params": [
            ParamDoc("f", "function|nil", True), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any", True),
        ],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the first matching card from the specified locations."],
        "description_zh": ["返回指定位置中第一张满足条件的卡。"],
    },
    "Card.IsFusionAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("attribute", "int"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Attribute while used as Fusion Material."],
        "description_zh": ["检查c作为融合素材使用时的属性。"],
    },
    "Duel.GetActivityCount": {
        "params": [ParamDoc("player", "int"), ParamDoc("activity_type1", "int"), ParamDoc("activity_type2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("int", "Count for activity_type1."), ReturnDoc("...?", "Additional counts for each extra activity_type.")],
        "description": ["Returns current activity counts for player."],
        "description_zh": ["返回player当前的行动次数。"],
    },
    "Effect.UseCountLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("p", "int"), ParamDoc("count", "int", True, "default: 1"), ParamDoc("oath_only", "bool", True, "default: false")],
        "returns": [],
        "description": ["Manually consumes e's count limit for player p."],
        "description_zh": ["手动消耗玩家p对效果e的次数限制。"],
    },
    "Card.GetOriginalRace": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's original Race."],
        "description_zh": ["返回c的原本种族。"],
    },
    "Card.GetOverlayCount": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns the number of Xyz Materials attached to c."],
        "description_zh": ["返回c叠放的超量素材数量。"],
    },
    "Card.IsCanAddCounter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("countertype", "int"), ParamDoc("count", "int"),
            ParamDoc("singly", "bool", True, "default: false"), ParamDoc("loc", "int", True, "default: 0"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether counters can be placed on c."],
        "description_zh": ["检查能否在c上放置指示物。"],
    },
    "Duel.SetLP": {
        "params": [ParamDoc("player", "int"), ParamDoc("lp", "int")],
        "returns": [],
        "description": ["Sets player's LP."],
        "description_zh": ["设置player的LP。"],
    },
    "Auxiliary.AddFusionProcCodeFun": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int|table"), ParamDoc("f", "function|table"), ParamDoc("cc", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers a code-plus-filter Fusion Material procedure."],
        "description_zh": ["登记卡号加筛选条件的融合素材手续。"],
    },
    "Duel.AnnounceNumber": {
        "params": [ParamDoc("player", "int"), ParamDoc("number1", "int"), ParamDoc("number2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("int", "Selected number."), ReturnDoc("int", "0-based option index selected by the core.")],
        "description": ["Lets player choose one of the supplied numbers."],
        "description_zh": ["让player从给定数字中选择1个。"],
    },
    "Card.GetBaseDefense": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current base DEF."],
        "description_zh": ["返回c当前的基础守备力。"],
    },
    "Card.SetSPSummonOnce": {
        "params": [ParamDoc("c", "Card"), ParamDoc("spsummon_code", "int")],
        "returns": [],
        "description": ["Sets c's shared once-per-turn Special Summon code."],
        "description_zh": ["设置c共享的每回合1次特殊召唤代码。"],
    },
    "Card.IsPreviousSetCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("setcode1", "int"), ParamDoc("setcode2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's previously recorded Set membership."],
        "description_zh": ["检查c之前记录的系列。"],
    },
    "Duel.IsAbleToEnterBP": {
        "params": [],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether the current turn player can enter the Battle Phase."],
        "description_zh": ["检查当前回合玩家能否进入战斗阶段。"],
    },
    "Duel.CheckTribute": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("min", "int"), ParamDoc("max", "int", True, "default: min"),
            ParamDoc("mg", "Group|nil", True), ParamDoc("toplayer", "int", True, "default: c's controller"),
            ParamDoc("zone", "int", True, "default: current extra-summon zone limit or 0x1f"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether valid Tribute candidates exist for c."],
        "description_zh": ["检查c是否存在合法祭品候选。"],
    },
    "Effect.GetActivateLocation": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns e's activation location."],
        "description_zh": ["返回效果e发动的位置。"],
    },
    "Card.AddMonsterAttribute": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("type", "int"), ParamDoc("attribute", "int", True, "default: 0"),
            ParamDoc("race", "int", True, "default: 0"), ParamDoc("level", "int", True, "default: 0"),
            ParamDoc("atk", "int", True, "default: 0"), ParamDoc("def", "int", True, "default: 0"),
        ],
        "returns": [],
        "description": ["Adds temporary monster properties to c."],
        "description_zh": ["给c追加临时怪兽属性。"],
    },
    "Card.GetPreviousTypeOnField": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's previously recorded on-field Type."],
        "description_zh": ["返回c之前记录的场上种类。"],
    },
    "Duel.GetFieldCard": {
        "params": [ParamDoc("player", "int"), ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the card at a field location and sequence."],
        "description_zh": ["返回指定位置序号上的卡。"],
    },
    "Card.GetOriginalAttribute": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's original Attribute."],
        "description_zh": ["返回c的原本属性。"],
    },
    "Duel.SelectTribute": {
        "params": [
            ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("min", "int"), ParamDoc("max", "int"),
            ParamDoc("mg", "Group|nil", True), ParamDoc("toplayer", "int", True, "default: player"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Lets player select Tribute candidates for c."],
        "description_zh": ["让player为c选择祭品。"],
    },
    "Auxiliary.bdocon": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks the opponent-battle EVENT_BATTLE_DESTROYING condition."],
        "description_zh": ["检查对方怪兽战斗破坏条件。"],
    },
    "Card.IsCanBeXyzMaterial": {
        "params": [ParamDoc("c", "Card"), ParamDoc("sc", "Card|nil", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be used as Xyz Material."],
        "description_zh": ["检查c能否作为超量素材。"],
    },
    "Card.GetPreviousControler": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's previous controller."],
        "description_zh": ["返回c之前的控制者。"],
    },
    "Card.GetEquipGroup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns Equip Cards currently equipped to c."],
        "description_zh": ["返回当前装备给c的装备卡。"],
    },
    "Card.GetLinkedGroup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns cards currently in zones linked by c."],
        "description_zh": ["返回当前位于c连接区域中的卡。"],
    },
    "Card.GetLinkedZone": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: c's controller")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's linked-zone bitmask."],
        "description_zh": ["返回c的连接区域位掩码。"],
    },
    "Card.GetPreviousSequence": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's previous sequence."],
        "description_zh": ["返回c之前的位置序号。"],
    },
    "Duel.ChainAttack": {
        "params": [ParamDoc("c", "Card", True)],
        "returns": [],
        "description": ["Marks the current attacker for another attack."],
        "description_zh": ["标记当前攻击怪兽可以再次攻击。"],
    },
    "Duel.IsCanRemoveCounter": {
        "params": [ParamDoc("player", "int"), ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("countertype", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can remove counters from field locations."],
        "description_zh": ["检查player能否从场上位置取除指示物。"],
    },
    "Card.IsControlerCanBeChanged": {
        "params": [ParamDoc("c", "Card"), ParamDoc("ignore_mzone", "bool", True, "default: false"), ParamDoc("zone", "int", True, "default: 0xff")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether control of c can move to the other player."],
        "description_zh": ["检查c的控制权能否转移给另一名玩家。"],
    },
    "Duel.NegateAttack": {
        "params": [],
        "returns": [ReturnDoc("bool")],
        "description": ["Attempts to negate the current attack."],
        "description_zh": ["尝试无效当前攻击。"],
    },
    "Card.GetCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("countertype", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns counter information on c."],
        "description_zh": ["返回c上的指示物信息。"],
    },
    "Card.GetDefense": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current DEF."],
        "description_zh": ["返回c当前的守备力。"],
    },
    "Card.IsDefensePos": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is in Defense Position."],
        "description_zh": ["检查c是否为守备表示。"],
    },
    "Card.IsReleasable": {
        "params": [ParamDoc("c", "Card"), ParamDoc("reason", "int", True, "default: REASON_COST")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be Released for a non-Summon reason."],
        "description_zh": ["检查c能否作为非召唤用途被解放。"],
    },
    "Card.SetCardTarget": {
        "params": [ParamDoc("c1", "Card"), ParamDoc("c2", "Card")],
        "returns": [],
        "description": ["Registers c2 as a card target of c1."],
        "description_zh": ["把c2登记为c1的卡片对象。"],
    },
    "Auxiliary.exccon": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks the shared GY timing condition for the handler."],
        "description_zh": ["检查处理者的共通墓地时点条件。"],
    },
    "Card.GetOriginalLevel": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's original Level."],
        "description_zh": ["返回c的原本等级。"],
    },
    "Group.RemoveCard": {
        "params": [ParamDoc("g", "Group"), ParamDoc("c", "Card")],
        "returns": [],
        "description": ["Removes c from g."],
        "description_zh": ["从g中移除c。"],
    },
    "Auxiliary.AddFusionProcCode2": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int"), ParamDoc("sub", "bool"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers a two-code Fusion Material procedure."],
        "description_zh": ["登记双卡号融合素材手续。"],
    },
    "Duel.IsEnvironment": {
        "params": [ParamDoc("code", "int"), ParamDoc("player", "int", True, "default: PLAYER_ALL"), ParamDoc("loc", "int", True, "default: LOCATION_ONFIELD")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks the current environment card/code state."],
        "description_zh": ["检查当前环境卡/卡号状态。"],
    },
    "Auxiliary.indoval": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("re", "Effect"), ParamDoc("rp", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Returns true for opponent-effect indestructibility checks."],
        "description_zh": ["对方效果破坏耐性检查用辅助函数。"],
    },
    "Duel.RaiseEvent": {
        "params": [ParamDoc("eg", "Card|Group"), ParamDoc("code", "int"), ParamDoc("re", "Effect|nil"), ParamDoc("r", "int"), ParamDoc("rp", "int"), ParamDoc("ep", "int"), ParamDoc("ev", "int")],
        "returns": [],
        "description": ["Raises an event for a Card or Group."],
        "description_zh": ["对Card或Group引发事件。"],
    },
    "Auxiliary.GCheckAdditional": {
        "params": [ParamDoc("sg", "Group"), ParamDoc("c", "Card|nil"), ParamDoc("g", "Group")],
        "returns": [ReturnDoc("bool")],
        "description": ["Additional subgroup-check hook."],
        "description_zh": ["额外子组检查钩子。"],
    },
    "Card.IsRank": {
        "params": [ParamDoc("c", "Card"), ParamDoc("rank1", "int"), ParamDoc("rank2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's Rank matches any supplied value."],
        "description_zh": ["检查c的阶级是否匹配任意给定值。"],
    },
    "Card.GetTextAttack": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's card-data ATK."],
        "description_zh": ["返回c卡片数据中的攻击力。"],
    },
    "Duel.CheckLocation": {
        "params": [ParamDoc("player", "int"), ParamDoc("location", "int"), ParamDoc("sequence", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether a location sequence is usable."],
        "description_zh": ["检查位置序号是否可用。"],
    },
    "Card.GetRank": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current Rank."],
        "description_zh": ["返回c当前的阶级。"],
    },
    "Card.GetOriginalCode": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's original card code."],
        "description_zh": ["返回c的原本卡号。"],
    },
    "Card.IsDefense": {
        "params": [ParamDoc("c", "Card"), ParamDoc("def1", "int"), ParamDoc("def2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's current DEF matches any supplied value."],
        "description_zh": ["检查c当前守备力是否匹配任意给定值。"],
    },
    "Auxiliary.fuslimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether st includes SUMMON_TYPE_FUSION."],
        "description_zh": ["检查st是否包含SUMMON_TYPE_FUSION。"],
    },
    "Card.IsAbleToChangeControler": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is free of cannot-change-control effects."],
        "description_zh": ["检查c是否不受不能变更控制权效果影响。"],
    },
    "Group.Sub": {
        "params": [ParamDoc("g1", "Group"), ParamDoc("g2", "Group")],
        "returns": [],
        "description": ["Removes g2's cards from g1."],
        "description_zh": ["从g1中移除g2的卡。"],
    },
    "Card.IsFusionType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's type while used as Fusion Material."],
        "description_zh": ["检查c作为融合素材使用时的种类。"],
    },
    "Duel.ReturnToField": {
        "params": [ParamDoc("c", "Card"), ParamDoc("pos", "int", True, "default: previous position"), ParamDoc("zone", "int", True, "default: 0xff")],
        "returns": [ReturnDoc("bool|nil", "Success flag, or nil if c was not temporarily removed from the field.")],
        "description": ["Returns a temporarily removed card to the field."],
        "description_zh": ["把临时离场的卡返回场上。"],
    },
    "Duel.SetChainLimit": {
        "params": [ParamDoc("f", "function")],
        "returns": [],
        "description": ["Registers a temporary Chain limit callback."],
        "description_zh": ["登记临时连锁限制回调。"],
    },
    "Card.CheckRemoveOverlayCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int"), ParamDoc("count", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether player can remove Xyz Materials from c."],
        "description_zh": ["检查player能否从c上取除超量素材。"],
    },
    "Card.IsDestructable": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be destroyed."],
        "description_zh": ["检查c能否被破坏。"],
    },
    "Card.RemoveOverlayCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("reason", "int")],
        "returns": [ReturnDoc("int", "Number of Xyz Materials actually removed.")],
        "description": ["Removes Xyz Materials from c."],
        "description_zh": ["从c上取除超量素材。"],
    },
    "Auxiliary.IsCodeListed": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("bool|nil", "true if code is listed by c; nil otherwise.")],
        "description": ["Checks whether c lists code."],
        "description_zh": ["检查c是否列名code。"],
    },
    "Card.IsCanOverlay": {
        "params": [ParamDoc("c", "Card"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be used as Xyz Material by player."],
        "description_zh": ["检查c能否由player作为超量素材使用。"],
    },
    "Card.GetReasonPlayer": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current reason player."],
        "description_zh": ["返回c当前记录的原因玩家。"],
    },
    "Group.SelectUnselect": {
        "params": [
            ParamDoc("cg", "Group"), ParamDoc("sg", "Group|nil", True), ParamDoc("player", "int"),
            ParamDoc("finishable", "bool", True, "default: false"), ParamDoc("cancelable", "bool", True, "default: false"),
            ParamDoc("min", "int", True, "default: 1"), ParamDoc("max", "int", True, "default: 1"),
        ],
        "returns": [ReturnDoc("Card|nil", "Chosen card, or nil if the selection is canceled.")],
        "description": ["Lets player add or remove one card from an interactive selection."],
        "description_zh": ["让player在交互选择中加入或移出1张卡。"],
    },
    "Card.GetAttribute": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current Attribute bitmask."],
        "description_zh": ["返回c当前的属性位掩码。"],
    },
    "Effect.GetOwnerPlayer": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns e's owner player."],
        "description_zh": ["返回效果e的拥有者玩家。"],
    },
    "Card.GetOriginalType": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's original card-data type."],
        "description_zh": ["返回c原本卡片数据中的种类。"],
    },
    "Card.IsAttack": {
        "params": [ParamDoc("c", "Card"), ParamDoc("atk1", "int"), ParamDoc("atk2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's current ATK matches any supplied value."],
        "description_zh": ["检查c当前攻击力是否匹配任意给定值。"],
    },
    "Duel.GetCurrentChain": {
        "params": [],
        "returns": [ReturnDoc("int")],
        "description": ["Returns the active Chain size."],
        "description_zh": ["返回当前连锁数量。"],
    },
    "Auxiliary.ExceptThisCard": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("Card|nil", "e's handler if it is still related to the current Chain; otherwise nil.")],
        "description": ["Returns e's handler while it is still related to the current Chain."],
        "description_zh": ["在处理者仍与当前连锁关联时返回处理者。"],
    },
    "Group.CreateGroup": {
        "params": [],
        "returns": [ReturnDoc("Group")],
        "description": ["Creates an empty Group."],
        "description_zh": ["创建空Group。"],
    },
    "Card.GetReasonCard": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns c's current reason card."],
        "description_zh": ["返回c当前记录的原因卡。"],
    },
    "Card.GetOverlayGroup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns c's current Xyz Materials."],
        "description_zh": ["返回c当前的超量素材。"],
    },
    "Card.IsAttackPos": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is in Attack Position."],
        "description_zh": ["检查c是否为攻击表示。"],
    },
    "Card.IsCanChangePosition": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks the effect-specific position-change helper for c."],
        "description_zh": ["检查c的效果改变表示形式能力。"],
    },
    "Duel.ConfirmDecktop": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int")],
        "returns": [],
        "description": ["Reveals the top cards of player's Main Deck."],
        "description_zh": ["公开player主卡组最上方的卡。"],
    },
    "Auxiliary.MustMaterialCheck": {
        "params": [ParamDoc("v", "Card|Group|nil"), ParamDoc("tp", "int"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether required-material effects are satisfied."],
        "description_zh": ["检查必须素材效果是否已满足。"],
    },
    "Effect.IsActivated": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether e has a Chain Link effect type."],
        "description_zh": ["检查效果e是否具有连锁环效果类型。"],
    },
    "Group.GetSum": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("...", "any")],
        "returns": [ReturnDoc("int")],
        "description": ["Sums f's value for every card in g."],
        "description_zh": ["累计g中每张卡调用f得到的数值。"],
    },
    "Card.AddCounter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("countertype", "int"), ParamDoc("count", "int"), ParamDoc("singly", "bool", True, "default: false")],
        "returns": [ReturnDoc("bool")],
        "description": ["Adds counters to c through the current reason effect."],
        "description_zh": ["通过当前原因效果给c放置指示物。"],
    },
    "Duel.MoveSequence": {
        "params": [ParamDoc("c", "Card"), ParamDoc("seq", "int")],
        "returns": [],
        "description": ["Moves c to another sequence in its current location."],
        "description_zh": ["将c移动到当前位置内的另一序号。"],
    },
    "Auxiliary.AddFusionProcFun2": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f1", "function|table"), ParamDoc("f2", "function|table"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers a two-filter Fusion Material procedure."],
        "description_zh": ["登记双筛选条件的融合素材手续。"],
    },
    "Group.RandomSelect": {
        "params": [ParamDoc("g", "Group"), ParamDoc("player", "int"), ParamDoc("count", "int")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns a random subset of g."],
        "description_zh": ["返回g的随机子Group。"],
    },
    "Card.IsAttackAbove": {
        "params": [ParamDoc("c", "Card"), ParamDoc("atk", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's current ATK is at least atk."],
        "description_zh": ["检查c当前攻击力是否大于等于atk。"],
    },
    "Card.IsLinkRace": {
        "params": [ParamDoc("c", "Card"), ParamDoc("race", "int"), ParamDoc("player", "int", True, "default: current reason player")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's Race while used as Link Material."],
        "description_zh": ["检查c作为连接素材使用时的种族。"],
    },
    "Auxiliary.SelectFromOptions": {
        "params": [ParamDoc("tp", "int"), ParamDoc("...", "table")],
        "returns": [ReturnDoc("any|nil", "Selected option value or 1-based option index; nil if no option is available.")],
        "description": ["Selects from conditionally available options."],
        "description_zh": ["从满足条件的选项中选择。"],
    },
    "Card.IsCanBeFusionMaterial": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fc", "Card|nil", True), ParamDoc("summon_type", "int", True, "default: SUMMON_TYPE_FUSION")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be used as Fusion Material."],
        "description_zh": ["检查c能否作为融合素材。"],
    },
    "Card.IsLinkType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's type while used as Link Material."],
        "description_zh": ["检查c作为连接素材使用时的种类。"],
    },
    "Card.IsLinkSetCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("setcode1", "int"), ParamDoc("setcode2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's set codes while used as Link Material."],
        "description_zh": ["检查c作为连接素材使用时的系列。"],
    },
    "Auxiliary.AddFusionProcFunRep": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function|table"), ParamDoc("cc", "int"), ParamDoc("insf", "bool")],
        "returns": [],
        "description": ["Registers a repeated-filter Fusion Material procedure."],
        "description_zh": ["登记重复筛选条件的融合素材手续。"],
    },
    "Card.GetFlagEffectLabel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("int|nil", "First label value, or nil if no matching flag effect exists."), ReturnDoc("...?", "Additional integer label values from additional matching flag effects.")],
        "description": ["Returns label values from flag effects with the given code on c."],
        "description_zh": ["返回c上编号为code的标记效果Label。"],
    },
    "Card.GetMaterial": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Group", "Cards currently stored as c's material cards.")],
        "description": ["Returns c's stored material cards."],
        "description_zh": ["返回c记录的素材卡。"],
    },
    "Duel.GetChainMaterial": {
        "params": [ParamDoc("player", "int")],
        "returns": [ReturnDoc("Effect|nil")],
        "description": ["Returns the first chain material effect applying to player."],
        "description_zh": ["返回适用于player的连锁素材效果。"],
    },
    "Duel.NegateRelatedChain": {
        "params": [ParamDoc("c", "Card"), ParamDoc("reset_flag", "int")],
        "returns": [],
        "description": ["Registers temporary chain-disable effects for related Chain Links handled by c."],
        "description_zh": ["为c相关的连锁登记临时连锁无效效果。"],
    },
    "Card.IsSummonLocation": {
        "params": [ParamDoc("c", "Card"), ParamDoc("loc", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks c's recorded Summon location."],
        "description_zh": ["检查c记录的召唤位置。"],
    },
    "Card.GetFieldID": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns c's current field ID."],
        "description_zh": ["返回c当前的field ID。"],
    },
    "Effect.GetFieldID": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns e's internal field ID."],
        "description_zh": ["返回效果e的内部field ID。"],
    },
    "Effect.IsHasProperty": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("prop1", "int"), ParamDoc("prop2", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks e's effect property flags."],
        "description_zh": ["检查效果e的Property标志。"],
    },
    "Card.CheckUniqueOnField": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("check_player", "int"),
            ParamDoc("check_location", "int", True, "default: LOCATION_ONFIELD"), ParamDoc("icard", "Card|nil", True),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c satisfies unique-on-field restrictions for check_player."],
        "description_zh": ["检查c在check_player场上是否满足唯一性规则。"],
    },
    "Duel.GetDecktopGroup": {
        "params": [ParamDoc("player", "int"), ParamDoc("count", "int")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns the top cards of player's Deck as a Group."],
        "description_zh": ["返回player卡组最上方的卡组成的Group。"],
    },
    "Duel.GetFusionMaterial": {
        "params": [ParamDoc("player", "int"), ParamDoc("location", "int", True, "default: LOCATION_HAND + LOCATION_MZONE")],
        "returns": [
            ReturnDoc("Group", "All currently usable Fusion Material candidates, including extra Fusion Material effects."),
            ReturnDoc("Group", "Base material pool from the requested locations only."),
        ],
        "description": ["Returns all Fusion Material candidates and the requested-location base pool."],
        "description_zh": ["返回全部融合素材候选和指定位置的基础素材池。"],
    },
    "Card.EnableCounterPermit": {
        "params": [ParamDoc("c", "Card"), ParamDoc("countertype", "int"), ParamDoc("location", "int", True), ParamDoc("condition", "function", True)],
        "returns": [],
        "description": ["Registers a counter permit effect on c."],
        "description_zh": ["给c登记指示物许可效果。"],
    },
    "Card.IsCanTurnSet": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be turned face-down."],
        "description_zh": ["检查c能否变成里侧表示。"],
    },
    "Duel.AddCustomActivityCounter": {
        "params": [ParamDoc("counter_id", "int"), ParamDoc("activity_type", "int"), ParamDoc("f", "function")],
        "returns": [],
        "description": ["Registers a custom activity counter."],
        "description_zh": ["登记自定义行动计数器。"],
    },
    "Card.IsAttackBelow": {
        "params": [ParamDoc("c", "Card"), ParamDoc("atk", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c's current ATK is known and at most atk."],
        "description_zh": ["检查c当前攻击力是否已确定且小于等于atk。"],
    },
    "Duel.GetCustomActivityCount": {
        "params": [ParamDoc("counter_id", "int"), ParamDoc("player", "int"), ParamDoc("activity_type", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns one player's count from a custom activity counter."],
        "description_zh": ["返回指定玩家的自定义行动计数。"],
    },
    "Card.IsCanBeSpecialSummoned": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("sumtype", "int"),
            ParamDoc("sumplayer", "int"), ParamDoc("nocheck", "bool"), ParamDoc("nolimit", "bool"),
            ParamDoc("sumpos", "int", True, "default: POS_FACEUP"), ParamDoc("toplayer", "int", True, "default: sumplayer"), ParamDoc("zone", "int", True, "default: 0xff"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c can be Special Summoned by effect e with the supplied summon parameters."],
        "description_zh": ["检查c是否可以用效果e和给定的召唤参数进行特殊召唤。"],
    },
    "Card.IsCode": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int", True), ParamDoc("...", "int", True)],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c matches any supplied card code."],
        "description_zh": ["检查c的卡号是否匹配任意给定的卡号。"],
    },
    "Duel.GetFirstTarget": {
        "params": [],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns target cards recorded for the current Chain."],
        "description_zh": ["返回当前连锁登记的对象卡。"],
    },
    "Duel.GetMatchingGroup": {
        "params": [
            ParamDoc("f", "function|nil", True), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns matching cards from the specified locations as a Group."],
        "description_zh": ["返回以player来看指定位置中满足f且不等于ex的卡组成的Group。"],
    },
    "Duel.IsExistingTarget": {
        "params": [
            ParamDoc("f", "function|nil", True), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("count", "int"), ParamDoc("ex", "Card|Group|nil", True),
            ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether enough matching cards can become targets for the current effect."],
        "description_zh": ["检查指定位置是否存在足够数量、满足f且可以成为当前效果对象的卡。"],
    },
    "Duel.SelectTarget": {
        "params": [
            ParamDoc("sel_player", "int"), ParamDoc("f", "function|nil", True), ParamDoc("player", "int"),
            ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"),
            ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Selects matching target cards and registers them as the current Chain's targets."],
        "description_zh": ["选择满足条件的对象卡，并把选择结果登记为当前连锁的对象。"],
    },
    "Duel.SpecialSummon": {
        "params": [
            ParamDoc("targets", "Card|Group"), ParamDoc("sumtype", "int"), ParamDoc("sumplayer", "int"),
            ParamDoc("target_player", "int"), ParamDoc("nocheck", "bool"), ParamDoc("nolimit", "bool"),
            ParamDoc("pos", "int"), ParamDoc("zone", "int", True, "default: 0xff"),
        ],
        "returns": [ReturnDoc("int")],
        "description": ["Special Summons targets and returns the number of cards successfully Summoned."],
        "description_zh": ["把targets特殊召唤到target_player场上，并返回成功特殊召唤的数量。"],
    },
    "Duel.ChangePosition": {
        "params": [
            ParamDoc("targets", "Card|Group"), ParamDoc("au", "int"), ParamDoc("ad", "int", True, "default: au"),
            ParamDoc("du", "int", True, "default: au"), ParamDoc("dd", "int", True, "default: au"), ParamDoc("noflip", "bool", True, "default: false"),
        ],
        "returns": [ReturnDoc("int")],
        "description": ["Changes battle positions and returns the number of cards whose position actually changed."],
        "description_zh": [
            "变更targets的表示形式，并返回实际变更表示形式的卡的数量。",
            "au、ad、du、dd分别对应当前表侧攻击、里侧攻击、表侧守备、里侧守备的目标表示形式；省略时使用au。MDPro3核心不读取旧文档中的第7个setavailable参数。",
        ],
    },
    "Duel.GetControl": {
        "params": [
            ParamDoc("targets", "Card|Group"), ParamDoc("player", "int"), ParamDoc("reset_phase", "int", True, "default: 0"),
            ParamDoc("reset_count", "int", True, "default: 0"), ParamDoc("zone", "int", True, "default: 0xff"),
        ],
        "returns": [ReturnDoc("int")],
        "description": ["Moves control of targets to player and returns the number of cards whose control actually changed."],
        "description_zh": [
            "把targets的控制权转移给player，并返回实际变更控制权的卡的数量。",
            "临时获得控制权时传入reset_phase和reset_count，例如PHASE_END, 1；只想指定可用区域时传入0, 0, zone。",
        ],
    },
    "Duel.SpecialSummonComplete": {
        "params": [],
        "returns": [ReturnDoc("int")],
        "description": ["Completes Special Summons started with Duel.SpecialSummonStep."],
        "description_zh": ["完成由Duel.SpecialSummonStep开始的特殊召唤处理，触发召唤相关事件，并返回完成的特殊召唤数量。"],
    },
    "Effect.SetCost": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("cost_func", "function")],
        "returns": [],
        "description": ["Sets e's cost callback."],
        "description_zh": ["设置效果e的Cost函数。"],
    },
    "Effect.SetTargetRange": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("s_range", "int"), ParamDoc("o_range", "int")],
        "returns": [],
        "description": ["Sets e's target range fields."],
        "description_zh": ["设置效果e的Target Range属性。"],
    },
    "Effect.GetOperation": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("function|nil")],
        "description": ["Returns e's operation callback, or nil if no operation callback is set."],
        "description_zh": ["返回e的Operation回调函数；未设置时返回nil。"],
    },
    "Effect.GetTarget": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("function|nil")],
        "description": ["Returns e's target callback, or nil if no target callback is set."],
        "description_zh": ["返回e的Target回调函数；未设置时返回nil。"],
    },
    "Effect.GetValue": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("function|int")],
        "description": ["Returns e's value callback or integer value."],
        "description_zh": ["返回e的Value回调函数或整数值。"],
    },
    "Card.IsHasEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("code", "int"), ParamDoc("player", "int", True)],
        "returns": [ReturnDoc("Effect|nil"), ReturnDoc("... Effect", "Additional matching effects, if any.")],
        "description": ["Returns effects affecting c with code, or nil if none match."],
        "description_zh": ["返回影响c且编号为code的效果；没有匹配效果时返回nil。"],
    },
    "Card.GetEquipTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the card that c is equipped to."],
        "description_zh": ["返回c当前装备到的卡。"],
    },
    "Duel.CreateToken": {
        "params": [ParamDoc("player", "int"), ParamDoc("code", "int")],
        "returns": [ReturnDoc("Card|false")],
        "description": ["Creates a Token card for player."],
        "description_zh": ["为player创建衍生物Card。"],
    },
    "Duel.SelectFusionMaterial": {
        "params": [
            ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("g", "Group"),
            ParamDoc("gc", "Card|nil", True), ParamDoc("chkf", "int", True, "default: PLAYER_NONE"),
            ParamDoc("not_material", "bool", True, "default: false"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Lets player select Fusion Materials for c from g."],
        "description_zh": ["让player从g中为c选择融合素材。"],
    },
    "Group.FilterSelect": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("player", "int"), ParamDoc("f", "function"),
            ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("ex", "Card|Group|nil", True),
            ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Lets player choose matching cards from g."],
        "description_zh": ["让player从g中选择满足条件的卡。"],
    },
    "Group.Filter": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any")],
        "returns": [ReturnDoc("Group")],
        "description": ["Returns the cards in g that satisfy f and are not excluded by ex."],
        "description_zh": ["从g中筛选满足f且不等于ex的卡，并返回新的Group。"],
    },
    "Group.GetFirst": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the first card in g and resets g's iterator."],
        "description_zh": ["返回g中的第一张卡，并把g的迭代指针重置到第一张卡。"],
    },
    "Group.GetNext": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Returns the next card from g's iterator."],
        "description_zh": ["把g的迭代指针移动到下一张卡并返回该卡。"],
    },
    "Group.IsExists": {
        "params": [ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("count", "int"), ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether at least count cards in g satisfy f and are not excluded by ex."],
        "description_zh": ["检查g中是否存在至少count张满足f且不等于ex的卡。"],
    },
    "Group.Select": {
        "params": [ParamDoc("g", "Group"), ParamDoc("player", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"), ParamDoc("ex", "Card|Group|nil", True)],
        "returns": [ReturnDoc("Group")],
        "description": ["Lets player choose min to max cards from g."],
        "description_zh": ["让玩家player从g中选择min到max张卡。"],
    },
    "Auxiliary.Stringid": {
        "params": [ParamDoc("code", "int"), ParamDoc("id", "int")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns the card-string id for card code and string index id."],
        "description_zh": ["返回卡片code的第id个卡片字符串编号；id从0开始。"],
    },
    "Card.IsFaceup": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is in face-up position."],
        "description_zh": ["检查c是否为表侧表示。"],
    },
    "Card.IsLocation": {
        "params": [ParamDoc("c", "Card"), ParamDoc("location", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is currently in location."],
        "description_zh": ["检查c当前是否在location位置。"],
    },
    "Card.IsRelateToEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c is still related to effect e."],
        "description_zh": ["检查c是否仍与效果e保持联系。"],
    },
    "Card.IsSetCard": {
        "params": [ParamDoc("c", "Card"), ParamDoc("...", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c belongs to any supplied set code."],
        "description_zh": ["检查c是否属于任意给定的系列代码。"],
    },
    "Card.IsType": {
        "params": [ParamDoc("c", "Card"), ParamDoc("type", "int")],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether c has at least one type flag from type."],
        "description_zh": ["检查c是否包含type中的任意类型。"],
    },
    "Card.RegisterEffect": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("forced", "bool", True)],
        "returns": [ReturnDoc("int|nil")],
        "description": ["Registers effect e to card c and returns the generated effect field ID."],
        "description_zh": ["把效果e注册给c，成功时返回效果的场上编号，并设置e的Handler为c。"],
    },
    "Duel.GetLocationCount": {
        "params": [
            ParamDoc("player", "int"), ParamDoc("location", "int"), ParamDoc("use_player", "int", True),
            ParamDoc("reason", "int", True), ParamDoc("zone", "int", True),
        ],
        "returns": [ReturnDoc("int"), ReturnDoc("int")],
        "description": ["Returns the available zone count and usable zone mask for location on player's field."],
        "description_zh": ["返回玩家player场上location可用区域数量以及对应的可用区域mask。"],
    },
    "Duel.Hint": {
        "params": [ParamDoc("hint_type", "int"), ParamDoc("player", "int"), ParamDoc("desc", "int")],
        "returns": [],
        "description": ["Sends a hint message of hint_type to player using desc as the message id."],
        "description_zh": ["给玩家player发送hint_type类型的提示消息，提示内容为desc。"],
    },
    "Duel.IsExistingMatchingCard": {
        "params": [
            ParamDoc("f", "function|nil", True), ParamDoc("player", "int"), ParamDoc("s", "int"),
            ParamDoc("o", "int"), ParamDoc("count", "int"), ParamDoc("ex", "Card|Group|nil", True),
            ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("bool")],
        "description": ["Checks whether the specified locations contain at least count matching cards."],
        "description_zh": ["过滤函数；检查以player来看指定位置是否存在至少count张满足f且不等于ex的卡。"],
    },
    "Duel.SelectMatchingCard": {
        "params": [
            ParamDoc("sel_player", "int"), ParamDoc("f", "function|nil", True), ParamDoc("player", "int"),
            ParamDoc("s", "int"), ParamDoc("o", "int"), ParamDoc("min", "int"), ParamDoc("max", "int"),
            ParamDoc("ex", "Card|Group|nil", True), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group")],
        "description": ["Lets sel_player choose min to max matching cards from the specified locations."],
        "description_zh": ["过滤函数；让玩家sel_player从指定位置选择min到max张满足f且不等于ex的卡。"],
    },
    "Effect.CreateEffect": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Effect")],
        "description": ["Creates a new empty Effect object owned by card c."],
        "description_zh": ["新建一个空效果，并把效果的Owner设为c。"],
    },
    "Effect.GetHandler": {
        "params": [ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("Card")],
        "description": ["Returns the card currently handling e."],
        "description_zh": ["返回效果e当前在哪张卡上生效。"],
    },
    "Effect.SetAbsoluteRange": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("playerid", "int"), ParamDoc("s_range", "int"), ParamDoc("o_range", "int")],
        "returns": [],
        "description": ["Sets e's target range from an absolute player viewpoint."],
        "description_zh": ["以绝对玩家视角设置效果e的Target Range属性。playerid为1时，s_range和o_range会在核心中交换保存。"],
    },
    "Effect.SetCategory": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("cate", "int")],
        "returns": [],
        "description": ["Sets e's operation category flags."],
        "description_zh": ["设置效果e的Category属性，用于声明效果可能包含的操作类别。"],
    },
    "Effect.SetCode": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("code", "int")],
        "returns": [],
        "description": ["Sets e's code."],
        "description_zh": ["设置效果e的Code属性。"],
    },
    "Effect.SetCondition": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("con_func", "function")],
        "returns": [],
        "description": ["Sets e's condition callback."],
        "description_zh": ["设置效果e的Condition函数。"],
    },
    "Effect.SetCountLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("count", "int"), ParamDoc("code", "int", True)],
        "returns": [],
        "description": ["Sets e's count limit and optional shared count code."],
        "description_zh": ["设置效果e的使用次数限制count，以及可选的共享次数代码code。"],
    },
    "Effect.SetDescription": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("desc", "int")],
        "returns": [],
        "description": ["Sets e's description id."],
        "description_zh": ["设置效果e的描述编号。"],
    },
    "Effect.SetOperation": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("op_func", "nil|function")],
        "returns": [],
        "description": ["Sets or clears e's operation callback."],
        "description_zh": ["设置或清除效果e的Operation函数。"],
    },
    "Effect.SetProperty": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("prop1", "int"), ParamDoc("prop2", "int", True)],
        "returns": [],
        "description": ["Sets e's property flags."],
        "description_zh": ["设置效果e的Property属性。"],
    },
    "Effect.SetRange": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("range", "int")],
        "returns": [],
        "description": ["Sets the location range where e applies or can be activated."],
        "description_zh": ["设置效果e的生效或可发动位置。"],
    },
    "Effect.SetReset": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("reset_flag", "int"), ParamDoc("reset_count", "int", True)],
        "returns": [],
        "description": ["Sets e's reset flags and optional reset count."],
        "description_zh": ["设置效果e的reset参数和可选的reset次数。"],
    },
    "Effect.SetTarget": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("targ_func", "function")],
        "returns": [],
        "description": ["Sets e's target callback."],
        "description_zh": ["设置效果e的Target函数。"],
    },
    "Effect.SetType": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("type", "int")],
        "returns": [],
        "description": ["Sets e's effect type flags."],
        "description_zh": ["设置效果e的Type属性。"],
    },
    "Effect.SetValue": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("val", "function|int|bool")],
        "returns": [],
        "description": ["Sets e's value field."],
        "description_zh": ["设置效果e的Value属性。"],
    },
    "Group.GetCount": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("int")],
        "description": ["Returns the number of cards in g."],
        "description_zh": ["返回g中的卡片数量。"],
    },
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
    "Auxiliary.UrsarcticExCostFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c can be banished as an Ursarctic replacement cost.")],
        "description": ["Replacement-cost filter for the shared Ursarctic Special Summon effect."],
    },
    "Auxiliary.UrsarcticReleaseFilter": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c is a Level 7 or higher monster in the hand.")],
        "description": ["Release-cost filter for the shared Ursarctic Special Summon effect."],
    },
    "Auxiliary.UrsarcticSpSummonCondition": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [ReturnDoc("bool", "true during Main Phase 1 or Main Phase 2.")],
        "description": ["Condition for the shared Ursarctic hand Quick Effect."],
    },
    "Auxiliary.UrsarcticSpSummonCost": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
            ParamDoc("chk", "bool"),
        ],
        "returns": [ReturnDoc("bool|nil", "true during cost checks; otherwise no meaningful return value.")],
        "description": ["Checks and pays the shared Ursarctic Special Summon cost."],
    },
    "Auxiliary.UrsarcticSpSummonLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true for Level 0 monsters.")],
        "description": ["Special Summon restriction target applied by the shared Ursarctic effect."],
    },
    "Auxiliary.UrsarcticSpSummonOperation": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
        ],
        "returns": [],
        "description": ["Operation for the shared Ursarctic Special Summon effect."],
    },
    "Auxiliary.UrsarcticSpSummonTarget": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "any"), ParamDoc("re", "Effect"), ParamDoc("r", "any"), ParamDoc("rp", "int"),
            ParamDoc("chk", "bool"),
        ],
        "returns": [ReturnDoc("bool|nil", "true during valid target checks; otherwise no meaningful return value.")],
        "description": ["Target function for the shared Ursarctic Special Summon effect."],
    },
    "Auxiliary.UseExtraReleaseCount": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int")],
        "returns": [],
        "description": ["Consumes count limits for extra release effects used by cards in g."],
    },
    "GetID": {
        "params": [],
        "returns": [
            ReturnDoc("table", "The current script table."),
            ReturnDoc("int", "The current card code."),
            ReturnDoc("int", "String ID offset, 1 or 100."),
        ],
        "description": ["Returns the current script table, card code, and string offset."],
    },
    "Group.CheckSubGroup": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("f", "function"), ParamDoc("min", "int", True),
            ParamDoc("max", "int", True), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("bool", "true if a valid subgroup exists.")],
        "description": ["Checks whether g has a subgroup satisfying f."],
    },
    "Group.CheckSubGroupEach": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("checks", "table"), ParamDoc("f", "function", True),
            ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("bool", "true if one card can satisfy each check.")],
        "description": ["Checks whether g can supply one card for each filter in checks."],
    },
    "Group.SelectSubGroup": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("f", "function"),
            ParamDoc("cancelable", "bool"), ParamDoc("min", "int", True), ParamDoc("max", "int", True),
            ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group|nil", "The selected subgroup, or nil if no valid selection is completed.")],
        "description": ["Lets tp select a subgroup satisfying f."],
    },
    "Group.SelectSubGroupEach": {
        "params": [
            ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("checks", "table"),
            ParamDoc("cancelable", "bool", True), ParamDoc("f", "function", True), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Group|nil", "The selected subgroup, or nil if no valid selection is completed.")],
        "description": ["Lets tp select one card for each filter in checks."],
    },
    "Duel.GetLocationCountFromEx": {
        "params": [
            ParamDoc("player", "int"),
            ParamDoc("reason_player", "int", True),
            ParamDoc("targets", "Group|Card|nil", True),
            ParamDoc("sc", "Card|int|nil", True),
            ParamDoc("zone", "int", True),
        ],
        "returns": [
            ReturnDoc("int", "Number of usable Monster Zones."),
            ReturnDoc("int", "Usable zone mask."),
        ],
        "description": ["Returns Extra Deck Special Summon zone availability."],
    },
    "Duel.IsPlayerCanSpecialSummonMonster": {
        "params": [
            ParamDoc("player", "int"),
            ParamDoc("code", "int"),
            ParamDoc("setcode", "int|nil", True),
            ParamDoc("type", "int|nil", True),
            ParamDoc("atk", "int|nil", True),
            ParamDoc("def", "int|nil", True),
            ParamDoc("level", "int|nil", True),
            ParamDoc("race", "int|nil", True),
            ParamDoc("attribute", "int|nil", True),
            ParamDoc("pos", "int", True),
            ParamDoc("target_player", "int", True),
            ParamDoc("sumtype", "int", True),
        ],
        "returns": [ReturnDoc("bool", "true if the virtual monster can be Special Summoned.")],
        "description": ["Checks whether a virtual monster can be Special Summoned with the supplied data."],
    },
    "Card.GetBattleTarget": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("Card|nil", "The monster battling c, or nil.")],
        "description": ["Returns c's current battle counterpart."],
    },
    "Auxiliary.TargetBoolFunction": {
        "params": [ParamDoc("f", "function"), ParamDoc("...", "any")],
        "returns": [ReturnDoc("function", "A target callback with parameters (effect, target).")],
        "description": ["Wraps a Card predicate for APIs that expect an effect target callback."],
    },
    "Auxiliary.Next": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("function", "Iterator function for generic for loops.")],
        "description": ["Creates an iterator over g using Group.GetFirst and Group.GetNext."],
    },
    "Auxiliary.EnablePendulumAttribute": {
        "params": [ParamDoc("c", "Card"), ParamDoc("reg", "bool|nil", True)],
        "returns": [],
        "description": ["Registers the standard Pendulum Summon procedure for c."],
    },
    "bit.band": {
        "params": [ParamDoc("a", "int"), ParamDoc("b", "int")],
        "returns": [ReturnDoc("int", "Bitwise AND of a and b.")],
        "description": ["Lua 5.3 bit32-compatible bitwise AND helper."],
    },
    "bit.bnot": {
        "params": [ParamDoc("a", "int")],
        "returns": [ReturnDoc("int", "Bitwise NOT of a.")],
        "description": ["Lua 5.3 bit32-compatible bitwise NOT helper."],
    },
    "bit.extract": {
        "params": [ParamDoc("r", "int"), ParamDoc("field", "int"), ParamDoc("width", "int", True)],
        "returns": [ReturnDoc("int", "The extracted bit field.")],
        "description": ["Extracts a bit field from r."],
    },
    "bit.replace": {
        "params": [ParamDoc("r", "int"), ParamDoc("v", "int"), ParamDoc("field", "int"), ParamDoc("width", "int", True)],
        "returns": [ReturnDoc("int", "r with the selected bit field replaced.")],
        "description": ["Replaces a bit field inside r."],
    },
    "Auxiliary.AddContactFusionProcedure": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function"), ParamDoc("self_location", "int", True),
            ParamDoc("opponent_location", "int", True), ParamDoc("mat_operation", "function"), ParamDoc("...", "any"),
        ],
        "returns": [ReturnDoc("Effect", "The created Contact Fusion procedure effect.")],
        "description": ["Registers a Contact Fusion Special Summon procedure on c."],
    },
    "Auxiliary.AddSynchroProcedure2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f1", "function|nil", True), ParamDoc("f2", "function|nil", True),
        ],
        "returns": [],
        "description": ["Registers the backward-compatible one-Tuner, one-non-Tuner Synchro Summon procedure on c."],
    },
    "Auxiliary.AddFusionEffectProc": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function"), ParamDoc("mat_location", "int"),
            ParamDoc("mat_filter", "function|nil", True), ParamDoc("mat_operation", "function|nil", True),
            ParamDoc("params", "table|nil", True),
        ],
        "returns": [ReturnDoc("Effect", "The created Fusion effect.")],
        "description": ["Convenience wrapper for Auxiliary.AddFusionEffectProcUltimate."],
    },
    "Auxiliary.AddRitualProcGreater2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function"), ParamDoc("summon_location", "int", True),
            ParamDoc("grave_filter", "function|nil", True), ParamDoc("mat_filter", "function|nil", True),
            ParamDoc("pause", "bool", True), ParamDoc("extra_operation", "function|nil", True),
            ParamDoc("extra_target", "function|nil", True),
        ],
        "returns": [ReturnDoc("Effect", "The created Ritual Summon effect.")],
        "description": ["Adds a greater-or-equal Ritual procedure using the Ritual Monster's current Level."],
    },
    "Auxiliary.AddRitualProcGreater2Code": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("summon_location", "int", True),
            ParamDoc("grave_filter", "function|nil", True), ParamDoc("mat_filter", "function|nil", True),
            ParamDoc("pause", "bool", True), ParamDoc("extra_operation", "function|nil", True),
            ParamDoc("extra_target", "function|nil", True),
        ],
        "returns": [ReturnDoc("Effect", "The created Ritual Summon effect.")],
        "description": ["Adds a greater-or-equal Ritual procedure restricted by one listed code."],
    },
    "Auxiliary.AddRitualProcGreater2Code2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("code1", "int"), ParamDoc("code2", "int"),
            ParamDoc("summon_location", "int", True), ParamDoc("grave_filter", "function|nil", True),
            ParamDoc("mat_filter", "function|nil", True), ParamDoc("pause", "bool", True),
            ParamDoc("extra_operation", "function|nil", True), ParamDoc("extra_target", "function|nil", True),
        ],
        "returns": [ReturnDoc("Effect", "The created Ritual Summon effect.")],
        "description": ["Adds a greater-or-equal Ritual procedure restricted by two listed codes."],
    },
    "Auxiliary.AddRitualProcUltimate": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function"), ParamDoc("level_function", "function"),
            ParamDoc("greater_or_equal", "string"), ParamDoc("summon_location", "int", True),
            ParamDoc("grave_filter", "function|nil", True), ParamDoc("mat_filter", "function|nil", True),
            ParamDoc("pause", "bool", True), ParamDoc("extra_operation", "function|nil", True),
            ParamDoc("extra_target", "function|nil", True),
        ],
        "returns": [ReturnDoc("Effect", "The created Ritual Summon activation effect.")],
        "description": ["Creates a configurable Ritual Summon activation effect."],
    },
    "Auxiliary.AssaultModeLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool", "true if the Summon matches /Assault Mode conditions.")],
        "description": ["Special Summon restriction value for /Assault Mode monsters."],
    },
    "Auxiliary.CheckXyz2XMaterial": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f", "function"), ParamDoc("lv", "int"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("mg", "Group"),
        ],
        "returns": [ReturnDoc("bool", "true if c can be Xyz Summoned with double-material support.")],
        "description": ["Checks whether c can be Xyz Summoned while counting valid double materials."],
    },
    "Auxiliary.ContactFusionCondition": {
        "params": [ParamDoc("filter", "function|nil", True), ParamDoc("self_location", "int"), ParamDoc("opponent_location", "int")],
        "returns": [ReturnDoc("function", "Condition function for a Contact Fusion procedure.")],
        "description": ["Returns the condition function for Contact Fusion procedures."],
    },
    "Auxiliary.ContactFusionMaterialFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("filter", "function|nil", True)],
        "returns": [ReturnDoc("bool", "true if c is valid Contact Fusion material for fc.")],
        "description": ["Material filter for Contact Fusion procedures."],
    },
    "Auxiliary.ContactFusionOperation": {
        "params": [ParamDoc("mat_operation", "function"), ParamDoc("operation_params", "table")],
        "returns": [ReturnDoc("function", "Operation function for a Contact Fusion procedure.")],
        "description": ["Returns the operation function for Contact Fusion procedures."],
    },
    "Auxiliary.ContactFusionSendToDeck": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("function", "Material operation that shuffles materials into the Deck.")],
        "description": ["Returns a Contact Fusion material operation that sends materials to the Deck."],
    },
    "Auxiliary.ContactFusionTarget": {
        "params": [ParamDoc("filter", "function|nil", True), ParamDoc("self_location", "int"), ParamDoc("opponent_location", "int")],
        "returns": [ReturnDoc("function", "Target function for a Contact Fusion procedure.")],
        "description": ["Returns the target function for Contact Fusion procedures."],
    },
    "Auxiliary.DarkFusionLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool", "true if the Summon matches Dark Fusion conditions.")],
        "description": ["Special Summon restriction value for Evil HERO/Dark Fusion effects."],
    },
    "Auxiliary.FCheckMix": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("mg", "Group"), ParamDoc("sg", "Group"), ParamDoc("fc", "Card"),
            ParamDoc("sub", "bool"), ParamDoc("fun1", "function"), ParamDoc("fun2", "function|nil", True),
            ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if the remaining mixed Fusion Material functions can be satisfied.")],
        "description": ["Recursive mixed Fusion Material checker."],
    },
    "Auxiliary.FCheckMixGoal": {
        "params": [
            ParamDoc("sg", "Group"), ParamDoc("tp", "int"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"),
            ParamDoc("chkfnf", "int"), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if sg is a valid mixed Fusion Material group.")],
        "description": ["Final group check for mixed Fusion Materials."],
    },
    "Auxiliary.FCheckMixRep": {
        "params": [
            ParamDoc("sg", "Group"), ParamDoc("g", "Group"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"),
            ParamDoc("chkf", "int"), ParamDoc("fun1", "function"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("fun2", "function|nil", True), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if the mixed-repeat material requirements can be satisfied.")],
        "description": ["Checks a selected mixed-repeat Fusion Material group."],
    },
    "Auxiliary.FCheckMixRepFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("sg", "Group"), ParamDoc("g", "Group"), ParamDoc("fc", "Card"),
            ParamDoc("sub", "bool"), ParamDoc("chkf", "int"), ParamDoc("fun1", "function"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("fun2", "function|nil", True),
            ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if c can satisfy this fixed material slot and the rest can be completed.")],
        "description": ["Recursive helper for Auxiliary.FCheckMixRep."],
    },
    "Auxiliary.FCheckMixRepGoal": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("sg", "Group"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"),
            ParamDoc("chkfnf", "int"), ParamDoc("fun1", "function"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if sg is a valid mixed-repeat Fusion Material group.")],
        "description": ["Final goal check for mixed-repeat Fusion Materials."],
    },
    "Auxiliary.FCheckMixRepGoalCheck": {
        "params": [ParamDoc("tp", "int"), ParamDoc("sg", "Group"), ParamDoc("fc", "Card"), ParamDoc("chkfnf", "int")],
        "returns": [ReturnDoc("bool", "true if shared mixed-repeat goal prechecks pass.")],
        "description": ["Shared precheck for mixed-repeat Fusion Material goals."],
    },
    "Auxiliary.FCheckMixRepSelected": {
        "params": [ParamDoc("c", "Card"), ParamDoc("...", "any")],
        "returns": [ReturnDoc("bool", "true if the selected-material recursion can succeed.")],
        "description": ["Selection-recursion helper for mixed-repeat Fusion Materials."],
    },
    "Auxiliary.FCheckMixRepSelectedCond": {
        "params": [ParamDoc("tp", "int"), ParamDoc("mg", "Group"), ParamDoc("sg", "Group"), ParamDoc("g", "Group"), ParamDoc("...", "any")],
        "returns": [ReturnDoc("bool", "true if the current mixed-repeat selection can continue or finish.")],
        "description": ["Checks recursive mixed-repeat selection state."],
    },
    "Auxiliary.FCheckMixRepTemplate": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("cond", "function"), ParamDoc("tp", "int"), ParamDoc("mg", "Group"),
            ParamDoc("sg", "Group"), ParamDoc("g", "Group"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"),
            ParamDoc("chkfnf", "int"), ParamDoc("fun1", "function"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if c can be assigned to a fixed or repeated material slot.")],
        "description": ["Generic recursive template for mixed-repeat Fusion Material checks."],
    },
    "Auxiliary.FCheckSelectMixRep": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("mg", "Group"), ParamDoc("sg", "Group"), ParamDoc("g", "Group"),
            ParamDoc("fc", "Card"), ParamDoc("sub", "bool"), ParamDoc("chkfnf", "int"),
            ParamDoc("fun1", "function"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"),
            ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if the current selection can be completed.")],
        "description": ["Checks whether a mixed-repeat Fusion Material selection can be completed."],
    },
    "Auxiliary.FCheckSelectMixRepAll": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("mg", "Group"), ParamDoc("sg", "Group"),
            ParamDoc("g", "Group"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"), ParamDoc("chkf", "int"),
            ParamDoc("fun1", "function"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"),
            ParamDoc("fun2", "function|nil", True), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if the selection can be completed through c.")],
        "description": ["Recursive helper for mixed-repeat Fusion selection without extra Monster Zone filtering."],
    },
    "Auxiliary.FCheckSelectMixRepM": {
        "params": [ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("...", "any")],
        "returns": [ReturnDoc("bool", "true if c is a valid Monster Zone candidate and the selection can be completed.")],
        "description": ["Recursive helper for mixed-repeat Fusion selection requiring a Monster Zone candidate."],
    },
    "Auxiliary.FConditionFilterMix": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("sub", "bool"), ParamDoc("notfusion", "bool"), ParamDoc("...", "function")],
        "returns": [ReturnDoc("bool", "true if c is valid material and satisfies any required material function.")],
        "description": ["Material filter used by mixed Fusion procedures."],
    },
    "Auxiliary.FConditionMix": {
        "params": [ParamDoc("insf", "bool"), ParamDoc("sub", "bool"), ParamDoc("...", "function")],
        "returns": [ReturnDoc("function", "Condition function for a fixed mixed Fusion Material procedure.")],
        "description": ["Returns the condition function for fixed mixed Fusion Material procedures."],
    },
    "Auxiliary.FConditionMixRep": {
        "params": [
            ParamDoc("insf", "bool"), ParamDoc("sub", "bool"), ParamDoc("fun1", "function"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("function", "Condition function for a mixed-repeat Fusion Material procedure.")],
        "description": ["Returns the condition function for mixed Fusion Material procedures with a repeated material slot."],
    },
    "Auxiliary.FMaterialFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c can be used as Fusion Material.")],
        "description": ["Default Fusion Material filter for Fusion effects."],
    },
    "Auxiliary.FMaterialRemove": {
        "params": [ParamDoc("mat", "Group|Card")],
        "returns": [],
        "description": ["Default operation for banishing Fusion Materials."],
    },
    "Auxiliary.FMaterialRemoveFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c can be banished.")],
        "description": ["Default Graveyard-material filter for Fusion effects that banish materials."],
    },
    "Auxiliary.FMaterialToDeck": {
        "params": [ParamDoc("mat", "Group|Card")],
        "returns": [],
        "description": ["Default operation for returning Fusion Materials to the Deck."],
    },
    "Auxiliary.FMaterialToGrave": {
        "params": [ParamDoc("mat", "Group|Card")],
        "returns": [],
        "description": ["Default operation for sending Fusion Materials to the Graveyard."],
    },
    "Auxiliary.FMaterialToGraveFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c can be sent to the Graveyard.")],
        "description": ["Default Fusion Material filter for effects that send materials to the Graveyard."],
    },
    "Auxiliary.FOperationMix": {
        "params": [ParamDoc("insf", "bool"), ParamDoc("sub", "bool"), ParamDoc("...", "function")],
        "returns": [ReturnDoc("function", "Operation function for a fixed mixed Fusion Material procedure.")],
        "description": ["Returns the operation function for fixed mixed Fusion Material procedures."],
    },
    "Auxiliary.FOperationMixRep": {
        "params": [
            ParamDoc("insf", "bool"), ParamDoc("sub", "bool"), ParamDoc("fun1", "function"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("function", "Operation function for a mixed-repeat Fusion Material procedure.")],
        "description": ["Returns the operation function for mixed Fusion Material procedures with a repeated material slot."],
    },
    "Auxiliary.FossilFusionLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool", "true if the Summon matches Fossil Fusion conditions.")],
        "description": ["Special Summon restriction value for Fossil Fusion effects."],
    },
    "Auxiliary.FSelectMixRep": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("mg", "Group"), ParamDoc("sg", "Group"),
            ParamDoc("fc", "Card"), ParamDoc("sub", "bool"), ParamDoc("chkfnf", "int"),
            ParamDoc("...", "function"),
        ],
        "returns": [ReturnDoc("bool", "true if adding c can complete or continue the selection.")],
        "description": ["Candidate test for mixed-repeat Fusion selection."],
    },
    "Auxiliary.FShaddollCondition": {
        "params": [ParamDoc("attr", "int")],
        "returns": [ReturnDoc("function", "Condition function for a Shaddoll Fusion procedure.")],
        "description": ["Returns the condition function for Shaddoll Fusion procedures."],
    },
    "Auxiliary.FShaddollExFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("attr", "int"), ParamDoc("fe", "Effect")],
        "returns": [ReturnDoc("bool", "true if c is a valid opponent-field Shaddoll Fusion Material.")],
        "description": ["Opponent-field Shaddoll Fusion Material filter used with effect code 81788994."],
    },
    "Auxiliary.FShaddollFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("attr", "int")],
        "returns": [ReturnDoc("bool", "true if c is valid Shaddoll Fusion Material.")],
        "description": ["Standard Shaddoll Fusion Material filter."],
    },
    "Auxiliary.FShaddollFilter1": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c belongs to Shaddoll Fusion set 0x9d.")],
        "description": ["Checks Shaddoll Fusion set membership."],
    },
    "Auxiliary.FShaddollFilter2": {
        "params": [ParamDoc("c", "Card"), ParamDoc("attr", "int")],
        "returns": [ReturnDoc("bool", "true if c has attr as Fusion Attribute or effect code 4904633.")],
        "description": ["Checks the required Shaddoll Fusion Attribute condition."],
    },
    "Auxiliary.FShaddollOperation": {
        "params": [ParamDoc("attr", "int")],
        "returns": [ReturnDoc("function", "Operation function for a Shaddoll Fusion procedure.")],
        "description": ["Returns the operation function for Shaddoll Fusion procedures."],
    },
    "Auxiliary.FShaddollSpFilter1": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("tp", "int"),
            ParamDoc("mg", "Group"), ParamDoc("exg", "Group|nil"), ParamDoc("attr", "int"),
            ParamDoc("chkf", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if c can be paired with another valid material.")],
        "description": ["Checks whether c can be paired with another valid Shaddoll Fusion Material."],
    },
    "Auxiliary.FShaddollSpFilter2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("fc", "Card"), ParamDoc("tp", "int"),
            ParamDoc("mc", "Card"), ParamDoc("attr", "int"), ParamDoc("chkf", "int"),
        ],
        "returns": [ReturnDoc("bool", "true if c and mc form a valid Shaddoll Fusion Material pair.")],
        "description": ["Checks a two-card Shaddoll Fusion Material pair."],
    },
    "Auxiliary.FusionEffectUltimateFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"),
            ParamDoc("mg", "Group"), ParamDoc("chkf", "int"), ParamDoc("params", "table"),
        ],
        "returns": [ReturnDoc("bool", "true if c can be Fusion Summoned with the provided material pool.")],
        "description": ["Checks whether c is a valid Fusion Summon target for the configured Fusion effect."],
    },
    "Auxiliary.FusionEffectUltimateMatFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("f", "function|nil")],
        "returns": [ReturnDoc("bool", "true if c is affected by e and passes f when provided.")],
        "description": ["Fusion effect material filter."],
    },
    "Auxiliary.FusionEffectUltimateMatLocFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"),
            ParamDoc("loc", "int"), ParamDoc("f", "function|nil"),
        ],
        "returns": [ReturnDoc("bool", "true if c is outside loc or passes f.")],
        "description": ["Location-specific Fusion material filter."],
    },
    "Auxiliary.FusionEffectUltimateOperation": {
        "params": [ParamDoc("params", "table")],
        "returns": [ReturnDoc("function", "Operation function for a configurable Fusion Summon effect.")],
        "description": ["Returns the operation function for configurable Fusion Summon effects."],
    },
    "Auxiliary.FusionEffectUltimateTarget": {
        "params": [ParamDoc("params", "table")],
        "returns": [ReturnDoc("function", "Target function for a configurable Fusion Summon effect.")],
        "description": ["Returns the target function for configurable Fusion Summon effects."],
    },
    "Auxiliary.GetLinkMaterials": {
        "params": [ParamDoc("tp", "int"), ParamDoc("f", "function|nil"), ParamDoc("lc", "Card"), ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("Group", "Available Link Materials.")],
        "description": ["Returns the available Link Materials for tp."],
    },
    "Auxiliary.GetMinSynchroLevel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("int", "Smallest Synchro Level value c can provide.")],
        "description": ["Returns the smallest Synchro Level value c can provide."],
    },
    "Auxiliary.GetSynchroLevelFlowerCardian": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("int", "Fixed Synchro Level value 2.")],
        "description": ["Returns the fixed Synchro Level value used by Flower Cardian helpers."],
    },
    "Auxiliary.GetSynMaterials": {
        "params": [ParamDoc("tp", "int"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("Group", "Available Synchro Materials.")],
        "description": ["Returns the available Synchro Materials for tp and syncard."],
    },
    "Auxiliary.LCheckGoal": {
        "params": [ParamDoc("sg", "Group"), ParamDoc("tp", "int"), ParamDoc("lc", "Card"), ParamDoc("gf", "function|nil"), ParamDoc("lmat", "Card|nil")],
        "returns": [ReturnDoc("bool", "true if sg is a valid Link Material group.")],
        "description": ["Final Link Material group check."],
    },
    "Auxiliary.LCheckOtherMaterial": {
        "params": [ParamDoc("c", "Card"), ParamDoc("mg", "Group"), ParamDoc("lc", "Card"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c is compatible with mg.")],
        "description": ["Checks extra Link Material compatibility for c."],
    },
    "Auxiliary.LConditionFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function|nil"), ParamDoc("lc", "Card"), ParamDoc("e", "Effect")],
        "returns": [ReturnDoc("bool", "true if c is regular Link Material.")],
        "description": ["Regular Link Material filter."],
    },
    "Auxiliary.LExtraFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function|nil"), ParamDoc("lc", "Card"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c can be used through an extra Link Material effect.")],
        "description": ["Extra Link Material filter."],
    },
    "Auxiliary.LExtraMaterialCount": {
        "params": [ParamDoc("mg", "Group"), ParamDoc("lc", "Card"), ParamDoc("tp", "int")],
        "returns": [],
        "description": ["Consumes count limits for selected extra Link Materials."],
    },
    "Auxiliary.LinkCondition": {
        "params": [ParamDoc("f", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gf", "function|nil")],
        "returns": [ReturnDoc("function", "Condition function for a Link Summon procedure.")],
        "description": ["Returns the condition function for Link Summon procedures."],
    },
    "Auxiliary.LinkOperation": {
        "params": [ParamDoc("f", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gf", "function|nil")],
        "returns": [ReturnDoc("function", "Operation function for a Link Summon procedure.")],
        "description": ["Returns the operation function for Link Summon procedures."],
    },
    "Auxiliary.LinkTarget": {
        "params": [ParamDoc("f", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gf", "function|nil")],
        "returns": [ReturnDoc("function", "Target function for a Link Summon procedure.")],
        "description": ["Returns the target function for Link Summon procedures."],
    },
    "Auxiliary.LUncompatibilityFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("sg", "Group"), ParamDoc("lc", "Card"), ParamDoc("tp", "int")],
        "returns": [ReturnDoc("bool", "true if c is incompatible with the rest of sg.")],
        "description": ["Checks Link Material incompatibility."],
    },
    "Auxiliary.MaskChangeLimit": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("se", "Effect"), ParamDoc("sp", "int"), ParamDoc("st", "int")],
        "returns": [ReturnDoc("bool", "true if the Summon matches Mask Change conditions.")],
        "description": ["Special Summon restriction value for Masked HERO/Mask Change effects."],
    },
    "Auxiliary.PConditionExtraFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("lscale", "int"), ParamDoc("rscale", "int"), ParamDoc("eset", "table")],
        "returns": [ReturnDoc("bool", "true if any extra Pendulum Summon effect allows c.")],
        "description": ["Checks extra Pendulum Summon effects for c."],
    },
    "Auxiliary.PConditionExtraFilterSpecific": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("lscale", "int"), ParamDoc("rscale", "int"), ParamDoc("te", "Effect|nil")],
        "returns": [ReturnDoc("bool", "true if te allows c or te is nil.")],
        "description": ["Checks one extra Pendulum Summon effect for c."],
    },
    "Auxiliary.PConditionFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("lscale", "int"), ParamDoc("rscale", "int"), ParamDoc("eset", "table")],
        "returns": [ReturnDoc("bool", "true if c can be Pendulum Summoned.")],
        "description": ["Pendulum Summon candidate filter."],
    },
    "Auxiliary.PendCondition": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("c", "Card|nil"), ParamDoc("og", "Group|nil")],
        "returns": [ReturnDoc("bool", "true if a Pendulum Summon is available.")],
        "description": ["Condition function for the shared Pendulum Summon procedure."],
    },
    "Auxiliary.PendOperation": {
        "params": [
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"),
            ParamDoc("ev", "int"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int"),
            ParamDoc("c", "Card"), ParamDoc("sg", "Group"), ParamDoc("og", "Group|nil"),
        ],
        "returns": [],
        "description": ["Operation function for the shared Pendulum Summon procedure."],
    },
    "Auxiliary.PendOperationCheck": {
        "params": [ParamDoc("ft1", "int"), ParamDoc("ft2", "int"), ParamDoc("ft", "int")],
        "returns": [ReturnDoc("function", "Group check for Pendulum Summon zone limits.")],
        "description": ["Returns a group check for Pendulum Summon zone limits."],
    },
    "Auxiliary.PendulumReset": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int")],
        "returns": [],
        "description": ["Resets the shared Pendulum Summon checklist."],
    },
    "Auxiliary.PendulumSummonableBool": {
        "params": [ParamDoc("c", "Card")],
        "returns": [ReturnDoc("bool", "true if c's current location is Pendulum Summonable by its flag.")],
        "description": ["Checks the psummonable_location flag for c."],
    },
    "Auxiliary.PSSCompleteProcedure": {
        "params": [ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("eg", "Group"), ParamDoc("ep", "int"), ParamDoc("ev", "int"), ParamDoc("re", "Effect"), ParamDoc("r", "int"), ParamDoc("rp", "int")],
        "returns": [],
        "description": ["Completes the procedure after a Pendulum Summon when appropriate."],
    },
    "Auxiliary.RitualCheckAdditional": {
        "params": [ParamDoc("c", "Card"), ParamDoc("lv", "int"), ParamDoc("greater_or_equal", "string")],
        "returns": [ReturnDoc("function", "Additional Ritual Material subgroup check.")],
        "description": ["Returns an additional subgroup check for Ritual Material selection."],
    },
    "Auxiliary.RitualCheckAdditionalLevel": {
        "params": [ParamDoc("c", "Card"), ParamDoc("rc", "Card")],
        "returns": [ReturnDoc("int", "Smallest usable Ritual Level value.")],
        "description": ["Returns the smaller usable Ritual Level value for c."],
    },
    "Auxiliary.RitualCheckEqual": {
        "params": [ParamDoc("g", "Group"), ParamDoc("c", "Card"), ParamDoc("lv", "int")],
        "returns": [ReturnDoc("bool", "true if g exactly matches lv.")],
        "description": ["Checks exact Ritual Material Level total."],
    },
    "Auxiliary.RitualCheckGreater": {
        "params": [ParamDoc("g", "Group"), ParamDoc("c", "Card"), ParamDoc("lv", "int")],
        "returns": [ReturnDoc("bool", "true if g reaches at least lv.")],
        "description": ["Checks greater-or-equal Ritual Material Level total."],
    },
    "Auxiliary.RitualExtraFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function")],
        "returns": [ReturnDoc("bool", "true if c is valid extra Graveyard Ritual Material.")],
        "description": ["Graveyard Ritual Material filter."],
    },
    "Auxiliary.RitualUltimateFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("filter", "function|nil"), ParamDoc("e", "Effect"), ParamDoc("tp", "int"),
            ParamDoc("m1", "Group"), ParamDoc("m2", "Group|nil"), ParamDoc("level_function", "function"),
            ParamDoc("greater_or_equal", "string"), ParamDoc("chk", "bool|nil"),
        ],
        "returns": [ReturnDoc("bool", "true if c can be Ritual Summoned.")],
        "description": ["Checks whether c is a valid Ritual Summon target."],
    },
    "Auxiliary.RitualUltimateOperation": {
        "params": [
            ParamDoc("filter", "function|nil"), ParamDoc("level_function", "function"),
            ParamDoc("greater_or_equal", "string"), ParamDoc("summon_location", "int"),
            ParamDoc("grave_filter", "function|nil"), ParamDoc("mat_filter", "function|nil"),
            ParamDoc("extra_operation", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Operation function for a configurable Ritual Summon effect.")],
        "description": ["Returns the operation function for configurable Ritual Summon effects."],
    },
    "Auxiliary.RitualUltimateTarget": {
        "params": [
            ParamDoc("filter", "function|nil"), ParamDoc("level_function", "function"),
            ParamDoc("greater_or_equal", "string"), ParamDoc("summon_location", "int"),
            ParamDoc("grave_filter", "function|nil"), ParamDoc("mat_filter", "function|nil"),
            ParamDoc("extra_target", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Target function for a configurable Ritual Summon effect.")],
        "description": ["Returns the target function for configurable Ritual Summon effects."],
    },
    "Auxiliary.SynCondition": {
        "params": [ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int")],
        "returns": [ReturnDoc("function", "Condition function for a basic Synchro Summon procedure.")],
        "description": ["Returns the condition function for basic Synchro Summon procedures."],
    },
    "Auxiliary.SynGroupCheckLevelAddition": {
        "params": [ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("function", "Group check for Synchro material Level pruning.")],
        "description": ["Returns a group check for Synchro material selection."],
    },
    "Auxiliary.SynLimitFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("f", "function|nil"), ParamDoc("e", "Effect"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("bool", "true if f rejects c.")],
        "description": ["Checks a Synchro material limit function."],
    },
    "Auxiliary.SynMaterialFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("bool", "true if c is usable Synchro Material.")],
        "description": ["Synchro Material filter."],
    },
    "Auxiliary.SynMixCheck": {
        "params": [
            ParamDoc("mg", "Group"), ParamDoc("sg1", "Group"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("syncard", "Card"), ParamDoc("mg1", "Group"),
            ParamDoc("smat", "Card|nil"), ParamDoc("gc", "function|nil"),
            ParamDoc("mgchk", "bool"), ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if the mixed Synchro Material selection can be completed.")],
        "description": ["Checks whether a mixed Synchro Material selection can be completed."],
    },
    "Auxiliary.SynMixCheckGoal": {
        "params": [
            ParamDoc("tp", "int"), ParamDoc("sg", "Group"), ParamDoc("minc", "int"),
            ParamDoc("ct", "int"), ParamDoc("syncard", "Card"), ParamDoc("sg1", "Group"),
            ParamDoc("smat", "Card|nil"), ParamDoc("gc", "function|nil"),
            ParamDoc("mgchk", "bool"), ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if sg plus sg1 is a valid mixed Synchro Material group.")],
        "description": ["Final mixed Synchro Material group check."],
    },
    "Auxiliary.SynMixCheckPrune": {
        "params": [ParamDoc("sg", "Group"), ParamDoc("sg1", "Group"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("bool", "true if the branch can be pruned by minimum Synchro Level total.")],
        "description": ["Pruning check for mixed Synchro searches."],
    },
    "Auxiliary.SynMixCheckRecursive": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("sg", "Group"),
            ParamDoc("mg", "Group"), ParamDoc("ct", "int"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("syncard", "Card"), ParamDoc("sg1", "Group"),
            ParamDoc("smat", "Card|nil"), ParamDoc("gc", "function|nil"),
            ParamDoc("mgchk", "bool"), ParamDoc("goalchk", "bool"), ParamDoc("fulltraversal", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if the recursive search can reach a valid group.")],
        "description": ["Recursive mixed Synchro Material search helper."],
    },
    "Auxiliary.SynMixCondition": {
        "params": [
            ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"),
            ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"),
            ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gc", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Condition function for a mixed Synchro Summon procedure.")],
        "description": ["Returns the condition function for mixed Synchro Summon procedures."],
    },
    "Auxiliary.SynMixFilter1": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"),
            ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("syncard", "Card"), ParamDoc("mg", "Group"),
            ParamDoc("smat", "Card|nil"), ParamDoc("gc", "function|nil"), ParamDoc("mgchk", "bool"),
            ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if c can fill the first fixed material slot.")],
        "description": ["First fixed-material candidate filter for mixed Synchro procedures."],
    },
    "Auxiliary.SynMixFilter2": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f2", "function|nil"), ParamDoc("f3", "function|nil"),
            ParamDoc("f4", "function|nil"), ParamDoc("minc", "int"), ParamDoc("maxc", "int"),
            ParamDoc("syncard", "Card"), ParamDoc("mg", "Group"), ParamDoc("smat", "Card|nil"),
            ParamDoc("c1", "Card"), ParamDoc("gc", "function|nil"), ParamDoc("mgchk", "bool"),
            ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if c can fill the second fixed material slot or advance selection.")],
        "description": ["Second fixed-material candidate filter for mixed Synchro procedures."],
    },
    "Auxiliary.SynMixFilter3": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"),
            ParamDoc("minc", "int"), ParamDoc("maxc", "int"), ParamDoc("syncard", "Card"),
            ParamDoc("mg", "Group"), ParamDoc("smat", "Card|nil"), ParamDoc("c1", "Card"),
            ParamDoc("c2", "Card"), ParamDoc("gc", "function|nil"), ParamDoc("mgchk", "bool"),
            ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if c can fill the third fixed material slot or advance selection.")],
        "description": ["Third fixed-material candidate filter for mixed Synchro procedures."],
    },
    "Auxiliary.SynMixFilter4": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("f4", "function|nil"), ParamDoc("minc", "int"),
            ParamDoc("maxc", "int"), ParamDoc("syncard", "Card"), ParamDoc("mg1", "Group"),
            ParamDoc("smat", "Card|nil"), ParamDoc("c1", "Card"), ParamDoc("c2", "Card|nil"),
            ParamDoc("c3", "Card|nil"), ParamDoc("gc", "function|nil"), ParamDoc("mgchk", "bool"),
            ParamDoc("goalchk", "bool"),
        ],
        "returns": [ReturnDoc("bool", "true if c can fill the variable material slot.")],
        "description": ["Variable-slot candidate filter for mixed Synchro procedures."],
    },
    "Auxiliary.SynMixHandCheck": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("bool", "true if hand Synchro Materials in g are legal.")],
        "description": ["Checks selected hand Synchro Materials."],
    },
    "Auxiliary.SynMixHandFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("tp", "int"), ParamDoc("syncard", "Card")],
        "returns": [ReturnDoc("bool", "true if c is a hand material enabled by another card.")],
        "description": ["Hand Synchro Material filter."],
    },
    "Auxiliary.SynMixOperation": {
        "params": [
            ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"),
            ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"),
            ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gc", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Operation function for a mixed Synchro Summon procedure.")],
        "description": ["Returns the operation function for mixed Synchro Summon procedures."],
    },
    "Auxiliary.SynMixTarget": {
        "params": [
            ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"),
            ParamDoc("f3", "function|nil"), ParamDoc("f4", "function|nil"),
            ParamDoc("minct", "int"), ParamDoc("maxct", "int"), ParamDoc("gc", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Target function for a mixed Synchro Summon procedure.")],
        "description": ["Returns the target function for mixed Synchro Summon procedures."],
    },
    "Auxiliary.SynOperation": {
        "params": [ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int")],
        "returns": [ReturnDoc("function", "Operation function for a basic Synchro Summon procedure.")],
        "description": ["Returns the operation function for basic Synchro Summon procedures."],
    },
    "Auxiliary.SynTarget": {
        "params": [ParamDoc("f1", "function|nil"), ParamDoc("f2", "function|nil"), ParamDoc("minct", "int"), ParamDoc("maxct", "int")],
        "returns": [ReturnDoc("function", "Target function for a basic Synchro Summon procedure.")],
        "description": ["Returns the target function for basic Synchro Summon procedures."],
    },
    "Auxiliary.TuneMagicianCheckAdditionalX": {
        "params": [ParamDoc("ecode", "int")],
        "returns": [ReturnDoc("function", "Group check that rejects invalid EFFECT_TUNE_MAGICIAN_* pairs.")],
        "description": ["Deprecated factory for Tune Magician additional checks."],
    },
    "Auxiliary.TuneMagicianCheckAdditionalXyz": {
        "params": [ParamDoc("g", "Group")],
        "returns": [ReturnDoc("bool", "true if g has no invalid EFFECT_TUNE_MAGICIAN_X pair.")],
        "description": ["Additional Xyz material group check for EFFECT_TUNE_MAGICIAN_X."],
    },
    "Auxiliary.Xyz2XMaterialEffectFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("xyzc", "Card"), ParamDoc("lv", "int"),
            ParamDoc("f", "function|nil"), ParamDoc("tp", "int"), ParamDoc("checked", "bool|nil"),
        ],
        "returns": [ReturnDoc("bool", "true if c has a valid EFFECT_DOUBLE_XMATERIAL effect.")],
        "description": ["Checks EFFECT_DOUBLE_XMATERIAL validity."],
    },
    "Auxiliary.Xyz2XMaterialFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("xyzc", "Card"), ParamDoc("lv", "int"), ParamDoc("f", "function|nil")],
        "returns": [ReturnDoc("bool", "true if c is valid Xyz Material for double-material handling.")],
        "description": ["Xyz Material filter for double-material handling."],
    },
    "Auxiliary.Xyz2XMaterialGoal": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("xyzc", "Card"), ParamDoc("minc", "int")],
        "returns": [ReturnDoc("bool", "true if g satisfies the double-material Xyz requirements.")],
        "description": ["Final group check for Xyz Summons using EFFECT_DOUBLE_XMATERIAL."],
    },
    "Auxiliary.Xyz2XMaterialOperation": {
        "params": [ParamDoc("tp", "int"), ParamDoc("mg", "Group"), ParamDoc("xyzc", "Card"), ParamDoc("minct", "int"), ParamDoc("maxct", "int")],
        "returns": [],
        "description": ["Consumes count limits for selected EFFECT_DOUBLE_XMATERIAL cards."],
    },
    "Auxiliary.XyzAlterFilter": {
        "params": [
            ParamDoc("c", "Card"), ParamDoc("alterf", "function"), ParamDoc("xyzc", "Card"),
            ParamDoc("e", "Effect"), ParamDoc("tp", "int"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("bool", "true if c is a valid alternate Xyz Material.")],
        "description": ["Alternate Xyz Summon candidate filter."],
    },
    "Auxiliary.XyzCondition": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("lv", "int"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Condition function for a standard Xyz Summon procedure.")],
        "description": ["Returns the condition function for standard Xyz Summon procedures."],
    },
    "Auxiliary.XyzLevelFreeCondition": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("gf", "function|nil"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Condition function for a Level-free Xyz Summon procedure.")],
        "description": ["Returns the condition function for Level-free Xyz Summon procedures."],
    },
    "Auxiliary.XyzLevelFreeFilter": {
        "params": [ParamDoc("c", "Card"), ParamDoc("xyzc", "Card"), ParamDoc("f", "function|nil")],
        "returns": [ReturnDoc("bool", "true if c is valid Level-free Xyz Material.")],
        "description": ["Level-free Xyz Material filter."],
    },
    "Auxiliary.XyzLevelFreeGoal": {
        "params": [ParamDoc("g", "Group"), ParamDoc("tp", "int"), ParamDoc("xyzc", "Card"), ParamDoc("gf", "function|nil")],
        "returns": [ReturnDoc("bool", "true if g satisfies the Level-free Xyz requirements.")],
        "description": ["Final group check for Level-free Xyz Summons."],
    },
    "Auxiliary.XyzLevelFreeOperation": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("gf", "function|nil"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Operation function for a Level-free Xyz Summon procedure.")],
        "description": ["Returns the operation function for Level-free Xyz Summon procedures."],
    },
    "Auxiliary.XyzLevelFreeTarget": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("gf", "function|nil"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Target function for a Level-free Xyz Summon procedure.")],
        "description": ["Returns the target function for Level-free Xyz Summon procedures."],
    },
    "Auxiliary.XyzOperation": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("lv", "int"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Operation function for a standard Xyz Summon procedure.")],
        "description": ["Returns the operation function for standard Xyz Summon procedures."],
    },
    "Auxiliary.XyzTarget": {
        "params": [
            ParamDoc("f", "function|nil"), ParamDoc("lv", "int"), ParamDoc("minct", "int"),
            ParamDoc("maxct", "int"), ParamDoc("alterf", "function|nil"),
            ParamDoc("alterdesc", "int|string|nil"), ParamDoc("alterop", "function|nil"),
        ],
        "returns": [ReturnDoc("function", "Target function for a standard Xyz Summon procedure.")],
        "description": ["Returns the target function for standard Xyz Summon procedures."],
    },
}

FINAL_IMPORTED_FUNCTION_EN_OVERRIDES = {
    "Auxiliary.AddFusionProcCode2FunRep": ["Registers a Fusion Material procedure requiring code1, code2, and between minc and maxc additional materials that satisfy f."],
    "Auxiliary.AddFusionProcMixRep": [
        "Registers a mixed Fusion Material procedure with one repeated slot and any number of fixed slots.",
        "fun1 is the repeated material requirement used minc to maxc times; additional arguments are fixed requirements. Each requirement may be a card code, filter function, or table of card codes and filters.",
    ],
    "Auxiliary.AddRitualProcEqual": ["Creates a Ritual Summon activation effect whose selected materials' Ritual Levels must exactly equal the Ritual Monster's original Level."],
    "Auxiliary.AddRitualProcEqual2Code2": ["Adds code1 and code2 to c's listed codes, then creates an equal-Level Ritual Summon procedure for Ritual Monsters with either code."],
    "Auxiliary.BecomeOriginalCode": ["Registers an EFFECT_CHANGE_CODE effect on c so its code becomes tc's original rule code until reset; reset defaults to standard event reset through the End Phase."],
    "Auxiliary.GetAdjacentGroup": ["Returns cards from location1/location2 that are orthogonally adjacent to the global field coordinate (i, j)."],
    "Auxiliary.GetFieldIndex": ["Returns c's global row and column indexes from player 0's field viewpoint."],
    "Auxiliary.xyzlimit": ["Special Summon condition helper that returns true only when st contains SUMMON_TYPE_XYZ."],
    "Card.ClearEffectRelation": ["Clears all effect relations currently stored on c."],
    "Card.GetBattledGroup": ["Returns the Group of cards that c has battled."],
    "Card.GetOriginalLeftScale": ["Returns c's printed left Pendulum Scale."],
    "Card.GetOriginalRightScale": ["Returns c's printed right Pendulum Scale."],
    "Card.GetPreviousRankOnField": ["Returns the Rank value c had while it was previously on the field."],
    "Card.GetRaceInGrave": ["Returns the Race c is treated as having in the GY for player, defaulting to the current reason player."],
    "Card.GetSynchroType": ["Returns c's Synchro Material Type mask used by Synchro Material checks."],
    "Card.IsFusionSummonableCard": ["Checks whether c can be Fusion Summoned as a Fusion Monster for summon type sum_type, defaulting to 0."],
    "Card.SetReason": ["Sets c's current reason bitmask to reason."],
    "Duel.ChangeAttacker": [
        "Changes the current attacking monster to attacker.",
        "Unless ignore_count is true, the new attacker gains an attack announcement count, and during the Damage Phase also gains attacked-count and attacked-card records.",
    ],
    "Duel.ChangeTargetParam": ["Changes target parameter data for Chain Link count to param."],
    "Duel.ChangeTargetPlayer": ["Changes the target player recorded for Chain Link count."],
    "Duel.ConfirmExtratop": ["Reveals count cards from the top of player's Extra Deck to the client, skipping face-up Pendulum cards tracked at the Extra Deck top."],
    "Duel.GetBattledCount": ["Returns how many battles player has conducted in the current Battle Phase tracking state."],
    "Duel.GetExtraTopGroup": ["Returns a Group containing up to count cards from the top of player's Extra Deck, after the face-up Pendulum section."],
    "Duel.IsPlayerCanSendtoDeck": ["Checks whether player can send cards to the Deck at all, or whether player can send c to the Deck."],
    "Duel.MajesticCopy": [
        "Copies monster initial effects from copy_target onto c until the End Phase.",
        "It copies chain-link monster effects, skips Xyz Material effects, converts mandatory trigger/quick effects to optional versions, and does not copy Spell/Trap effects.",
    ],
    "Duel.RockPaperScissors": ["Runs the Rock-Paper-Scissors selector and returns the winning player; repeat defaults to true."],
    "Duel.SetCoinResult": ["Sets the stored coin results in the core result slots; only 0 and 1 are preserved, and other values are stored as 0."],
    "Effect.CheckCountLimit": ["Checks whether e's count limit is still available for player p."],
    "Effect.GetActivateSequence": ["Returns the sequence where e was activated."],
    "Group.Equal": ["Checks whether g1 and g2 contain exactly the same cards in the same internal order."],
    "Group.SelectWithSumGreater": ["Lets player select a subset of g whose f-value sum reaches or exceeds sum according to the core's exact greater-sum selection rule; returns an empty Group if no valid subset exists."],
    "Auxiliary.AddFusionEffectProcUltimate": [
        "Creates the configurable Fusion Summon activation effect described by params.",
        "Missing material locations, material filters, material operations, Special Summon nocheck, and category fields are filled with the MDPro3 defaults. Unless params.reg is false, the effect is registered to c as an activation effect.",
    ],
    "Auxiliary.AddFusionProcCodeRep2": ["Registers a Fusion Material procedure requiring between minc and maxc copies of code1, with optional substitute and Instant Fusion handling."],
    "Auxiliary.AddRitualProcEqual2Code": ["Adds code1 to c's listed codes, then creates an equal-Level Ritual Summon procedure using the Ritual Monster's current Level."],
    "Auxiliary.AddRitualProcGreater": ["Creates a Ritual Summon activation effect whose selected materials' Ritual Levels must be greater than or equal to the Ritual Monster's original Level."],
    "Auxiliary.AdjacentFilter": ["Returns whether c's global field coordinate is directly adjacent to (i, j), sharing an edge rather than a diagonal."],
    "Auxiliary.BeginPuzzle": ["Sets up puzzle-duel handling by skipping player 0's Draw and Standby Phases and making player 0 lose at the End Phase."],
    "Auxiliary.DualNormalCondition": ["Gemini helper condition that returns true when the handler is face-up and not currently in Gemini treated-as-effect state."],
    "Auxiliary.GetLinkCount": ["Returns 1 plus the Link Rating shifted into the high word for Link Monsters with Link Rating greater than 1; otherwise returns 1."],
    "Auxiliary.GoldenAllureQueenFilter": ["Returns true for cards whose original set code is 0x3, used by Golden Allure Queen quick-effect handling."],
    "Auxiliary.IsNotDualState": ["Gemini helper condition that returns true when the effect is disabled or its handler is not in Gemini treated-as-effect state."],
    "Auxiliary.MustMaterialCounterFilter": ["Returns true when c is not contained in g; used to detect mandatory materials missing from a candidate material group."],
    "Auxiliary.OrcustratedBabelFilter": ["Returns true for original Orcust cards that are Link Monsters on the field or monsters in the GY."],
    "Auxiliary.TuneMagicianFilter": ["Calls the effect's value function as f(e, c) and returns that result."],
    "Card.GetAttackedGroup": ["Returns the Group of cards that c has attacked."],
    "Card.GetAttackedGroupCount": ["Returns the number of attack records stored for c."],
    "Card.GetFusionType": ["Returns c's Fusion Material Type mask used by Fusion Material checks."],
    "Card.GetLinkType": ["Returns c's Link Material Type mask used by Link Material checks."],
    "Card.GetMutualLinkedZone": ["Returns the zone mask of c's mutually linked zones, swapped to player viewpoint when a player argument opposite c's controller is supplied."],
    "Card.GetOverlayTarget": ["Returns the card that c is attached to as an Xyz Material, or nil when c is not attached."],
    "Card.GetOwnerTarget": ["Returns the Group of cards that are targeting c as their persistent card-target owner."],
    "Card.GetOwnerTargetCount": ["Returns the number of cards targeting c as their persistent card-target owner."],
    "Card.GetTunerLimit": ["Returns the tuner-material-limit effect affecting c, that effect's target function or nil, its value or nil, and the allowed minimum and maximum counts; if no such effect applies, no values are returned."],
    "Card.GetXyzType": ["Returns c's Xyz Material Type mask used by Xyz Material checks."],
    "Card.IsAllColumn": ["Checks whether c is treated as occupying or applying to all columns."],
    "Card.IsCanBeBattleTarget": ["Checks whether c1 can be chosen as a battle target by c2."],
    "Card.IsDirectAttacked": ["Checks whether c has a direct-attack record."],
    "Card.IsExtraLinkState": ["Checks whether c is part of an Extra Link state."],
    "Card.IsSpecialSummonable": ["Checks whether c can be Special Summoned by player under sum_type, defaulting to 0 and using the current reason player."],
    "Card.ReleaseRelation": ["Releases c1's relation to card c2."],
    "Card.ResetNegateEffect": ["Resets negate-related card effects on c for each supplied reset code."],
    "Debug.AddCard": ["Creates a card with code and places it in the requested test field location, or attaches it as Xyz Material if an occupied Monster Zone contains an Xyz Monster; proc marks its procedure complete."],
    "Debug.Message": ["Sends tostring(msg) to the local debug message handler."],
    "Debug.PreAddCounter": ["Adds count counters of countertype directly to c for field setup; count defaults to 1."],
    "Debug.PreEquip": ["Pre-equips equip_card to target during field setup and returns whether the relationship was created."],
    "Debug.PreSetTarget": ["Adds target as a persistent card target of c during field setup."],
    "Debug.PreSummon": ["Sets c's stored summon information to summon_type plus optional summon_location in the high word."],
    "Debug.ReloadFieldBegin": ["Clears the duel and starts a field reload with duel option flag and optional rule; when rule is omitted, obsolete ruling flags choose rule 1, otherwise the current rule is used."],
    "Debug.ReloadFieldEnd": ["Finishes a field reload by disabling pending shuffle checks and rebuilding field information."],
    "Debug.SetAIName": ["Writes the local AI name message, truncated to the core AI-name buffer size."],
    "Debug.ShowHint": ["Writes tostring(msg) as a local show-hint message, truncated to the core hint buffer size."],
    "Duel.Activate": ["Queues e to be activated by the core activation processor."],
    "Duel.CheckSummonedCount": ["Checks whether the current reason player has a Normal Summon/Set count available, or whether c provides an extra summon-count effect."],
    "Duel.CheckSynchroMaterial": ["Checks whether scard has a legal Synchro Material selection with optional tuner/non-tuner filters, count limits, required Synchro Material, and material group."],
    "Duel.CheckTiming": ["Checks whether timing is present in either player's current hint timing mask."],
    "Duel.CheckTunerMaterial": ["Checks whether tuner can be used with scard under the supplied tuner/non-tuner filters, count limits, and optional material group."],
    "Duel.CheckXyzMaterial": ["Checks whether scard has a legal Xyz Material selection for Level lv, material count range, optional filter, and optional material group."],
    "Duel.GetChainEvent": ["Returns the event group, event player, event value, reason effect, reason, and reason player stored on Chain Link count."],
    "Duel.GetLinkedGroupCount": ["Returns the number of cards linked to player-relative locations s and o."],
    "Duel.GetTributeCount": ["Returns the number of available Tribute candidates for target, optionally restricted to mg and extra handling."],
    "Duel.GetTributeGroup": ["Returns the Group of cards that can be Tributed for a Normal Summon/Set of target."],
    "Duel.GrabSelectedCard": ["Returns the current must-select cards as a Group and clears the core must-select list."],
    "Duel.IncreaseSummonedCount": ["Consumes the current reason player's Normal Summon/Set count, or invokes c's extra summon-count effect when present."],
    "Duel.IsPlayerCanFlipSummon": ["Checks whether player can Flip Summon at all, or whether player can Flip Summon c."],
    "Duel.IsPlayerCanMSet": ["Checks whether player can Set monsters at all, or whether player can Set c with summon type sumtype."],
    "Duel.IsPlayerCanSendtoHand": ["Checks whether player can send cards to the hand at all, or whether player can send c to the hand."],
    "Duel.IsSummonCancelable": ["Returns the core summon-cancelable flag for the current Summon selection."],
    "Duel.SelectSequence": ["No-op stub in this core; it only checks action permission and returns no values."],
    "Duel.SelectTunerMaterial": ["Lets player select Synchro Materials for scard using the fixed tuner, optional filters, count limits, and optional material group."],
    "Duel.SelectXyzMaterial": ["Lets player select Xyz Materials for scard for Level lv and material count range, with optional filter and material group."],
    "Duel.SpecialSummonRule": ["Performs a rule Special Summon of c for player with optional summon type sumtype, unless the core is in effect damage step processing."],
    "Effect.GetRange": ["Returns e's range bitmask."],
    "Effect.GlobalEffect": ["Creates a new effect owned by the duel temporary card with effect owner player 0."],
    "Group.__add": ["Returns a new Group containing cards from both operands, where each operand may be a Card or Group."],
    "Group.__band": ["Returns a new Group containing cards present in both operands."],
    "Group.__bor": ["Returns a new Group containing cards from both operands; this uses the same core handler as Group.__add."],
    "Group.__bxor": ["Returns a new Group containing cards present in exactly one operand."],
    "Group.__len": ["Returns the number of cards in g."],
    "Group.__sub": ["Returns a new Group containing cards from the left operand that are not in the right operand."],
    "Group.ForEach": ["Utility stub for calling f once for each card in g with any extra arguments."],
    "Group.GetBinClassCount": ["Calls f for each card in g, ORs the returned integer values together, and returns the number of set bits in the result."],
    "Group.SearchCard": ["Returns the first card in g that satisfies f with any extra arguments, or nil if none does."],
}

FINAL_IMPORTED_FUNCTION_ZH_OVERRIDES = {
    "Auxiliary.AddFusionProcCode2FunRep": ["登记融合素材手续，要求code1、code2，以及minc到maxc张满足f的额外素材。"],
    "Auxiliary.AddFusionProcMixRep": [
        "登记混合融合素材手续，包含一个重复素材槽和任意数量的固定素材槽。",
        "fun1是重复使用minc到maxc次的素材要求；后续参数是固定要求。每个要求可以是卡号、筛选函数，或由卡号和筛选函数组成的表。",
    ],
    "Auxiliary.AddRitualProcEqual": ["创建仪式召唤发动效果，所选素材的仪式等级合计必须正好等于仪式怪兽的原本等级。"],
    "Auxiliary.AddRitualProcEqual2Code2": ["把code1和code2加入c的列名卡号，然后为卡号为其中之一的仪式怪兽创建等等级仪式召唤手续。"],
    "Auxiliary.BecomeOriginalCode": ["给c登记EFFECT_CHANGE_CODE效果，使其卡号变为tc按规则使用的原本卡号直到reset；reset默认持续到结束阶段并使用标准事件重置。"],
    "Auxiliary.GetAdjacentGroup": ["返回location1/location2中与全局场地坐标(i, j)正交相邻的卡。"],
    "Auxiliary.GetFieldIndex": ["从玩家0的场地视角返回c的全局行号和列号。"],
    "Auxiliary.xyzlimit": ["特殊召唤条件辅助函数：仅当st包含SUMMON_TYPE_XYZ时返回true。"],
    "Card.ClearEffectRelation": ["清除c当前保存的全部效果关系。"],
    "Card.GetBattledGroup": ["返回c已经战斗过的卡组成的Group。"],
    "Card.GetOriginalLeftScale": ["返回c记载的左灵摆刻度。"],
    "Card.GetOriginalRightScale": ["返回c记载的右灵摆刻度。"],
    "Card.GetPreviousRankOnField": ["返回c先前在场上时的阶级值。"],
    "Card.GetRaceInGrave": ["返回c在墓地中对player视为具有的种族；player省略时使用当前原因玩家。"],
    "Card.GetSynchroType": ["返回c用于同调素材检查的同调素材种类位掩码。"],
    "Card.IsFusionSummonableCard": ["检查c能否作为融合怪兽用召唤类型sum_type进行融合召唤；sum_type默认0。"],
    "Card.SetReason": ["把c当前的原因位掩码设为reason。"],
    "Duel.ChangeAttacker": [
        "把当前攻击怪兽改为attacker。",
        "除非ignore_count为true，否则新的攻击怪兽会增加攻击宣言次数；在伤害阶段中还会记录已攻击次数和已攻击卡。",
    ],
    "Duel.ChangeTargetParam": ["把连锁环count记录的对象参数改为param。"],
    "Duel.ChangeTargetPlayer": ["改变连锁环count记录的对象玩家。"],
    "Duel.ConfirmExtratop": ["向客户端公开player额外卡组最上方count张卡，会跳过额外卡组顶端记录的表侧灵摆卡部分。"],
    "Duel.GetBattledCount": ["返回player在当前战斗阶段记录状态中的战斗次数。"],
    "Duel.GetExtraTopGroup": ["返回player额外卡组最上方至多count张卡组成的Group，起点在表侧灵摆卡部分之后。"],
    "Duel.IsPlayerCanSendtoDeck": ["检查player是否能把卡送去Deck，或检查player能否把c送去Deck。"],
    "Duel.MajesticCopy": [
        "把copy_target的怪兽initial_effect复制给c，持续到结束阶段。",
        "它复制连锁环怪兽效果，跳过超量素材效果，把强制诱发/快速效果改成任意发动版本，并且不复制魔法/陷阱效果。",
    ],
    "Duel.RockPaperScissors": ["执行猜拳选择并返回胜方玩家；repeat默认true。"],
    "Duel.SetCoinResult": ["设置核心保存的硬币结果槽；只有0和1会保留，其他值会按0保存。"],
    "Effect.CheckCountLimit": ["检查效果e对玩家p是否仍有可用次数。"],
    "Effect.GetActivateSequence": ["返回效果e发动时所在的位置序号。"],
    "Group.Equal": ["检查g1和g2是否以相同内部顺序包含完全相同的卡。"],
    "Group.SelectWithSumGreater": ["让player从g中选择一个子集，使f的取值合计按核心的精确大于等于规则达到sum；没有合法子集时返回空Group。"],
    "Auxiliary.AddFusionEffectProcUltimate": [
        "创建由params描述的可配置融合召唤发动效果。",
        "缺省的素材位置、素材筛选、素材操作、特殊召唤nocheck和Category字段会填入MDPro3默认值。除非params.reg为false，否则该效果会作为发动效果登记给c。",
    ],
    "Auxiliary.AddFusionProcCodeRep2": ["登记融合素材手续，要求minc到maxc张code1，并带有可选代用素材和Instant Fusion处理。"],
    "Auxiliary.AddRitualProcEqual2Code": ["把code1加入c的列名卡号，然后使用仪式怪兽当前等级创建等等级仪式召唤手续。"],
    "Auxiliary.AddRitualProcGreater": ["创建仪式召唤发动效果，所选素材的仪式等级合计必须大于等于仪式怪兽的原本等级。"],
    "Auxiliary.AdjacentFilter": ["检查c的全局场地坐标是否与(i, j)直接相邻；只计算上下左右，不计算斜向。"],
    "Auxiliary.BeginPuzzle": ["设置解谜决斗处理：跳过玩家0的抽卡阶段和准备阶段，并在结束阶段让玩家0失败。"],
    "Auxiliary.DualNormalCondition": ["二重辅助条件：处理对象表侧表示且当前不处于二重怪兽视为效果怪兽的状态时返回true。"],
    "Auxiliary.GetLinkCount": ["连接怪兽且连接值大于1时，返回1加上连接值左移到高16位后的值；其他情况返回1。"],
    "Auxiliary.GoldenAllureQueenFilter": ["检查c的原本系列代码是否为0x3，供Golden Allure Queen快速效果处理使用。"],
    "Auxiliary.IsNotDualState": ["二重辅助条件：效果被无效，或处理对象不处于二重怪兽视为效果怪兽状态时返回true。"],
    "Auxiliary.MustMaterialCounterFilter": ["c不包含在g中时返回true，用于检查候选素材组是否漏掉必须素材。"],
    "Auxiliary.OrcustratedBabelFilter": ["检查原本为Orcust系列的卡是否是在场上的连接怪兽，或在墓地的怪兽。"],
    "Auxiliary.TuneMagicianFilter": ["取得效果e的Value函数并以f(e, c)调用，返回该结果。"],
    "Card.GetAttackedGroup": ["返回c攻击过的卡组成的Group。"],
    "Card.GetAttackedGroupCount": ["返回c保存的攻击记录数量。"],
    "Card.GetFusionType": ["返回c用于融合素材检查的融合素材种类位掩码。"],
    "Card.GetLinkType": ["返回c用于连接素材检查的连接素材种类位掩码。"],
    "Card.GetMutualLinkedZone": ["返回c互相连接的区域位掩码；提供与c控制者相对的player参数时，会交换为该玩家视角。"],
    "Card.GetOverlayTarget": ["返回c作为超量素材叠放到的卡；c未作为素材叠放时返回nil。"],
    "Card.GetOwnerTarget": ["返回把c作为持续卡片对象拥有者的卡组成的Group。"],
    "Card.GetOwnerTargetCount": ["返回把c作为持续卡片对象拥有者的卡数量。"],
    "Card.GetTunerLimit": ["返回影响c的调整素材限制效果、该效果的Target函数或nil、Value或nil，以及允许的最小和最大数量；没有该效果时不返回值。"],
    "Card.GetXyzType": ["返回c用于超量素材检查的超量素材种类位掩码。"],
    "Card.IsAllColumn": ["检查c是否被视为占用或适用于全部纵列。"],
    "Card.IsCanBeBattleTarget": ["检查c1能否被c2选择为攻击对象。"],
    "Card.IsDirectAttacked": ["检查c是否保存有直接攻击记录。"],
    "Card.IsExtraLinkState": ["检查c是否处于额外连接状态。"],
    "Card.IsSpecialSummonable": ["检查c能否由当前原因玩家以sum_type特殊召唤；sum_type默认0。"],
    "Card.ReleaseRelation": ["解除c1与卡c2之间的关系。"],
    "Card.ResetNegateEffect": ["按每个给定的重置代码重置c上相关的无效效果。"],
    "Debug.AddCard": ["创建卡号code的卡并放到指定测试场地位置；如果目标怪兽区域已被超量怪兽占用，则作为超量素材叠放；proc会标记正规手续完成。"],
    "Debug.Message": ["把tostring(msg)发送到本地调试消息处理。"],
    "Debug.PreAddCounter": ["在场地设置阶段直接给c添加count个countertype指示物；count默认1。"],
    "Debug.PreEquip": ["在场地设置阶段预先把equip_card装备给target，并返回是否建立成功。"],
    "Debug.PreSetTarget": ["在场地设置阶段把target加入c的持续卡片对象。"],
    "Debug.PreSummon": ["把c保存的召唤信息设为summon_type，并可把summon_location写入高16位。"],
    "Debug.ReloadFieldBegin": ["清空决斗并用决斗选项flag和可选rule开始重新载入场地；省略rule时，旧规则标志会使用规则1，否则使用当前规则。"],
    "Debug.ReloadFieldEnd": ["结束重新载入场地：关闭待处理洗切检查并重建场地信息。"],
    "Debug.SetAIName": ["写入本地AI名称消息，长度会按核心AI名称缓冲区截断。"],
    "Debug.ShowHint": ["把tostring(msg)写成本地显示提示消息，长度会按核心提示缓冲区截断。"],
    "Duel.Activate": ["把效果e加入核心发动处理队列。"],
    "Duel.CheckSummonedCount": ["检查当前原因玩家是否还有通常召唤/盖放次数，或c是否提供额外召唤次数效果。"],
    "Duel.CheckSynchroMaterial": ["检查scard是否存在合法的同调素材选择，可带调整/非调整筛选、数量限制、指定同调素材和素材Group。"],
    "Duel.CheckTiming": ["检查timing是否存在于任一玩家当前的hint timing掩码中。"],
    "Duel.CheckTunerMaterial": ["检查tuner能否在给定调整/非调整筛选、数量限制和可选素材Group下与scard一起使用。"],
    "Duel.CheckXyzMaterial": ["检查scard是否存在合法的超量素材选择，使用等级lv、素材数量范围、可选筛选函数和可选素材Group。"],
    "Duel.GetChainEvent": ["返回连锁环count保存的事件Group、事件玩家、事件数值、原因效果、原因和原因玩家。"],
    "Duel.GetLinkedGroupCount": ["返回与player视角位置s和o连接的卡数量。"],
    "Duel.GetTributeCount": ["返回target可用的祭品候选数量，可选用mg和额外处理限制。"],
    "Duel.GetTributeGroup": ["返回可为target通常召唤/盖放而解放的卡组成的Group。"],
    "Duel.GrabSelectedCard": ["把当前必须选择的卡作为Group返回，并清空核心必须选择列表。"],
    "Duel.IncreaseSummonedCount": ["消耗当前原因玩家的通常召唤/盖放次数；若c存在额外召唤次数效果，则调用该效果。"],
    "Duel.IsPlayerCanFlipSummon": ["检查player是否能进行反转召唤，或检查player能否反转召唤c。"],
    "Duel.IsPlayerCanMSet": ["检查player是否能盖放怪兽，或检查player能否以召唤类型sumtype盖放c。"],
    "Duel.IsPlayerCanSendtoHand": ["检查player是否能把卡送去手牌，或检查player能否把c送去手牌。"],
    "Duel.IsSummonCancelable": ["返回当前召唤选择的核心可取消标志。"],
    "Duel.SelectSequence": ["此核心中的空操作存根；只检查动作权限，不返回值。"],
    "Duel.SelectTunerMaterial": ["让player以固定tuner、可选筛选、数量限制和可选素材Group为scard选择同调素材。"],
    "Duel.SelectXyzMaterial": ["让player为scard选择等级lv和素材数量范围对应的超量素材，可带可选筛选函数和素材Group。"],
    "Duel.SpecialSummonRule": ["为player按规则特殊召唤c，可带召唤类型sumtype；核心处于效果伤害步骤处理时不会执行。"],
    "Effect.GetRange": ["返回效果e的Range位掩码。"],
    "Effect.GlobalEffect": ["创建一个由决斗临时卡拥有、效果拥有者为玩家0的新效果。"],
    "Group.__add": ["返回包含两个操作数中卡的新Group；每个操作数都可以是Card或Group。"],
    "Group.__band": ["返回同时存在于两个操作数中的卡组成的新Group。"],
    "Group.__bor": ["返回包含两个操作数中卡的新Group；它与Group.__add使用同一个核心处理。"],
    "Group.__bxor": ["返回只存在于其中一个操作数中的卡组成的新Group。"],
    "Group.__len": ["返回g中的卡片数量。"],
    "Group.__sub": ["返回左操作数中有、右操作数中没有的卡组成的新Group。"],
    "Group.ForEach": ["工具存根：对g中的每张卡以任意额外参数调用一次f。"],
    "Group.GetBinClassCount": ["对g中的每张卡调用f，把返回的整数值按位或合并，然后返回结果中置位的数量。"],
    "Group.SearchCard": ["返回g中第一张满足f和额外参数的卡；没有则返回nil。"],
}

FUNCTION_EN_OVERRIDES.update(FINAL_IMPORTED_FUNCTION_EN_OVERRIDES)
FUNCTION_ZH_OVERRIDES.update(FINAL_IMPORTED_FUNCTION_ZH_OVERRIDES)
CORE_DOC_OVERRIDES.update({
    "Card.GetTunerLimit": {
        "params": [ParamDoc("c", "Card")],
        "returns": [
            ReturnDoc("Effect", "The tuner-material-limit effect."),
            ReturnDoc("function|nil", "The effect target function, if any."),
            ReturnDoc("int|nil", "The effect value, if any."),
            ReturnDoc("int", "Minimum allowed material count."),
            ReturnDoc("int", "Maximum allowed material count."),
        ],
        "description": ["Returns tuner material limit information, or no values if no limit applies."],
        "description_zh": ["返回调整素材限制信息；没有限制时不返回值。"],
    },
    "Duel.GetChainEvent": {
        "params": [ParamDoc("count", "int")],
        "returns": [
            ReturnDoc("Group", "Event cards."),
            ReturnDoc("int", "Event player."),
            ReturnDoc("int", "Event value."),
            ReturnDoc("Effect", "Reason effect."),
            ReturnDoc("int", "Reason flags."),
            ReturnDoc("int", "Reason player."),
        ],
        "description": ["Returns event data stored on a Chain Link."],
        "description_zh": ["返回连锁环保存的事件数据。"],
    },
    "Duel.RockPaperScissors": {
        "params": [ParamDoc("repeat", "bool", True, "default: true")],
        "returns": [ReturnDoc("int", "Winning player.")],
        "description": ["Runs Rock-Paper-Scissors."],
        "description_zh": ["执行猜拳。"],
    },
    "Duel.SpecialSummonRule": {
        "params": [ParamDoc("player", "int"), ParamDoc("c", "Card"), ParamDoc("sumtype", "int", True, "default: 0")],
        "returns": [],
        "description": ["Performs a rule Special Summon."],
        "description_zh": ["执行规则特殊召唤。"],
    },
    "Duel.SelectSequence": {
        "params": [],
        "returns": [],
        "description": ["No-op stub in this core."],
        "description_zh": ["此核心中的空操作存根。"],
    },
    "Effect.GlobalEffect": {
        "params": [],
        "returns": [ReturnDoc("Effect")],
        "description": ["Creates a global Effect object."],
        "description_zh": ["创建全局Effect对象。"],
    },
    "Debug.AddCard": {
        "params": [
            ParamDoc("code", "int"),
            ParamDoc("owner", "int"),
            ParamDoc("player", "int"),
            ParamDoc("location", "int"),
            ParamDoc("seq", "int"),
            ParamDoc("pos", "int"),
            ParamDoc("proc", "bool", True),
        ],
        "returns": [ReturnDoc("Card|nil")],
        "description": ["Adds a card to the debug field."],
        "description_zh": ["向调试场地加入卡。"],
    },
    "Debug.ReloadFieldBegin": {
        "params": [ParamDoc("flag", "int"), ParamDoc("rule", "int", True)],
        "returns": [],
        "description": ["Begins debug field reload."],
        "description_zh": ["开始调试场地重新载入。"],
    },
})


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
            "- `MySyntaxHighlighter.cs` also hardcodes many function names, so editor highlighting will remain stale until it is changed to read generated data.",
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
