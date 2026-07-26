# Card.AssumeProperty

## Signature

```lua
Card.AssumeProperty(Card c, int assume_type, int assume_value) -> void
```

## Description

Temporarily assumes one property of c for core checks.
assume_type is one of ASSUME_CODE, ASSUME_TYPE, ASSUME_LEVEL, ASSUME_RANK, ASSUME_ATTRIBUTE, ASSUME_RACE, ASSUME_ATTACK, or ASSUME_DEFENSE.

## Parameters

- `c` `Card`
- `assume_type` `int`
- `assume_value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3663`
