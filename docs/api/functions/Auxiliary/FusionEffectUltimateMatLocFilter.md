# Auxiliary.FusionEffectUltimateMatLocFilter

## Signature

```lua
Auxiliary.FusionEffectUltimateMatLocFilter(Card c, Effect e, int tp, int loc, function|nil f) -> bool
```

## Description

Location-specific Fusion material filter; cards outside loc pass, and cards in loc must satisfy f when one is provided.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `loc` `int`
- `f` `function|nil`

## Returns

- `bool` - true if c is outside loc or passes f.

## Source

- `Utilities/procedure.lua:1496`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
