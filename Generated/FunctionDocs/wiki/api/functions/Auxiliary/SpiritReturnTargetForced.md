# Auxiliary.SpiritReturnTargetForced

## Signature

```lua
Auxiliary.SpiritReturnTargetForced(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Target function for the mandatory Spirit Monster End Phase return effect. During the check step it always returns true, then registers return-to-hand operation info.

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

- `bool|nil` - true during target checks; otherwise no meaningful return value.

## Source

- `Utilities/utility.lua:204`
