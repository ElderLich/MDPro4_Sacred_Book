# Auxiliary.AddFusionProcCodeRep2

## Signature

```lua
Auxiliary.AddFusionProcCodeRep2(Card c, int|table code1, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use minc-maxc identical monsters with code as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, sub, insf, code1, minc, maxc)

## Parameters

- `c` `Card`
- `code1` `int|table`
- `minc` `int`
- `maxc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1253`
