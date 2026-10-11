# RushDuel.CostSendSelfToDeck

Alias: `RD.CostSendSelfToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToDeck() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让自己场上表侧表示的这张卡回到卡组
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:349`

```lua
function RushDuel.CostSendSelfToDeck()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToDeckAsCost()
        end
        RushDuel.SendToDeckSort(e:GetHandler(), SEQ_DECKSHUFFLE, REASON_COST, tp)
        return true
    end
end
```
