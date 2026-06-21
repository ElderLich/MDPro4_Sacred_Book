# Auxiliary.SpiritReturnConditionOptional

## Signature

```lua
Auxiliary.SpiritReturnConditionOptional(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the optional Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does have the optional-return permission effect.

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

- `bool` - true if the optional Spirit return effect should apply.

## Source

- `Utilities/utility.lua:208`
