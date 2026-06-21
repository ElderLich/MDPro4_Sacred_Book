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
