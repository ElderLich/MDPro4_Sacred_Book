# RushDuel.IsCanBeUnionFusionMaterial2

Alias: `RD.IsCanBeUnionFusionMaterial2`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeUnionFusionMaterial2(any card, any code1, any code2) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以作为2只不同卡名的融合术素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code1` `any`: Type and behavior are not yet reviewed; see the source.
- `code2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:173`

```lua
function RushDuel.IsCanBeUnionFusionMaterial2(card, code1, code2)
    local effects = {card:IsHasEffect(EFFECT_UNION_FUSION_MATERIAL)}
    for i, effect in ipairs(effects) do
        local c1, c2 = effect:GetLabel()
        if (c1 == code1 and c2 == code2) or (c1 == code2 and c2 == code1) then
            return true
        end
    end
    return false
end
```
