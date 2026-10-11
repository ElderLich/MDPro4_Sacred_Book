# Card.IsPreviousCardTypeOnField

## Signature

```lua
Card.IsPreviousCardTypeOnField(Card c, int type) -> bool
```

## Description

Returns true if at least one requested TYPE_* bit is present in the previous on-field card-type snapshot.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3535`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
