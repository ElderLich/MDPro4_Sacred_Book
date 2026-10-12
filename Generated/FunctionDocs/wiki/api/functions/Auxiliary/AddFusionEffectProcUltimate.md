# Auxiliary.AddFusionEffectProcUltimate

## Signature

```lua
Auxiliary.AddFusionEffectProcUltimate(Card c, table params) -> Effect
```

## Description

Creates the configurable Fusion Summon activation effect described by params.
Missing material locations, material filters, material operations, Special Summon nocheck, and category fields are filled with the MDPro4 defaults. Unless params.reg is false, the effect is registered to c as an activation effect.
The generated effect checks Fusion Monsters in the Extra Deck, gathers and filters Fusion Materials, supports Chain Material fallback, selects materials, moves them with the configured operations, Special Summons with SUMMON_TYPE_FUSION, and completes the procedure.

## Parameters

- `c` `Card`
- `params` `table`

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:1453`
