# Auxiliary.MergedDelayEventCheck1_ToSingleCard

## Signature

```lua
Auxiliary.MergedDelayEventCheck1_ToSingleCard(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Internal callback for single-card merged delayed events. It collects event cards, clears them if the owner card moved, and raises the stored custom event immediately when possible.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:1751`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
