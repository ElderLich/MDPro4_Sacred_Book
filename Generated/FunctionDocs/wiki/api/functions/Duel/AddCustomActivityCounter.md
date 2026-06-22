# Duel.AddCustomActivityCounter

## Signature

```lua
Duel.AddCustomActivityCounter(int counter_id, int activity_type, function f) -> void
```

## Description

Registers a custom activity counter with id counter_id for the selected ACTIVITY_* type.
For Summon and attack counters, f is called with a Card and the counter increases when f returns false. For ACTIVITY_CHAIN, f is called with effect, player, chain_id and also counts false results. ACTIVITY_BATTLE_PHASE and unknown activity types do not register a custom counter in this core.

## Parameters

- `counter_id` `int` - Script-chosen identifier used later with Duel.GetCustomActivityCount.
- `activity_type` `int` - ACTIVITY_* constant selecting which activity map receives the counter.
- `f` `function` - Filter callback. Returning false marks that activity as counted for the acting player.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5068`
