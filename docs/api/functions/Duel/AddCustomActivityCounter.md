# Duel.AddCustomActivityCounter

## Signature

```lua
Duel.AddCustomActivityCounter(int counter_id, int activity_type, function f) -> void
```

## Description

Set the action type to activity_type, code counter_id counter, placed in the initial_effect function
F for the filter function, the card type parameters, the return value of false cards for the following types of operations, the counter increased by 1 (at present up to 1)
The activity_type is of the following type
ACTIVITY_SUMMON call (not including the usual call set)
ACTIVITY_NORMALSUMMON usually called (including the usual call set)
ACTIVITY_SPSUMMON Special call
ACTIVITY_FLIPSUMMON Reverse call
ACTIVITY_CHAIN ​​Activates the effect

## Parameters

- `counter_id` `int`
- `activity_type` `int`
- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5068`
