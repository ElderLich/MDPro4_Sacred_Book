# RushDuel.CostOnlyCondition

Alias: `RD.CostOnlyCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostOnlyCondition(any condition) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 只有条件
```

## Parameters

- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:140`

```lua
function RushDuel.CostOnlyCondition(condition)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        return condition(e, tp, eg, ep, ev, re, r, rp, chk)
    end
end
```
