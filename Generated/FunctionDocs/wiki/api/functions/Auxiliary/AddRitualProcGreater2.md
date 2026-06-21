# Auxiliary.AddRitualProcGreater2

## Signature

```lua
Auxiliary.AddRitualProcGreater2(Card c, function filter, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Adds a Ritual Summon effect for c that uses the Ritual Monster's current Level and requires materials whose total Level is greater than or equal to it.

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1934`
