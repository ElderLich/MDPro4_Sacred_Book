# RushDuel.CostSendHandSubToGrave

Alias: `RD.CostSendHandSubToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandSubToGrave(any filter, any check, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡送去墓地 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:306`

```lua
function RushDuel.CostSendHandSubToGrave(filter, check, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    local cost = RushDuel.CostSendGroupToGrave(filter, check, LOCATION_HAND, min, max, true, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel.NoCostCheck(cost, EFFECT_NO_COST_SEND_HAND_TO_GRAVE)
end
```
