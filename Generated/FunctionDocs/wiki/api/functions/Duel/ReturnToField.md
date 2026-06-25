# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool|nil
```

## Description

Returns a card temporarily removed from the field to its previous controller and previous location.
pos defaults to the previous position and zone defaults to 0xff. If c was not removed for REASON_TEMPORARY, the binding returns no Lua value; otherwise it yields and returns whether the move succeeded.
Use this only for temporary removal lifecycles, not as a generic way to place cards on the field.

## How To Use It

Use this to close a real temporary-banish lifecycle. The card should have left the field with `Duel.Remove(..., REASON_EFFECT+REASON_TEMPORARY)` or an equivalent temporary removal reason.

```lua
if Duel.Remove(tc,0,REASON_EFFECT+REASON_TEMPORARY)>0 then
    e1:SetLabelObject(tc)
end

local rc=e:GetLabelObject()
if rc then
    Duel.ReturnToField(rc)
end
```

Do not use this as a generic field-placement helper. Use `Duel.SpecialSummon`, `Duel.SSet`, `Duel.MSet`, `Duel.Equip`, or `Duel.MoveToField` for ordinary placement actions.

## Related Functions

- [Duel.Remove](/api/functions/Duel/Remove)
- [Card.IsReason](/api/functions/Card/IsReason)
- [Duel.MoveToField](/api/functions/Duel/MoveToField)

## Parameters

- `c` `Card`
- `pos` `int` optional - default: previous position
- `zone` `int` optional - default: 0xff

## Returns

- `bool|nil` - Success flag, or nil if c was not temporarily removed from the field.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`
