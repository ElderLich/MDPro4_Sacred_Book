# RushDuel.CostSendSelfToDeckTop

Alias: `RD.CostSendSelfToDeckTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToDeckTop() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让自己场上表侧表示的这张卡回到卡组上面
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:359`

```lua
function RushDuel.CostSendSelfToDeckTop()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToDeckAsCost()
        end
        RushDuel.SendToDeckSort(e:GetHandler(), SEQ_DECKTOP, REASON_COST, tp)
        return true
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
