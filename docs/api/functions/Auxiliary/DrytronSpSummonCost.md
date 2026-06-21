# Auxiliary.DrytronSpSummonCost

## Signature

```lua
Auxiliary.DrytronSpSummonCost(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Checks and pays the shared Drytron self-Summon cost.
The player must not have Special Summoned a monster that can be Normal Summoned/Set this turn. On payment, it applies the matching Special Summon oath, then either Tributes one valid cost card or banishes one valid replacement-cost card.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`
- `chk` `bool`

## Source

- `Utilities/utility.lua:1020`
