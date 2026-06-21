# Auxiliary.LExtraFilter

## Signature

```lua
Auxiliary.LExtraFilter(Card c, function|nil f, Card lc, int tp) -> bool
```

## Description

Extra Link Material filter for hand, Spell & Trap Zone, or opponent-field cards granted by EFFECT_EXTRA_LINK_MATERIAL.

## Parameters

- `c` `Card`
- `f` `function|nil`
- `lc` `Card`
- `tp` `int`

## Returns

- `bool` - true if c can be used through an extra Link Material effect.

## Source

- `Utilities/procedure.lua:2147`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
