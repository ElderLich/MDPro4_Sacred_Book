# Continuous Stat Modifiers

ATK/DEF changes are one of the easiest ways to learn continuous effects because
the result is visible immediately. The script shape changes depending on who
receives the modifier:

- the handler itself
- cards in a field range
- the equipped monster
- a monster using this card as material

## Handler-Only Modifier

Use `EFFECT_TYPE_SINGLE` when the card modifies itself.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

If the modifier should only apply while the card is in a specific location,
add `EFFECT_FLAG_SINGLE_RANGE` and `SetRange`.

```lua
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetRange(LOCATION_MZONE)
```

Without the range property, `SetRange` is not the normal way to bind a single
continuous stat modifier to a location.

## Dynamic Self Modifier

`SetValue` can receive a function. For many stat modifiers, the callback is
called with the effect and the affected card.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetValue(s.atkval)
c:RegisterEffect(e1)

function s.atkval(e,c)
    return Duel.GetMatchingGroupCount(s.filter,c:GetControler(),LOCATION_MZONE,0,nil)*400
end
```

This shape is used by local scripts for monsters whose ATK depends on other
face-up monsters.

## Field Modifier

Use `EFFECT_TYPE_FIELD` when a card changes other cards in a range.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(0,LOCATION_MZONE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(s.val)
c:RegisterEffect(e1)
```

`SetRange` says where the handler must be. `SetTargetRange` says which zones
the modifier reaches.

```lua
function s.val(e,c)
    return Duel.GetMatchingGroupCount(s.vfilter,e:GetOwnerPlayer(),LOCATION_MZONE,0,nil)*-300
end
```

If the modifier only applies to some cards in the target range, add
`SetTarget`.

```lua
e1:SetTarget(s.tg)

function s.tg(e,c)
    return c:IsFaceup() and c:IsSetCard(0x123)
end
```

## Equip Modifier

Equip Cards use `EFFECT_TYPE_EQUIP` because the affected card is the equipped
monster.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_EQUIP)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(800)
c:RegisterEffect(e1)
```

When the value depends on the Equip Card, read from `e:GetHandler()`.

```lua
function s.atkval(e,c)
    return e:GetHandler():GetCounter(0x1)*500
end
```

Equip modifiers usually belong beside an Equip activation effect and an
`EFFECT_EQUIP_LIMIT` effect. See [Equip Spells and Equip Cards](equip-spells).

## Xyz Material Modifier

Some cards grant a continuous modifier while they are attached as Xyz Material.
Those effects use a material-related effect type such as
`EFFECT_TYPE_XMATERIAL`, combined with the effect code and value that the card
grants.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_XMATERIAL)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

Always verify material-effect patterns against local scripts for the mechanic
you are copying. Material effects are sensitive to the exact effect type and
where the engine expects the card to be.

## Temporary Stat Modifier

When an activated effect creates a temporary modifier, register the new effect
on the affected card and give it a reset.

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(1000)
e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
tc:RegisterEffect(e1)
```

The reset is not decoration. It is what makes the modifier expire when the card
leaves the expected state or the duration ends.

## Clone for ATK and DEF

When ATK and DEF use the same range, target, and value, clone the effect and
change only the code.

```lua
local e2=e1:Clone()
e2:SetCode(EFFECT_UPDATE_DEFENSE)
c:RegisterEffect(e2)
```

This keeps paired stat modifiers consistent.

## Quick Diagnosis

| Symptom | Likely issue |
| --- | --- |
| Modifier applies everywhere. | Missing `EFFECT_FLAG_SINGLE_RANGE` or wrong `SetRange`. |
| Field modifier hits the wrong side. | Check `SetTargetRange` and controller-relative ranges. |
| Equip bonus affects the Equip Card instead of the monster. | Use `EFFECT_TYPE_EQUIP`. |
| Temporary bonus never expires. | Add the correct `SetReset`. |
| Dynamic value is stale. | Recalculate in the `SetValue` function instead of storing once. |

Useful API pages:

- [`Effect.SetValue`](/api/functions/Effect/SetValue)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.Clone`](/api/functions/Effect/Clone)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
