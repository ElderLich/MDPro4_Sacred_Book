# Auxiliary.GetLinkCount

## Signature

```lua
Auxiliary.GetLinkCount(Card c) -> void
```

## Description

Return the number of materials card c counts as when used as a Link Material
function Auxiliary.GetLinkCount(c)
  if c:IsType(TYPE_LINK) and c:GetLink()>1 then
    return 1+0x10000*c:GetLink()
  else return 1 end
end

## Parameters

- `c` `Card`

## Source

- `Utilities/procedure.lua:2158`
