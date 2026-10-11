# RushDuel.SummonProcedureConditionZero

Alias: `RD.SummonProcedureConditionZero`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SummonProcedureConditionZero(any condition) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:33`

```lua
function RushDuel.SummonProcedureConditionZero(condition)
    return function(e, c, minc)
        if c == nil then
            return true
        end
        local tp = c:GetControler()
        return minc == 0 and c:IsLevelAbove(5) and Duel.GetLocationCount(tp, LOCATION_MZONE) > 0 and
                   (not condition or condition(c, e, tp))
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
