# RushDuel.CostMerge

Alias: `RD.CostMerge`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostMerge(function cost1, function cost2) -> function
```

## Description

Returns a cost callback that checks both costs with short-circuit 'and' when chk==0. During payment it calls both costs in order, ignoring their return values. Each cost must remain payable after the first payment; independently successful checks alone do not prove shared resources are sufficient.

## Parameters

- `cost1` `function`: First cost callback.
- `cost2` `function`: Second cost callback.

## Returns

- `function`: Combined cost callback.

## Source

`Rush/Utilities/RDCost.lua:531`

```lua
function RushDuel.CostMerge(cost1, cost2)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return cost1(e, tp, eg, ep, ev, re, r, rp, chk) and cost2(e, tp, eg, ep, ev, re, r, rp, chk)
        end
        cost1(e, tp, eg, ep, ev, re, r, rp, chk)
        cost2(e, tp, eg, ep, ev, re, r, rp, chk)
    end
end
```
