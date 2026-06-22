# Auxiliary.AddRitualProcEqualCode

## Signature

```lua
Auxiliary.AddRitualProcEqualCode(Card c, int code1, [int summon_location], [function grave_filter], [function mat_filter], [bool pause], [function extra_operation], [function extra_target]) -> Effect
```

## Description

Creates a Ritual Summon activation effect for Ritual Monster code1.
The selected materials' Ritual Levels must exactly equal the Ritual Monster's original Level, and optional Graveyard material, material filter, and extra callbacks are forwarded to the shared Ritual procedure.

## Parameters

- `c` `Card`
- `code1` `int`
- `summon_location` `int` optional - default: LOCATION_HAND
- `grave_filter` `function` optional
- `mat_filter` `function` optional
- `pause` `bool` optional
- `extra_operation` `function` optional
- `extra_target` `function` optional

## Returns

- `Effect` - Created Ritual Summon activation effect.

## Source

- `Utilities/procedure.lua:1917`
