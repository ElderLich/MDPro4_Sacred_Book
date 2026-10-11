# Auxiliary.UrsarcticSpSummonCondition

## Signature

```lua
Auxiliary.UrsarcticSpSummonCondition(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the shared Ursarctic hand Quick Effect; returns true during either Main Phase.

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

- `bool` - true during Main Phase 1 or Main Phase 2.

## Source

- `Utilities/utility.lua:955`
