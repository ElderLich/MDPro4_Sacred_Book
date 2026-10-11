# RushDuel.TargetDraw

Alias: `RD.TargetDraw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDraw(int player, int count) -> void
```

## Description

Stores the target player and draw count on the current chain link and declares CATEGORY_DRAW operation information. This helper does not draw cards or check deck availability.

## Parameters

- `player` `int`: Drawing player.
- `count` `int`: Number to draw.

## Returns

No return values.

## Source

`Rush/Utilities/RDTarget.lua:5`

```lua
function RushDuel.TargetDraw(player, count)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(count)
    Duel.SetOperationInfo(0, CATEGORY_DRAW, nil, 0, player, count)
end
```
