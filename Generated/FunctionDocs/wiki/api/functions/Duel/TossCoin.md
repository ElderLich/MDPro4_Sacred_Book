# Duel.TossCoin

## Signature

```lua
Duel.TossCoin(int player, int count) -> int,...?
```

## Description

Tosses count coins for player and returns one integer result per toss.
Results are 0 or 1. Normal script use passes a positive count up to MAX_COIN_COUNT; the binding rejects 0 and values below -1, and clamps large positive counts to the core maximum.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `int` - First coin result, 0 or 1.
- `...?` - Additional coin results.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5036`
