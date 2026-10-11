# RushDuel.CostPayLP

Alias: `RD.CostPayLP`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostPayLP(int lp) -> function
```

## Description

Returns a cost callback that checks Duel.CheckLPCost during chk==0, then pays the specified LP when the cost is performed.

## Parameters

- `lp` `int`: LP to pay.

## Returns

- `function`: Cost callback for Effect.SetCost.

## Example

```lua
e1:SetCost(RD.CostPayLP(1000))
```

## Source

`Rush/Utilities/RDCost.lua:196`

```lua
function RushDuel.CostPayLP(lp)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.CheckLPCost(tp, lp)
        end
        Duel.PayLPCost(tp, lp)
        return true
    end
end
```
