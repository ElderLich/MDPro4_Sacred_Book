# RushDuel.FusionProcedureMaterialFilter

Alias: `RD.FusionProcedureMaterialFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionProcedureMaterialFilter(any c, any fc, any sub, any funcs, any rep) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合手续 - 素材过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `rep` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:147`

```lua
function RushDuel.FusionProcedureMaterialFilter(c, fc, sub, funcs, rep)
    if not c:IsCanBeFusionMaterial(fc, SUMMON_TYPE_FUSION) then
        return false
    end
    for _, func in ipairs(funcs) do
        if func(c, fc, sub) then
            return true
        end
    end
    if rep and rep(c, fc, sub) then
        return true
    end
    return false
end
```
