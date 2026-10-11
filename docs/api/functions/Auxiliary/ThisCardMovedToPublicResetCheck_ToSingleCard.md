# Auxiliary.ThisCardMovedToPublicResetCheck_ToSingleCard

## Signature

```lua
Auxiliary.ThisCardMovedToPublicResetCheck_ToSingleCard(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Reset check used by single-card merged delayed events. If the owner card is now face-up or public, it clears the stored event group.

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

- `Utilities/utility.lua:1749`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
