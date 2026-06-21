# Auxiliary.XyzAlterFilter

## Signature

```lua
Auxiliary.XyzAlterFilter(Card c, function alterf, Card xyzc, Effect e, int tp, function|nil alterop) -> bool
```

## Description

Alternate Xyz Summon candidate filter. It checks alterf, Xyz Material legality, Extra Monster Zone availability, mandatory Xyz Materials, EFFECT_XYZ_MIN_COUNT, and optional alterop validation.

## Parameters

- `c` `Card`
- `alterf` `function`
- `xyzc` `Card`
- `e` `Effect`
- `tp` `int`
- `alterop` `function|nil`

## Returns

- `bool` - true if c is a valid alternate Xyz Material.

## Source

- `Utilities/procedure.lua:471`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
