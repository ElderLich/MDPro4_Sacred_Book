# Duel.GetCustomActivityCount

## Signature

```lua
Duel.GetCustomActivityCount(int counter_id, int player, int activity_type) -> int
```

## Description

Returns player 0's or player 1's count for the custom counter_id and ACTIVITY_* type.
Counts are reset each turn. In this core, most card-based custom counters only record whether that player has performed a counted activity at least once, while Chain counters can increase and decrease with Chain creation and cancellation.

## Parameters

- `counter_id` `int` - Identifier previously registered with Duel.AddCustomActivityCounter.
- `player` `int` - Player whose count is read; use 0 or 1.
- `activity_type` `int` - ACTIVITY_* constant selecting which custom activity map is read.

## Returns

- `int` - Stored count for that player, counter ID, and activity type, or 0 if no matching custom counter exists.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5069`
