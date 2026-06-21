# Auxiliary.FCheckMixRepGoal

## Signature

```lua
Auxiliary.FCheckMixRepGoal(int tp, Group sg, Card fc, bool sub, int chkfnf, function fun1, int minc, int maxc, ... function) -> bool
```

## Description

Final goal check for mixed-repeat Fusion Materials. It validates selected count limits, Extra Monster Zone availability, additional Fusion hooks, and fixed/repeated material requirements.

## Parameters

- `tp` `int`
- `sg` `Group`
- `fc` `Card`
- `sub` `bool`
- `chkfnf` `int`
- `fun1` `function`
- `minc` `int`
- `maxc` `int`
- `...` `function`

## Returns

- `bool` - true if sg is a valid mixed-repeat Fusion Material group.

## Source

- `Utilities/procedure.lua:1114`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
