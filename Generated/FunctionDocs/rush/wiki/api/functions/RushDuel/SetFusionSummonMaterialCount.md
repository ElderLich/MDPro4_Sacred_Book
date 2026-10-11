# RushDuel.SetFusionSummonMaterialCount

Alias: `RD.SetFusionSummonMaterialCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFusionSummonMaterialCount(any e, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
设置进行融合召唤的素材数量限制 (需要使用 Property 和 Label)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:608`

```lua
function RushDuel.SetFusionSummonMaterialCount(e, min, max)
    e:SetProperty(EFFECT_FLAG_SPSUM_PARAM)
    e:SetLabel(min, max)
end
```
