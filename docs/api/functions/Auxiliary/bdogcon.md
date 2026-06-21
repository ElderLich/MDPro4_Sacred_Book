# Auxiliary.bdogcon

## Signature

```lua
Auxiliary.bdogcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING, when battling an opponent's monster and destroying it by battle, sending it to the Graveyard, as a condition
function Auxiliary.bdogcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  local bc=c:GetBattleTarget()
  return c:IsRelateToBattle() and c:IsStatus(STATUS_OPPO_BATTLE) and bc:IsLocation(LOCATION_GRAVE) and bc:IsType(TYPE_MONSTER)
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

- `Utilities/utility.lua:780`
