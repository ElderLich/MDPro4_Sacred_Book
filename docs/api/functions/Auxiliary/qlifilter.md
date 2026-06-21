# Auxiliary.qlifilter

## Signature

```lua
Auxiliary.qlifilter(Effect e, Effect te) -> void
```

## Description

Simplified method for the filter function for Qli Monster general immunity (unaffected by effects of monsters with lower original Level/Rank than this card's Level), used in effect registration for SetValue
te is the effect that would affect e:GetHandler()
function aux.qlifilter(e, te)
  if te:IsActiveType(TYPE_MONSTER) and te:IsActivated() then
    local lv=e:GetHandler():GetLevel()
    local ec=te:GetOwner()
    if ec:IsType(TYPE_LINK) then
      return false
    elseif ec:IsType(TYPE_XYZ) then
      return ec:GetOriginalRank()<lv
    else
      return ec:GetOriginalLevel()<lv
    end
  else
    return false
  end
end

## Parameters

- `e` `Effect`
- `te` `Effect`

## Source

- `Utilities/utility.lua:892`
