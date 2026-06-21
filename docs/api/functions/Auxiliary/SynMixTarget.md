# Auxiliary.SynMixTarget

## Signature

```lua
Auxiliary.SynMixTarget(function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minct, int maxct, function|nil gc) -> function
```

## Description

Returns the target function for mixed Synchro Summon procedures; it guides material selection and stores the selected group on the effect.

## Parameters

- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gc` `function|nil`

## Returns

- `function` - Target function for a mixed Synchro Summon procedure.

## Source

- `Utilities/procedure.lua:225`
