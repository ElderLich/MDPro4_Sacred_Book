# Card.SetHint

## Signature

```lua
Card.SetHint(Card c, int type, int value) -> void
```

## Description

Set the card prompt for type c to c
Type can only be the following value, the corresponding value type is
CHINT_TURN Turns
CHINT_CARD card id
CHINT_RACE race
CHINT_ATTRIBUTE property
CHINT_NUMBER number
CHINT_DESC Description

## Parameters

- `c` `Card`
- `type` `int`
- `value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3655`
