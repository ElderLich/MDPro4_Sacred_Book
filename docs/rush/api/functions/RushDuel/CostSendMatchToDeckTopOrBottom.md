# RushDuel.CostSendMatchToDeckTopOrBottom

Alias: `RD.CostSendMatchToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMatchToDeckTopOrBottom(any filter, any field, any min, any max, any except_self, any top_desc, any bottom_desc, any hint_selection, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 选择匹配卡片, 返回卡组上面或下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `field` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint_selection` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:174`

```lua
function RushDuel.CostSendMatchToDeckTopOrBottom(filter, field, min, max, except_self, top_desc, bottom_desc,
    hint_selection, confirm, set_label_before, set_object_before, set_label_after, set_object_after)
    local action = RushDuel._private_action_send_deck_top_or_bottom(top_desc, bottom_desc, REASON_COST, hint_selection,
        confirm, set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel._private_cost_select_match(HINTMSG_TODECK, filter, field, 0, min, max, except_self, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
