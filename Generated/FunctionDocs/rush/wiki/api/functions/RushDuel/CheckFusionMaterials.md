# RushDuel.CheckFusionMaterials

Alias: `RD.CheckFusionMaterials`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckFusionMaterials(any group, any fc, any sub, any funcs) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
检查融合素材 (多组素材使用)
```

## Parameters

- `group` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:217`

```lua
function RushDuel.CheckFusionMaterials(group, fc, sub, funcs)
    if #group < #funcs then
        return false
    end
    local sg = Group.CreateGroup()
    return group:IsExists(RushDuel.CheckFusionMaterialsStep, 1, nil, group, sg, fc, sub, table.unpack(funcs))
end
```
