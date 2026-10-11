# RushDuel.SummonProcedureOperationTwo

Alias: `RD.SummonProcedureOperationTwo`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SummonProcedureOperationTwo(any filter, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:103`

```lua
function RushDuel.SummonProcedureOperationTwo(filter, operation)
    return function(e, tp, eg, ep, ev, re, r, rp, c)
        local mg = RushDuel._private_get_tribute_group(filter, e, tp)
        local sg = Duel.SelectTribute(tp, c, 2, 2, mg)
        c:SetMaterial(sg)
        Duel.Release(sg, REASON_SUMMON + REASON_MATERIAL)
        if operation then
            operation(e, tp, eg, ep, ev, re, r, rp, c, sg)
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
