# RushDuel.IsPlayerNoDrawInThisMain

Alias: `RD.IsPlayerNoDrawInThisMain`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerNoDrawInThisMain(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家在这次主要阶段没有抽卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:73`

```lua
function RushDuel.IsPlayerNoDrawInThisMain(player)
    return Duel.GetFlagEffect(player, FLAG_HAS_DRAW_IN_MAIN_PHASE) == 0
end
```
