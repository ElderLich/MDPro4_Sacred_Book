# Card.GetPreviousCardTypeOnField

## Signature

```lua
Card.GetPreviousCardTypeOnField(Card c) -> int
```

## Description

Returns the card-type bitmask saved in the previous on-field state, before the card moved. This is the previous GetCardType value, not the previous ordinary GetType value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3498`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
