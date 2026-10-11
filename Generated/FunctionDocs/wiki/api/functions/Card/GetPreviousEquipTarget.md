# Card.GetPreviousEquipTarget

## Signature

```lua
Card.GetPreviousEquipTarget(Card c) -> Card|nil
```

## Description

Returns c's previous Equip target, or nil.
Use this for lost-target and sent-from-field Equip Card triggers after the live equip relationship is gone.

## How To Use It

Use this after an Equip Card has left its equip relationship and the effect needs to know which monster it was previously equipped to.

```lua
local ec=e:GetHandler():GetPreviousEquipTarget()
return e:GetHandler():IsReason(REASON_LOST_TARGET) and ec~=nil
```

This is the usual read for lost-target or sent-from-field Equip Card triggers. It is not a live equip relationship.

## Related Functions

- [Card.GetEquipTarget](/api/functions/Card/GetEquipTarget)
- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.IsReason](/api/functions/Card/IsReason)

## Parameters

- `c` `Card`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3575`
