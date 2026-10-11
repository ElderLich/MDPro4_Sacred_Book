# RushDuel.DiscardDeck

Alias: `RD.DiscardDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.DiscardDeck(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 盲堆 - 结算
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:49`

```lua
function RushDuel.DiscardDeck(player, count)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.DiscardDeck(player or p, count or d, REASON_EFFECT)
end
```
