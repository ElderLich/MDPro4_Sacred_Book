# Card.GetRightScale

## Signature

```lua
Card.GetRightScale(Card c) -> int
```

## Description

Returns c's current right Pendulum Scale value.
While c is in a Pendulum Zone, the core applies EFFECT_UPDATE_RSCALE and EFFECT_CHANGE_RSCALE modifiers. Outside a Pendulum Zone, it returns the card-data right scale.

## Parameters

- `c` `Card`

## Returns

- `int` - Current right Pendulum Scale value.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3418`
