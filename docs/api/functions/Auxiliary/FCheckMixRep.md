# Auxiliary.FCheckMixRep

## Signature

```lua
Auxiliary.FCheckMixRep(Group sg, Group g, Card fc, bool sub, int chkf, function fun1, int minc, int maxc, [function|nil fun2], ... function) -> bool
```

## Description

Checks a selected mixed-repeat Fusion Material group. The repeated material function must cover the variable-count materials, while each remaining function is satisfied once.

## Parameters

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

- `bool` - true if the mixed-repeat material requirements can be satisfied.

## Source

- `Utilities/procedure.lua:1088`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
