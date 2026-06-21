# Auxiliary.PConditionExtraFilter

## Signature

```lua
Auxiliary.PConditionExtraFilter(Card c, Effect e, int tp, int lscale, int rscale, table eset) -> bool
```

## Description

Checks whether any extra Pendulum Summon effect in eset allows c for the current scales.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `lscale` `int`
- `rscale` `int`
- `eset` `table`

## Returns

- `bool` - true if any extra Pendulum Summon effect allows c.

## Source

- `Utilities/procedure.lua:1985`
