# RushDuel.SummonProcedureConditionTwo

Alias: `RD.SummonProcedureConditionTwo`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SummonProcedureConditionTwo(any filter, any condition) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:93`

```lua
function RushDuel.SummonProcedureConditionTwo(filter, condition)
    return function(e, c, minc)
        if c == nil then
            return true
        end
        local tp = c:GetControler()
        local mg = RushDuel._private_get_tribute_group(filter, e, tp)
        return minc <= 2 and Duel.CheckTribute(c, 2, 2, mg) and (not condition or condition(c, e, tp))
    end
end
```
