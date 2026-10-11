# RushDuel.IsCanChangePosition

Alias: `RD.IsCanChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangePosition(any card, any effect, any player, any reason) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否改变表示形式
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:111`

```lua
function RushDuel.IsCanChangePosition(card, effect, player, reason)
    if not card:IsCanChangePosition() or RushDuel.IsMaximumMode(card) then
        return false
    end
    return true
end
```
