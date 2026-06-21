# Auxiliary.nzdef

## Signature

```lua
Auxiliary.nzdef(Card c) -> void
```

## Description

Simplified method for the filter function for face-up monsters with non-zero DEF
function aux.nzdef(c)
  return c:IsFaceup() and c:GetDefense()&gt;0
end

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:844`
