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
