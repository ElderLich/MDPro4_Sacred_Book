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
