# Effects That Apply Continuously

Continuous effects are effects that keep applying while their conditions remain
true, or that watch game events without being activated as a normal Chain Link.
They are common for ATK/DEF updates, restrictions, protection, equip bonuses,
replacement effects, and temporary locks.

## Continuous Is Not One Shape

Several different effect types can feel "continuous":

| Shape | What it usually means |
| --- | --- |
| `EFFECT_TYPE_SINGLE` | A rule about the handler itself. |
| `EFFECT_TYPE_FIELD` | A rule applied to cards or players in a range. |
| `EFFECT_TYPE_EQUIP` | A rule applied by an Equip Card to its equipped monster. |
| `EFFECT_TYPE_CONTINUOUS` | An event watcher or replacement-style effect. |

The exact behavior depends on `SetCode`, `SetRange`, `SetTargetRange`,
`SetTarget`, and `SetValue`.

Continuous effects usually do not have an operation function. They are active
rules that the engine checks while their range, target, and reset conditions
are true. Event-watching continuous effects are the exception: those use a
continuous type with an event code and callback functions.

## Build Order

When a continuous effect does not work, walk through the setters in this order.

| Step | Question | Setter or check |
| --- | --- | --- |
| Effect code | What rule is being applied or watched? | `SetCode` |
| Effect owner shape | Is the rule self-only, outward-facing, equip-based, material-based, or an event watcher? | `SetType` |
| Handler range | Where must the card providing the rule be? | `SetRange`, or `EFFECT_FLAG_SINGLE_RANGE` plus `SetRange` for many self-only continuous rules |
| Affected side or zone | Which cards or players can be affected? | `SetTargetRange` |
| Affected card filter | Which cards inside that range qualify? | `SetTarget` |
| Rule value | What amount, permission, restriction, or replacement answer does the code need? | `SetValue`, or `SetOperation` for event watchers and replacement effects |
| Lifetime | When should a temporary rule expire? | `SetReset` |

Local `c10012614.lua` is the compact field-stat version of this checklist:
`EFFECT_TYPE_FIELD`, `SetRange(LOCATION_SZONE)`,
`SetTargetRange(LOCATION_MZONE,0)`, `SetCode(EFFECT_UPDATE_ATTACK)`, a battle
phase condition, and `SetValue(200)`. Nothing in that shape creates a Chain
Link; it simply applies while the Continuous Spell is face-up and the condition
is true.

## Target And Value Are Not Chain Target And Operation

Activated effects use `SetTarget` for activation legality, Chain target
selection, and operation info. Continuous effects often use the same setter for
a different job: deciding which card or player the continuous rule applies to.

Read these callbacks through the effect shape:

| Continuous shape | Common callback role |
| --- | --- |
| Field stat modifier | `SetTarget` filters affected cards; `SetValue` supplies the amount. |
| Player restriction | `SetTargetRange` chooses affected players; `SetTarget` filters the restricted action. |
| Equip limit | `SetValue` answers whether the equipped card is still legal. |
| Replacement or event watcher | `SetTarget` asks whether to replace or respond; `SetOperation` performs the replacement/action. |

`c10002346.lua` shows both sides on one card. Its ATK/DEF field effects use
`SetValue(c10002346.val)` as a live continuous amount. Its destroy replacement
effect uses `EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE`,
`SetTarget(c10002346.reptg)`, and `SetOperation(c10002346.repop)` because that
continuous effect watches a destruction event instead of constantly applying a
stat value.

## Handler-Only Effects

Use `EFFECT_TYPE_SINGLE` when the card itself gains or loses a property.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

If the effect should only apply in a specific location, add
`EFFECT_FLAG_SINGLE_RANGE` and `SetRange`.

```lua
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetRange(LOCATION_MZONE)
```

For a step-by-step stat-focused version of this pattern, see
[Continuous stat modifiers](continuous-stat-modifiers).

## Field Effects

Field effects apply outward. A common pattern is "while this card is face-up,
your monsters gain ATK."

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_MZONE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(200)
c:RegisterEffect(e1)
```

`SetRange` says where the handler must be. `SetTargetRange` says what the
effect reaches.

## Values Can Be Numbers or Functions

Static values use a number.

```lua
e1:SetValue(800)
```

Dynamic values use a function.

```lua
function s.atkval(e,c)
    return e:GetHandler():GetOverlayCount()*200
end
e1:SetValue(s.atkval)
```

The callback receives the effect and, for many continuous value effects, the
card being affected.

Local script `c10002346.lua` uses this pattern for a field modifier:

```lua
function s.val(e,c)
    return e:GetHandler():GetOverlayCount()*200
end
```

Here `e:GetHandler()` is the card providing the effect, while `c` is each
monster receiving the ATK or DEF update. Recalculate inside the value function
when the amount can change during the Duel.

## Equip Effects

Equip Cards usually register both the bonus and the equip limit.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_EQUIP)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(800)
c:RegisterEffect(e1)

local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_EQUIP_LIMIT)
e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
e2:SetValue(s.eqlimit)
c:RegisterEffect(e2)
```

`s.eqlimit` answers whether the equipped monster is legal for this Equip Card.
The equip activation flow itself is covered in
[Equip Spells and Equip Cards](equip-spells).

## Xyz Material Effects

Some effects apply while the card is attached as Xyz Material. In those cases
the card is not applying a normal field or equip effect; the script uses a
material effect type such as `EFFECT_TYPE_XMATERIAL`.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_XMATERIAL)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

Material effects should be copied from a local script using the same mechanic,
because the correct type flag and effect code depend on how the core reads that
material state.

## Player-Affecting Field Effects

Some continuous field effects apply to players instead of cards. These often
use player target flags and a `SetTargetRange` of players rather than zones.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
e1:SetRange(LOCATION_MZONE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetTargetRange(1,0)
e1:SetTarget(s.splimit)
c:RegisterEffect(e1)
```

Read `SetTargetRange(1,0)` here as "the handler controller is affected; the
opponent is not." With card-zone effects, the same setter is usually a pair of
locations.

## Event Watchers

`EFFECT_TYPE_CONTINUOUS` can watch a game event and run an operation.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE)
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetCode(EFFECT_DESTROY_REPLACE)
e1:SetRange(LOCATION_MZONE)
e1:SetTarget(s.reptg)
e1:SetOperation(s.repop)
c:RegisterEffect(e1)
```

The callback shape depends on the effect code. Replacement effects, phase
watchers, and event watchers do not all ask the same questions.

## TargetRange Means Cards Or Players

`SetTargetRange` has two common modes. The mode is decided by the effect
property and effect code.

| Shape | `SetTargetRange` meaning |
| --- | --- |
| Card-affecting field effect | Locations relative to the handler controller, such as `LOCATION_MZONE,0`. |
| Player-affecting field effect | Player flags such as `1,0` after `EFFECT_FLAG_PLAYER_TARGET`. |

For card ranges, read `SetTargetRange(LOCATION_MZONE,0)` as "the handler
controller's Monster Zone, not the opponent's Monster Zone." For player ranges,
read `SetTargetRange(1,0)` as "the handler controller is affected, not the
opponent." Local scripts such as `c10140443.lua` use the player-target form for
temporary Special Summon restrictions.

## Temporary Continuous Effects

Effects created during resolution need a reset.

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
e1:SetTargetRange(1,0)
e1:SetTarget(s.splimit)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

Without `SetReset`, a temporary restriction can remain longer than the card text
allows.

## Quick Diagnosis

| Symptom | Likely issue |
| --- | --- |
| A self-only effect works in every location. | Missing `EFFECT_FLAG_SINGLE_RANGE` or missing `SetRange`. |
| A field effect applies to the wrong player. | `SetTargetRange` is reversed, or a player-target effect is missing `EFFECT_FLAG_PLAYER_TARGET`. |
| A field stat effect exists but affects no cards. | `SetTargetRange` names the wrong zone, or `SetTarget` filters every candidate out. |
| A value callback returns the same number forever. | The script stored a label once instead of recalculating through `SetValue`. |
| A temporary restriction lasts too long. | Missing or incomplete `SetReset`. |
| An event watcher never fires. | The `SetCode` event, `SetType(EFFECT_TYPE_CONTINUOUS+...)`, range, or callback signature does not match a local script pattern. |

Useful API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Effect.SetReset`](/api/functions/Effect/SetReset)
