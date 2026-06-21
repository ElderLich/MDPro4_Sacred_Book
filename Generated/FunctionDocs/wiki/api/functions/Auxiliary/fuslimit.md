# Auxiliary.fuslimit

## Signature

```lua
Auxiliary.fuslimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Fusion Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.fuslimit(e, se, sp, st)
  return st&SUMMON_TYPE_FUSION==SUMMON_TYPE_FUSION
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2289`
