# RushDuel.Damage

Alias: `RD.Damage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Damage(any player, any damage) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 伤害 - 结算
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `damage` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:44`

```lua
function RushDuel.Damage(player, damage)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.Damage(player or p, damage or d, REASON_EFFECT)
end
```
