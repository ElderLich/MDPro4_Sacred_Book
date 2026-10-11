# RushDuel.SendDeckBottomToTop

Alias: `RD.SendDeckBottomToTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckBottomToTop(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
将玩家卡组最下面的N张卡移到卡组最上面
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:145`

```lua
function RushDuel.SendDeckBottomToTop(player, count)
    local g = Duel.GetFieldGroup(player, LOCATION_DECK, 0)
    for i = 1, count do
        Duel.MoveSequence(g:GetMinGroup(Card.GetSequence):GetFirst(), 0)
    end
end
```
