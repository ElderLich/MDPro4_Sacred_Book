# RushDuel.CostChangeSelfPosition

Alias: `RD.CostChangeSelfPosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChangeSelfPosition(any pos1, any pos2) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 改变自身的表示形式
```

## Parameters

- `pos1` `any`: Type and behavior are not yet reviewed; see the source.
- `pos2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:515`

```lua
function RushDuel.CostChangeSelfPosition(pos1, pos2)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        local c = e:GetHandler()
        if chk == 0 then
            return (not pos1 or c:IsPosition(pos1)) and RushDuel.IsCanChangePosition(c, e, tp, REASON_COST)
        end
        if pos2 then
            RushDuel.ChangePosition(c, e, tp, REASON_COST, pos2)
        else
            RushDuel.ChangePosition(c, e, tp, REASON_COST)
        end
        return true
    end
end
```
