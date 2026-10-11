# RushDuel.IsCanChangeRace

Alias: `RD.IsCanChangeRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeRace(any card, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以被改变种族
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:355`

```lua
function RushDuel.IsCanChangeRace(card, race)
    local effects = {card:IsHasEffect(EFFECT_CHANGE_RACE)}
    local curret = card:GetOriginalRace()
    local active = nil
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value ~= curret or effect:GetLabel() == FLAG_ATTACH_EFFECT then
            curret = value
            active = effect
        end
    end
    -- 被改变了种族
    if active then
        if active:GetLabel() ~= FLAG_ATTACH_EFFECT then
            -- 不是赋予类效果，可以随便更改
            return true
        else
            return not card:IsRace(curret)
        end
    else
        return not card:IsRace(race)
    end
end
```
