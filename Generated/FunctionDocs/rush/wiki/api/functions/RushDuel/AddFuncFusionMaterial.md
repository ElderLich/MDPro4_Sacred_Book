# RushDuel.AddFuncFusionMaterial

Alias: `RD.AddFuncFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFuncFusionMaterial(any codes, any funcs, any func) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合素材 - 条件
```

## Parameters

- `codes` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `func` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:83`

```lua
function RushDuel.AddFuncFusionMaterial(codes, funcs, func)
    table.insert(funcs, function(c, fc, sub, mg, sg)
        return func(c, fc, sub, mg, sg) and not c:IsHasEffect(6205579)
    end)
end
```
