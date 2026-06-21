# Auxiliary.bdgcon

## Signature

```lua
Auxiliary.bdgcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING and when an opponent's monster is destroyed by battle and sent to the Graveyard, as a condition
function Auxiliary.bdgcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  local bc=c:GetBattleTarget()
  return c:IsRelateToBattle() and bc:IsLocation(LOCATION_GRAVE) and bc:IsType(TYPE_MONSTER)
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

- `Utilities/utility.lua:774`
