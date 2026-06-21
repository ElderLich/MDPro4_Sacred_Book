# Auxiliary.AddRitualProcEqual

## Signature

```lua
Auxiliary.AddRitualProcEqual(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a ritual summon effect to c
Filter for the ritual monster to meet the conditions, the material level must be equal to the ritual monster level

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1914`
