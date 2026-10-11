# RushDuel.TargetRecover

Alias: `RD.TargetRecover`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetRecover(any player, any recover) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 恢复 - 对象
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `recover` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:11`

```lua
function RushDuel.TargetRecover(player, recover)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(recover)
    Duel.SetOperationInfo(0, CATEGORY_RECOVER, nil, 0, player, recover)
end
```
