# Auxiliary.bdcon

## Signature

```lua
Auxiliary.bdcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for the condition of EVENT_BATTLE_DESTROYING
function Auxiliary.bdcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  return c:IsRelateToBattle()
end

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

- `Utilities/utility.lua:764`
