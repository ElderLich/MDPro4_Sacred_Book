# Auxiliary.Xyz2XMaterialEffectFilter

## Signature

```lua
Auxiliary.Xyz2XMaterialEffectFilter(Card c, Card xyzc, int lv, function|nil f, int tp, bool|nil checked) -> bool
```

## Description

Checks whether c has a valid EFFECT_DOUBLE_XMATERIAL effect for xyzc, optionally skipping the normal Xyz Material filter when checked is true.

## Parameters

- `c` `Card`
- `xyzc` `Card`
- `lv` `int`
- `f` `function|nil`
- `tp` `int`
- `checked` `bool|nil`

## Returns

- `bool` - true if c has a valid EFFECT_DOUBLE_XMATERIAL effect.

## Source

- `Utilities/procedure.lua:532`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
