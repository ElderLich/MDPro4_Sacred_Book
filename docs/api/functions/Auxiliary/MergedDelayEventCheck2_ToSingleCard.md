# Auxiliary.MergedDelayEventCheck2_ToSingleCard

## Signature

```lua
Auxiliary.MergedDelayEventCheck2_ToSingleCard(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Internal Chain End callback for single-card merged delayed events. It clears stale public-move entries, raises the stored custom event for collected cards, then clears the group.

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

- `Utilities/utility.lua:1766`
