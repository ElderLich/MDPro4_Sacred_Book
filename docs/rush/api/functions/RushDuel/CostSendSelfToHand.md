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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendSelfToHand) with `RushDuel.CostSendSelfToHand`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Star Replacer | `120244022` | [Rush/Scripts/c120244022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244022.lua) | 1 |

## Script Examples

### Star Replacer (`120244022`)

Source: [Rush/Scripts/c120244022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244022.lua)

```lua
	return Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)<=1
end
cm.cost=RD.CostSendSelfToHand()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
```
