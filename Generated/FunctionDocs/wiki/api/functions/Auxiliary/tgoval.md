# Auxiliary.tgoval

## Signature

```lua
Auxiliary.tgoval(Effect e, Effect re, int rp) -> void
```

## Description

Simplified method for the filter function preventing being targeted by opponent's card effects, used in effect registration for SetValue
function aux.tgoval(e, re, rp)
  return rp==e:GetHandlerPlayer()
end

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:836`
