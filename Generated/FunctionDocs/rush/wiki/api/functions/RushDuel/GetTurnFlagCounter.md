# RushDuel.GetTurnFlagCounter

Alias: `RD.GetTurnFlagCounter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetTurnFlagCounter(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取以回合为基础的标记计数器
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:251`

```lua
function RushDuel.GetTurnFlagCounter(player, code)
    local counter = Duel.GetFlagEffectLabel(player, code)
    if not counter then
        return 0
    else
        return counter
    end
end
```
