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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
