# RushDuel.IsPlayerNoActivateInThisTurn

Alias: `RD.IsPlayerNoActivateInThisTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerNoActivateInThisTurn(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家在这个回合没有发动过特定卡名的效果
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:81`

```lua
function RushDuel.IsPlayerNoActivateInThisTurn(player, code)
    local codes = RushDuel.ActivateCodes[player + 1] or {}
    return not codes[code]
end
```
