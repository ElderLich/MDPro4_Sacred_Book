# Auxiliary.AddRitualProcGreater

## Signature

```lua
Auxiliary.AddRitualProcGreater(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Creates a Ritual Summon activation effect whose selected materials' Ritual Levels must be greater than or equal to the Ritual Monster's original Level.

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

- `Utilities/procedure.lua:1906`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
