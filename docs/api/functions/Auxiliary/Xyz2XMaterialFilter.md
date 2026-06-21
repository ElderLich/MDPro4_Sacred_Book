# Auxiliary.Xyz2XMaterialFilter

## Signature

```lua
Auxiliary.Xyz2XMaterialFilter(Card c, Card xyzc, int lv, function|nil f) -> bool
```

## Description

Xyz Material filter for double-material handling; c must be face-up or public, usable as Xyz Material for xyzc, match lv, and satisfy f when provided.

## Parameters

- `c` `Card`
- `xyzc` `Card`
- `lv` `int`
- `f` `function|nil`

## Returns

- `bool` - true if c is valid Xyz Material for double-material handling.

## Source

- `Utilities/procedure.lua:529`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
