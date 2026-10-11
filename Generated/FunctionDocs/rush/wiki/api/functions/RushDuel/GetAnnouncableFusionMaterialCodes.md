# RushDuel.GetAnnouncableFusionMaterialCodes

Alias: `RD.GetAnnouncableFusionMaterialCodes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetAnnouncableFusionMaterialCodes(any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取可以宣言的融合素材的卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:641`

```lua
function RushDuel.GetAnnouncableFusionMaterialCodes(card, target)
    local codes = {}
    local code = card:GetCode()
    for code, _ in pairs(target.material or {}) do
        if not card:IsCode(code) then
            table.insert(codes, code)
        end
    end
    return codes
end
```
