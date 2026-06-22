# EFFECT_TYPE Constants and Templates

`SetType` decides the broad shape of an effect. Some scripts combine values with
`+` because a field trigger, for example, is both `EFFECT_TYPE_FIELD` and
`EFFECT_TYPE_TRIGGER_O`.

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

See all values in [constants](/api/constants).
