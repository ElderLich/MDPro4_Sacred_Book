# Auxiliary.XyzLevelFreeGoal

## Signature

```lua
Auxiliary.XyzLevelFreeGoal(Group g, int tp, Card xyzc, function|nil gf) -> bool
```

## Description

Final group check for Level-free Xyz Summons. It validates Extra Monster Zone availability, optional group filter gf, and EFFECT_XYZ_MIN_COUNT requirements.

## Parameters

- `g` `Group`
- `tp` `int`
- `xyzc` `Card`
- `gf` `function|nil`

## Returns

- `bool` - true if g satisfies the Level-free Xyz requirements.

## Source

- `Utilities/procedure.lua:717`
