# Duel.GetCustomActivityCount

## Signature

```lua
Duel.GetCustomActivityCount(int counter_id, int player, int activity_type) -> int
```

## Description

Returns player 0's or player 1's count for the custom counter_id and ACTIVITY_* type.
Counts are reset each turn. In this core, most card-based custom counters only record whether that player has performed a counted activity at least once, while Chain counters can increase and decrease with Chain creation and cancellation.

## Parameters

- `counter_id` `int`
- `player` `int`
- `activity_type` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5069`
