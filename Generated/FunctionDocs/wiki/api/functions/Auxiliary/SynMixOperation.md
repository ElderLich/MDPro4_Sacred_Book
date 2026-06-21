# Auxiliary.SynMixOperation

## Signature

```lua
Auxiliary.SynMixOperation(function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minct, int maxct, function|nil gc) -> function
```

## Description

Returns the operation function for mixed Synchro Summon procedures; it sets materials, sends them to the Graveyard, and releases the kept group.

## Parameters

- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gc` `function|nil`

## Returns

- `function` - Operation function for a mixed Synchro Summon procedure.

## Source

- `Utilities/procedure.lua:314`
