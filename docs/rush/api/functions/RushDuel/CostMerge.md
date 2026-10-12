# RushDuel.CostMerge

Alias: `RD.CostMerge`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostMerge(function cost1, function cost2) -> function
```

## Description

Returns a cost callback that checks both costs with short-circuit 'and' when chk==0. During payment it calls both costs in order, ignoring their return values. Each cost must remain payable after the first payment; independently successful checks alone do not prove shared resources are sufficient.

## Parameters

- `cost1` `function`: First cost callback.
- `cost2` `function`: Second cost callback.

## Returns

- `function`: Combined cost callback.

## Source

`Rush/Utilities/RDCost.lua:531`

```lua
function RushDuel.CostMerge(cost1, cost2)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return cost1(e, tp, eg, ep, ev, re, r, rp, chk) and cost2(e, tp, eg, ep, ev, re, r, rp, chk)
        end
        cost1(e, tp, eg, ep, ev, re, r, rp, chk)
        cost2(e, tp, eg, ep, ev, re, r, rp, chk)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostMerge) with `RushDuel.CostMerge`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Surtr the Brilliant Magical Sword | `120306100` | [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua) | 1 |
| Supreme Dog Ropero | `120239022` | [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua) | 1 |
| Ancient Gear Supplier | `120271010` | [Rush/Scripts/c120271010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271010.lua) | 1 |
| Striping Wyvern | `120253005` | [Rush/Scripts/c120253005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253005.lua) | 1 |
| Trombow the Music Princess of Melodic Crown | `120260071` | [Rush/Scripts/c120260071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260071.lua) | 1 |
| Summoner Monk | `120307009` | [Rush/Scripts/c120307009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307009.lua) | 1 |
| Chaoswordrider | `120293033` | [Rush/Scripts/c120293033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293033.lua) | 1 |
| Chaos Material | `120293034` | [Rush/Scripts/c120293034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293034.lua) | 1 |
| Destructor Soldier Helmet | `120247043` | [Rush/Scripts/c120247043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247043.lua) | 1 |
| Worker Warrior - Multitasking Manager | `120304028` | [Rush/Scripts/c120304028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304028.lua) | 1 |

## Script Examples

### Surtr the Brilliant Magical Sword (`120306100`)

Source: [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua)

```lua
cm.cost1=RD.CostPayLP(500)
cm.cost2=RD.CostSendSelfToGrave()
cm.cost=RD.CostMerge(cm.cost1,cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_MZONE,0,1,e:GetHandler()) end
```

### Supreme Dog Ropero (`120239022`)

Source: [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua)

```lua
cm.cost1=RD.CostPayLP(500)
cm.cost2=RD.CostSendHandToDeck(Card.IsAbleToDeckAsCost,2,2,false)
cm.cost=RD.CostMerge(cm.cost1,cm.cost2)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```

### Ancient Gear Supplier (`120271010`)

Source: [Rush/Scripts/c120271010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271010.lua)

```lua
end)
cm.cost2=RD.CostSendGraveToDeck(cm.costfilter2,2,2)
cm.cost=RD.CostMerge(cm.cost1,cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_ONFIELD,1,nil) end
```
