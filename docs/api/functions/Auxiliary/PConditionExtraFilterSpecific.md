# Auxiliary.PConditionExtraFilterSpecific

## Signature

```lua
Auxiliary.PConditionExtraFilterSpecific(Card c, Effect e, int tp, int lscale, int rscale, Effect|nil te) -> bool
```

## Description

Checks whether one extra Pendulum Summon effect allows c for the current scales.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `lscale` `int`
- `rscale` `int`
- `te` `Effect|nil`

## Returns

- `bool` - true if te allows c or te is nil.

## Source

- `Utilities/procedure.lua:1980`
