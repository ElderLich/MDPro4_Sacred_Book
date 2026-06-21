# Auxiliary.AddFusionProcMixRep

## Signature

```lua
Auxiliary.AddFusionProcMixRep(Card fcard, bool sub, bool insf, number|function|table fun1, int minc, int maxc, ... number|function|table) -> void
```

## Description

Add a Fusion Summon procedure for c
Use minc-maxc monsters satisfying f1 and 1 of each monster in the additional parameters as Fusion Materials
Additional parameters can be function or card code (int code), where passing a code is equivalent to passing function(code) return c:IsFusionCode(code) end

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
