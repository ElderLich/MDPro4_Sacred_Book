# Auxiliary.imval1

## Signature

```lua
Auxiliary.imval1(Effect e, Card c) -> void
```

## Description

Simplified method for the filter function preventing a card from being targeted for attacks, used in effect registration for SetValue
function aux.imval1(e, c)
  return not c:IsImmuneToEffect(e)
end

## Parameters

- `e` `Effect`
- `c` `Card`

## Source

- `Utilities/utility.lua:820`
