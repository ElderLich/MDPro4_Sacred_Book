# RushDuel.CostSendHandToDeckBottom

Alias: `RD.CostSendHandToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToDeckBottom(any filter, any min, any max, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡返回卡组下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:431`

```lua
function RushDuel.CostSendHandToDeckBottom(filter, min, max, confirm, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_HAND, min, max, true, SEQ_DECKBOTTOM, false, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandToDeckBottom) with `RushDuel.CostSendHandToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| [Grace Princess Hina](/examples/rush-cards/120287020) | `120287020` | [Rush/Scripts/c120287020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287020.lua) | 1 |
| Shadow Flower Clone | `120228049` | [Rush/Scripts/c120228049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228049.lua) | 1 |
| Super Soldier Radiance | `120293042` | [Rush/Scripts/c120293042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293042.lua) | 1 |
| Salvage Wolfish | `120228036` | [Rush/Scripts/c120228036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228036.lua) | 1 |
| Prime Claw Girl | `120257004` | [Rush/Scripts/c120257004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257004.lua) | 1 |
| The Mysterious Flying Plants Are Real!! | `120306048` | [Rush/Scripts/c120306048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306048.lua) | 1 |
| Brick Phone Nyan Nyan | `120217053` | [Rush/Scripts/c120217053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217053.lua) | 1 |
| Cat Claw Girl | `120235016` | [Rush/Scripts/c120235016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235016.lua) | 1 |
| Royal Rebel's Echo | `120205046` | [Rush/Scripts/c120205046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205046.lua) | 1 |
| Star Restart | `120196045` | [Rush/Scripts/c120196045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196045.lua) | 1 |
| Gulflare, the Skysavior | `120253049` | [Rush/Scripts/c120253049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253049.lua) | 1 |
| Sneezing Greedizauls | `120151008` | [Rush/Scripts/c120151008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151008.lua) | 1 |
| Dragonic Progression | `120253050` | [Rush/Scripts/c120253050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253050.lua) | 1 |
| Galactica Amnesia | `120216004` | [Rush/Scripts/c120216004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120216004.lua) | 1 |
| Miginagi the Talismanic Warrior | `120222037` | [Rush/Scripts/c120222037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222037.lua) | 1 |
| Fullmetarion Ashurastar | `120271016` | [Rush/Scripts/c120271016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271016.lua) | 1 |
| Magnet Speeder | `120285024` | [Rush/Scripts/c120285024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285024.lua) | 1 |
| Nyanderful Rush | `120235049` | [Rush/Scripts/c120235049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235049.lua) | 1 |
| Shitotsu the Talismanic Warrior | `120208029` | [Rush/Scripts/c120208029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208029.lua) | 1 |
| Abysslayer Vodyanoy | `120239031` | [Rush/Scripts/c120239031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239031.lua) | 1 |
| Scarechair Code | `120260072` | [Rush/Scripts/c120260072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260072.lua) | 1 |
| Alpiris the Sower | `120228019` | [Rush/Scripts/c120228019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228019.lua) | 1 |
| ...and 11 more |  |  |  |

## Script Examples

### Rising Protect (`120304055`)

Source: [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua)

```lua
	return (cm.filter1(tc1) and cm.filter2(tc2)) or (cm.filter1(tc2) and cm.filter2(tc1))
end
cm.cost=RD.CostSendHandToDeckBottom(Card.IsAbleToDeckAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_GRAVE,0,1,nil) end
```

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
	return RD.IsBaseDefense(c,1200) and c:IsFusionAttribute(ATTRIBUTE_WIND)
end
cm.cost=RD.CostSendHandToDeckBottom(Card.IsAbleToDeckAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
```

### Grace Princess Hina (`120287020`)

Source: [Rush/Scripts/c120287020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287020.lua)

```lua
	return c:IsType(TYPE_RITUAL) and c:IsType(TYPE_SPELL) and c:IsSSetable()
end
cm.cost=RD.CostSendHandToDeckBottom(Card.IsAbleToDeckAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
```
