# Auxiliary.AddFusionProcCodeFunRep

## Signature

```lua
Auxiliary.AddFusionProcCodeFunRep(Card c, int|table code1, function|table f, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Registers a Fusion procedure requiring code1 plus between minc and maxc materials that satisfy f.

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
