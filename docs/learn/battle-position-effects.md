# Battle Position Effects

Battle position effects either change a card once during resolution or apply a
rule that forces or prevents a position change. Keep those two shapes separate:
one calls a `Duel` action, the other registers an effect.

## One-Time Position Changes

Book of Moon (`c14087893.lua`) targets a face-up monster that can be Set, then
turns it to face-down Defense Position at resolution:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsCanTurnSet()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
        Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
    end
end
```

Use [`Card.IsCanTurnSet`](/api/functions/Card/IsCanTurnSet) for effects that
turn a card face-down. The local API page notes that this returns false for
Link Monsters, Tokens, already face-down cards, and cards or players affected
by `EFFECT_CANNOT_TURN_SET`.

## Face-Up Attack And Defense Changes

Enemy Controller (`c98045062.lua`) shows a simple face-up position change:

```lua
function s.filter1(c)
    return c:IsFaceup() and c:IsCanChangePosition()
end

if tc and tc:IsRelateToEffect(e) and tc:IsFaceup() then
    Duel.ChangePosition(tc,POS_FACEUP_DEFENSE,0,POS_FACEUP_ATTACK,0)
end
```

Use [`Card.IsCanChangePosition`](/api/functions/Card/IsCanChangePosition) for
general effect-driven position changes. In this MDPro3/YGOPro core, that
helper returns false for Link Monsters.

## Duel.ChangePosition Argument Order

[`Duel.ChangePosition`](/api/functions/Duel/ChangePosition) accepts one card or
a group. The first position argument is the destination for cards currently in
face-up Attack Position. The optional arguments handle the other starting
positions.

| Argument | Current position it handles |
| --- | --- |
| `au` | Face-up Attack Position |
| `ad` | Face-down Attack Position |
| `du` | Face-up Defense Position |
| `dd` | Face-down Defense Position |

If the optional values are omitted, the core uses the first destination for
all starting positions.

```lua
Duel.ChangePosition(tc,POS_FACEUP_DEFENSE)
Duel.ChangePosition(tc,POS_FACEUP_DEFENSE,POS_FACEDOWN_DEFENSE,POS_FACEUP_ATTACK,POS_FACEUP_ATTACK)
```

The function returns the number of cards whose position actually changed. Use
that return when the next part of the effect depends on the position change
happening.

## Set Versus Change Position

Turning a monster face-down is often described as "Set" in official text, but
the script action is still usually `Duel.ChangePosition`:

```lua
Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
```

Use [`Duel.MSet`](/api/functions/Duel/MSet) when the effect actually Normal
Sets or Sets a monster from a hand-like location. Use `Duel.ChangePosition`
when the card is already on the field and its battle position changes.

## Forced Position Rules

Some cards continuously force monsters into a position. Those do not call
`Duel.ChangePosition` every time. They register a field effect.

Cosmic Slicer Zer'oll's local script (`c1487805.lua`) applies
`EFFECT_SET_POSITION` to opponent's monsters with a specific counter:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_FIELD)
e3:SetCode(EFFECT_SET_POSITION)
e3:SetRange(LOCATION_MZONE)
e3:SetTargetRange(0,LOCATION_MZONE)
e3:SetTarget(s.actg)
e3:SetValue(POS_FACEUP_DEFENSE)
c:RegisterEffect(e3)

function s.actg(e,c)
    return c:IsFaceup() and c:GetCounter(0x100e)>0
end
```

Knight Dragolich (`c88724332.lua`) uses the same effect code for monsters
Special Summoned from the Deck or Extra Deck:

```lua
e1:SetCode(EFFECT_SET_POSITION)
e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
e1:SetValue(POS_FACEUP_DEFENSE)
```

Use this shape when the text creates a lasting rule, not a one-time position
change at resolution.

## Preventing Position Changes

Preventing position changes is also a registered effect.

Wattsquirrel (`c12296376.lua`) gives the battled monster
`EFFECT_CANNOT_CHANGE_POSITION`:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_CANNOT_CHANGE_POSITION)
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
bc:RegisterEffect(e1)
```

Use `EFFECT_CANNOT_TURN_SET` for text that specifically prevents turning a
card face-down. Use `EFFECT_CANNOT_CHANGE_POSITION` for broader position-change
prevention.

## Targeting And Resolution Checklist

For a targeting position effect, usually check:

| Stage | Check |
| --- | --- |
| Target filter | `c:IsFaceup()` plus `IsCanTurnSet` or `IsCanChangePosition`. |
| `chk==0` branch | At least one legal target exists. |
| Target selection | `Duel.SelectTarget` and `CATEGORY_POSITION` operation info. |
| Resolution | Target is still related, still in the Monster Zone, and still in the expected visible state. |

The target branch proves that the effect can be activated. The operation
should still recheck the parts that can change before resolution.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Targeting a monster without checking whether it can change position. | Use `IsCanChangePosition` or `IsCanTurnSet` in the target filter. |
| Using `IsCanChangePosition` for a face-down Set effect. | Use `IsCanTurnSet` when the result is face-down Defense Position. |
| Forgetting that Link Monsters cannot be placed in Defense Position. | Let the local helper reject them instead of hardcoding a type list. |
| Calling `Duel.ChangePosition` without checking relation at resolution. | Recheck `tc:IsRelateToEffect(e)` before changing a targeted card. |
| Using a one-time operation for a lasting forced-position rule. | Register `EFFECT_SET_POSITION` with a target and value. |
| Using `Duel.MSet` on a monster that is already on the field. | Use `Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)`. |

Useful API pages:

- [`Duel.ChangePosition`](/api/functions/Duel/ChangePosition)
- [`Duel.MSet`](/api/functions/Duel/MSet)
- [`Card.IsCanChangePosition`](/api/functions/Card/IsCanChangePosition)
- [`Card.IsCanTurnSet`](/api/functions/Card/IsCanTurnSet)
- [`Card.IsPosition`](/api/functions/Card/IsPosition)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
