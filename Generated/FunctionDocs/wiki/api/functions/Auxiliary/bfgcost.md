# Auxiliary.bfgcost

## Signature

```lua
Auxiliary.bfgcost(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Simplified method for the filter condition of banishing this card, used in effect registration for cost
function aux.bfgcost(e, tp, eg, ep, ev, re, r, rp, chk)
  if chk==0 then return e:GetHandler():IsAbleToRemoveAsCost() end
  Duel.Remove(e:GetHandler(), POS_FACEUP, REASON_COST)
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
- `chk` `bool`

## Source

- `Utilities/utility.lua:1121`
