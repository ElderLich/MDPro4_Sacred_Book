# RushDuel.AddHandSpecialSummonProcedure

Alias: `RD.AddHandSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandSpecialSummonProcedure(any card, any desc, any condition, any target, any operation, any value, any position) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加手卡特殊召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:382`

```lua
function RushDuel.AddHandSpecialSummonProcedure(card, desc, condition, target, operation, value, position)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SPSUMMON_PROC)
    if position == nil then
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    else
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SPSUM_PARAM)
        e1:SetTargetRange(position, 0)
    end
    e1:SetRange(LOCATION_HAND)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if target ~= nil then
        e1:SetTarget(target)
    end
    if operation ~= nil then
        e1:SetOperation(operation)
    end
    if value ~= nil then
        e1:SetValue(value)
    end
    card:RegisterEffect(e1)
    return e1
end
```
