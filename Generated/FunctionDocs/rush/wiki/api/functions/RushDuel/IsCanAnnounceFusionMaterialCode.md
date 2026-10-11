# RushDuel.IsCanAnnounceFusionMaterialCode

Alias: `RD.IsCanAnnounceFusionMaterialCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAnnounceFusionMaterialCode(any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以宣言融合素材的卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:184`

```lua
function RushDuel.IsCanAnnounceFusionMaterialCode(card, target)
    local codes = RushDuel.GetAnnouncableFusionMaterialCodes(card, target)
    return #codes > 0
end
```
