# RushDuel.SummonProcedureOperationThree

Alias: `RD.SummonProcedureOperationThree`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SummonProcedureOperationThree(any filter, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:142`

```lua
function RushDuel.SummonProcedureOperationThree(filter, operation)
    return function(e, tp, eg, ep, ev, re, r, rp, c)
        local mg = RushDuel._private_get_tribute_group(filter, e, tp)
        local sg = Duel.SelectTribute(tp, c, 3, 3, mg)
        c:SetMaterial(sg)
        Duel.Release(sg, REASON_SUMMON + REASON_MATERIAL)
        if operation then
            operation(e, tp, eg, ep, ev, re, r, rp, c, sg)
        end
    end
end
```
