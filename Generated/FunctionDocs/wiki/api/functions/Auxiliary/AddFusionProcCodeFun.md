# Auxiliary.AddFusionProcCodeFun

## Signature

```lua
Auxiliary.AddFusionProcCodeFun(Card c, int|table code1, function|table f, int cc, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Summon procedure on c requiring code1 and cc additional Fusion Materials matching f.
The helper builds cc copies of f and forwards them to Auxiliary.AddFusionProcMix together with sub and insf.

## Parameters

- `c` `Card`
- `code1` `int|table`
- `f` `function|table`
- `cc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1263`
