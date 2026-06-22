# Auxiliary.AddFusionProcCode2

## Signature

```lua
Auxiliary.AddFusionProcCode2(Card c, int code1, int code2, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Summon procedure on c requiring materials with card codes code1 and code2.
The helper forwards sub and insf unchanged to Auxiliary.AddFusionProcMix.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1209`
