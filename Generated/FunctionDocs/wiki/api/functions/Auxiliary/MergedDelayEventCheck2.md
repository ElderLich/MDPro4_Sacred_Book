# Auxiliary.MergedDelayEventCheck2

## Signature

```lua
Auxiliary.MergedDelayEventCheck2(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Internal callback for Auxiliary.RegisterMergedDelayedEvent. At Chain End, it raises one merged custom event for all collected cards, then clears the stored group.

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

- `Utilities/utility.lua:1677`
