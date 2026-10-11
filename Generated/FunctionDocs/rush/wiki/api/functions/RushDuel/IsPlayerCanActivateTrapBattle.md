# RushDuel.IsPlayerCanActivateTrapBattle

Alias: `RD.IsPlayerCanActivateTrapBattle`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanActivateTrapBattle(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够在战斗阶段发动陷阱卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:417`

```lua
function RushDuel.IsPlayerCanActivateTrapBattle(player)
    return RushDuel.IsPlayerCanActivateTrap(player) and not Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP_BATTLE)
end
```
