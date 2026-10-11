# RushDuel.Draw

Alias: `RD.Draw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Draw([int player], [int count]) -> int
```

## Description

Draws with REASON_EFFECT using the supplied player/count, or the current chain's target player/parameter when arguments are omitted. Pair RD.TargetDraw(tp, count) in targeting with RD.Draw() in resolution.

## Parameters

- `player` `int` (optional): Player; defaults to CHAININFO_TARGET_PLAYER.
- `count` `int` (optional): Count; defaults to CHAININFO_TARGET_PARAM.

## Returns

- `int`: Result returned by Duel.Draw.

## Source

`Rush/Utilities/RDTarget.lua:34`

```lua
function RushDuel.Draw(player, count)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.Draw(player or p, count or d, REASON_EFFECT)
end
```
