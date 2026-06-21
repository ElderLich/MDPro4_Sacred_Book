# Auxiliary.penlimit

## Signature

```lua
Auxiliary.penlimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Pendulum Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.penlimit(e, se, sp, st)
  return st&SUMMON_TYPE_PENDULUM==SUMMON_TYPE_PENDULUM
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2305`
