# EFFECT_TYPE Constants and Templates

`SetType` decides the broad shape of an effect. These constants are engine
shape flags, not official card-text labels. There is no single universal
"Trigger Effect" type to copy for every trigger. A trigger on the handler, a
trigger watched from the field, and a trigger granted while the card is Xyz
Material all use different combinations.

Some scripts combine values with `+` because a field trigger, for example, is
both `EFFECT_TYPE_FIELD` and `EFFECT_TYPE_TRIGGER_O`.

## Common Types

| Type | Typical use | Common companion setters |
| --- | --- | --- |
| `EFFECT_TYPE_ACTIVATE` | Activating a Spell/Trap Card. | `SetCode(EVENT_FREE_CHAIN)`, `SetTarget`, `SetOperation` |
| `EFFECT_TYPE_IGNITION` | An effect the turn player chooses to activate in an open game state. | `SetRange`, `SetCountLimit`, `SetTarget`, `SetOperation` |
| `EFFECT_TYPE_TRIGGER_O` | Optional trigger effect. | `SetCode`, `SetProperty(EFFECT_FLAG_DELAY)` when needed |
| `EFFECT_TYPE_TRIGGER_F` | Mandatory trigger effect. | `SetCode`, `SetCondition`, `SetOperation` |
| `EFFECT_TYPE_QUICK_O` | Optional fast effect. | `SetCode(EVENT_FREE_CHAIN)`, timing hints, count limits |
| `EFFECT_TYPE_SINGLE` | Continuous property of the handler itself. | `SetCode`, `SetValue`, sometimes `SetCondition` |
| `EFFECT_TYPE_FIELD` | Applies to cards or players in a range. | `SetRange`, `SetTargetRange`, `SetTarget` |
| `EFFECT_TYPE_CONTINUOUS` | Watches an event and runs without becoming an activated Chain Link. | `SetCode`, `SetOperation` |
| `EFFECT_TYPE_EQUIP` | Equip Card effect applied to the equipped monster. | `SetCode`, `SetValue` |
| `EFFECT_TYPE_XMATERIAL` | Effect applied while the card is Xyz Material. | `SetCode`, `SetValue` |
| `EFFECT_TYPE_GRANT` | A field-style effect that grants another effect to matching cards. | `SetTargetRange`, `SetTarget`, `SetLabelObject` |

## Choosing A Type Shape

Pick the shape from what the effect object does, then fill in `SetCode`, range,
properties, and callbacks.

| Need | Common type shape |
| --- | --- |
| Spell/Trap Card activation. | `EFFECT_TYPE_ACTIVATE` |
| Player chooses an effect in an open game state. | `EFFECT_TYPE_IGNITION` |
| Fast optional response. | `EFFECT_TYPE_QUICK_O` |
| Handler itself has an optional event trigger. | `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O` |
| Handler itself has a mandatory event trigger. | `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F` |
| A card in range watches a field, player, or phase event and may activate. | `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O` |
| A card in range watches a mandatory field, player, or phase event. | `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F` |
| A non-chain watcher, replacement, or rule callback. | `EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE` or `EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_FIELD` |
| A continuous rule on the handler. | `EFFECT_TYPE_SINGLE` |
| A continuous rule applied outward to cards or players. | `EFFECT_TYPE_FIELD` |
| An Equip Card's applying modifier. | `EFFECT_TYPE_EQUIP` |
| A rule or activated effect gained by the monster using this card as Xyz Material. | `EFFECT_TYPE_XMATERIAL` plus the rule or activated type |
| A field effect that grants an effect object to matching cards. | `EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT` |

## Activate, Ignition, Trigger, Quick

Activated effects form Chain Links. Their callbacks usually follow the
condition/cost/target/operation pattern.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.drtg)
e1:SetOperation(s.drop)
c:RegisterEffect(e1)
```

Use this family when card text says the player activates an effect, chooses to
do something, or responds to timing.

See [Activated effects](activated-effects) for the full Chain Link lifecycle.
See [Spell Card Patterns](spell-card-patterns) and [Trap Card Patterns](trap-card-patterns)
for how card type changes the activation speed and follow-up effects.

For Continuous Spells/Traps or Field Spells whose card activation does nothing
special, the activation effect can be very small.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e1)
```

The card's continuous behavior is then registered as separate effects.

Quick Effects often need hint timing so the client asks at useful windows.

```lua
e1:SetType(EFFECT_TYPE_QUICK_O)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_MAIN_END)
```

See [Categories, Properties, And Hint Timing](categories-properties-and-hints)
for the deeper metadata layer: category flags, operation info, target flags,
Damage Step properties, and client prompts.

## Common Combinations

Effect types are bit flags. Scripts combine them when one effect needs both a
source shape and an activation/timing shape.

| Combination | Read it as |
| --- | --- |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O` | The handler has an optional trigger. |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F` | The handler has a mandatory trigger. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O` | A card in a range watches a field event and may activate. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F` | A card in a range watches a field event and must activate when legal. |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_FLIP` | A Flip Effect on the handler. |
| `EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE` | A continuous watcher or replacement effect tied to the handler. |
| `EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_FIELD` | A continuous watcher applied from a field range. |
| `EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_IGNITION` | The Xyz Monster gets an Ignition Effect while this card is material. |
| `EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_QUICK_O` | The Xyz Monster gets a Quick Effect while this card is material. |
| `EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_TRIGGER_O` | The Xyz Monster gets an optional trigger while this card is material. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT` | A live field effect grants another effect object to matching cards. |

Local scripts use both `+` and bitwise-style constants for these combinations.
Read either form as "this effect has all of these type flags."

## Trigger Source Shapes

Trigger type flags only tell the engine that an effect can activate from an
event. The source flag tells the engine where the trigger lives.

| Shape | Read it as |
| --- | --- |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O` | This card itself saw the event and may activate. |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F` | This card itself saw the event and must activate when legal. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O` | This card is in range and watches an event that can involve other cards or players. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F` | This card is in range and watches a mandatory event. |

`EVENT_*` goes in `SetCode`; optional versus mandatory comes from
`EFFECT_TYPE_TRIGGER_O` versus `EFFECT_TYPE_TRIGGER_F`. Damage Step behavior is
not automatic. Copy the local script pattern for the exact event and add the
same Damage Step properties or conditions only when the local pattern needs
them.

## Flip Effects

Flip Effects usually combine the handler shape with `EFFECT_TYPE_FLIP`.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_FLIP)
e1:SetOperation(s.flipop)
c:RegisterEffect(e1)
```

If the Flip Effect also targets or has a cost-like activation check, add the
same callback discipline used by other activated effects.

## Single Effects

`EFFECT_TYPE_SINGLE` describes the handler itself. It is often used for
immunity, material restrictions, ATK/DEF changes, equip limits, and special
rules about how the card can be Summoned.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

If the value only applies while the handler is in a specific place, add
`EFFECT_FLAG_SINGLE_RANGE` and `SetRange`.

## Field Effects

`EFFECT_TYPE_FIELD` applies outward from its handler or from a temporary Duel
effect. It usually needs a range and a target range.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_MZONE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(200)
c:RegisterEffect(e1)
```

With normal range handling, `SetTargetRange(a,b)` means the handler controller's
side first and the opponent's side second. With `EFFECT_FLAG_ABSOLUTE_RANGE`,
those fields mean player 0 and player 1 instead.

Some effects use the same setter in a special mode. With
`EFFECT_FLAG_SPSUM_PARAM`, `SetTargetRange` stores Special Summon position and
destination player data instead of affected card locations. See
[Creation, Building, and Registration of an Effect Object](effect-object) for
the target-range mode table.

## Continuous Event Watchers

`EFFECT_TYPE_CONTINUOUS` often appears with `EFFECT_TYPE_SINGLE` or
`EFFECT_TYPE_FIELD`. It watches an event and runs an operation.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_DESTROY_REPLACE)
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetRange(LOCATION_MZONE)
e1:SetTarget(s.reptg)
e1:SetOperation(s.repop)
c:RegisterEffect(e1)
```

This does not behave like an activated effect with a normal Chain Link. The
callback shape depends on the continuous effect code.

## Equip Effects

`EFFECT_TYPE_EQUIP` applies from an Equip Card to the equipped monster.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_EQUIP)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(800)
c:RegisterEffect(e1)
```

Equip Cards usually also register an `EFFECT_EQUIP_LIMIT` single effect so the
client knows which monster the card may remain equipped to.

## Material And Granted Effects

Some effects apply only while the card is used as material. Xyz Material
effects commonly use `EFFECT_TYPE_XMATERIAL` with a normal effect code and
value.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_XMATERIAL)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

`EFFECT_TYPE_XMATERIAL` can also combine with an activated type. Local
`c99229085.lua` grants the Xyz Monster an Ignition Effect while the card is
material:

```lua
local e2=Effect.CreateEffect(c)
e2:SetDescription(aux.Stringid(id,1))
e2:SetType(EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_IGNITION)
e2:SetCondition(s.effcon)
e2:SetCost(aux.dxmcostgen(1,1,nil))
e2:SetTarget(s.destg)
e2:SetOperation(s.desop)
c:RegisterEffect(e2)
```

Do not add `SetRange` to that material effect just because ordinary Ignition
Effects usually have one. The material type changes where the effect is gained
from.

Granted effects use a separate effect object stored with `SetLabelObject`. The
granting effect decides which cards receive that object.

```lua
local ge=Effect.CreateEffect(c)
ge:SetType(EFFECT_TYPE_SINGLE)
ge:SetCode(EFFECT_UPDATE_ATTACK)
ge:SetValue(500)

local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT)
e1:SetRange(LOCATION_SZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetTarget(s.gtarget)
e1:SetLabelObject(ge)
c:RegisterEffect(e1)
```

The grant target callback receives the granting effect and the possible
recipient card:

```lua
function s.gtarget(e,c)
    return c:IsFaceup() and c:IsSetCard(0x123)
end
```

Local `c10604644.lua` uses this shape with `SetRange(LOCATION_SZONE)`,
`SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)`, a two-argument recipient
filter, and `SetLabelObject` to provide the granted effect object while the
granting card remains live.

When you copy a procedure, material, or grant template, verify the exact local
script pattern for that mechanic. These effects are more sensitive to the
effect type than a normal Ignition Effect.

Useful API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject)
- [Constants](/api/constants)
