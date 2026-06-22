# Duel.GetActivityCount

## Signature

```lua
Duel.GetActivityCount(int player, int activity_type1, [int activity_type2], [... int]) -> int,...?
```

## Description

Returns activity counts for player in the same order as the requested activity_type values.
Supported built-in activity types are ACTIVITY_SUMMON, ACTIVITY_NORMALSUMMON, ACTIVITY_SPSUMMON, ACTIVITY_FLIPSUMMON, ACTIVITY_ATTACK, and ACTIVITY_BATTLE_PHASE. Other values, including ACTIVITY_CHAIN in this binding, return 0.

## Parameters

- `player` `int`
- `activity_type1` `int`
- `activity_type2` `int` optional
- `...` `int` optional

## Returns

- `int` - Count for activity_type1.
- `...?` - Additional counts for each extra activity_type.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5066`
