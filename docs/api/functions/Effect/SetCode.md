---
pageClass: effect-setcode-page
outline: [2, 4]
---

# Effect.SetCode

## Signature

```lua
Effect.SetCode(Effect e, int code) -> void
```

## Description

Stores the engine code for e. Depending on the effect type, this is an EVENT_* timing, an EFFECT_* rule or procedure, or a composed/custom code. It is unrelated to a card's archetype setcode.

## How To Use It

`Effect.SetCode` is **not** related to a card's archetype setcode. The separate **Archetypes and Setcodes** Learn page documents card membership. This function stores the engine code that identifies what an `Effect` listens for or what rule it applies.

The core stores the supplied integer directly. Its meaning comes from the effect's `SetType`:

| Effect shape | `SetCode` family | Purpose |
| --- | --- | --- |
| Spell/Trap activation (`EFFECT_TYPE_ACTIVATE`) | Usually `EVENT_FREE_CHAIN`, or a specific `EVENT_*` | Chooses the activation window. |
| Trigger or Quick effect | `EVENT_*`, a composed phase/counter event, or a custom event | Chooses the event that can wake the effect. |
| Event-watching Continuous effect | A continuous-only `EVENT_*` | Runs an operation immediately when that engine event is processed. |
| Single, Field, Equip, Xyz-material, or Grant rule | `EFFECT_*` | Chooses the rule, modifier, restriction, procedure, or replacement being applied. |
| Ignition effect | Usually no code | Ignition effects are selected by the player during an open Main Phase; `SetRange` and callbacks normally define them. |
| Flip Effect | `EVENT_FLIP` is assigned by `SetType` | The core normalizes `EFFECT_TYPE_FLIP` and overwrites the code with `EVENT_FLIP`. |

Call `SetType` before `SetCode`, especially for Flip Effects, and finish setting the code before `RegisterEffect`. Registration indexes the effect under its current code; changing the code afterward does not reindex it.

`EFFECT_TYPE_CONTINUOUS` means an event-processing action with an `Operation` callback. An ordinary persistent ATK modifier, summon restriction, material rule, or player rule normally uses `EFFECT_TYPE_SINGLE`, `EFFECT_TYPE_FIELD`, `EFFECT_TYPE_EQUIP`, or another non-action type instead.

A normal optional trigger listens for an event:

```lua
e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
e1:SetCode(EVENT_SUMMON_SUCCESS)
```

A rule effect uses an `EFFECT_*` code instead:

```lua
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
```

`EVENT_ADJUST` is a special continuous-only event. It is used when a script must reconcile state after the core finishes an adjustment pass, such as maintaining a card group, repairing a derived rule, or checking an unusual win condition:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
e1:SetCode(EVENT_ADJUST)
e1:SetRange(LOCATION_MZONE)
e1:SetOperation(s.adjustop)
c:RegisterEffect(e1)
```

An adjust operation can run many times. Make it idempotent: inspect current state and change only what is actually wrong. Do not use `EVENT_ADJUST` as a substitute for a known summon, movement, chain, or phase event.

The core reserves these event codes for `EFFECT_TYPE_CONTINUOUS`: `EVENT_ADJUST`, `EVENT_BREAK_EFFECT`, `EVENT_TURN_END`, `EVENT_PRE_BATTLE_DAMAGE`, `EVENT_SPSUMMON_SUCCESS_G_P`, and every `EVENT_PHASE_START+PHASE_*` code. The core rejects a Trigger or Quick effect registered with one of those codes.

Phase-end triggers compose the event base and phase:

```lua
e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
e2:SetCode(EVENT_PHASE+PHASE_END)
e2:SetRange(LOCATION_GRAVE)
e2:SetCondition(s.epcon)
e2:SetOperation(s.epop)
c:RegisterEffect(e2)
```

Custom events require a listener and a matching raise call. Use the same stable code on both sides:

```lua
local custom_code=EVENT_CUSTOM+id

e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
e3:SetCode(custom_code)
e3:SetRange(LOCATION_MZONE)
e3:SetOperation(s.customop)
c:RegisterEffect(e3)

-- In the operation that creates the custom event:
Duel.RaiseSingleEvent(c,custom_code,e,REASON_EFFECT,tp,tp,0)
```

Choose the code family first, then add the callbacks required by that specific code. `SetCode` alone does not supply a target range, value, condition, cost, target, or operation.

## Complete Code Reference

`SetCode` accepts a 32-bit integer, so there is no finite list of every possible custom number. The current engine snapshot defines **342 named code bases** for this parameter: **76 `EVENT_*` bases**, **265 ordinary `EFFECT_*` codes**, and **1 card-ID flag base**.

The local script snapshot contains **34,714 direct `SetCode` calls** using **447 distinct written expressions**. The tables below list every named engine code. **Direct uses** counts only expressions that spell that constant explicitly; a variable such as `custom_code` cannot be assigned to a base constant reliably by static text scanning.

### Codes that are built from a base

| Need | Correct shape | Effect type |
| --- | --- | --- |
| End of a phase | `EVENT_PHASE+PHASE_*` | Trigger/Quick, or an activation effect when appropriate |
| Start of a phase | `EVENT_PHASE_START+PHASE_*` | `EFFECT_TYPE_CONTINUOUS` |
| A counter is added/removed | `EVENT_ADD_COUNTER+counter_type` / `EVENT_REMOVE_COUNTER+counter_type` | Trigger/Quick |
| A script-defined event | `EVENT_CUSTOM+stable_unique_id` | Trigger/Quick; another operation must raise the exact same code |
| Counter permission/limit/replacement | `EFFECT_COUNTER_PERMIT+counter_type`, `EFFECT_COUNTER_LIMIT+counter_type`, or `EFFECT_RCOUNTER_REPLACE+counter_type` | Rule effect |
| A card-ID flag-style code | `EFFECT_FLAG_EFFECT+card_id` | Rule/flag effect; usually created through flag-effect helpers |
| A private marker on a non-action rule effect | A raw card ID | Only when other scripts deliberately query that same ID with `IsHasEffect`/`IsAffectedByEffect` |

Do not combine unrelated ordinary `EVENT_*` values or unrelated `EFFECT_*` values. The `+` forms above work because the high bits identify a code family and the low bits carry a phase, counter type, or custom ID.

Valid phase-end forms are `EVENT_PHASE+PHASE_DRAW`, `+PHASE_STANDBY`, `+PHASE_BATTLE_START`, `+PHASE_BATTLE`, and `+PHASE_END`. Valid continuous phase-start forms use `EVENT_PHASE_START` with `PHASE_DRAW`, `PHASE_STANDBY`, `PHASE_MAIN1`, `PHASE_BATTLE_START`, `PHASE_MAIN2`, or `PHASE_END`.

### Values that are not general `SetCode` arguments

- `EFFECT_TYPE_*`, `EFFECT_FLAG_*`, `CATEGORY_*`, `RESET_*`, `SUMMON_TYPE_*`, and a bare `PHASE_*` belong to other APIs. They are not interchangeable with event/effect codes.
- An Ignition effect normally omits `SetCode`; writing `SetCode(0)` adds no useful meaning.
- Do not copy the legacy `SetCode(RESET_CHAIN)` pattern. `RESET_CHAIN` is a reset mask, not an effect code.
- A raw card ID is only an intentional private marker for a non-action rule effect. For a script-raised action event, use `EVENT_CUSTOM+id` on both the listener and raise call.
- `SetCode(0x182)` does not give a card archetype membership. For that rule, use `SetCode(EFFECT_ADD_SETCODE)` with `SetValue(0x182)`.

### Every event code

For `EFFECT_TYPE_SINGLE`, an ordinary event generally concerns the handler itself. For `EFFECT_TYPE_FIELD`, it can observe matching events elsewhere, subject to range, condition, and property rules. Continuous-only events are called out explicitly.

#### Engine, movement, and Chain events

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EVENT_STARTUP` | `1000` | Legacy/reserved local constant that is absent from the current core snapshot. No indexed card script registers it directly. | 0 |
| `EVENT_FLIP` | `1001` | When flipped | 111 |
| `EVENT_FREE_CHAIN` | `1002` | Open activation timing rather than a past occurrence. Common for Spell/Trap activations and optional Quick Effects. | 5786 |
| `EVENT_DESTROY` | `1010` | Before a confirmed destroyed card moves | 8 |
| `EVENT_REMOVE` | `1011` | When banished | 192 |
| `EVENT_TO_HAND` | `1012` | When added to hand | 101 |
| `EVENT_TO_DECK` | `1013` | When returned to Deck | 25 |
| `EVENT_TO_GRAVE` | `1014` | When sent to Graveyard (excluding REASON_RETURN) | 1278 |
| `EVENT_LEAVE_FIELD` | `1015` | When leaving the field | 323 |
| `EVENT_CHANGE_POS` | `1016` | When position changes | 58 |
| `EVENT_RELEASE` | `1017` | When Tributed | 91 |
| `EVENT_DISCARD` | `1018` | When discarding from hand | 14 |
| `EVENT_LEAVE_FIELD_P` | `1019` | Before a card leaving the field moves | 66 |
| `EVENT_CHAIN_SOLVING` | `1020` | When chain resolution starts (after EVENT_CHAIN_ACTIVATING) | 148 |
| `EVENT_CHAIN_ACTIVATING` | `1021` | When chain activation is preparing | 0 |
| `EVENT_CHAIN_SOLVED` | `1022` | When chain resolution ends | 107 |
| `EVENT_CHAIN_ACTIVATED` | `1023` | Legacy/reserved local constant that is absent from the current core snapshot. No indexed card script registers it directly. | 0 |
| `EVENT_CHAIN_NEGATED` | `1024` | When chain activation is negated (after EVENT_CHAIN_ACTIVATING) | 27 |
| `EVENT_CHAIN_DISABLED` | `1025` | When chain effect is negated | 54 |
| `EVENT_CHAIN_END` | `1026` | When chain ends | 45 |
| `EVENT_CHAINING` | `1027` | When an effect is activated | 1028 |
| `EVENT_BECOME_TARGET` | `1028` | When becoming an effect target | 26 |
| `EVENT_DESTROYED` | `1029` | When destroyed | 647 |
| `EVENT_MOVE` | `1030` | When moving a card (e.g., Urgent Rabbit Horse) | 37 |
| `EVENT_LEAVE_GRAVE` | `1031` | When leaving the Graveyard | 6 |
| `EVENT_LEAVE_DECK` | `1032` | When leaving the Deck or Extra Deck | 3 |
| `EVENT_ADJUST` | `1040` | Continuous-only. Runs after the core completes an adjustment pass; use for idempotent state reconciliation or unusual win checks. | 23 |
| `EVENT_BREAK_EFFECT` | `1050` | Continuous-only. Runs when `Duel.BreakEffect()` creates a visible resolution break. | 25 |

#### Summon, material, damage, and control events

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EVENT_SUMMON_SUCCESS` | `1100` | When Normal Summon succeeds | 1382 |
| `EVENT_FLIP_SUMMON_SUCCESS` | `1101` | When Flip Summon succeeds | 165 |
| `EVENT_SPSUMMON_SUCCESS` | `1102` | When Special Summon succeeds | 2451 |
| `EVENT_SUMMON` | `1103` | During Normal Summon (before monster appears, e.g., Solemn Warning timing) | 25 |
| `EVENT_FLIP_SUMMON` | `1104` | During Flip Summon | 16 |
| `EVENT_SPSUMMON` | `1105` | During Special Summon | 51 |
| `EVENT_MSET` | `1106` | When Setting a monster | 17 |
| `EVENT_SSET` | `1107` | When Setting a Spell/Trap | 16 |
| `EVENT_BE_MATERIAL` | `1108` | When used as Synchro/Xyz/Link Material, used as Ritual/Fusion Material, or Tributed for a Tribute Summon | 241 |
| `EVENT_BE_PRE_MATERIAL` | `1109` | When about to be used as Synchro/Xyz/Link Material or Tributed for a Tribute Summon | 6 |
| `EVENT_DRAW` | `1110` | When drawing | 59 |
| `EVENT_DAMAGE` | `1111` | When dealing battle/effect damage | 74 |
| `EVENT_RECOVER` | `1112` | When recovering LP | 20 |
| `EVENT_PREDRAW` | `1113` | Before normal draw in Draw Phase | 25 |
| `EVENT_SUMMON_NEGATED` | `1114` | When Normal Summon is negated | 3 |
| `EVENT_FLIP_SUMMON_NEGATED` | `1115` | When Flip Summon is negated | 0 |
| `EVENT_SPSUMMON_NEGATED` | `1116` | When Special Summon is negated | 1 |
| `EVENT_SPSUMMON_SUCCESS_G_P` | `1117` | Continuous-only. Runs before a group-procedure Special Summon such as a Pendulum Summon succeeds. | 3 |
| `EVENT_CONTROL_CHANGED` | `1120` | When control changes | 9 |
| `EVENT_EQUIP` | `1121` | When an Equip Card is equipped | 17 |

#### Battle and random-result events

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EVENT_ATTACK_ANNOUNCE` | `1130` | When attack is declared | 482 |
| `EVENT_BE_BATTLE_TARGET` | `1131` | When selected as attack target | 150 |
| `EVENT_BATTLE_START` | `1132` | When Damage Step starts (before flipping) | 125 |
| `EVENT_BATTLE_CONFIRM` | `1133` | Before damage calculation (after flipping) | 35 |
| `EVENT_PRE_DAMAGE_CALCULATE` | `1134` | During damage calculation (e.g., Wing Slash) | 132 |
| `EVENT_DAMAGE_CALCULATING` | `1135` | Legacy/reserved local constant that is absent from the current core snapshot. No indexed card script registers it directly. | 0 |
| `EVENT_PRE_BATTLE_DAMAGE` | `1136` | Continuous-only. Runs immediately before battle damage is applied. | 4 |
| `EVENT_BATTLE_END` | `1137` | Legacy/reserved local constant that is absent from the current core snapshot. No indexed card script registers it directly. | 0 |
| `EVENT_BATTLED` | `1138` | After damage calculation (e.g., Alien Girl, same timing as Flip Effects) | 158 |
| `EVENT_BATTLE_DESTROYING` | `1139` | When destroying a monster by battle and sending it to Graveyard (e.g., Blackwing - Shura the Blue Flame) | 332 |
| `EVENT_BATTLE_DESTROYED` | `1140` | When destroyed by battle and sent to Graveyard (e.g., Mystic Tomato) | 341 |
| `EVENT_DAMAGE_STEP_END` | `1141` | When Damage Step ends | 139 |
| `EVENT_ATTACK_DISABLED` | `1142` | When attack is negated (e.g., Double Chance) | 6 |
| `EVENT_BATTLE_DAMAGE` | `1143` | When dealing battle damage | 210 |
| `EVENT_TOSS_DICE` | `1150` | After dice roll result | 1 |
| `EVENT_TOSS_COIN` | `1151` | After coin toss result | 4 |
| `EVENT_TOSS_COIN_NEGATE` | `1152` | When re-tossing a coin | 2 |
| `EVENT_TOSS_DICE_NEGATE` | `1153` | When re-rolling a dice | 3 |

#### Level, cost, material, and turn-end events

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EVENT_LEVEL_UP` | `1200` | When Level increases | 1 |
| `EVENT_PAY_LPCOST` | `1201` | When paying LP cost | 7 |
| `EVENT_DETACH_MATERIAL` | `1202` | When removing Xyz Material | 9 |
| `EVENT_RETURN_TO_GRAVE` | `1203` | Legacy/reserved local constant that is absent from the current core snapshot. No indexed card script registers it directly. | 0 |
| `EVENT_TURN_END` | `1210` | Continuous-only turn-end processing event. For an ordinary End Phase trigger, use `EVENT_PHASE+PHASE_END`. | 7 |

#### Phase, counter, and custom event bases

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EVENT_PHASE` | `0x1000` | Composed base. Add a `PHASE_*` value, for example `EVENT_PHASE+PHASE_END`, for a phase-end Trigger or Quick effect. | 1526 |
| `EVENT_PHASE_START` | `0x2000` | Continuous-only composed base. Add a `PHASE_*` value, for example `EVENT_PHASE_START+PHASE_DRAW`. | 42 |
| `EVENT_ADD_COUNTER` | `0x10000` | Composed base. Add the 16-bit counter type, for example `EVENT_ADD_COUNTER+0x1`. The core raises it after counters are successfully added. | 2 |
| `EVENT_REMOVE_COUNTER` | `0x20000` | Composed base. Add the 16-bit counter type. `Duel.RemoveCounter` raises it automatically; `Card.RemoveCounter` does not. | 1 |
| `EVENT_CUSTOM` | `0x10000000` | Composed base for script-defined events. Add a stable unique ID and raise that exact code with `Duel.RaiseEvent` or `Duel.RaiseSingleEvent`. | 76 |

### Every engine effect code

These codes identify continuous rules, modifiers, restrictions, procedures, and replacements. The description states the role of the code; the exact callback contract can additionally require `SetRange`, `SetTargetRange`, `SetTarget`, `SetValue`, `SetCondition`, or `SetOperation`. Search the local scripts for a proven pattern before using an unfamiliar low-level or reserved code.

#### Core rules and action restrictions

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_IMMUNE_EFFECT` | `1` | Immune to effects | 248 |
| `EFFECT_DISABLE` | `2` | Negates effects (e.g., Skill Drain) | 725 |
| `EFFECT_CANNOT_DISABLE` | `3` | Effect cannot be negated | 12 |
| `EFFECT_SET_CONTROL` | `4` | Sets control | 26 |
| `EFFECT_CANNOT_CHANGE_CONTROL` | `5` | Cannot change control | 11 |
| `EFFECT_CANNOT_ACTIVATE` | `6` | Player cannot activate effects | 326 |
| `EFFECT_CANNOT_TRIGGER` | `7` | Card cannot trigger effects | 115 |
| `EFFECT_DISABLE_EFFECT` | `8` | Negates effects (e.g., Forbidden Chalice) | 601 |
| `EFFECT_DISABLE_CHAIN` | `9` | Negates in chain (processor.cpp) | 1 |
| `EFFECT_DISABLE_TRAPMONSTER` | `10` | Negates Trap Monsters | 107 |
| `EFFECT_CANNOT_INACTIVATE` | `12` | Activation cannot be negated | 18 |
| `EFFECT_CANNOT_DISEFFECT` | `13` | Cannot be negated during effect processing | 16 |
| `EFFECT_CANNOT_CHANGE_POSITION` | `14` | Cannot change position | 75 |
| `EFFECT_TRAP_ACT_IN_HAND` | `15` | Trap can activate from hand | 45 |
| `EFFECT_TRAP_ACT_IN_SET_TURN` | `16` | Trap can activate in the turn it was Set | 56 |
| `EFFECT_REMAIN_FIELD` | `17` | Remains on field for X turns (e.g., Swords of Revealing Light) | 57 |
| `EFFECT_MONSTER_SSET` | `18` | Monster can be Set in Spell/Trap Zone | 20 |
| `EFFECT_CANNOT_SUMMON` | `20` | Cannot Normal Summon monsters | 136 |
| `EFFECT_CANNOT_FLIP_SUMMON` | `21` | Cannot Flip Summon monsters | 34 |
| `EFFECT_CANNOT_SPECIAL_SUMMON` | `22` | Cannot Special Summon monsters | 920 |
| `EFFECT_CANNOT_MSET` | `23` | Cannot Set monsters | 46 |
| `EFFECT_CANNOT_SSET` | `24` | Cannot Set Spells/Traps | 27 |
| `EFFECT_CANNOT_DRAW` | `25` | Cannot draw cards | 9 |
| `EFFECT_CANNOT_DISABLE_SUMMON` | `26` | Summon cannot be negated | 9 |
| `EFFECT_CANNOT_DISABLE_SPSUMMON` | `27` | Special Summon cannot be negated | 21 |
| `EFFECT_SET_SUMMON_COUNT_LIMIT` | `28` | Limits Normal Summon count per turn | 6 |
| `EFFECT_EXTRA_SUMMON_COUNT` | `29` | Increases Normal Summon count | 74 |
| `EFFECT_SPSUMMON_CONDITION` | `30` | Special Summon condition | 668 |
| `EFFECT_REVIVE_LIMIT` | `31` | Monsters with revival restrictions (Card.EnableReviveLimit()) | 0 |

#### Summon and Set procedures

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_SUMMON_PROC` | `32` | Summon rule effect | 166 |
| `EFFECT_LIMIT_SUMMON_PROC` | `33` | Summon rule restriction | 23 |
| `EFFECT_SPSUMMON_PROC` | `34` | Special Summon rule | 693 |
| `EFFECT_EXTRA_SET_COUNT` | `35` | Increases Set (Normal Summon) count | 7 |
| `EFFECT_SET_PROC` | `36` | Set (Normal Summon) rule | 30 |
| `EFFECT_LIMIT_SET_PROC` | `37` | Set (Normal Summon) rule restriction | 16 |
| `EFFECT_DIVINE_LIGHT` | `38` | Divine Light | 1 |
| `EFFECT_CANNOT_DISABLE_FLIP_SUMMON` | `39` | Flip Summon cannot be negated | 1 |

#### Movement, targeting, combat permissions, and costs

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_INDESTRUCTABLE` | `40` | Cannot be destroyed | 2 |
| `EFFECT_INDESTRUCTABLE_EFFECT` | `41` | Cannot be destroyed by effects | 449 |
| `EFFECT_INDESTRUCTABLE_BATTLE` | `42` | Cannot be destroyed by battle | 523 |
| `EFFECT_UNRELEASABLE_SUM` | `43` | Cannot be Tributed for a Tribute Summon | 67 |
| `EFFECT_UNRELEASABLE_NONSUM` | `44` | Cannot be Tributed except for a Tribute Summon | 48 |
| `EFFECT_DESTROY_SUBSTITUTE` | `45` | Mandatory destruction substitute (replace this card's destruction with another card) | 41 |
| `EFFECT_CANNOT_RELEASE` | `46` | Cannot perform Tribute actions | 7 |
| `EFFECT_INDESTRUCTABLE_COUNT` | `47` | Cannot be destroyed X times per turn | 109 |
| `EFFECT_UNRELEASABLE_EFFECT` | `48` | Cannot be Tributed | 1 |
| `EFFECT_DESTROY_REPLACE` | `50` | Optional destruction substitute (replace destruction with another action) | 246 |
| `EFFECT_RELEASE_REPLACE` | `51` | Tribute substitute | 0 |
| `EFFECT_SEND_REPLACE` | `52` | Can send to another location instead of the intended one (e.g., Dessert Castle) | 5 |
| `EFFECT_CANNOT_DISCARD_HAND` | `55` | Cannot discard from hand | 2 |
| `EFFECT_CANNOT_DISCARD_DECK` | `56` | Cannot send cards from Deck to Graveyard | 3 |
| `EFFECT_CANNOT_USE_AS_COST` | `57` | Cannot be used as cost | 0 |
| `EFFECT_CANNOT_PLACE_COUNTER` | `58` | Cannot place counters | 1 |
| `EFFECT_CANNOT_TO_GRAVE_AS_COST` | `59` | Cannot be sent to Graveyard as cost | 1 |
| `EFFECT_LEAVE_FIELD_REDIRECT` | `60` | Redirect destination when leaving field | 275 |
| `EFFECT_TO_HAND_REDIRECT` | `61` | Redirect destination when returning to hand | 4 |
| `EFFECT_TO_DECK_REDIRECT` | `62` | Redirect destination when returning to Deck | 2 |
| `EFFECT_TO_GRAVE_REDIRECT` | `63` | Redirect destination when sent to Graveyard | 35 |
| `EFFECT_REMOVE_REDIRECT` | `64` | Redirect destination when banished | 0 |
| `EFFECT_CANNOT_TO_HAND` | `65` | Cannot be added to hand | 21 |
| `EFFECT_CANNOT_TO_DECK` | `66` | Cannot be returned to Deck | 4 |
| `EFFECT_CANNOT_REMOVE` | `67` | Cannot be banished | 22 |
| `EFFECT_CANNOT_TO_GRAVE` | `68` | Cannot be sent to Graveyard | 3 |
| `EFFECT_CANNOT_TURN_SET` | `69` | Cannot be Set face-down | 9 |
| `EFFECT_CANNOT_BE_BATTLE_TARGET` | `70` | Cannot be targeted for attacks | 57 |
| `EFFECT_CANNOT_BE_EFFECT_TARGET` | `71` | Cannot be targeted by effects | 320 |
| `EFFECT_IGNORE_BATTLE_TARGET` | `72` | Cannot be targeted for attacks - weak type (e.g., Legendary Fisherman) | 15 |
| `EFFECT_CANNOT_DIRECT_ATTACK` | `73` | Cannot attack directly | 108 |
| `EFFECT_DIRECT_ATTACK` | `74` | Can attack directly | 195 |
| `EFFECT_DUAL_STATUS` | `75` | Gemini status | 2 |
| `EFFECT_EQUIP_LIMIT` | `76` | Equip target restriction | 608 |
| `EFFECT_DUAL_SUMMONABLE` | `77` | Can be re-summoned (Gemini) | 1 |
| `EFFECT_UNION_LIMIT` | `78` | Union restriction | 20 |
| `EFFECT_REVERSE_DAMAGE` | `80` | Converts damage to recovery | 9 |
| `EFFECT_REVERSE_RECOVER` | `81` | Converts recovery to damage | 2 |
| `EFFECT_CHANGE_DAMAGE` | `82` | Changes damage value | 90 |
| `EFFECT_REFLECT_DAMAGE` | `83` | Reflects damage | 12 |
| `EFFECT_CANNOT_ATTACK` | `85` | Cannot attack | 329 |
| `EFFECT_CANNOT_ATTACK_ANNOUNCE` | `86` | Cannot declare an attack | 104 |
| `EFFECT_CANNOT_CHANGE_POS_E` | `87` | Cannot be changed to Defense Position by effects (e.g., Aggro Cloud) | 1 |
| `EFFECT_ACTIVATE_COST` | `90` | Activation cost (e.g., Magical Shackles) | 7 |
| `EFFECT_SUMMON_COST` | `91` | Summon cost | 20 |
| `EFFECT_SPSUMMON_COST` | `92` | Special Summon cost (e.g., Tyrant Dragon) | 28 |
| `EFFECT_FLIPSUMMON_COST` | `93` | Flip Summon cost | 0 |
| `EFFECT_MSET_COST` | `94` | Monster Set cost | 1 |
| `EFFECT_SSET_COST` | `95` | Spell/Trap Set cost | 1 |
| `EFFECT_ATTACK_COST` | `96` | Attack cost (e.g., Mist Valley Falcon) | 17 |

#### Stats, identity, position, Tributes, and counters

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_UPDATE_ATTACK` | `100` | Increase/decrease ATK | 2120 |
| `EFFECT_SET_ATTACK` | `101` | Set ATK, ATK becomes X for Special Summon, or continuously change ATK | 106 |
| `EFFECT_SET_ATTACK_FINAL` | `102` | Temporarily change ATK (all chain-entering effects) | 374 |
| `EFFECT_SET_BASE_ATTACK` | `103` | Set original ATK or continuously change original ATK | 75 |
| `EFFECT_UPDATE_DEFENSE` | `104` | Increase/decrease DEF | 506 |
| `EFFECT_SET_DEFENSE` | `105` | Set DEF, DEF becomes X for Special Summon, or continuously change DEF | 58 |
| `EFFECT_SET_DEFENSE_FINAL` | `106` | Temporarily change DEF (all chain-entering effects) | 106 |
| `EFFECT_SET_BASE_DEFENSE` | `107` | Set original DEF or continuously change original DEF | 28 |
| `EFFECT_REVERSE_UPDATE` | `108` | Invert ATK/DEF increase/decrease (e.g., Tengu) | 1 |
| `EFFECT_SWAP_AD` | `109` | Swap ATK and DEF (e.g., Super Crashbug) | 1 |
| `EFFECT_SWAP_BASE_AD` | `110` | Swap original ATK and DEF | 4 |
| `EFFECT_SET_BASE_ATTACK_FINAL` | `111` | Temporarily change original ATK | 27 |
| `EFFECT_SET_BASE_DEFENSE_FINAL` | `112` | Temporarily change original DEF | 10 |
| `EFFECT_ADD_CODE` | `113` | Add card code | 5 |
| `EFFECT_CHANGE_CODE` | `114` | Change card code | 66 |
| `EFFECT_ADD_TYPE` | `115` | Add card type (Types) | 133 |
| `EFFECT_REMOVE_TYPE` | `116` | Remove card type | 12 |
| `EFFECT_CHANGE_TYPE` | `117` | Change card type | 89 |
| `EFFECT_ADD_RACE` | `120` | Add race | 0 |
| `EFFECT_REMOVE_RACE` | `121` | Remove race | 1 |
| `EFFECT_CHANGE_RACE` | `122` | Change race | 69 |
| `EFFECT_ADD_ATTRIBUTE` | `125` | Add attribute | 20 |
| `EFFECT_REMOVE_ATTRIBUTE` | `126` | Remove attribute | 1 |
| `EFFECT_CHANGE_ATTRIBUTE` | `127` | Change attribute | 86 |
| `EFFECT_UPDATE_LEVEL` | `130` | Change Level | 264 |
| `EFFECT_CHANGE_LEVEL` | `131` | Set Level | 239 |
| `EFFECT_UPDATE_RANK` | `132` | Change Rank | 6 |
| `EFFECT_CHANGE_RANK` | `133` | Set Rank | 3 |
| `EFFECT_UPDATE_LSCALE` | `134` | Change Left Scale | 15 |
| `EFFECT_CHANGE_LSCALE` | `135` | Set Left Scale | 20 |
| `EFFECT_UPDATE_RSCALE` | `136` | Change Right Scale | 15 |
| `EFFECT_CHANGE_RSCALE` | `137` | Set Right Scale | 20 |
| `EFFECT_SET_POSITION` | `140` | Set position | 15 |
| `EFFECT_SELF_DESTROY` | `141` | Non-chain destruction (e.g., Sin series) | 88 |
| `EFFECT_SELF_TOGRAVE` | `142` | Non-chain send to Graveyard | 17 |
| `EFFECT_DOUBLE_TRIBUTE` | `150` | Can be used as two Tributes | 29 |
| `EFFECT_DECREASE_TRIBUTE` | `151` | Decrease Tributes | 8 |
| `EFFECT_DECREASE_TRIBUTE_SET` | `152` | Decrease Tributes for Setting monsters | 1 |
| `EFFECT_EXTRA_RELEASE` | `153` | Mandatory Tribute substitute (e.g., Soul Exchange) | 1 |
| `EFFECT_TRIBUTE_LIMIT` | `154` | Tribute restriction | 9 |
| `EFFECT_EXTRA_RELEASE_SUM` | `155` | Tribute substitute for summon (e.g., Kaiser Cyclone) | 1 |
| `EFFECT_TRIPLE_TRIBUTE` | `156` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_ADD_EXTRA_TRIBUTE` | `157` | Add usable Tributes (e.g., True Draco) | 14 |
| `EFFECT_EXTRA_RELEASE_NONSUM` | `158` | Tribute substitute for effect cost (e.g., Dark World) | 2 |
| `EFFECT_PUBLIC` | `160` | Make hand public | 22 |

#### LP, phases, attacking, damage, and randomness

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_LPCOST_CHANGE` | `170` | Change LP cost value | 6 |
| `EFFECT_LPCOST_REPLACE` | `171` | Replace LP cost with another action | 1 |
| `EFFECT_SKIP_DP` | `180` | Skip Draw Phase | 14 |
| `EFFECT_SKIP_SP` | `181` | Skip Standby Phase | 2 |
| `EFFECT_SKIP_M1` | `182` | Skip Main Phase 1 | 6 |
| `EFFECT_SKIP_BP` | `183` | Skip Battle Phase | 21 |
| `EFFECT_SKIP_M2` | `184` | Skip Main Phase 2 | 1 |
| `EFFECT_CANNOT_BP` | `185` | Cannot enter Battle Phase | 50 |
| `EFFECT_CANNOT_M2` | `186` | Cannot enter Main Phase 2 | 0 |
| `EFFECT_CANNOT_EP` | `187` | Cannot enter End Phase | 1 |
| `EFFECT_SKIP_TURN` | `188` | Skip entire turn | 5 |
| `EFFECT_DEFENSE_ATTACK` | `190` | Can attack in Defense Position | 19 |
| `EFFECT_MUST_ATTACK` | `191` | Must attack | 54 |
| `EFFECT_FIRST_ATTACK` | `192` | Must attack first | 1 |
| `EFFECT_ATTACK_ALL` | `193` | Can attack all monsters | 43 |
| `EFFECT_EXTRA_ATTACK` | `194` | Increase attack count | 162 |
| `EFFECT_MUST_BE_ATTACKED` | `195` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_ONLY_BE_ATTACKED` | `196` | Can only attack this card | 1 |
| `EFFECT_ATTACK_DISABLED` | `197` | Attack negated (marker for successful Duel.NegateAttack()) | 0 |
| `EFFECT_NO_BATTLE_DAMAGE` | `200` | Does not inflict battle damage to opponent | 31 |
| `EFFECT_AVOID_BATTLE_DAMAGE` | `201` | Does not take battle damage | 142 |
| `EFFECT_REFLECT_BATTLE_DAMAGE` | `202` | Opponent takes battle damage instead | 26 |
| `EFFECT_PIERCE` | `203` | Piercing damage | 188 |
| `EFFECT_BATTLE_DESTROY_REDIRECT` | `204` | Redirect destination when destroyed by battle | 20 |
| `EFFECT_BATTLE_DAMAGE_TO_EFFECT` | `205` | Treat battle damage as effect damage | 1 |
| `EFFECT_BOTH_BATTLE_DAMAGE` | `206` | Both players take battle damage | 3 |
| `EFFECT_ALSO_BATTLE_DAMAGE` | `207` | Opponent also takes battle damage dealt to you | 5 |
| `EFFECT_CHANGE_BATTLE_DAMAGE` | `208` | Change battle damage dealt by this card or received by player | 74 |
| `EFFECT_TOSS_COIN_REPLACE` | `220` | Replace coin toss | 0 |
| `EFFECT_TOSS_DICE_REPLACE` | `221` | Replace dice roll | 0 |

#### Fusion, Synchro, Xyz, Link materials, and zones

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_FUSION_MATERIAL` | `230` | Specify Fusion Material conditions | 8 |
| `EFFECT_CHAIN_MATERIAL` | `231` | Player affected by Chain Material effect | 2 |
| `EFFECT_EXTRA_SYNCHRO_MATERIAL` | `232` | Can be treated as your Synchro Material from the hand or opponent's field | 3 |
| `EFFECT_XYZ_MATERIAL` | `233` | Can be used as Xyz Material | 0 |
| `EFFECT_FUSION_SUBSTITUTE` | `234` | Fusion Material substitute | 12 |
| `EFFECT_CANNOT_BE_FUSION_MATERIAL` | `235` | Cannot be used as Fusion Material | 51 |
| `EFFECT_CANNOT_BE_SYNCHRO_MATERIAL` | `236` | Cannot be used as Synchro Material | 101 |
| `EFFECT_SYNCHRO_MATERIAL_CUSTOM` | `237` | Custom Tuner Synchro process | 7 |
| `EFFECT_CANNOT_BE_XYZ_MATERIAL` | `238` | Cannot be used as Xyz Material | 76 |
| `EFFECT_CANNOT_BE_LINK_MATERIAL` | `239` | Cannot be used as Link Material | 69 |
| `EFFECT_SYNCHRO_LEVEL` | `240` | Level when used as Synchro Material | 5 |
| `EFFECT_RITUAL_LEVEL` | `241` | Level when used as Ritual Tribute | 10 |
| `EFFECT_XYZ_LEVEL` | `242` | Level when used as Xyz Material | 18 |
| `EFFECT_EXTRA_RITUAL_MATERIAL` | `243` | Can be used as Ritual Tribute from Graveyard | 11 |
| `EFFECT_NONTUNER` | `244` | Treated as non-Tuner monster (e.g., Phantom King Hydride) | 14 |
| `EFFECT_OVERLAY_REMOVE_REPLACE` | `245` | Substitute for removing Xyz Material | 11 |
| `EFFECT_SCRAP_CHIMERA` | `246` | Scrap Chimera | 1 |
| `EFFECT_TUNE_MAGICIAN_X` | `247` | Tuning Magician Xyz Material restriction | 1 |
| `EFFECT_TUNE_MAGICIAN_F` | `248` | Lua procedure convention used by the local Synchro helpers even though the current core has no native consumer for this name. | 1 |
| `EFFECT_PRE_MONSTER` | `250` | Access various monster values (used with Card.AddMonsterAttribute()) | 0 |
| `EFFECT_MATERIAL_CHECK` | `251` | Check materials | 195 |
| `EFFECT_DISABLE_FIELD` | `260` | Disable zones (e.g., Ojama King) | 23 |
| `EFFECT_USE_EXTRA_MZONE` | `261` | Lock Monster Zones | 1 |
| `EFFECT_USE_EXTRA_SZONE` | `262` | Lock Spell/Trap Zones | 0 |
| `EFFECT_MAX_MZONE` | `263` | Maximum Monster Zone slots | 3 |
| `EFFECT_MAX_SZONE` | `264` | Maximum Spell/Trap Zone slots | 2 |
| `EFFECT_MUST_USE_MZONE` | `265` | Must use specific Monster Zone slots | 9 |

#### Player rules, Deck state, and material requirements

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_HAND_LIMIT` | `270` | Hand size limit | 5 |
| `EFFECT_DRAW_COUNT` | `271` | Number of cards drawn in Draw Phase | 12 |
| `EFFECT_SPIRIT_DONOT_RETURN` | `280` | Spirit Monster does not return to hand | 1 |
| `EFFECT_SPIRIT_MAYNOT_RETURN` | `281` | Spirit Monster can choose not to return to hand | 2 |
| `EFFECT_CHANGE_ENVIRONMENT` | `290` | Change Field Spell | 2 |
| `EFFECT_NECRO_VALLEY` | `291` | Necrovalley | 2 |
| `EFFECT_FORBIDDEN` | `292` | Cannot be played (e.g., Forbidden Order) | 2 |
| `EFFECT_NECRO_VALLEY_IM` | `293` | Unaffected by Necrovalley | 5 |
| `EFFECT_REVERSE_DECK` | `294` | Reverse Deck order | 1 |
| `EFFECT_REMOVE_BRAINWASHING` | `295` | Remove brainwashing | 6 |
| `EFFECT_BP_TWICE` | `296` | Two Battle Phases | 4 |
| `EFFECT_UNIQUE_CHECK` | `297` | Only one can exist on field (used with Card.SetUniqueOnField()) | 0 |
| `EFFECT_MATCH_KILL` | `300` | Match victory (e.g., Victory Dragon) | 1 |
| `EFFECT_SYNCHRO_CHECK` | `310` | Genomix Fighter | 2 |
| `EFFECT_QP_ACT_IN_NTPHAND` | `311` | Activate from hand in opponent's turn (e.g., Ecclesia the Virtuous) | 12 |
| `EFFECT_MUST_BE_SMATERIAL` | `312` | Must be used as Synchro Material (e.g., Phonon Pulse Dragon) | 2 |
| `EFFECT_TO_GRAVE_REDIRECT_CB` | `313` | Redirect destination (e.g., Gem Beasts) | 18 |
| `EFFECT_CHANGE_INVOLVING_BATTLE_DAMAGE` | `314` | Change battle damage caused by this card | 13 |
| `EFFECT_CHANGE_RANK_FINAL` | `315` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_MUST_BE_FMATERIAL` | `316` | Must be used as Fusion Material | 1 |
| `EFFECT_MUST_BE_XMATERIAL` | `317` | Must be used as Xyz Material | 1 |
| `EFFECT_MUST_BE_LMATERIAL` | `318` | Must be used as Link Material | 1 |

#### Advanced procedures, materials, and modern rules

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_SPSUMMON_PROC_G` | `320` | Pendulum Summon rule | 2 |
| `EFFECT_SPSUMMON_COUNT_LIMIT` | `330` | Special Summon count limit | 5 |
| `EFFECT_LEFT_SPSUMMON_COUNT` | `331` | Remaining summon count (e.g., Summon Limit) | 5 |
| `EFFECT_CANNOT_SELECT_BATTLE_TARGET` | `332` | Opponent cannot select as attack target | 135 |
| `EFFECT_CANNOT_SELECT_EFFECT_TARGET` | `333` | Opponent cannot select as effect target | 1 |
| `EFFECT_ADD_SETCODE` | `334` | Treated as specific archetype effect | 12 |
| `EFFECT_NO_EFFECT_DAMAGE` | `335` | Player affected by "effect damage becomes 0" | 56 |
| `EFFECT_UNSUMMONABLE_CARD` | `336` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_DISABLE_CHAIN_FIELD` | `337` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_DISCARD_COST_CHANGE` | `338` | Change discard cost for Counter Traps (e.g., Ariadne the Absolver) | 1 |
| `EFFECT_HAND_SYNCHRO` | `339` | Use hand monsters as Synchro Material | 9 |
| `EFFECT_ADD_FUSION_CODE` | `340` | Treated as specific card name for Fusion Material (e.g., Fusion Identification) | 5 |
| `EFFECT_ADD_FUSION_SETCODE` | `341` | Treated as specific archetype for Fusion Material (e.g., Toy Parade) | 4 |
| `EFFECT_RISE_TO_FULL_HEIGHT` | `342` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_ONLY_ATTACK_MONSTER` | `343` | Can only attack specific monster | 1 |
| `EFFECT_MUST_ATTACK_MONSTER` | `344` | Must attack specific monster if attacking | 25 |
| `EFFECT_PATRICIAN_OF_DARKNESS` | `345` | Opponent chooses attack target (e.g., Patrician of Darkness) | 5 |
| `EFFECT_EXTRA_ATTACK_MONSTER` | `346` | Attack a monster X times | 55 |
| `EFFECT_UNION_STATUS` | `347` | Union status | 1 |
| `EFFECT_OLDUNION_STATUS` | `348` | Old Union status | 1 |
| `EFFECT_ADD_FUSION_ATTRIBUTE` | `349` | Reserved/unsupported in the current core snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_REMOVE_FUSION_ATTRIBUTE` | `350` | Reserved/unsupported in the current core snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_CHANGE_FUSION_ATTRIBUTE` | `351` | Attribute when used as Fusion Material | 1 |
| `EFFECT_EXTRA_FUSION_MATERIAL` | `352` | Additional Fusion Material (e.g., Omni Alchemist) | 10 |
| `EFFECT_TUNER_MATERIAL_LIMIT` | `353` | Synchro Material restriction | 12 |
| `EFFECT_ADD_LINK_CODE` | `354` | Card name when used as Link Material | 2 |
| `EFFECT_ADD_LINK_SETCODE` | `355` | Reserved/unsupported in the current core snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_ADD_LINK_ATTRIBUTE` | `356` | Attribute when used as Link Material | 1 |
| `EFFECT_ADD_LINK_RACE` | `357` | Race when used as Link Material | 1 |
| `EFFECT_EXTRA_LINK_MATERIAL` | `358` | Hand as Link Material | 18 |
| `EFFECT_QP_ACT_IN_SET_TURN` | `359` | Quick-Play Spell can activate in the turn it was Set | 8 |
| `EFFECT_EXTRA_PENDULUM_SUMMON` | `360` | Additional Pendulum Summon | 9 |
| `EFFECT_MATERIAL_LIMIT` | `361` | Material restriction | 2 |
| `EFFECT_SET_BATTLE_ATTACK` | `362` | Use set ATK for battle damage calculation | 6 |
| `EFFECT_SET_BATTLE_DEFENSE` | `363` | Use set DEF for battle damage calculation | 4 |
| `EFFECT_OVERLAY_RITUAL_MATERIAL` | `364` | Xyz Materials can be used for Ritual Summon | 1 |
| `EFFECT_CHANGE_GRAVE_ATTRIBUTE` | `365` | Change attribute of cards in Graveyard (e.g., Advanced Shift) | 1 |
| `EFFECT_CHANGE_GRAVE_RACE` | `366` | Change race of cards in Graveyard (e.g., Advanced Shift) | 2 |
| `EFFECT_ACTIVATION_COUNT_LIMIT` | `367` | Reserved/unsupported in the current snapshot; no indexed script uses it directly. | 0 |
| `EFFECT_LIMIT_SPECIAL_SUMMON_POSITION` | `368` | Cannot Special Summon in specific position | 21 |
| `EFFECT_TUNER` | `369` | Can be treated as a Tuner for a Synchro Summon (Hundred Apple Dragon - Apple Wyrm) | 3 |
| `EFFECT_KAISER_COLOSSEUM` | `370` | Kaiser Colosseum | 1 |
| `EFFECT_REPLACE_DAMAGE` | `371` | Damage is replaced by a specific action | 2 |
| `EFFECT_XYZ_MIN_COUNT` | `372` | Can only be used for an Xyz Summon with at least X materials | 1 |
| `EFFECT_SYNCHRO_LEVEL_EX` | `373` | Allows monsters without Levels to be used as Synchro Material | 3 |
| `EFFECT_RITUAL_LEVEL_EX` | `374` | Allows monsters without Levels to be used as Ritual Material | 0 |
| `EFFECT_DOUBLE_XMATERIAL` | `375` | Counts as 2 materials when Xyz Summoning a monster that requires 3 or more materials | 5 |
| `EFFECT_REVEAL_ONFIELD` | `376` | Affected face-down cards on the field can be inspected by the effect controller | 1 |
| `EFFECT_ADD_CARD_TYPE` | `377` | Adds TYPE_* bits to the card type used by Card.GetCardType (distinct from ordinary EFFECT_ADD_TYPE) | 2 |
| `EFFECT_REMOVE_CARD_TYPE` | `378` | Removes TYPE_* bits from the card type used by Card.GetCardType | 0 |
| `EFFECT_CHANGE_CARD_TYPE` | `379` | Replaces the card type used by Card.GetCardType with the supplied TYPE_* bitmask | 0 |

#### Encoded and engine-managed effect codes

| Code | Value | What it is for | Direct uses |
| --- | ---: | --- | ---: |
| `EFFECT_COUNTER_PERMIT` | `0x10000` | Encoded base. Add the counter type to allow that kind of counter on the affected card. | 3 |
| `EFFECT_COUNTER_LIMIT` | `0x20000` | Encoded base. Add the counter type; `SetValue` supplies the permitted limit. | 0 |
| `EFFECT_RCOUNTER_REPLACE` | `0x30000` | Encoded base. Add the counter type to replace removal of that kind of counter. | 1 |
| `EFFECT_FLAG_EFFECT` | `0x20000000` | Card-ID flag-effect base. Add a card ID for a manually registered flag-style code; `RegisterFlagEffect` normally creates these codes for you. | 11 |

### Engine sources

- [Current `SetCode` binding](https://github.com/Fluorohydride/ygopro-core/blob/8b020270e752c56a5df52a8f827f094837be5b64/libeffect.cpp#L120-L128)
- [Event-code classification and continuous-only rules](https://github.com/Fluorohydride/ygopro-core/blob/8b020270e752c56a5df52a8f827f094837be5b64/effect.cpp#L21-L32)
- [Code-family layout and continuous-event set](https://github.com/Fluorohydride/ygopro-core/blob/8b020270e752c56a5df52a8f827f094837be5b64/effect.h#L626-L641)
- [Registration check that rejects Trigger/Quick effects on continuous-only events](https://github.com/Fluorohydride/ygopro-core/blob/8b020270e752c56a5df52a8f827f094837be5b64/card.cpp#L1752-L1760)
- [Effect registration indexes the current code](https://github.com/Fluorohydride/ygopro-core/blob/8b020270e752c56a5df52a8f827f094837be5b64/field.cpp#L1166-L1176)
- [Named script constants](https://github.com/Fluorohydride/ygopro-scripts/blob/b605741f9bcf114bdc9087e264de2130736e27e0/constant.lua#L351-L692)
- [Generated constants reference](/api/constants)

## Related Functions

- [Effect.SetType](/api/functions/Effect/SetType)
- [Effect.SetRange](/api/functions/Effect/SetRange)

## Parameters

- `e` `Effect`
- `code` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:613`

## Guided Examples

Learn how to use this function in context:

- [Activated Effects](/learn/activated-effects)
- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)
- [Beginner Script Ladder](/learn/beginner-script-ladder)
- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)
- [Effects That Apply Continuously](/learn/continuous-effects)
- [Counter Traps](/learn/counter-traps)

::: details More guided lessons (7)

- [Counters](/learn/counters)
- [Creation, Building, and Registration of an Effect Object](/learn/effect-object)
- [EFFECT_TYPE Constants and Templates](/learn/effect-types)
- [Normal And Continuous Traps](/learn/normal-and-continuous-traps)
- [Quick-Play Spells](/learn/quick-play-spells)
- [Spell Card Patterns](/learn/spell-card-patterns)
- [Trap Card Patterns](/learn/trap-card-patterns)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12863** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.SetCode) with `Effect.SetCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 7 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 3 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 5 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 5 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 3 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 4 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 4 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 7 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 4 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 3 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 6 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 5 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 7 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 4 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 3 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 4 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25158975.lua) | 5 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17350692.lua) | 3 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 8 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 2 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 3 |
| ...and 12839 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	e1:SetCategory(CATEGORY_EQUIP+CATEGORY_POSITION+CATEGORY_MSET)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetHintTiming(TIMING_DAMAGE_STEP)
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_GRAVE_SPSUMMON)
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e2:SetCode(custom_code)
	e2:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DELAY)
	e2:SetRange(LOCATION_HAND)
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	e0:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e0:SetCode(EVENT_SPSUMMON_SUCCESS)
	e0:SetCondition(s.condition)
	e0:SetOperation(s.regop)
```
