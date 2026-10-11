# RushDuel.Recover

Alias: `RD.Recover`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Recover(any player, any recover) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 恢复 - 结算
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `recover` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:39`

```lua
function RushDuel.Recover(player, recover)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.Recover(player or p, recover or d, REASON_EFFECT)
end
```
