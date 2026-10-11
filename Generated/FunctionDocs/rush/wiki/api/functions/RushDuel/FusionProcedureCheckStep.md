# RushDuel.FusionProcedureCheckStep

Alias: `RD.FusionProcedureCheckStep`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionProcedureCheckStep(any c, any mg, any sg, any fc, any sub, any rep, any func1, any func2, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合手续 - 素材组合
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `mg` `any`: Type and behavior are not yet reviewed; see the source.
- `sg` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `rep` `any`: Type and behavior are not yet reviewed; see the source.
- `func1` `any`: Type and behavior are not yet reviewed; see the source.
- `func2` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:231`

```lua
function RushDuel.FusionProcedureCheckStep(c, mg, sg, fc, sub, rep, func1, func2, ...)
    if func2 then
        local res = false
        sg:AddCard(c)
        if func1(c, fc, false, mg, sg) then
            res = mg:IsExists(RushDuel.FusionProcedureCheckStep, 1, sg, mg, sg, fc, sub, rep, func2, ...)
        elseif sub and func1(c, fc, true, mg, sg) then
            res = mg:IsExists(RushDuel.FusionProcedureCheckStep, 1, sg, mg, sg, fc, false, rep, func2, ...)
        end
        sg:RemoveCard(c)
        return res
    elseif func1 then
        return func1(c, fc, sub, mg, sg)
    elseif rep then
        local eg = mg:Clone()
        eg:Sub(sg)
        return eg:FilterCount(rep, nil, fc, false, mg, sg) == #eg
    end
    return false
end
```
