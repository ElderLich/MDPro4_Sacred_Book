# Auxiliary.indsval

## Signature

```lua
Auxiliary.indsval(Effect e, Effect re, int rp) -> void
```

## Description

Simplified method for the filter function preventing destruction by your own card effects, used in effect registration for SetValue
function aux.indsval(e, re, rp)
  return rp==e:GetHandlerPlayer()
end

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:824`
