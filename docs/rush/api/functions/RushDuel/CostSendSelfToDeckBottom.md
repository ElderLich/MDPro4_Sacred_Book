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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendSelfToDeckBottom) with `RushDuel.CostSendSelfToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Rescue Rabbit](/examples/rush-cards/120109057) | `120109057` | [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua) | 1 |

## Script Examples

### Rescue Rabbit (`120109057`)

Source: [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua)

```lua
	return g:GetClassCount(Card.GetRace)==1
end
cm.cost=RD.CostSendSelfToDeckBottom()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local mg=Duel.GetMatchingGroup(cm.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
```
