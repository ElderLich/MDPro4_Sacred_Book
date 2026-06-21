# Auxiliary.BESRemoveOperation

## Signature

```lua
Auxiliary.BESRemoveOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Resolves the shared B.E.S. maintenance effect by removing one 0x1f counter from the handler, or destroying it if no counter can be removed.

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

- `Utilities/utility.lua:1813`
