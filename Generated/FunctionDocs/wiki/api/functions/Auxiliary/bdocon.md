# Auxiliary.bdocon

## Signature

```lua
Auxiliary.bdocon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition helper for EVENT_BATTLE_DESTROYING effects; it returns true when the handler is still related to battle and battled an opponent's monster.

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

- `bool`

## Source

- `Utilities/utility.lua:772`
