# Auxiliary.linklimit

## Signature

```lua
Auxiliary.linklimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Link Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.linklimit(e, se, sp, st)
  return st&SUMMON_TYPE_LINK==SUMMON_TYPE_LINK
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2309`
