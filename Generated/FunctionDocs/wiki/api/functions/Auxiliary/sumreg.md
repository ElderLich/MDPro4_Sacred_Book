# Auxiliary.sumreg

## Signature

```lua
Auxiliary.sumreg(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> void
```

## Description

For each card in eg whose original code equals e's label, registers a same-code flag effect that lasts through the End Phase/reset.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Source

- `Utilities/utility.lua:848`
