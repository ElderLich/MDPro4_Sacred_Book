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
