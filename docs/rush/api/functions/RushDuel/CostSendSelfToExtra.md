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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendSelfToExtra) with `RushDuel.CostSendSelfToExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rising HERO Argent O | `120304042` | [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua) | 1 |

## Script Examples

### Rising HERO Argent O (`120304042`)

Source: [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua)

```lua
	return Duel.GetCustomActivityCount(m,tp,ACTIVITY_SPSUMMON)==0
end
cm.cost=RD.CostSendSelfToExtra()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_ONFIELD,1,nil) end
```
