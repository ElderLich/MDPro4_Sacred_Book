# RushDuel.FilterToDeckTarget

Alias: `RD.FilterToDeckTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FilterToDeckTarget(any card, any effect, any player, any reason, any hints) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
过滤可以加入卡组的卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `hints` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:354`

```lua
function RushDuel.FilterToDeckTarget(card, effect, player, reason, hints)
    if effect:IsHasProperty(EFFECT_FLAG_IGNORE_IMMUNE) then
        return true
    end
    local effects = {card:IsHasEffect(EFFECT_CANNOT_TO_DECK_EFFECT)}
    for i, e in ipairs(effects) do
        local value = e:GetValue()
        if value == 1 then
            hints:AddCard(e:GetHandler())
            return false
        elseif type(value) == "function" and value(e, effect, reason, player) then
            hints:AddCard(e:GetHandler())
            return false
        end
    end
    return true
end
```
