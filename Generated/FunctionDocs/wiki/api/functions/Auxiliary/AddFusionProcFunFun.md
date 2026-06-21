# Auxiliary.AddFusionProcFunFun

## Signature

```lua
Auxiliary.AddFusionProcFunFun(Card c, function|table f1, function|table f2, int cc, bool insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 monster satisfying filter condition f1 and cc monsters satisfying filter condition f2 as Fusion Materials
Equivalent to aux.AddFusionProcMix(c, false, insf, f1, table.unpack(fun)), where fun is a table of cc cards satisfying condition f2

## Parameters

- `c` `Card`
- `f1` `function|table`
- `f2` `function|table`
- `cc` `int`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1305`
