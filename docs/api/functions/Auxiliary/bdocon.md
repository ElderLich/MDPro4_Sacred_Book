# Auxiliary.bdocon

## Signature

```lua
Auxiliary.bdocon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when battling an opponent's monster, as a condition
function Auxiliary.bdocon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  return c:IsRelateToBattle() and c:IsStatus(STATUS_OPPO_BATTLE)
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

- `Utilities/utility.lua:769`
