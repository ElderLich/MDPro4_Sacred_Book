# RushDuel.CostShowGroupExtra

Alias: `RD.CostShowGroupExtra`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowGroupExtra(any filter, any check, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把额外卡组给对方观看 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:232`

```lua
function RushDuel.CostShowGroupExtra(filter, check, min, max, set_label, set_object)
    return RushDuel._private_cost_select_group(HINTMSG_CONFIRM, filter, check, LOCATION_EXTRA, 0, min, max, false,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
        end)
end
```
