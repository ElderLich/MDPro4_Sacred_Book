# RushDuel.CostSendGraveSubToDeckTopOrBottom

Alias: `RD.CostSendGraveSubToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveSubToDeckTopOrBottom(any filter, any check, any min, any max, any top_desc, any bottom_desc, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组上面或下面 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:485`

```lua
function RushDuel.CostSendGraveSubToDeckTopOrBottom(filter, check, min, max, top_desc, bottom_desc, set_label_before,
    set_object_before, set_label_after, set_object_after)
    return RushDuel.CostSendGroupToDeckTopOrBottom(filter, check, LOCATION_GRAVE, min, max, false, top_desc,
        bottom_desc, false, true, set_label_before, set_object_before, set_label_after, set_object_after)
end
```
