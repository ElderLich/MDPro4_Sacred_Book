# Auxiliary.FusionEffectUltimateMatFilter

## Signature

```lua
Auxiliary.FusionEffectUltimateMatFilter(Card c, Effect e, int tp, function|nil f) -> bool
```

## Description

Fusion effect material filter; rejects materials immune to e and applies the optional material filter f.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `f` `function|nil`

## Returns

- `bool` - true if c is affected by e and passes f when provided.

## Source

- `Utilities/procedure.lua:1493`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
