# Auxiliary.FusionEffectUltimateFilter

## Signature

```lua
Auxiliary.FusionEffectUltimateFilter(Card c, Effect e, int tp, Group mg, int chkf, table params) -> bool
```

## Description

Checks whether c is a Fusion Monster that can be Fusion Summoned by e using mg and the filters stored in params.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `mg` `Group`
- `chkf` `int`
- `params` `table`

## Returns

- `bool` - true if c can be Fusion Summoned with the provided material pool.

## Source

- `Utilities/procedure.lua:1482`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
