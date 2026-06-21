# Duel.GetCustomActivityCount

## Signature

```lua
Duel.GetCustomActivityCount(int counter_id, int player, int activity_type) -> int
```

## Description

Counter number counter_id count, the number of players to return to the following (currently up to 1)
The activity_type is of the following type
ACTIVITY_SUMMON call (not including the usual call set)
ACTIVITY_NORMALSUMMON usually called (including the usual call set)
ACTIVITY_SPSUMMON Special call
ACTIVITY_FLIPSUMMON Reverse call
ACTIVITY_CHAIN ​​Activates the effect

## Parameters

- `counter_id` `int`
- `player` `int`
- `activity_type` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5069`
