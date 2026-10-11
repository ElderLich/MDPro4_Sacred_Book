# RushDuel.FusionProcedureOperation

Alias: `RD.FusionProcedureOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionProcedureOperation(any sub, any insf, any funcs, any rep, any min, any max, any checker) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合手续 - 操作
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

`Rush/Utilities/RDFusion.lua:187`

```lua
function RushDuel.FusionProcedureOperation(sub, insf, funcs, rep, min, max, checker)
    return function(e, tp, eg, ep, ev, re, r, rp, gc, chkfnf)
        local c = e:GetHandler()
        local tp = c:GetControler()
        local mg = eg:Filter(RushDuel.FusionProcedureMaterialFilter, c, c, sub, funcs, rep)
        if gc then
            Duel.SetSelectedCard(gc)
        end
        local minc, maxc = #funcs + min, #funcs + max
        if RushDuel.MinFusionMaterialCount ~= nil then
            minc = math.max(minc, RushDuel.MinFusionMaterialCount)
        end
        if RushDuel.MaxFusionMaterialCount ~= nil then
            maxc = math.min(maxc, RushDuel.MaxFusionMaterialCount)
        end
        maxc = math.min(maxc, #mg)
        local sg = RushDuel.Select(HINTMSG_FUSION_MATERIAL, tp, mg, RushDuel.FusionProcedureMaterialChecker, true, minc, maxc, tp, c, chkfnf, sub, funcs, rep, checker)
        if sg == nil then
            sg = Group.CreateGroup()
        end
        Duel.SetFusionMaterial(sg)
    end
end
```
