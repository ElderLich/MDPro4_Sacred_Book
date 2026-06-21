# Auxiliary.gbspcon

## Signature

```lua
Auxiliary.gbspcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Simplified method for the filter condition of Gladiator Beast general effects (Special Summoned by the effect of a "Gladiator Beast" monster), used in effect registration for SetCondition
2619149, 4253484, 31247589, 42592719, 65984457, 78868776, though written differently, work fine
function aux.gbspcon(e, tp, eg, ep, ev, re, r, rp)
  local st=e:GetHandler():GetSummonType()
  return st&gt;=(SUMMON_TYPE_SPECIAL+100) and st&lt;(SUMMON_TYPE_SPECIAL+150)
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

- `Utilities/utility.lua:908`
