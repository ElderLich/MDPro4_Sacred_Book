# RushDuel.IsPlayerCanActivateTrap

Alias: `RD.IsPlayerCanActivateTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanActivateTrap(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够发动陷阱卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:413`

```lua
function RushDuel.IsPlayerCanActivateTrap(player)
    return not Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP)
end
```
