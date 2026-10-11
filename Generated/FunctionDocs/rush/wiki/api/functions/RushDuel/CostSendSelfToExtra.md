# RushDuel.CostSendSelfToExtra

Alias: `RD.CostSendSelfToExtra`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToExtra() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让自己场上表侧表示的这张卡回到额外卡组
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:379`

```lua
function RushDuel.CostSendSelfToExtra()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToExtraAsCost()
        end
        Duel.SendtoDeck(RushDuel.ToMaximunGroup(e:GetHandler()), nil, SEQ_DECKSHUFFLE, REASON_COST)
        return true
    end
end
```
