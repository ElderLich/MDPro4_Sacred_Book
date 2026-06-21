# Auxiliary.NeosReturnConditionOptional

## Signature

```lua
Auxiliary.NeosReturnConditionOptional(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the optional Elemental HERO Neos Fusion End Phase return effect; true while the handler is affected by Neo Space's effect code 42015635.

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

- `bool` - true if the optional Neos return effect should apply.

## Source

- `Utilities/utility.lua:252`
