# Duel.GetActivityCount

## Signature

```lua
Duel.GetActivityCount(int player, int activity_type, ... any) -> int,...
```

## Description

Returns the number of times the player performed the corresponding activity_type operation
The activity_type is of the following type
ACTIVITY_SUMMON call (not including the usual call placed)
ACTIVITY_NORMALSUMMON Usually called (including the usual call placed)
ACTIVITY_SPSUMMON Special call
ACTIVITY_FLIPSUMMON Reverse call
ACTIVITY_ATTACK attack
ACTIVITY_BATTLE_PHASE enters the combat phase

## Parameters

- `player` `int`
- `activity_type` `int`
- `...` `any`

## Returns

- `int`
- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5066`
