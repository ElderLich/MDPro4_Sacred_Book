# RushDuel.CostSendMZoneToDeckTopOrBottom

Alias: `RD.CostSendMZoneToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMZoneToDeckTopOrBottom(any filter, any min, any max, any top_desc, any bottom_desc, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让怪兽返回卡组上面或下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:401`

```lua
function RushDuel.CostSendMZoneToDeckTopOrBottom(filter, min, max, top_desc, bottom_desc, except_self, set_label_before,
    set_object_before, set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckTopOrBottom(filter, LOCATION_MZONE, min, max, except_self, top_desc, bottom_desc,
        true, false, set_label_before, set_object_before, set_label_after, set_object_after)
end
```
