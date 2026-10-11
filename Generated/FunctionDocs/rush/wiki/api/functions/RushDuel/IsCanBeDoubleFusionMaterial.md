# RushDuel.IsCanBeDoubleFusionMaterial

Alias: `RD.IsCanBeDoubleFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeDoubleFusionMaterial(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以作为2只数量的融合术素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:151`

```lua
function RushDuel.IsCanBeDoubleFusionMaterial(card, code)
    local effects = {card:IsHasEffect(EFFECT_DOUBLE_FUSION_MATERIAL)}
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value == code then
            return true
        end
    end
    return false
end
```
