# Auxiliary.FCheckSelectMixRep

## Signature

```lua
Auxiliary.FCheckSelectMixRep(int tp, Group mg, Group sg, Group g, Card fc, bool sub, int chkfnf, function fun1, int minc, int maxc, ... function) -> bool
```

## Description

Checks whether a mixed-repeat Fusion Material selection can be completed from the current chosen group.

## Parameters

- `tp` `int`
- `mg` `Group`
- `sg` `Group`
- `g` `Group`
- `fc` `Card`
- `sub` `bool`
- `chkfnf` `int`
- `fun1` `function`
- `minc` `int`
- `maxc` `int`
- `...` `function`

## Returns

- `bool` - true if the current selection can be completed.

## Source

- `Utilities/procedure.lua:1156`
