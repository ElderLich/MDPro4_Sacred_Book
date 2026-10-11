# Auxiliary.EPDestroyOperation

## Signature

```lua
Auxiliary.EPDestroyOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Operation for delayed End Phase destruction effects. It destroys the Card or Group stored as e's label object.

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

- `Utilities/utility.lua:1829`
