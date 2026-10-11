# RushDuel.CostSendSelfToHand

Alias: `RD.CostSendSelfToHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToHand() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让自己场上表侧表示的这张卡返回手卡
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:505`

```lua
function RushDuel.CostSendSelfToHand()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToHandAsCost()
        end
        Duel.SendtoHand(RushDuel.ToMaximunGroup(e:GetHandler()), nil, REASON_COST)
        return true
    end
end
```
