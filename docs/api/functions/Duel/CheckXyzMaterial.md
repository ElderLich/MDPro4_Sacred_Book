# Duel.CheckXyzMaterial

## Signature

```lua
Duel.CheckXyzMaterial(Card scard, function|nil f, int lv, int minc, int maxc, [Group|nil materials]) -> bool
```

## Description

Checks whether scard has a legal Xyz Material selection for material Xyz Level lv, material count range, optional filter, and optional material group.
This is the boolean check used by Xyz procedure targets. It does not select or move cards.

## Parameters

- `scard` `Card` - Xyz Monster whose material procedure is checked.
- `f` `function|nil` - Optional per-material filter.
- `lv` `int` - Required material Xyz Level.
- `minc` `int` - Minimum material count.
- `maxc` `int` - Maximum material count.
- `materials` `Group|nil` optional - Optional candidate material group. When omitted, procedure code usually supplies the player's Monster Zone group.

## Returns

- `bool` - true if a legal Xyz Material selection exists.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5012`

## Guided Examples

Learn how to use this function in context:

- [Xyz Procedure Guide](/learn/xyz-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
