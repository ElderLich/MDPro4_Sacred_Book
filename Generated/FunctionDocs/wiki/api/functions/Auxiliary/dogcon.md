# Auxiliary.dogcon

## Signature

```lua
Auxiliary.dogcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() was destroyed by the opponent and sent to the Graveyard from your field, used for SetCondition
function Auxiliary.dogcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  return c:GetPreviousControler()==tp and c:IsReason(REASON_DESTROY) and rp==1-tp
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

- `Utilities/utility.lua:791`
