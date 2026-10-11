# RushDuel.CanDiscardDeck

Alias: `RD.CanDiscardDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDiscardDeck(any desc, any player, any min, any max, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 盲堆
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:580`

```lua
function RushDuel.CanDiscardDeck(desc, player, min, max, break_effect, target_player)
    target_player = target_player or player
    if Duel.IsPlayerCanDiscardDeck(target_player, min) and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        max = max or min
        local ct = Duel.GetFieldGroupCount(target_player, LOCATION_DECK, 0)
        local ops = {}
        for i = min, math.min(max, ct) do
            if Duel.IsPlayerCanDiscardDeck(target_player, i) then
                table.insert(ops, i)
            end
        end
        local count = 0
        if #ops == 1 then
            count = table.remove(ops)
        elseif #ops > 1 then
            Duel.Hint(HINT_SELECTMSG, player, HINTMSG_OPERATE_COUNT)
            count = Duel.AnnounceNumber(player, table.unpack(ops))
        end
        return Duel.DiscardDeck(target_player, count, REASON_EFFECT)
    end
    return 0
end
```
