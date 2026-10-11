# RushDuel.CanDraw

Alias: `RD.CanDraw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDraw(any desc, any player, any count, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 抽卡
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:570`

```lua
function RushDuel.CanDraw(desc, player, count, break_effect)
    if Duel.IsPlayerCanDraw(player, count) and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Draw(player, count, REASON_EFFECT)
    end
    return 0
end
```
