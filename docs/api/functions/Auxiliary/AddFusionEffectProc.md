# Auxiliary.AddFusionEffectProc

## Signature

```lua
Auxiliary.AddFusionEffectProc(Card c, function filter, int mat_location, [function|nil mat_filter], [function|nil mat_operation], [table|nil params]) -> Effect
```

## Description

Convenience wrapper for Auxiliary.AddFusionEffectProcUltimate.
It builds a params table from the common Fusion Summon arguments: Extra Deck filter, material locations, material filter, material movement operation, and optional advanced params.

## Parameters

- `c` `Card`
- `filter` `function` - Fusion Monster filter for the Extra Deck candidate.
- `mat_location` `int` - Base material locations, commonly LOCATION_HAND+LOCATION_MZONE.
- `mat_filter` `function|nil` optional - Optional candidate material filter.
- `mat_operation` `function|nil` optional - Optional operation that moves the selected material group.
- `params` `table|nil` optional - Optional advanced params forwarded to AddFusionEffectProcUltimate.

## Returns

- `Effect` - The created Fusion effect.

## Source

- `Utilities/procedure.lua:1677`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
