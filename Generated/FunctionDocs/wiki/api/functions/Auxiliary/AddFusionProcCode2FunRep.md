# Auxiliary.AddFusionProcCode2FunRep

## Signature

```lua
Auxiliary.AddFusionProcCode2FunRep(Card c, int|table code1, int|table code2, function|table f, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Material procedure requiring code1, code2, and between minc and maxc additional materials that satisfy f.

## Parameters

- `c` `Card`
- `code1` `int|table`
- `code2` `int|table`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1336`
