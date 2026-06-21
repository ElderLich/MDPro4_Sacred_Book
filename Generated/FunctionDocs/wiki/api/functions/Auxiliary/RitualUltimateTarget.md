# Auxiliary.RitualUltimateTarget

## Signature

```lua
Auxiliary.RitualUltimateTarget(function|nil filter, function level_function, string greater_or_equal, int summon_location, function|nil grave_filter, function|nil mat_filter, function|nil extra_target) -> function
```

## Description

Returns the target function for configurable Ritual Summon effects. It checks Ritual Monsters and material pools, then registers Special Summon, banish, and extra target information.

## Parameters

- `filter` `function|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `summon_location` `int`
- `grave_filter` `function|nil`
- `mat_filter` `function|nil`
- `extra_target` `function|nil`

## Returns

- `function` - Target function for a configurable Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1845`
