# Control Change

Changing control means the card stays on the field but its controller changes.
Do not move the card manually with a send or summon function. Use the control
APIs so the engine can update zones, control-change resets, equipment state,
and effect checks.

## The Basic Take-Control Shape

Change of Heart (`c4031928.lua`) is the small baseline:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsLocation(LOCATION_MZONE)
            and chkc:IsControler(1-tp)
            and chkc:IsControlerCanBeChanged()
    end
    if chk==0 then
        return Duel.IsExistingTarget(Card.IsControlerCanBeChanged,tp,0,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONTROL)
    local g=Duel.SelectTarget(tp,Card.IsControlerCanBeChanged,tp,0,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_CONTROL,g,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) then
        Duel.GetControl(tc,tp,PHASE_END,1)
    end
end
```

[`Duel.GetControl`](/api/functions/Duel/GetControl) changes control to the
given player. `PHASE_END,1` makes the control change temporary until the End
Phase. Omit those arguments for a permanent control change.

## Legality Checks

Use the local control helpers instead of hardcoding your own rule list.

| Check | Common use |
| --- | --- |
| [`Card.IsControlerCanBeChanged`](/api/functions/Card/IsControlerCanBeChanged) | A direct take-control target. It includes Monster Zone availability unless told to ignore it. |
| [`Card.IsAbleToChangeControler`](/api/functions/Card/IsAbleToChangeControler) | A broader "this card may change control" check, useful before swap-control logic. |
| [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount) | Manual zone-space checks, especially for swaps where each player will receive a card. |

The API uses the engine spelling `Controler` in function names. In prose, use
"controller".

## Use The Return Value

`Duel.GetControl` returns the number of cards whose control actually changed.
Mind Control (`c37520316.lua`) uses that return before adding the attack and
Tribute restrictions:

```lua
if tc:IsRelateToEffect(e) and Duel.GetControl(tc,tp,PHASE_END,1)~=0 then
    local reset=RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_UNRELEASABLE_SUM)
    e1:SetReset(reset)
    e1:SetValue(1)
    tc:RegisterEffect(e1)
    local e2=e1:Clone()
    e2:SetCode(EFFECT_UNRELEASABLE_NONSUM)
    tc:RegisterEffect(e2)
    local e3=e1:Clone()
    e3:SetCode(EFFECT_CANNOT_ATTACK)
    tc:RegisterEffect(e3)
end
```

That matters because the follow-up restrictions only make sense if the monster
actually came under your control.

## Swap Control

Swap effects need two cards and enough Monster Zone space after both cards
leave their current zones. Mind Castlin (`c12172567.lua`) checks both sides
with `LOCATION_REASON_CONTROL`:

```lua
function s.swapfilter(c)
    local tp=c:GetControler()
    return c:IsAbleToChangeControler()
        and Duel.GetMZoneCount(tp,c,tp,LOCATION_REASON_CONTROL)>0
        and c:IsFaceup()
end
```

Its operation then swaps the handler with the selected opponent's monster:

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) and tc and tc:IsRelateToEffect(e) then
        Duel.SwapControl(c,tc)
    end
end
```

[`Duel.SwapControl`](/api/functions/Duel/SwapControl) can also take reset
phase/count arguments for temporary swaps.

## Continuous Control From Equip Cards

Some cards do not call `Duel.GetControl` after activation. They equip to the
monster, then apply a continuous equip effect that sets the controller.

Comic Hand (`c33453260.lua`) equips to an opponent's monster and registers:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_EQUIP)
e3:SetCode(EFFECT_SET_CONTROL)
e3:SetValue(s.cval)
c:RegisterEffect(e3)

function s.cval(e,c)
    return e:GetHandlerPlayer()
end
```

That is an equip relationship. If the Equip Card stops applying or leaves the
field, the continuous control rule stops applying too.

## Owner And Controller

Control changes do not change ownership. The owner is the player whose card it
is; the controller is the player currently controlling it.

Use the right question:

| Question | Function |
| --- | --- |
| Who controls this card right now? | [`Card.GetControler`](/api/functions/Card/GetControler) |
| Is this card currently controlled by player `p`? | [`Card.IsControler`](/api/functions/Card/IsControler) |
| Who owns this card? | [`Card.GetOwner`](/api/functions/Card/GetOwner) |

Most take-control effects care about current controller. Some immunity or
ownership-based text cares about owner instead.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Sending a monster to another zone to represent control change. | Use `Duel.GetControl` or `Duel.SwapControl`. |
| Forgetting Monster Zone space. | Use `Card.IsControlerCanBeChanged` for direct take-control effects or `Duel.GetMZoneCount` for swaps. |
| Adding follow-up restrictions even when control did not change. | Check `Duel.GetControl(...)~=0`. |
| Using owner checks when the text cares about current control. | Use controller functions for "your opponent controls" and owner functions for ownership text. |
| Targeting a monster that cannot change control. | Put `IsControlerCanBeChanged` or `IsAbleToChangeControler` in the target filter. |
| Treating equip-based control like a one-time control change. | Use `EFFECT_SET_CONTROL` on the Equip Card when the control is maintained by the equip relationship. |

Useful API pages:

- [`Duel.GetControl`](/api/functions/Duel/GetControl)
- [`Duel.SwapControl`](/api/functions/Duel/SwapControl)
- [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount)
- [`Card.IsControlerCanBeChanged`](/api/functions/Card/IsControlerCanBeChanged)
- [`Card.IsAbleToChangeControler`](/api/functions/Card/IsAbleToChangeControler)
- [`Card.GetControler`](/api/functions/Card/GetControler)
- [`Card.GetOwner`](/api/functions/Card/GetOwner)
