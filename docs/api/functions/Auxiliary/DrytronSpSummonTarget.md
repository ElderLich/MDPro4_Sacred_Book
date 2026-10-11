# Auxiliary.DrytronSpSummonTarget

## Signature

```lua
Auxiliary.DrytronSpSummonTarget(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Target function for the shared Drytron self-Summon effect. It checks the Monster Zone requirement, confirms the handler can be Special Summoned in face-up Defense Position, and sets Special Summon operation info.

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

- `Utilities/utility.lua:1060`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
