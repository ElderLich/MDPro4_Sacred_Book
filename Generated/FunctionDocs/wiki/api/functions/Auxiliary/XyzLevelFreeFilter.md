# Auxiliary.XyzLevelFreeFilter

## Signature

```lua
Auxiliary.XyzLevelFreeFilter(Card c, Card xyzc, function|nil f) -> bool
```

## Description

Level-free Xyz Material filter; c must be face-up if on the field, usable as Xyz Material for xyzc, and satisfy f when provided.

## Parameters

- `c` `Card`
- `xyzc` `Card`
- `f` `function|nil`

## Returns

- `bool` - true if c is valid Level-free Xyz Material.

## Source

- `Utilities/procedure.lua:714`
