# RushDuel.CheckFusionMaterialsStep

Alias: `RD.CheckFusionMaterialsStep`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckFusionMaterialsStep(any c, any mg, any sg, any fc, any sub, any fun1, any fun2, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `mg` `any`: Type and behavior are not yet reviewed; see the source.
- `sg` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `fun1` `any`: Type and behavior are not yet reviewed; see the source.
- `fun2` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:224`

```lua
function RushDuel.CheckFusionMaterialsStep(c, mg, sg, fc, sub, fun1, fun2, ...)
    if fun2 then
        sg:AddCard(c)
        local res = false
        if fun1(c, fc, false, mg, sg) then
            res = mg:IsExists(RushDuel.CheckFusionMaterialsStep, 1, sg, mg, sg, fc, sub, fun2, ...)
        elseif sub and fun1(c,fc,true,mg,sg) then
            res = mg:IsExists(RushDuel.CheckFusionMaterialsStep, 1, sg, mg, sg, fc, false, fun2, ...)
        end
        sg:RemoveCard(c)
        return res
    else
        return fun1(c, fc, sub, mg, sg)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
