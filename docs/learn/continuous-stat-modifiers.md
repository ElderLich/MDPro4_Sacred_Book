# Continuous Stat Modifiers

ATK/DEF changes are one of the easiest ways to learn continuous effects because
the result is visible immediately. The script shape changes depending on who
receives the modifier:

- the handler itself
- cards in a field range
- the equipped monster
- a monster using this card as material

## Choose The Modifier Shape

Pick the effect type by asking who receives the modifier.

| Receiver | Effect type | Key setters |
| --- | --- | --- |
| The handler itself | `EFFECT_TYPE_SINGLE` | `SetCode`, `SetValue`, and usually `EFFECT_FLAG_SINGLE_RANGE` plus `SetRange` |
| Monsters or cards in a zone range | `EFFECT_TYPE_FIELD` | `SetRange`, `SetTargetRange`, optional `SetTarget`, `SetValue` |
| The equipped monster | `EFFECT_TYPE_EQUIP` | `SetCode`, `SetValue`, plus a separate `EFFECT_EQUIP_LIMIT` |
| The monster using this card as Xyz Material | `EFFECT_TYPE_XMATERIAL` | Material effect type, effect code, and value |
| A temporary boost from an activated effect | Usually `EFFECT_TYPE_SINGLE` registered during resolution | `SetReset` is required |

The value can be a fixed number or a callback. Use a callback when the amount
depends on current cards, Levels, counters, materials, or another changing
state.

## Pick The Stat Code

The effect code tells the engine what the value means.

| Text shape | Common code family | What the value means |
| --- | --- | --- |
| "gains/loses 500 ATK" | `EFFECT_UPDATE_ATTACK` or `EFFECT_UPDATE_DEFENSE` | Add or subtract from the current stat. |
| "ATK becomes 0" as an always-on rule | `EFFECT_SET_ATTACK` or `EFFECT_SET_DEFENSE` | Set the stat while the continuous rule applies. |
| "ATK becomes 0 until..." from a resolving effect | `EFFECT_SET_ATTACK_FINAL` or `EFFECT_SET_DEFENSE_FINAL` | Set a final temporary value with the reset used by the resolving effect. |

Do not use `EFFECT_UPDATE_ATTACK` for every ATK-related text. If the card says a
stat "becomes" a value, look for a matching local script and copy the set-style
code family and reset pattern. If the card says it gains or loses an amount,
`EFFECT_UPDATE_ATTACK` or `EFFECT_UPDATE_DEFENSE` is usually the right family.

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

Here are common dynamic sources:

```lua
function s.levelval(e,c)
    return c:GetLevel()*200
end
```

```lua
function s.oppdragonval(e,c)
    return Duel.GetMatchingGroupCount(s.dragonfilter,c:GetControler(),0,
        LOCATION_MZONE+LOCATION_GRAVE,nil)*500
end
```

Use the affected card `c` when the value depends on the card receiving the
modifier. Use `e:GetHandler()` when the value depends on the card providing the
modifier.

## Value Functions Do Not Receive `tp`

Continuous value callbacks usually receive `(e,c)`, not the activated-effect
callback list. If the value needs a player as a reference, derive it from the
effect or the affected card.

```lua
function s.val(e,c)
    local tp=e:GetHandlerPlayer()
    return Duel.GetMatchingGroupCount(s.filter,tp,0,LOCATION_MZONE,nil)*500
end
```

Use `e:GetHandlerPlayer()` when the card providing the effect defines the
reference player. Use `c:GetControler()` when each affected card should use its
own controller. Local `c10000020.lua` uses `c:GetControler()` in its stat value
because the amount is based on the affected card's controller's hand.

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

Local `c10002346.lua` uses the field-modifier version of this idea. It applies
ATK and DEF updates to the controller's monsters, and the value function reads
the handler's current Xyz Material count:

```lua
function s.val(e,c)
    return e:GetHandler():GetOverlayCount()*200
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

When the value depends on the equipped monster, use the affected card `c`.

```lua
function s.eqlevelval(e,c)
    return c:GetLevel()*100
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

Dynamic Xyz Material values can read the affected Xyz Monster.

```lua
function s.xyzval(e,c)
    return c:GetOverlayCount()*300
end
```

Always verify material-effect patterns against local scripts for the mechanic
you are copying. Material effects are sensitive to the exact effect type and
where the engine expects the card to be.

## Dynamic Field Modifier

Field modifiers can use the affected card in the same way.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetTarget(s.rttg)
e1:SetValue(s.rtval)
c:RegisterEffect(e1)

function s.rttg(e,c)
    return c:IsFaceup() and c:IsType(TYPE_RITUAL)
end

function s.rtval(e,c)
    return c:GetLevel()*100
end
```

The value callback is run for each affected monster, so `c` is the monster
being modified, not necessarily the handler.

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
- [`Duel.GetMatchingGroupCount`](/api/functions/Duel/GetMatchingGroupCount)
- [`Effect.GetHandlerPlayer`](/api/functions/Effect/GetHandlerPlayer)
