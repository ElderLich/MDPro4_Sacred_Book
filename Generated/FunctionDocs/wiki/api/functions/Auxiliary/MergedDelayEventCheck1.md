# Auxiliary.MergedDelayEventCheck1

## Signature

```lua
Auxiliary.MergedDelayEventCheck1(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Internal callback for Auxiliary.RegisterMergedDelayedEvent. It collects event cards and, if not inside a Chain, raises EVENT_CUSTOM plus the stored code immediately.

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

- `Utilities/utility.lua:1668`
