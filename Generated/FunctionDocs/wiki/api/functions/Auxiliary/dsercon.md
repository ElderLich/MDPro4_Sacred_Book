# Auxiliary.dsercon

## Signature

```lua
Auxiliary.dsercon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Condition for EVENT_DAMAGE_STEP_END effects; true if the handler is still related to battle or was battle destroyed.

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

- `Utilities/utility.lua:786`
