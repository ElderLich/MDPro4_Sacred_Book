# Auxiliary.damcon1

## Signature

```lua
Auxiliary.damcon1(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Simplified method for the condition of player tp taking damage, used in effect registration for SetCondition
function aux.damcon1(e, tp, eg, ep, ev, re, r, rp)
  local e1=Duel.IsPlayerAffectedByEffect(tp, EFFECT_REVERSE_DAMAGE)
  local e2=Duel.IsPlayerAffectedByEffect(tp, EFFECT_REVERSE_RECOVER)
  local rd=e1 and not e2
  local rr=not e1 and e2
  local ex,cg,ct,cp,cv=Duel.GetOperationInfo(ev, CATEGORY_DAMAGE)
  if ex and (cp==tp or cp==PLAYER_ALL) and not rd and not Duel.IsPlayerAffectedByEffect(tp, EFFECT_NO_EFFECT_DAMAGE) then
    return true
  end
  ex,cg,ct,cp,cv=Duel.GetOperationInfo(ev, CATEGORY_RECOVER)
  return ex and (cp==tp or cp==PLAYER_ALL) and rr and not Duel.IsPlayerAffectedByEffect(tp, EFFECT_NO_EFFECT_DAMAGE)
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

- `Utilities/utility.lua:879`
