# Auxiliary.AddFusionProcFunRep2

## Signature

```lua
Auxiliary.AddFusionProcFunRep2(Card c, function|table f, int minc, int maxc, bool insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use minc-maxc monsters satisfying the same condition f as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, false, insf, f, minc, maxc)

## Parameters

- `c` `Card`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1296`
