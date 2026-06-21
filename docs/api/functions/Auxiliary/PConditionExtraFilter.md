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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
