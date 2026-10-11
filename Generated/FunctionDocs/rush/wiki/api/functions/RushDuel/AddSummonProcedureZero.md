# RushDuel.AddSummonProcedureZero

Alias: `RD.AddSummonProcedureZero`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddSummonProcedureZero(any card, any desc, any condition, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加不用解放的妥协召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:19`

```lua
function RushDuel.AddSummonProcedureZero(card, desc, condition, operation)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetCondition(RushDuel.SummonProcedureConditionZero(condition))
    if operation ~= nil then
        e1:SetOperation(operation)
    end
    e1:SetValue(SUMMON_VALUE_ZERO + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1)
    return e1
end
```
