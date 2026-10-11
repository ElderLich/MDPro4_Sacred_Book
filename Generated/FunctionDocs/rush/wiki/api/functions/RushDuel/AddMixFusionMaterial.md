# RushDuel.AddMixFusionMaterial

Alias: `RD.AddMixFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddMixFusionMaterial(any codes, any funcs, any list) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合素材 - 混合
```

## Parameters

- `codes` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `list` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:89`

```lua
function RushDuel.AddMixFusionMaterial(codes, funcs, list)
    local mixs = {}
    for _, val in ipairs(list) do
        local val_type = type(val)
        if val_type == "number" then
            RushDuel.AddCodeFusionMaterial(codes, mixs, val)
        elseif val_type == "function" then
            RushDuel.AddFuncFusionMaterial(codes, mixs, val)
        end
    end
    table.insert(funcs, function(c, fc, sub, mg, sg)
        for _, func in ipairs(mixs) do
            if func(c, fc, sub, mg, sg) then
                return true
            end
        end
        return false
    end)
end
```
