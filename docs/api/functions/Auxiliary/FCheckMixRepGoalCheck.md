# Auxiliary.FCheckMixRepGoalCheck

## Signature

```lua
Auxiliary.FCheckMixRepGoalCheck(int tp, Group sg, Card fc, int chkfnf) -> bool
```

## Description

Shared precheck for mixed-repeat Fusion Material goals. It rejects invalid Tune Magician combinations, missing mandatory Fusion Materials, and failed goal hooks.

## Parameters

- `tp` `int`
- `sg` `Group`
- `fc` `Card`
- `chkfnf` `int`

## Returns

- `bool` - true if shared mixed-repeat goal prechecks pass.

## Source

- `Utilities/procedure.lua:1107`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
