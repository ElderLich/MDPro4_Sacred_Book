# RushDuel.CostChangeSelfPosition

Alias: `RD.CostChangeSelfPosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChangeSelfPosition(any pos1, any pos2) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 改变自身的表示形式
```

## Parameters

- `pos1` `any`: Type and behavior are not yet reviewed; see the source.
- `pos2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:515`

```lua
function RushDuel.CostChangeSelfPosition(pos1, pos2)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        local c = e:GetHandler()
        if chk == 0 then
            return (not pos1 or c:IsPosition(pos1)) and RushDuel.IsCanChangePosition(c, e, tp, REASON_COST)
        end
        if pos2 then
            RushDuel.ChangePosition(c, e, tp, REASON_COST, pos2)
        else
            RushDuel.ChangePosition(c, e, tp, REASON_COST)
        end
        return true
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **31** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostChangeSelfPosition) with `RushDuel.CostChangeSelfPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Matter Freya | `120261027` | [Rush/Scripts/c120261027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261027.lua) | 1 |
| Delirium Shewel | `120274058` | [Rush/Scripts/c120274058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274058.lua) | 1 |
| The Nomnom Liliputian | `120309054` | [Rush/Scripts/c120309054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309054.lua) | 1 |
| Summoner Monk | `120307009` | [Rush/Scripts/c120307009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307009.lua) | 1 |
| Delirium Drone | `120274059` | [Rush/Scripts/c120274059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274059.lua) | 1 |
| Draco the Hand-Picked | `120294005` | [Rush/Scripts/c120294005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294005.lua) | 1 |
| Flower Fan Clematis | `120254072` | [Rush/Scripts/c120254072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254072.lua) | 1 |
| Delirium Polynea | `120277033` | [Rush/Scripts/c120277033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277033.lua) | 1 |
| Delirium Mariquita | `120274057` | [Rush/Scripts/c120274057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274057.lua) | 1 |
| Weaksauce Brassdes | `120304066` | [Rush/Scripts/c120304066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304066.lua) | 1 |
| Draco the Palm Greaser | `120301067` | [Rush/Scripts/c120301067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301067.lua) | 1 |
| Twin Edge Phantom Dragon | `120261030` | [Rush/Scripts/c120261030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261030.lua) | 1 |
| Metarion Armarostar | `120272046` | [Rush/Scripts/c120272046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272046.lua) | 1 |
| Voidvelg Hecatoncheir | `120227007` | [Rush/Scripts/c120227007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227007.lua) | 1 |
| Yamiruler the Dark Delayer | `120120029` | [Rush/Scripts/c120120029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120029.lua) | 1 |
| Gamabot | `120285009` | [Rush/Scripts/c120285009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285009.lua) | 1 |
| Grace Cat | `120287022` | [Rush/Scripts/c120287022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287022.lua) | 1 |
| Baron Wight | `120271057` | [Rush/Scripts/c120271057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271057.lua) | 1 |
| Princess Ladybug White | `120208023` | [Rush/Scripts/c120208023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208023.lua) | 1 |
| Plus Skull | `120261040` | [Rush/Scripts/c120261040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261040.lua) | 1 |
| Yurushima Sage | `120140003` | [Rush/Scripts/c120140003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140003.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Long Shield Gardna | `120145037` | [Rush/Scripts/c120145037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145037.lua) | 1 |
| Royal Rebel's Grunge | `120254074` | [Rush/Scripts/c120254074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254074.lua) | 1 |
| ...and 7 more |  |  |  |

## Script Examples

### Dark Matter Freya (`120261027`)

Source: [Rush/Scripts/c120261027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261027.lua)

```lua
	return Duel.IsAbleToEnterBP()
end
cm.cost=RD.CostChangeSelfPosition()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_MZONE,0,1,nil) end
```

### Delirium Shewel (`120274058`)

Source: [Rush/Scripts/c120274058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274058.lua)

```lua
	return Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,e:GetHandler())
end
cm.cost=RD.CostChangeSelfPosition(POS_FACEUP_ATTACK,POS_FACEUP_DEFENSE)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(RD.IsCanChangePosition,tp,0,LOCATION_MZONE,1,nil) end
```

### The Nomnom Liliputian (`120309054`)

Source: [Rush/Scripts/c120309054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309054.lua)

```lua
	return c:IsCode(list[2]) and c:IsAbleToDeck()
end
cm.cost=RD.CostChangeSelfPosition(POS_FACEUP_ATTACK,POS_FACEUP_DEFENSE)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,2) end
```
