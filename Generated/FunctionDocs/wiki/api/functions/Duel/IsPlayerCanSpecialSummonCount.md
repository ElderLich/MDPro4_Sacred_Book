# Duel.IsPlayerCanSpecialSummonCount

## Signature

```lua
Duel.IsPlayerCanSpecialSummonCount(int player, int count) -> bool
```

## Description

Checks whether player can perform count Special Summons under the current remaining Special Summon-count limits.
The core checks EFFECT_LEFT_SPSUMMON_COUNT effects and the player's Special Summon counter.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5053`
