# Auxiliary.SpiritReturnTargetOptional

## Signature

```lua
Auxiliary.SpiritReturnTargetOptional(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Target function for the optional Spirit Monster End Phase return effect. During the check step it requires the handler to be able to return to the hand, then registers return-to-hand operation info.

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

- `Utilities/utility.lua:212`
