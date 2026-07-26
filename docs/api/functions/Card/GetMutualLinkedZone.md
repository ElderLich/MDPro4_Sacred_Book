# Card.GetMutualLinkedZone

## Signature

```lua
Card.GetMutualLinkedZone(Card c, [int player]) -> int
```

## Description

Returns the zone mask of c's mutually linked zones, swapped to player viewpoint when a player argument opposite c's controller is supplied.

## Parameters

- `c` `Card`
- `player` `int` optional - default: c:GetControler()

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3427`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
