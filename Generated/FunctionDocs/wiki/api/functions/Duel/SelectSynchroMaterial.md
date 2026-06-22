# Duel.SelectSynchroMaterial

## Signature

```lua
Duel.SelectSynchroMaterial(int player, Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> Group
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

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4993`
