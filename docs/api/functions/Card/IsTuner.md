# Card.IsTuner

## Signature

```lua
Card.IsTuner(Card c, Card scard) -> bool
```

## Description

Checks whether c is a Tuner monster for scard.
Besides TYPE_TUNER, this also checks effects that can make c be treated as a Tuner.

## Parameters

- `c` `Card`
- `scard` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3506`
