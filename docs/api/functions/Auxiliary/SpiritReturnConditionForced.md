# Auxiliary.SpiritReturnConditionForced

## Signature

```lua
Auxiliary.SpiritReturnConditionForced(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the mandatory Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does not have the optional-return permission effect.

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

- `bool` - true if the mandatory Spirit return effect should apply.

## Source

- `Utilities/utility.lua:200`
