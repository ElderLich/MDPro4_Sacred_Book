# Auxiliary.SpiritReturnOperation

## Signature

```lua
Auxiliary.SpiritReturnOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Operation for the shared Spirit Monster End Phase return effect. If the handler is still related to the effect, it returns that card to the hand.

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

- `Utilities/utility.lua:216`
