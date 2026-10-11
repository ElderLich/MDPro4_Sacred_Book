# RushDuel.EnableChangeCode

Alias: `RD.EnableChangeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableChangeCode(any c, any code, any location, any condition) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续改变卡名
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `location` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:46`

```lua
function RushDuel.EnableChangeCode(c, code, location, condition)
    Auxiliary.AddCodeList(c, code)
    local loc = c:GetOriginalType() & TYPE_MONSTER ~= 0 and LOCATION_MZONE or LOCATION_SZONE
    local e1 = Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_CHANGE_CODE)
    e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
    e1:SetRange(location or loc)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    e1:SetValue(code)
    c:RegisterEffect(e1)
    return e1
end
```
