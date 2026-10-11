# Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_RaiseEvent

## Signature

```lua
Auxiliary.RegisterMergedDelayedEvent_ToSingleCard_RaiseEvent(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Global Chain End helper for single-card merged delayed events. It raises each pending generated custom event once, then clears its stored group.

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

- `Utilities/utility.lua:1786`
