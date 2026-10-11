# Card.GetCardType

## Signature

```lua
Card.GetCardType(Card c) -> int
```

## Description

Returns the card-type bitmask after EFFECT_ADD_CARD_TYPE, EFFECT_REMOVE_CARD_TYPE and EFFECT_CHANGE_CARD_TYPE are applied to the printed type. Unlike GetType, it does not apply ordinary EFFECT_*_TYPE modifiers or the Pendulum Zone conversion.

## Parameters

- `c` `Card`

## Returns

- `int` - Card-type bitmask; test with TYPE_* constants.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3449`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
