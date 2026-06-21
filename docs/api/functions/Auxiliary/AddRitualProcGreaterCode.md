# Auxiliary.AddRitualProcGreaterCode

## Signature

```lua
Auxiliary.AddRitualProcGreaterCode(Card c, any code1, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
code is the card code of the Ritual Monster; the sum of the Ritual Levels of the materials can exceed the original Level of the Ritual Monster
Equivalent to: aux.AddRitualProcGreater(c, aux.FilterBoolFunction(Card.IsCode, code)), with fit_monster=code added

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

- `Utilities/procedure.lua:1909`
