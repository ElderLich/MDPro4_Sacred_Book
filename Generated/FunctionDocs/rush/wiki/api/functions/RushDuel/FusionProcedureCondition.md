# RushDuel.FusionProcedureCondition

Alias: `RD.FusionProcedureCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionProcedureCondition(any sub, any insf, any funcs, any rep, any min, any max, any checker) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合手续 - 条件
```

## Parameters

- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `insf` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `rep` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `checker` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:162`

```lua
function RushDuel.FusionProcedureCondition(sub, insf, funcs, rep, min, max, checker)
    return function(e, g, gc, chkfnf)
        local c = e:GetHandler()
        local tp = c:GetControler()
        if g == nil then
            return insf and Auxiliary.MustMaterialCheck(nil, tp, EFFECT_MUST_BE_FMATERIAL)
        end
        local mg = g:Filter(RushDuel.FusionProcedureMaterialFilter, c, c, sub, funcs, rep)
        if gc then
            if not mg:IsContains(gc) then
                return false
            end
            Duel.SetSelectedCard(gc)
        end
        local minc, maxc = #funcs + min, #funcs + max
        if RushDuel.MinFusionMaterialCount ~= nil and maxc < RushDuel.MinFusionMaterialCount then
            return false
        end
        if RushDuel.MaxFusionMaterialCount ~= nil and minc > RushDuel.MaxFusionMaterialCount then
            return false
        end
        return mg:CheckSubGroup(RushDuel.FusionProcedureMaterialChecker, minc, maxc, tp, c, chkfnf, sub, funcs, rep, checker)
    end
end
```
