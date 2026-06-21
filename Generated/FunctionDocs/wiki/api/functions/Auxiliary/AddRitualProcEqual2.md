# Auxiliary.AddRitualProcEqual2

## Signature

```lua
Auxiliary.AddRitualProcEqual2(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
filter is the condition the Ritual Monster must satisfy; the sum of the Ritual Levels of the materials must equal the Ritual Monster's Level (which may be altered by other card effects)

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

- `Utilities/procedure.lua:1922`
