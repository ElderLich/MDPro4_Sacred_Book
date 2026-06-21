# Auxiliary.LCheckOtherMaterial

## Signature

```lua
Auxiliary.LCheckOtherMaterial(Card c, Group mg, Card lc, int tp) -> bool
```

## Description

Checks whether c is compatible with the other selected Link Materials through EFFECT_EXTRA_LINK_MATERIAL handlers.

## Parameters

- `c` `Card`
- `mg` `Group`
- `lc` `Card`
- `tp` `int`

## Returns

- `bool` - true if c is compatible with mg.

## Source

- `Utilities/procedure.lua:2169`
