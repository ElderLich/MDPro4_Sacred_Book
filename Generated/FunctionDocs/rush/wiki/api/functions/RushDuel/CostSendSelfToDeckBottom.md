# RushDuel.CostSendSelfToDeckBottom

Alias: `RD.CostSendSelfToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToDeckBottom() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让自己场上表侧表示的这张卡回到卡组下面
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:369`

```lua
function RushDuel.CostSendSelfToDeckBottom()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToDeckAsCost()
        end
        RushDuel.SendToDeckSort(e:GetHandler(), SEQ_DECKBOTTOM, REASON_COST, tp)
        return true
    end
end
```
