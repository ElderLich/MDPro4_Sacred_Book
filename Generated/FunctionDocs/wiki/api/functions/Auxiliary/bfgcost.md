# Auxiliary.bfgcost

## Signature

```lua
Auxiliary.bfgcost(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Shared cost function that checks whether the handler can be banished as cost, then banishes it face-up as REASON_COST.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`
- `chk` `bool`

## Source

- `Utilities/utility.lua:1121`
