# RushDuel.CostSendGroupToDeckSort

Alias: `RD.CostSendGroupToDeckSort`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGroupToDeckSort(any filter, any check, any field, any min, any max, any except_self, any sequence, any hint_selection, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 选择子卡片组, 返回卡组 (排序)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `field` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `sequence` `any`: Type and behavior are not yet reviewed; see the source.
- `hint_selection` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:167`

```lua
function RushDuel.CostSendGroupToDeckSort(filter, check, field, min, max, except_self, sequence, hint_selection,
    confirm, set_label_before, set_object_before, set_label_after, set_object_after)
    local action = RushDuel._private_action_send_deck_sort(sequence, REASON_COST, hint_selection, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel._private_cost_select_group(HINTMSG_TODECK, filter, check, field, 0, min, max, except_self, action)
end
```
