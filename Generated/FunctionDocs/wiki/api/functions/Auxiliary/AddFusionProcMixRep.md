# Auxiliary.AddFusionProcMixRep

## Signature

```lua
Auxiliary.AddFusionProcMixRep(Card fcard, bool sub, bool insf, number|function|table fun1, int minc, int maxc, ... number|function|table) -> void
```

## Description

Fusion monster, mixed material * minc to maxc + material + ...

## Parameters

- `fcard` `Card`
- `sub` `bool` - Can be fusion summoned with substitute material
- `insf` `bool` - Can be fusion summoned with no material (Instant Fusion)
- `fun1` `number|function|table`
- `minc` `int`
- `maxc` `int`
- `...` `number|function|table`

## Source

- `Utilities/procedure.lua:991`
