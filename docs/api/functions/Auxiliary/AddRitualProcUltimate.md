# Auxiliary.AddRitualProcUltimate

## Signature

```lua
Auxiliary.AddRitualProcUltimate(Card c, function filter, function level_function, string greater_or_equal, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Creates the configurable Ritual Summon activation effect for c and returns it. The effect can be paused from registration, can use Graveyard materials, and can run extra target/operation callbacks.

## Parameters

- `c` `Card`
- `filter` `function`
- `level_function` `function`
- `greater_or_equal` `string`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon activation effect.

## Source

- `Utilities/procedure.lua:1750`
