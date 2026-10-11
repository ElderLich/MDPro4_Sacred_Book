# RushDuel.IsCanDoubleTribute

Alias: `RD.IsCanDoubleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanDoubleTribute(any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以使用双重解放
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:380`

```lua
function RushDuel.IsCanDoubleTribute(card, target)
    local effects = {card:IsHasEffect(EFFECT_DOUBLE_TRIBUTE)}
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value == 1 then
            return true
        elseif value(effect, target) then
            return true
        end
    end
    return false
end
```
