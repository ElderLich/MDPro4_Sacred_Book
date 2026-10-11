# RushDuel.IsPlayerCanUseRaceAttack

Alias: `RD.IsPlayerCanUseRaceAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanUseRaceAttack(any player, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够使用特定种族进行攻击
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:400`

```lua
function RushDuel.IsPlayerCanUseRaceAttack(player, race)
    if Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ATTACK) then
        return false
    end
    local effects = {Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_RACE_CANNOT_ATTACK)}
    for i, effect in ipairs(effects) do
        if (race & effect:GetValue()) == race then
            return false
        end
    end
    return true
end
```
