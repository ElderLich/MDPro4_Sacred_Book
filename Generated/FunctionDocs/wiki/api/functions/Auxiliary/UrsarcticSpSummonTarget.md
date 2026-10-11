# Auxiliary.UrsarcticSpSummonTarget

## Signature

```lua
Auxiliary.UrsarcticSpSummonTarget(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Target function for the shared Ursarctic Special Summon effect. It requires an open Monster Zone and that the handler can be Special Summoned, then sets Special Summon operation info.

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

- `bool|nil` - true during valid target checks; otherwise no meaningful return value.

## Source

- `Utilities/utility.lua:979`
