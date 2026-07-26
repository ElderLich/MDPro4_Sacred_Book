# Duel.SelectSynchroMaterial

## Signature

```lua
Duel.SelectSynchroMaterial(int player, Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> Group|nil
```

## Description

Lets player select Synchro Materials for c and returns the selected Group.
f1 filters the Tuner material, f2 filters non-Tuner materials, min and max restrict the non-Tuner count, smat forces a required material, and mg supplies an optional material pool.

## Parameters

- `player` `int`
- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `smat` `Card|nil` optional
- `mg` `Group|nil` optional

## Returns

- `Group|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4993`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
