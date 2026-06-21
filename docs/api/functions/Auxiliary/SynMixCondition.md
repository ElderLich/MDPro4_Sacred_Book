# Auxiliary.SynMixCondition

## Signature

```lua
Auxiliary.SynMixCondition(function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minct, int maxct, function|nil gc) -> function
```

## Description

Returns the condition function for mixed Synchro Summon procedures with up to three fixed material filters and a variable material slot.

## Parameters

- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gc` `function|nil`

## Returns

- `function` - Condition function for a mixed Synchro Summon procedure.

## Source

- `Utilities/procedure.lua:181`
