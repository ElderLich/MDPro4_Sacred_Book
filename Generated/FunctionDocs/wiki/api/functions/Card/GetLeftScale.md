# Card.GetLeftScale

## Signature

```lua
Card.GetLeftScale(Card c) -> int
```

## Description

Returns c's current left Pendulum Scale value.
While c is in a Pendulum Zone, the core applies EFFECT_UPDATE_LSCALE and EFFECT_CHANGE_LSCALE modifiers. Outside a Pendulum Zone, it returns the card-data left scale.

## Parameters

- `c` `Card`

## Returns

- `int` - Current left Pendulum Scale value.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3464`
