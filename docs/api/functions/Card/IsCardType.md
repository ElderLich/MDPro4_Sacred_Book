# Card.IsCardType

## Signature

```lua
Card.IsCardType(Card c, int type) -> bool
```

## Description

Returns true if at least one bit in type is present in c:GetCardType(). Use IsAllCardTypes when every requested bit must match.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3533`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
