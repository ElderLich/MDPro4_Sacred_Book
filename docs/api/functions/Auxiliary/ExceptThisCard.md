# Auxiliary.ExceptThisCard

## Signature

```lua
Auxiliary.ExceptThisCard(Effect e) -> void
```

## Description

If e:GetHandler() is related to effect e, return e:GetHandler(); otherwise return nil
function aux.ExceptThisCard(e)
  local c=e:GetHandler()
  if c:IsRelateToEffect(e) then return c else return nil end
end

## Parameters

- `e` `Effect`

## Source

- `Utilities/utility.lua:1176`
