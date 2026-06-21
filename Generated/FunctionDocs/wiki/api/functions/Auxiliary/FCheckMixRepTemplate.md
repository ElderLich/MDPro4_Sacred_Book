# Auxiliary.FCheckMixRepTemplate

## Signature

```lua
Auxiliary.FCheckMixRepTemplate(Card c, function cond, int tp, Group mg, Group sg, Group g, Card fc, bool sub, int chkfnf, function fun1, int minc, int maxc, ... function) -> bool
```

## Description

Generic recursive template for mixed-repeat Fusion Material checks. It tries assigning c to each fixed material function or to the repeated material slot.

## Parameters

- `c` `Card`
- `cond` `function`
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

- `bool` - true if c can be assigned to a fixed or repeated material slot.

## Source

- `Utilities/procedure.lua:1123`
