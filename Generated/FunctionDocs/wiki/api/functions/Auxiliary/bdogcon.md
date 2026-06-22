# Auxiliary.bdogcon

## Signature

```lua
Auxiliary.bdogcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition helper for a battle-destroying monster: the handler is still related to battle, battled an opponent's monster, and that battle target is a monster in the GY.

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

- `Utilities/utility.lua:780`
