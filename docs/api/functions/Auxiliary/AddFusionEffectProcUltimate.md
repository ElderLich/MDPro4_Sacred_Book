# Auxiliary.AddFusionEffectProcUltimate

## Signature

```lua
Auxiliary.AddFusionEffectProcUltimate(Card c, table params) -> Effect
```

## Description

Creates the configurable Fusion Summon activation effect described by params.
Missing material locations, material filters, material operations, Special Summon nocheck, and category fields are filled with the MDPro3 defaults. Unless params.reg is false, the effect is registered to c as an activation effect.

## Parameters

- `c` `Card`
- `params` `table`

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:1453`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
