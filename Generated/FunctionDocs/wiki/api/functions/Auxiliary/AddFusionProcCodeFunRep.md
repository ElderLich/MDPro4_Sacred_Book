# Auxiliary.AddFusionProcCodeFunRep

## Signature

```lua
Auxiliary.AddFusionProcCodeFunRep(Card c, int|table code1, function|table f, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 monster with code and minc-maxc monsters satisfying filter condition f as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, sub, insf, f, minc, maxc, code1)

## Parameters

- `c` `Card`
- `code1` `int|table`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1324`
