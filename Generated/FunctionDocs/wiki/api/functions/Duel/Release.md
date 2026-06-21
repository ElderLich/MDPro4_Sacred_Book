# Duel.Release

## Signature

```lua
Duel.Release(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

The reason for the liberation of targets to return the value of the actual liberation of the number of targets
If the reason contains REASON_COST, it will not check whether the card is not affected by the effect

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4881`
