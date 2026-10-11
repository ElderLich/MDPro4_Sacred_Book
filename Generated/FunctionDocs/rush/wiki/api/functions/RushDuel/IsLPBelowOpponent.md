# RushDuel.IsLPBelowOpponent

Alias: `RD.IsLPBelowOpponent`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLPBelowOpponent(any player, any lp) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的LP比对方少 lp 以上
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `lp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:69`

```lua
function RushDuel.IsLPBelowOpponent(player, lp)
    return Duel.GetLP(player) <= Duel.GetLP(1 - player) - (lp or 0)
end
```
