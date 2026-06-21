# Auxiliary.tgsval

## Signature

```lua
Auxiliary.tgsval(Effect e, Effect re, int rp) -> void
```

## Description

Simplified method for the filter function preventing being targeted by your own card effects, used in effect registration for SetValue
function aux.tgsval(e, re, rp)
  return rp==e:GetHandlerPlayer()
end

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:832`
