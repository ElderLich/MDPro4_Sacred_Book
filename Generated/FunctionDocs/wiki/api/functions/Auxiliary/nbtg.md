# Auxiliary.nbtg

## Signature

```lua
Auxiliary.nbtg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Target helper for effects that negate an activation and banish the activating card. It sets negate operation info, adds banish info when the activating card is still related, and marks CATEGORY_GRAVE_ACTION for effects activated in the Graveyard.

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

- `Utilities/utility.lua:1469`
