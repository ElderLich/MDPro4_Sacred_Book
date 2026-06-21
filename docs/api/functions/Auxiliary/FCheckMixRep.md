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
