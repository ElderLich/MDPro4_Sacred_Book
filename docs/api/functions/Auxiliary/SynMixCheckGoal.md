# Auxiliary.SynMixCheckGoal

## Signature

```lua
Auxiliary.SynMixCheckGoal(int tp, Group sg, int minc, int ct, Card syncard, Group sg1, Card|nil smat, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

Final mixed Synchro Material group check. It validates count, Extra Monster Zone availability, group callback, fixed material, mandatory Synchro Materials, EFFECT_TUNE_MAGICIAN restrictions, Level total, hand-material limits, and tuner limits.

## Parameters

- `tp` `int`
- `sg` `Group`
- `minc` `int`
- `ct` `int`
- `syncard` `Card`
- `sg1` `Group`
- `smat` `Card|nil`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if sg plus sg1 is a valid mixed Synchro Material group.

## Source

- `Utilities/procedure.lua:413`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
