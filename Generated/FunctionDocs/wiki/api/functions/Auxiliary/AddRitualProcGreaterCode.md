# Auxiliary.AddRitualProcGreaterCode

## Signature

```lua
Auxiliary.AddRitualProcGreaterCode(Card c, int code1, [int summon_location], [function grave_filter], [function mat_filter], [bool pause], [function extra_operation], [function extra_target]) -> Effect
```

## Description

Registers a Ritual Summon procedure for Ritual Monster code1, allowing material Ritual Levels to meet or exceed the Ritual Monster's original Level.
The helper also adds code1 to c's code/material list and returns the created procedure effect.

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

- `Effect`

## Source

- `Utilities/procedure.lua:1909`
