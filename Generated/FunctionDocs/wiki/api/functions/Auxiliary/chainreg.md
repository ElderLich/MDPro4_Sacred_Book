# Auxiliary.chainreg

## Signature

```lua
Auxiliary.chainreg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Registers FLAG_ID_CHAINING on e's handler if that flag is not already present.
The flag resets by the standard event reset, except turn Set reset, and also at the end of the Chain.

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

- `Utilities/utility.lua:817`
