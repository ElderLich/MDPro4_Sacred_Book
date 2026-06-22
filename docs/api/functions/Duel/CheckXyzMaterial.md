# Duel.CheckXyzMaterial

## Signature

```lua
Duel.CheckXyzMaterial(Card c, [function|nil f], int lv, int min, int max, [Group|nil mg]) -> bool
```

## Description

Checks whether scard has a legal Xyz Material selection for Level lv, material count range, optional filter, and optional material group.

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `lv` `int`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5012`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
