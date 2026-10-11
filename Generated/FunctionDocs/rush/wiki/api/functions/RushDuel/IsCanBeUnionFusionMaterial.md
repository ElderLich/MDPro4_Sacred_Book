# RushDuel.IsCanBeUnionFusionMaterial

Alias: `RD.IsCanBeUnionFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeUnionFusionMaterial(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以作为2只不同卡名的融合术素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:162`

```lua
function RushDuel.IsCanBeUnionFusionMaterial(card, code)
    local effects = {card:IsHasEffect(EFFECT_UNION_FUSION_MATERIAL)}
    for i, effect in ipairs(effects) do
        local code1, code2 = effect:GetLabel()
        if code1 == code or code2 == code then
            return true
        end
    end
    return false
end
```
