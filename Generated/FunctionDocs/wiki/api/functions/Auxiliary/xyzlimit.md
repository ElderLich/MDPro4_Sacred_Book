# Auxiliary.xyzlimit

## Signature

```lua
Auxiliary.xyzlimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Xyz Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.xyzlimit(e, se, sp, st)
  return st&SUMMON_TYPE_XYZ==SUMMON_TYPE_XYZ
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2301`
