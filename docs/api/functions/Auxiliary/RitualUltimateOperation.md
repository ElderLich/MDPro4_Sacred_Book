# Auxiliary.RitualUltimateOperation

## Signature

```lua
Auxiliary.RitualUltimateOperation(function|nil filter, function level_function, string greater_or_equal, int summon_location, function|nil grave_filter, function|nil mat_filter, function|nil extra_operation) -> function
```

## Description

Returns the operation function for configurable Ritual Summon effects. It selects the Ritual Monster and materials, releases or banishes the materials, Special Summons the monster, and runs extra callbacks.

## Parameters

- `filter` `function|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `summon_location` `int`
- `grave_filter` `function|nil`
- `mat_filter` `function|nil`
- `extra_operation` `function|nil`

## Returns

- `function` - Operation function for a configurable Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1865`
