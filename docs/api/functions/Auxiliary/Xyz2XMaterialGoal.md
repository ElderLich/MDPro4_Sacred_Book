# Auxiliary.Xyz2XMaterialGoal

## Signature

```lua
Auxiliary.Xyz2XMaterialGoal(Group g, int tp, Card xyzc, int minc) -> bool
```

## Description

Final group check for Xyz Summons that may use EFFECT_DOUBLE_XMATERIAL. It validates Extra Monster Zone availability, EFFECT_XYZ_MIN_COUNT, and whether double-material effects cover minc.

## Parameters

- `g` `Group`
- `tp` `int`
- `xyzc` `Card`
- `minc` `int`

## Returns

- `bool` - true if g satisfies the double-material Xyz requirements.

## Source

- `Utilities/procedure.lua:540`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
