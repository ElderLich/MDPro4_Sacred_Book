# RushDuel.CostChangePosition

Alias: `RD.CostChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChangePosition(any filter, any min, any max, any position, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 改变怪兽的表示形式
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:497`

```lua
function RushDuel.CostChangePosition(filter, min, max, position, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    local action = RushDuel._private_action_change_position(position, set_label_before, set_object_before,
        set_label_after, set_object_after)
    return RushDuel._private_cost_select_match(HINTMSG_POSCHANGE, filter, LOCATION_MZONE, 0, min, max, except_self,
        action)
end
```
