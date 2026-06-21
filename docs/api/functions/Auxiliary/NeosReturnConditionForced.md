# Auxiliary.NeosReturnConditionForced

## Signature

```lua
Auxiliary.NeosReturnConditionForced(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the mandatory Elemental HERO Neos Fusion End Phase return effect; true while the handler is not affected by Neo Space's effect code 42015635.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Returns

- `bool` - true if the forced Neos return effect should apply.

## Source

- `Utilities/utility.lua:242`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
