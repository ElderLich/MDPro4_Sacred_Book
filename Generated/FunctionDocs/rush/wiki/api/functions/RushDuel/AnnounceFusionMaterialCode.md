# RushDuel.AnnounceFusionMaterialCode

Alias: `RD.AnnounceFusionMaterialCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AnnounceFusionMaterialCode(any player, any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
宣言融合素材的卡名
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:653`

```lua
function RushDuel.AnnounceFusionMaterialCode(player, card, target)
    local codes = RushDuel.GetAnnouncableFusionMaterialCodes(card, target)
    if #codes > 0 then
        return RushDuel.AnnounceCodes(player, codes)
    else
        return nil
    end
end
```
