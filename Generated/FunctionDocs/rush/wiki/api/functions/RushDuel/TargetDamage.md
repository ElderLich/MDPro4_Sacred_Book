# RushDuel.TargetDamage

Alias: `RD.TargetDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDamage(any player, any damage) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 伤害 - 对象
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `damage` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:17`

```lua
function RushDuel.TargetDamage(player, damage)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(damage)
    Duel.SetOperationInfo(0, CATEGORY_DAMAGE, nil, 0, player, damage)
end
```
