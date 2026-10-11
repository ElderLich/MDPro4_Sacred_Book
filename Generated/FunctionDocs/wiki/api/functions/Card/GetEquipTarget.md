# Card.GetEquipTarget

## Signature

```lua
Card.GetEquipTarget(Card c) -> Card|nil
```

## Description

Returns the card that c is currently equipped to, or nil if c has no equip target.
Use this while the Equip Card is still equipped. After it leaves the relationship, use Card.GetPreviousEquipTarget for leave-field triggers.

## How To Use It

Use this while the card is currently equipped and you need the monster it is equipped to.

```lua
local ec=e:GetHandler():GetEquipTarget()
if ec and ec:IsFaceup() then
    -- use the equipped monster
end
```

After the Equip Card leaves the field, this relationship is gone. Use `Card.GetPreviousEquipTarget` in leave-field or sent-to-GY triggers.

## Related Functions

- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.GetPreviousEquipTarget](/api/functions/Card/GetPreviousEquipTarget)
- [Card.GetEquipGroup](/api/functions/Card/GetEquipGroup)

## Parameters

- `c` `Card`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3574`
