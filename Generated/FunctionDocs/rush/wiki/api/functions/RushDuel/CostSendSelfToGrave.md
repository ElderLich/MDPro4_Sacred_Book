# RushDuel.CostSendSelfToGrave

Alias: `RD.CostSendSelfToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToGrave() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把自己场上表侧表示的这张卡送去墓地
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:289`

```lua
function RushDuel.CostSendSelfToGrave()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToGraveAsCost()
        end
        Duel.SendtoGrave(RushDuel.ToMaximunGroup(e:GetHandler()), REASON_COST)
        return true
    end
end
```
