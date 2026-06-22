# Duel.AddCustomActivityCounter

## Signature

```lua
Duel.AddCustomActivityCounter(int counter_id, int activity_type, function f) -> void
```

## Description

Registers a custom activity counter with id counter_id for the selected ACTIVITY_* type.
For Summon and attack counters, f is called with a Card and the counter increases when f returns false. For ACTIVITY_CHAIN, f is called with effect, player, chain_id and also counts false results.

## Parameters

- `counter_id` `int`
- `activity_type` `int`
- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5068`
