# Duel.IsPlayerCanRemove

## Signature

```lua
Duel.IsPlayerCanRemove(int player, [Card c], [int reason]) -> bool
```

## Description

With only player, checks whether player is not forbidden from banishing.
With c, checks whether player can banish c for reason; reason defaults to REASON_EFFECT.

## Parameters

- `player` `int`
- `c` `Card` optional
- `reason` `int` optional - default: REASON_EFFECT

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5055`
