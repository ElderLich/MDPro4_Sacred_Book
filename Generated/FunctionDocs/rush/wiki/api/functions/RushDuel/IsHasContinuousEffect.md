# RushDuel.IsHasContinuousEffect

Alias: `RD.IsHasContinuousEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsHasContinuousEffect(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否拥有永续效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:134`

```lua
function RushDuel.IsHasContinuousEffect(card)
    local has_effect = card.continuous_effect
    if RushDuel.IsMaximumMode(card) then
        card:GetOverlayGroup():ForEach(function(tc)
            has_effect = has_effect or tc.continuous_effect
        end)
    end
    return has_effect
end
```
