# Auxiliary.AddRitualProcEqual2Code2

## Signature

```lua
Auxiliary.AddRitualProcEqual2Code2(Card c, any code1, any code2, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
code1, code2 are the card codes of the Ritual Monsters; the sum of the Levels of the materials must equal the Ritual Monster's Level
Equivalent to: aux.AddRitualProcEqual2(c, aux.FilterBoolFunction(Card.IsCode, code1, code2)), with fit_monster={code1, code2} added

## Parameters

- `c` `Card`
- `code1` `any`
- `code2` `any`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1929`
