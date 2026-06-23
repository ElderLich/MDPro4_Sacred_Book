# Duel.SelectXyzMaterial

## Signature

```lua
Duel.SelectXyzMaterial(int player, Card scard, function|nil f, int lv, int minc, int maxc, [Group|nil materials]) -> Group
```

## Description

Lets player select Xyz Materials for scard for material Xyz Level lv and material count range, with optional filter and material group.
Use this only after a matching Duel.CheckXyzMaterial check has succeeded. It yields and returns the selected Group.

## Parameters

- `player` `int` - Player choosing the Xyz Materials.
- `scard` `Card` - Xyz Monster whose materials are being selected.
- `f` `function|nil` - Optional per-material filter.
- `lv` `int` - Required material Xyz Level.
- `minc` `int` - Minimum material count.
- `maxc` `int` - Maximum material count.
- `materials` `Group|nil` optional - Optional candidate material group.

## Returns

- `Group` - The selected Xyz Materials.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5013`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
