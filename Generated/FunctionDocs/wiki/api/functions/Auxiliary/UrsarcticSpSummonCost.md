# Auxiliary.UrsarcticSpSummonCost

## Signature

```lua
Auxiliary.UrsarcticSpSummonCost(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Checks and pays the shared Ursarctic Special Summon cost. The player releases a Level 7 or higher monster from the hand, or banishes a valid Graveyard replacement-cost card and consumes that effect's count limit.

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

## Returns

- `bool|nil` - true during cost checks; otherwise no meaningful return value.

## Source

- `Utilities/utility.lua:964`
