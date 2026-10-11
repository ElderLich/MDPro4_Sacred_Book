# RushDuel.CostShowGroupHand

Alias: `RD.CostShowGroupHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowGroupHand(any filter, any check, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡给对方观看 (子卡片组)
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

`Rush/Utilities/RDCost.lua:215`

```lua
function RushDuel.CostShowGroupHand(filter, check, min, max, set_label, set_object)
    return RushDuel._private_cost_select_group(HINTMSG_CONFIRM, filter, check, LOCATION_HAND, 0, min, max, true,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
            Duel.ShuffleHand(tp)
        end)
end
```
