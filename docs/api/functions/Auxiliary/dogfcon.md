# Auxiliary.dogfcon

## Signature

```lua
Auxiliary.dogfcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Condition for EVENT_TO_GRAVE triggers: true when the handler was previously on the field under tp's control, was destroyed, and the opponent was the reason player.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:796`
