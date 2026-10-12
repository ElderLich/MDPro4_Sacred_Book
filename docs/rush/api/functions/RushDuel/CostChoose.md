# RushDuel.CostChoose

Alias: `RD.CostChoose`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChoose(any hit1, any cost1, any hit2, any cost2, any set_label) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 从2个代价中选择1个(分开选)
```

## Parameters

- `hit1` `any`: Type and behavior are not yet reviewed; see the source.
- `cost1` `any`: Type and behavior are not yet reviewed; see the source.
- `hit2` `any`: Type and behavior are not yet reviewed; see the source.
- `cost2` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:541`

```lua
function RushDuel.CostChoose(hit1, cost1, hit2, cost2, set_label)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        local s1 = cost1(e, tp, eg, ep, ev, re, r, rp, 0)
        local s2 = cost2(e, tp, eg, ep, ev, re, r, rp, 0)
        if chk == 0 then
            return s1 or s2
        end
        local res = 0
        if s1 and s2 then
            RushDuel.CostCancelable = true
            ::cancel::
            res = RushDuel.SelectOption(tp, {s1, hit1}, {s2, hit2})
            if res == 1 then
                if not cost1(e, tp, eg, ep, ev, re, r, rp, 1) then
                    goto cancel
                end
            elseif res == 2 then
                if not cost2(e, tp, eg, ep, ev, re, r, rp, 1) then
                    goto cancel
                end
            end
            RushDuel.CostCancelable = false
        elseif s1 then
            cost1(e, tp, eg, ep, ev, re, r, rp, 1)
            res = 1
        elseif s2 then
            cost2(e, tp, eg, ep, ev, re, r, rp, 1)
            res = 2
        end
        if res ~= 0 and set_label then
            e:SetLabel(res)
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostChoose) with `RushDuel.CostChoose`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Super Soldier Radiance | `120293042` | [Rush/Scripts/c120293042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293042.lua) | 1 |
| Quick Attack Knight | `120293037` | [Rush/Scripts/c120293037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293037.lua) | 1 |
| Familiar of the Earth Spiritualist | `120301013` | [Rush/Scripts/c120301013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301013.lua) | 1 |
| Familiar of the Water Spiritualist | `120301014` | [Rush/Scripts/c120301014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301014.lua) | 1 |
| Familiar of the Fire Spiritualist | `120301015` | [Rush/Scripts/c120301015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301015.lua) | 1 |
| Familiar of the Wind Spiritualist | `120301016` | [Rush/Scripts/c120301016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301016.lua) | 1 |
| King's Greed | `120254083` | [Rush/Scripts/c120254083.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254083.lua) | 1 |
| Ace Sword Slash | `120294052` | [Rush/Scripts/c120294052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294052.lua) | 1 |
| Strange Attractor | `120260017` | [Rush/Scripts/c120260017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260017.lua) | 1 |
| Voidalfr Voyastrider | `120300002` | [Rush/Scripts/c120300002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300002.lua) | 1 |
| Stratohammer Mjolnir | `120287071` | [Rush/Scripts/c120287071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287071.lua) | 1 |
| Voidvelg Stork | `120300001` | [Rush/Scripts/c120300001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300001.lua) | 1 |

## Script Examples

### Super Soldier Radiance (`120293042`)

Source: [Rush/Scripts/c120293042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293042.lua)

```lua
cm.cost1=RD.CostSendHandToDeckBottom(cm.costfilter1,1,1,false)
cm.cost2=RD.CostChangePosition(cm.costfilter2,1,1)
cm.cost=RD.CostChoose(HINTMSG_TODECK,cm.cost1,HINTMSG_POSCHANGE,cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil,e,tp) end
```

### Quick Attack Knight (`120293037`)

Source: [Rush/Scripts/c120293037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293037.lua)

```lua
cm.cost1=RD.CostSendHandToGrave(cm.costfilter1,1,1)
cm.cost2=RD.CostShowHand(cm.costfilter2,1,1)
cm.cost=RD.CostChoose(aux.Stringid(m,1),cm.cost1,aux.Stringid(m,2),cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,1) end
```

### Familiar of the Earth Spiritualist (`120301013`)

Source: [Rush/Scripts/c120301013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301013.lua)

```lua
cm.cost1=RD.CostSendSelfToGrave()
cm.cost2=RD.CostSendDeckTopToGrave(1)
cm.cost=RD.CostChoose(aux.Stringid(m,1),cm.cost1,aux.Stringid(m,2),cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil) end
```
