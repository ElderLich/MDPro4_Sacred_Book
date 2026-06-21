# Auxiliary.evospcon

## Signature

```lua
Auxiliary.evospcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Simplified method for the filter condition of Evolsaur general effects (Special Summoned by the effect of an "Evolsaur" monster), used in effect registration for SetCondition
function aux.evospcon(e, tp, eg, ep, ev, re, r, rp)
  local st=e:GetHandler():GetSummonType()
  return st>=(SUMMON_TYPE_SPECIAL+150) and st<(SUMMON_TYPE_SPECIAL+180)
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

- `Utilities/utility.lua:914`
