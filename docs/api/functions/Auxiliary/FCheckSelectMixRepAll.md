# Auxiliary.FCheckSelectMixRepAll

## Signature

```lua
Auxiliary.FCheckSelectMixRepAll(Card c, int tp, Group mg, Group sg, Group g, Card fc, bool sub, int chkf, function fun1, int minc, int maxc, [function|nil fun2], ... function) -> bool
```

## Description

Recursive helper for mixed-repeat Fusion selection when field-space constraints are already satisfied or not required.

## Parameters

- `c` `Card`
- `tp` `int`
- `mg` `Group`
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

- `bool` - true if the selection can be completed through c.

## Source

- `Utilities/procedure.lua:1166`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
