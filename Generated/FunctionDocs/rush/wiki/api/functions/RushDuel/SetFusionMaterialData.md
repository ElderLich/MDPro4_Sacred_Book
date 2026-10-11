# RushDuel.SetFusionMaterialData

Alias: `RD.SetFusionMaterialData`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFusionMaterialData(any card, any codes, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
设置融合素材数据
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `codes` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:110`

```lua
function RushDuel.SetFusionMaterialData(card, codes, min, max)
    local mt = getmetatable(card)
    -- 卡名记述的素材
    if codes ~= nil then
        RushDuel.AddCodeList(card, codes)
        local mat = {}
        for _, code in ipairs(codes) do
            mat[code] = true
        end
        mt.material = mat
    end
    -- 素材的数量
    if mt.material_count == nil then
        mt.material_count = {min, max}
    end
end
```
