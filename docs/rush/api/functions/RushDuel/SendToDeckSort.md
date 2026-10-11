# RushDuel.SendToDeckSort

Alias: `RD.SendToDeckSort`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToDeckSort(any target, any sequence, any reason, any sort_player) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
返回卡组并排序
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `sequence` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `sort_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:163`

```lua
function RushDuel.SendToDeckSort(target, sequence, reason, sort_player)
    local g = RushDuel.ToMaximunGroup(target)
    local ct = 0
    if sequence == SEQ_DECKTOP then
        ct = Auxiliary.PlaceCardsOnDeckTop(sort_player, g, reason)
    elseif sequence == SEQ_DECKBOTTOM then
        ct = Auxiliary.PlaceCardsOnDeckBottom(sort_player, g, reason)
    else
        ct = Duel.SendtoDeck(target, nil, sequence, reason)
    end
    local og = Duel.GetOperatedGroup()
    return og, ct
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
