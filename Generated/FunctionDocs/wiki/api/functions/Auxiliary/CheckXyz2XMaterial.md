# Auxiliary.CheckXyz2XMaterial

## Signature

```lua
Auxiliary.CheckXyz2XMaterial(Card c, function f, int lv, int minc, int maxc, Group mg) -> bool
```

## Description

Checks whether c can be Xyz Summoned using materials from mg while allowing valid EFFECT_DOUBLE_XMATERIAL cards to count as two materials.

## Parameters

- `c` `Card`
- `f` `function`
- `lv` `int`
- `minc` `int`
- `maxc` `int`
- `mg` `Group`

## Returns

- `bool` - true if c can be Xyz Summoned with double-material support.

## Source

- `Utilities/procedure.lua:565`
