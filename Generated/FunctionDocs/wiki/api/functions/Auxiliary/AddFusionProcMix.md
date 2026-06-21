# Auxiliary.AddFusionProcMix

## Signature

```lua
Auxiliary.AddFusionProcMix(Card fcard, bool sub, bool insf, ... number|function|table) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 of each card in the additional parameters as Fusion Materials; additional parameters can be function or card code (int code), where passing a code is equivalent to passing function(code) return c:IsFusionCode(code) end
sub indicates whether Fusion Substitute Materials can be used; insf=false means the Fusion Summon must use the specified materials. If this monster can only be Fusion Summoned with the specified cards, both sub and insf must be false

## Parameters

- `fcard` `Card`
- `sub` `bool` - Can be fusion summoned with substitute material
- `insf` `bool` - Can be fusion summoned with no material (Instant Fusion)
- `...` `number|function|table`

## Source

- `Utilities/procedure.lua:862`
