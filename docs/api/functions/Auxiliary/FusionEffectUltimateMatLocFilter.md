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
