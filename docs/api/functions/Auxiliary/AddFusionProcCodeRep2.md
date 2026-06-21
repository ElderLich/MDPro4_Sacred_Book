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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
