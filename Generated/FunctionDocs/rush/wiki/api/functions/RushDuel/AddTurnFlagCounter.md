# RushDuel.AddTurnFlagCounter

Alias: `RD.AddTurnFlagCounter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddTurnFlagCounter(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加以回合为基础的标记计数器
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:241`

```lua
function RushDuel.AddTurnFlagCounter(player, code)
    local counter = Duel.GetFlagEffectLabel(player, code)
    if not counter then
        Duel.RegisterFlagEffect(player, code, RESET_PHASE + PHASE_END, 0, 1, 1)
    else
        Duel.SetFlagEffectLabel(player, code, counter + 1)
    end
end
```
