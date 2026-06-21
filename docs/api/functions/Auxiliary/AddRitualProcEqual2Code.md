# Auxiliary.AddRitualProcEqual2Code

## Signature

```lua
Auxiliary.AddRitualProcEqual2Code(Card c, any code1, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
code is the card code of the Ritual Monster; the sum of the Levels of the materials must equal the Ritual Monster's Level
Equivalent to: aux.AddRitualProcEqual2(c, aux.FilterBoolFunction(Card.IsCode, code)), with fit_monster=code added

## Parameters

- `c` `Card`
- `code1` `any`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1925`
