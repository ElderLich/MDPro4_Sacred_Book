# Auxiliary.AddFusionProcMixRep

## Signature

```lua
Auxiliary.AddFusionProcMixRep(Card fcard, bool sub, bool insf, number|function|table fun1, int minc, int maxc, ... number|function|table) -> void
```

## Description

Registers a mixed Fusion Material procedure with one repeated slot and any number of fixed slots.
fun1 is the repeated material requirement used minc to maxc times; additional arguments are fixed requirements. Each requirement may be a card code, filter function, or table of card codes and filters.

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
