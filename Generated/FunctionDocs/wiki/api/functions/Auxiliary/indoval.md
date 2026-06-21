# Auxiliary.indoval

## Signature

```lua
Auxiliary.indoval(Effect e, Effect re, int rp) -> void
```

## Description

Simplified method for the filter function preventing destruction by opponent's card effects, used in effect registration for SetValue
function aux.indoval(e, re, rp)
  return rp==1-e:GetHandlerPlayer()
end

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:828`
