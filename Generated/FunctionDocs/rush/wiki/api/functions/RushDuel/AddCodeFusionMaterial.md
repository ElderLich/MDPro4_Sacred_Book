# RushDuel.AddCodeFusionMaterial

Alias: `RD.AddCodeFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddCodeFusionMaterial(any codes, any funcs, any code) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合素材 - 卡名
```

## Parameters

- `codes` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:76`

```lua
function RushDuel.AddCodeFusionMaterial(codes, funcs, code)
    table.insert(codes, code)
    table.insert(funcs, function(c, fc, sub, mg, sg)
        return c:IsFusionCode(code) or (sub and c:CheckFusionSubstitute(fc))
    end)
end
```
