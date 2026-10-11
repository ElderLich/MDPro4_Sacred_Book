# RushDuel.AddSummonProcedureThree

Alias: `RD.AddSummonProcedureThree`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddSummonProcedureThree(any card, any desc, any condition, any filter, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加解放3只的妥协召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:116`

```lua
function RushDuel.AddSummonProcedureThree(card, desc, condition, filter, operation)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetCondition(RushDuel.SummonProcedureConditionThree(filter, condition))
    e1:SetOperation(RushDuel.SummonProcedureOperationThree(filter, operation))
    e1:SetValue(SUMMON_TYPE_ADVANCE + SUMMON_VALUE_THREE + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1)
    local mt = getmetatable(card)
    if mt.is_can_triple_tribute == nil then
        mt.is_can_triple_tribute = true
    end
    return e1
end
```
