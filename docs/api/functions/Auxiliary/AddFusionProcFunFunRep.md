# Auxiliary.AddFusionProcFunFunRep

## Signature

```lua
Auxiliary.AddFusionProcFunFunRep(Card c, any f1, any f2, any minc, any maxc, any insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 monster satisfying filter condition f1 and minc-maxc monsters satisfying filter condition f2 as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, false, insf, f2, minc, maxc, f1)

## Parameters

- `c` `Card`
- `f1` `any`
- `f2` `any`
- `minc` `any`
- `maxc` `any`
- `insf` `any`

## Source

- `Utilities/procedure.lua:1313`
