# RushDuel.CostSendOnFieldToDeckBottom

Alias: `RD.CostSendOnFieldToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendOnFieldToDeckBottom(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让场上的卡返回卡组下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:413`

```lua
function RushDuel.CostSendOnFieldToDeckBottom(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_ONFIELD, min, max, except_self, SEQ_DECKBOTTOM, true,
        false, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
