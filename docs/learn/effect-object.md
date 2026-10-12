# Creation, Building, and Registration of an Effect Object

Most card effects are built in three steps:

1. Create an `Effect`.
2. Set properties on it.
3. Register it to a card or to the Duel.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_TOHAND)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.thtg)
e1:SetOperation(s.thop)
c:RegisterEffect(e1)
```

## What Each Setter Answers

| Setter | Question |
| --- | --- |
| `SetDescription` | Which card text line or prompt should be shown? |
| `SetCategory` | What kind of action should the engine announce? |
| `SetType` | What kind of effect is this? |
| `SetCode` | Which event, phase, or continuous rule does this use? |
| `SetProperty` | Does it target, work in the Damage Step, ignore immunity, and so on? |
| `SetRange` | Where must the handler be for this effect to exist or activate? |
| `SetTargetRange` | Which cards or players are affected by a field/equip/procedure effect? |
| `SetValue` | Which number or function supplies the continuous value? |
| `SetCountLimit` | How often may this effect be used? |
| `SetHintTiming` | Which timing hints should the client show for optional fast effects? |
| `SetCondition` | Is the effect allowed to be considered? |
| `SetCost` | Can the cost be paid, and how is it paid? |
| `SetTarget` | Can it activate, and what will it affect? |
| `SetOperation` | What happens when it resolves or when a continuous event fires? |
| `SetLabel` | Which small integer should this effect remember? |
| `SetLabelObject` | Which object, usually another Effect or Group, should this effect remember? |
| `SetReset` | When does a temporary effect disappear? |

The setter list is not just vocabulary. It is a review checklist. If a script
does something unexpected, ask which question was answered incorrectly: wrong
effect type, wrong event code, missing property flag, wrong range, missing
target range, a count code shared with the wrong effect, or a temporary effect
without a reset.

## Core Setter Shapes

Most setters follow one of these shapes.

| Shape | Examples | Notes |
| --- | --- | --- |
| Plain value | `SetType`, `SetCode`, `SetRange`, `SetValue(500)` | The effect stores an integer or bitmask. |
| Function callback | `SetCondition`, `SetCost`, `SetTarget`, `SetOperation`, `SetValue(s.val)` | The engine calls the function later with a signature determined by the effect type/code. |
| Player or location pair | `SetTargetRange(a,b)` | The meaning changes depending on the effect flags and effect code. |
| Stored data | `SetLabel`, `SetLabelObject` | Labels are small integers; label objects are Effect, Group, Card, or other Lua-exposed objects. |
| Lifetime rule | `SetReset` | Needed for temporary effects created after script load. |

Do not guess callback signatures from the setter name alone. A target function
for an activated effect, a target function for a continuous field effect, and a
target function for an inherent Special Summon procedure all receive different
arguments.

## Type Decides Setter Meaning

Start by reading `SetType`, then interpret the other setters through that
shape. The same setter can answer a different question on a different kind of
effect.

| Effect shape | What `SetCode` usually means | What to inspect next |
| --- | --- | --- |
| `EFFECT_TYPE_SINGLE`, `EFFECT_TYPE_FIELD`, `EFFECT_TYPE_EQUIP`, or `EFFECT_TYPE_XMATERIAL` by itself | The continuous rule, usually an `EFFECT_*` constant. | `SetRange`, `SetTargetRange`, `SetTarget`, and `SetValue`. |
| Trigger, Quick, or event-watching Continuous effects | The event or phase that wakes the effect, usually `EVENT_*` or `EVENT_PHASE+PHASE_*`. | `SetCondition`, `SetCost`, `SetTarget`, and `SetOperation`. |
| Spell/Trap card activation with `EFFECT_TYPE_ACTIVATE` | The activation event, such as `EVENT_FREE_CHAIN`, when the card needs one. | Activation legality in `SetCost` and `SetTarget`. |
| Special Summon procedure effects | A procedure code such as `EFFECT_SPSUMMON_PROC`. | Procedure flags, `SetTargetRange`, and the procedure callback signatures. |

Local examples show the split. Cyber Dragon Infinity (`c10443957.lua`) uses
`EFFECT_UPDATE_ATTACK` as the code for a continuous single ATK update, but
`EVENT_CHAINING` as the code for its Quick Effect negation. Lava Golem
(`c102380.lua`) uses `EVENT_PHASE+PHASE_STANDBY` for a mandatory Standby Phase
trigger, and `EFFECT_SPSUMMON_PROC` for its hand procedure.

This is why copying a block by shape is safer than copying one setter at a
time. If `SetCode` names an event, you are probably building an activated or
event-watching effect. If it names an `EFFECT_*` rule, you are probably building
a continuous rule that needs value, range, or target-range review.

## User-Facing Text And Categories

`SetDescription` usually receives `aux.Stringid(id,n)`, where `n` selects the
card text string shown to the player for that effect.

```lua
e1:SetDescription(aux.Stringid(id,0))
```

Some scripts use built-in description constants or raw description IDs. Prefer
`aux.Stringid(id,n)` when the prompt belongs to this card's own text.

`SetCategory` stores category flags. Combine multiple categories with the same
bit-flag style used by local scripts.

```lua
e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
```

The category should describe what the effect announces, not every helper check
inside the script.

## Properties

`SetProperty` controls special handling such as targeting, Damage Step
permission, delayed triggers, or continuous targeting.

```lua
e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
```

The local core accepts a second property slot too. Local scripts mostly use the
first slot, but the signature is:

```lua
e1:SetProperty(prop1,prop2)
```

Use the second slot only for constants that are documented as second-property
flags. Do not mix ordinary `EFFECT_FLAG_*` values into the wrong slot.

Common first-slot flags:

| Flag | Use |
| --- | --- |
| `EFFECT_FLAG_CARD_TARGET` | The activation targets one or more cards. Pair it with target APIs. |
| `EFFECT_FLAG_PLAYER_TARGET` | The effect targets or affects players; `SetTargetRange` usually uses `1`/`0` player bits. |
| `EFFECT_FLAG_DELAY` | Optional trigger can activate after an event group is processed when its timing allows it. |
| `EFFECT_FLAG_DAMAGE_STEP` | The effect may be used in the Damage Step. |
| `EFFECT_FLAG_DAMAGE_CAL` | The effect may be used during damage calculation, when the card text/ruling allows it. |
| `EFFECT_FLAG_SINGLE_RANGE` | A single continuous effect only applies while the handler is in `SetRange`. |
| `EFFECT_FLAG_CANNOT_DISABLE` | Used for rule/procedure support effects that should not be negated like ordinary card effects. |

These flags do not replace legality checks. For example,
`EFFECT_FLAG_DAMAGE_STEP` can permit a Quick Effect to be offered in the Damage
Step, but the condition/target still has to verify the card text's real
requirements.

## Target Range Modes

`SetTargetRange` is context-sensitive.

| Context | Example | Meaning |
| --- | --- | --- |
| Field effect affecting cards | `e:SetTargetRange(LOCATION_MZONE,0)` | Cards in the handler controller's Monster Zones only. |
| Field effect affecting both fields | `e:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)` | Cards in both players' Monster Zones. |
| Player-affecting field effect with `EFFECT_FLAG_PLAYER_TARGET` | `e:SetTargetRange(1,0)` | The handler controller is affected; the opponent is not. |
| Special Summon procedure with `EFFECT_FLAG_SPSUM_PARAM` | `e:SetTargetRange(POS_FACEUP,1)` | Summon position and target player/opponent field parameter for that procedure. |

Lava Golem's local script (`c102380.lua`) is a useful reminder that
`SetTargetRange` can mean something very different once procedure flags are
involved. Its Special Summon procedure uses `SetTargetRange(POS_FACEUP,1)`,
while its later summon restriction uses `EFFECT_FLAG_PLAYER_TARGET` with
`SetTargetRange(1,0)`.

## Hint Timing

`SetHintTiming` controls when the client should offer an optional activation
prompt. The local define file documents the second argument as the handler
controller's timing and the optional third argument as the opponent-turn timing.
If the third argument is omitted, the second value is reused.

```lua
e1:SetHintTiming(TIMING_END_PHASE)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_MAIN_END)
e1:SetHintTiming(TIMING_DAMAGE_STEP,TIMING_DAMAGE_STEP+TIMING_END_PHASE)
```

This does not make an effect legal by itself. It only helps the client ask at
the right windows after the effect's type, code, condition, cost, and target
checks allow activation.

## Registering to a Card

Use `c:RegisterEffect(e)` when the effect belongs to the card whose script is
loading.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

After registration, the engine knows that the card has this effect. For most
normal card text, this is the registration you want.

## Registering to the Duel

Use `Duel.RegisterEffect(e,tp)` for a temporary rule that is created while an
effect resolves and is not simply attached as one of the handler's regular
effects.

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
e1:SetTargetRange(1,0)
e1:SetTarget(s.splimit)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

Temporary Duel effects almost always need `SetReset`. Without a reset, the
effect can last longer than intended.

## Cloning Effects

When two effects share most settings, scripts often clone the first one and
change only the difference.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_MZONE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(200)
c:RegisterEffect(e1)
local e2=e1:Clone()
e2:SetCode(EFFECT_UPDATE_DEFENSE)
c:RegisterEffect(e2)
```

This pattern appears in scripts such as `c10002346.lua`: one field effect
updates ATK, the clone updates DEF.

Cloning copies the current settings. Change the fields that differ before
registration. If two effects need different reset, category, code, target, or
operation behavior, set those differences explicitly on the clone.

## Labels And Label Objects

`SetLabel` is useful for small numbers that the operation needs later.

```lua
e:SetLabel(op)
```

The local core supports multiple integer labels.

```lua
e:SetLabel(race,attribute)
local race,attribute=e:GetLabel()
```

`SetLabelObject` stores a Lua-exposed object. Grant effects commonly store the
effect object that will be granted to other cards.

```lua
local ge=Effect.CreateEffect(c)
ge:SetType(EFFECT_TYPE_SINGLE)
ge:SetCode(EFFECT_UPDATE_ATTACK)
ge:SetValue(500)

local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT)
e1:SetLabelObject(ge)
c:RegisterEffect(e1)
```

Use labels for simple Chain choices. Use label objects only when the local
script pattern expects an object to be attached to the effect.

When storing a `Group` in a label object beyond the current callback, local
scripts commonly call `g:KeepAlive()` and later clean up the kept group when the
effect no longer needs it. Do not use a label object as a casual global
variable; it creates lifetime concerns that a plain label avoids.

Local scripts show two common long-lived Group patterns:

```lua
local sg=rg:SelectSubGroup(tp,s.fselect,true,2,2,tp)
if sg then
    sg:KeepAlive()
    e:SetLabelObject(sg)
    return true
end
```

```lua
local g=e:GetLabelObject()
Duel.Release(g,REASON_SPSUMMON)
g:DeleteGroup()
```

That shape appears in Lava Golem (`c102380.lua`): the procedure stores the
selected Tributed monsters in the target callback, then releases and deletes
that kept Group in the operation. Rescue Hedgehog (`c99742859.lua`) shows the
other common pattern: keep a Group for a delayed End Phase watcher, store a
field ID with `SetLabel`, and delete/reset the effect when the kept cards are
gone.

## Count Limits From Text

`SetCountLimit` belongs on the effect object, but the correct arguments come
from card text.

| Card text shape | Common MDPro4/YGOPro shape |
| --- | --- |
| "Once per turn..." on one local effect | `e:SetCountLimit(1)` |
| "You can only use this effect of [card] once per turn" | `e:SetCountLimit(1,id)` |
| Several effects on the same card each once per turn | `id`, `id+o`, `id+o*2`, or another stable distinct code |
| "You can only activate 1 [card] per turn" | Usually the activation effect gets the card-name count code. |
| "Once per Chain" | `e:SetCountLimit(1,EFFECT_COUNT_CODE_CHAIN)` |
| Shared one-effect-only clauses | Give the related effects the same count code. |

For the full count-code discussion, see [Count Limits And Once Per Turn](count-limits).
The important habit here is to decide the count code before cloning or
registering several related effects. Accidentally sharing a code is just as bad
as forgetting a count limit.

## Reset For Temporary Effects

Effects created in `initial_effect` are usually part of the card's normal text.
Effects created during an operation are usually temporary and should say when
they disappear.

```lua
e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```

The exact reset depends on the card text. A stat boost until the End Phase, a
lingering summon restriction, and a copied effect do not necessarily share the
same reset flags. For the full lifetime pattern, see
[Reset Flags And Effect Duration](reset-flags-and-duration).

## Building Order

The engine does not require every setter to appear in a single exact order, but
readable scripts usually group them like this:

1. User-facing fields: `SetDescription`, `SetCategory`.
2. Shape and timing: `SetType`, `SetCode`, `SetProperty`.
3. Location and limits: `SetRange`, `SetTargetRange`, `SetCountLimit`.
4. Logic and stored data: `SetCondition`, `SetCost`, `SetTarget`,
   `SetOperation`, `SetValue`, `SetLabel`, `SetLabelObject`.
5. Registration: `RegisterEffect` or `Duel.RegisterEffect`.

Keeping that order makes later review much easier.

Relevant API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Effect.Clone`](/api/functions/Effect/Clone)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
- [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit)
- [`Effect.SetLabel`](/api/functions/Effect/SetLabel)
- [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject)
- [`Group.KeepAlive`](/api/functions/Group/KeepAlive)
- [`Group.DeleteGroup`](/api/functions/Group/DeleteGroup)
