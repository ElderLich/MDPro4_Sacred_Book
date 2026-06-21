# Auxiliary.dscon

## Signature

```lua
Auxiliary.dscon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Condition for Quick Effects that change ATK/DEF; true outside the Damage Phase, or during the Damage Phase before damage calculation has been performed.

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

- `Utilities/utility.lua:810`
