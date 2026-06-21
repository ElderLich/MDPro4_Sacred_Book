# Auxiliary.FCheckMixRepFilter

## Signature

```lua
Auxiliary.FCheckMixRepFilter(Card c, Group sg, Group g, Card fc, bool sub, int chkf, function fun1, int minc, int maxc, [function|nil fun2], ... function) -> bool
```

## Description

Recursive helper for Auxiliary.FCheckMixRep. It temporarily assigns c to one remaining fixed material function and continues checking the rest.

## Parameters

- `c` `Card`
- `sg` `Group`
- `g` `Group`
- `fc` `Card`
- `sub` `bool`
- `chkf` `int`
- `fun1` `function`
- `minc` `int`
- `maxc` `int`
- `fun2` `function|nil` optional
- `...` `function`

## Returns

- `bool` - true if c can satisfy this fixed material slot and the rest can be completed.

## Source

- `Utilities/procedure.lua:1097`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
