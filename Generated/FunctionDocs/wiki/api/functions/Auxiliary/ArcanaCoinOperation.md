# Auxiliary.ArcanaCoinOperation

## Signature

```lua
Auxiliary.ArcanaCoinOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Performs the shared Arcana Force coin-toss operation.
It tosses a coin, or lets the player choose the result while affected by the relevant replacement effect, then stores the result on c with client hints.

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

- `Utilities/utility.lua:285`
