# RushDuel.CostShowHand

Alias: `RD.CostShowHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowHand(any filter, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡给对方观看
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:206`

```lua
function RushDuel.CostShowHand(filter, min, max, set_label, set_object)
    return RushDuel._private_cost_select_match(HINTMSG_CONFIRM, filter, LOCATION_HAND, 0, min, max, true,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
            Duel.ShuffleHand(tp)
        end)
end
```
