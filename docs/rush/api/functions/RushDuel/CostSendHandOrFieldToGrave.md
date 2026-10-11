# RushDuel.CostSendHandOrFieldToGrave

Alias: `RD.CostSendHandOrFieldToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandOrFieldToGrave(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡·场上的卡送去墓地
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:337`

```lua
function RushDuel.CostSendHandOrFieldToGrave(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToGrave(filter, LOCATION_HAND + LOCATION_ONFIELD, min, max, except_self, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandOrFieldToGrave) with `RushDuel.CostSendHandOrFieldToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Tama Tama Gachance | `120109053` | [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua) | 1 |
| Swarming Basic Insect | `120298040` | [Rush/Scripts/c120298040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298040.lua) | 1 |
| The Secret of Manifestation | `120257051` | [Rush/Scripts/c120257051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257051.lua) | 1 |
| Vic Viper Spread Bomb | `120294025` | [Rush/Scripts/c120294025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294025.lua) | 1 |
| Jointech Arcscorpio | `120249006` | [Rush/Scripts/c120249006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249006.lua) | 1 |
| Loot from the Clad Dragondom | `120304051` | [Rush/Scripts/c120304051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304051.lua) | 1 |
| Aussa the Earth Spiritualist | `120301009` | [Rush/Scripts/c120301009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301009.lua) | 1 |
| Bandiva Duo the Elegy of the Wailing Winds | `120283027` | [Rush/Scripts/c120283027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283027.lua) | 1 |
| Freshberry Pleasure | `120264023` | [Rush/Scripts/c120264023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264023.lua) | 1 |
| Lovely Fereshte | `120300019` | [Rush/Scripts/c120300019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300019.lua) | 1 |
| Wynn the Wind Spiritualist | `120301012` | [Rush/Scripts/c120301012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301012.lua) | 1 |
| Freshberry Rich | `120264027` | [Rush/Scripts/c120264027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264027.lua) | 1 |
| Piping Hot Delivery | `120290045` | [Rush/Scripts/c120290045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290045.lua) | 1 |
| Freshberry Happiness Harvest | `120264022` | [Rush/Scripts/c120264022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264022.lua) | 1 |
| Glacies the Snowmeister of Sacred Splendor | `120253034` | [Rush/Scripts/c120253034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253034.lua) | 1 |
| Sparkhearts Passion Girl | `120298018` | [Rush/Scripts/c120298018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298018.lua) | 1 |
| Hiita the Fire Spiritualist | `120301011` | [Rush/Scripts/c120301011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301011.lua) | 1 |
| Freshberry Smart | `120264024` | [Rush/Scripts/c120264024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264024.lua) | 1 |
| Freshberry Cure | `120264025` | [Rush/Scripts/c120264025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264025.lua) | 1 |
| Freshberry Chesty | `120272028` | [Rush/Scripts/c120272028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272028.lua) | 1 |
| Sparkhearts Passion Anesh | `120298019` | [Rush/Scripts/c120298019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298019.lua) | 1 |

## Script Examples

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
	return c:IsFaceup() and not c:IsType(TYPE_MAXIMUM) and c:IsLevelBelow(10)
end
cm.cost=RD.CostSendHandOrFieldToGrave(Card.IsAbleToGraveAsCost,1,1,true,nil,nil,function(g)
	local c=g:GetFirst()
	if c:IsAttribute(ATTRIBUTE_WATER) and c:IsRace(RACE_AQUA) then
```

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
	return RD.IsSummonOrSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendHandOrFieldToGrave(cm.costfilter,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_GRAVE,1,nil) end
```

### Tama Tama Gachance (`120109053`)

Source: [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua)

```lua
	return ct==1 or g:FilterCount(Card.IsCode,nil,list[1])==ct
end
cm.cost=RD.CostSendHandOrFieldToGrave(cm.costfilter,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,3) end
```
