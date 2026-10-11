# RushDuel.ResetFusionSummonMaterialCount

Alias: `RD.ResetFusionSummonMaterialCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ResetFusionSummonMaterialCount(any e) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
重置进行融合召唤的素材数量限制 (需要使用 Property 和 Label)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:614`

```lua
function RushDuel.ResetFusionSummonMaterialCount(e)
    e:SetProperty(0)
    e:SetLabel(0)
end
```
