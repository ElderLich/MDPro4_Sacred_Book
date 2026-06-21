# Auxiliary.GetLinkCount

## Signature

```lua
Auxiliary.GetLinkCount(Card c) -> void
```

## Description

Return the number of materials card c counts as when used as a Link Material
function Auxiliary.GetLinkCount(c)
  if c:IsType(TYPE_LINK) and c:GetLink()&gt;1 then
    return 1+0x10000*c:GetLink()
  else return 1 end
end

## Parameters

- `c` `Card`

## Source

- `Utilities/procedure.lua:2158`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
