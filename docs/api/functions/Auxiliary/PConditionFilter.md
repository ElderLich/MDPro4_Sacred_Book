# Auxiliary.PConditionFilter

## Signature

```lua
Auxiliary.PConditionFilter(Card c, Effect e, int tp, int lscale, int rscale, table eset) -> bool
```

## Description

Pendulum Summon candidate filter. It checks location, Level or pendulum_level, scales, Special Summon legality, forbidden state, and extra Pendulum Summon permissions.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `lscale` `int`
- `rscale` `int`
- `eset` `table`

## Returns

- `bool` - true if c can be Pendulum Summoned.

## Source

- `Utilities/procedure.lua:1991`
