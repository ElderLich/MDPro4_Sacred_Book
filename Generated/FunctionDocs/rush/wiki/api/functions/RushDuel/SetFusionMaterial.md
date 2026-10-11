# RushDuel.SetFusionMaterial

Alias: `RD.SetFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFusionMaterial(any card, any codes, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
手动添加融合素材列表
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `codes` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:128`

```lua
function RushDuel.SetFusionMaterial(card, codes, min, max)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    RushDuel.SetFusionMaterialData(card, codes, min, max)
end
```
