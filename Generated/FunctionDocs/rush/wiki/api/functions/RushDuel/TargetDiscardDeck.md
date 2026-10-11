# RushDuel.TargetDiscardDeck

Alias: `RD.TargetDiscardDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDiscardDeck(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 盲堆 - 对象
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:23`

```lua
function RushDuel.TargetDiscardDeck(player, count)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(count)
    Duel.SetOperationInfo(0, CATEGORY_DECKDES, nil, 0, player, count)
end
```
