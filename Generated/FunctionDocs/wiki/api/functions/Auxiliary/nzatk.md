# Auxiliary.nzatk

## Signature

```lua
Auxiliary.nzatk(Card c) -> void
```

## Description

Simplified method for the filter function for face-up monsters with non-zero ATK
function aux.nzatk(c)
  return c:IsFaceup() and c:GetAttack()&gt;0
end

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:840`
