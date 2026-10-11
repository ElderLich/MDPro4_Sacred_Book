# RushDuel.CostSendGraveToDeck

Alias: `RD.CostSendGraveToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveToDeck(any filter, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:443`

```lua
function RushDuel.CostSendGraveToDeck(filter, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_GRAVE, min, max, false, SEQ_DECKSHUFFLE, false, true,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **188** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveToDeck) with `RushDuel.CostSendGraveToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dolphin Counterattack](/examples/rush-cards/120199058) | `120199058` | [Rush/Scripts/c120199058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199058.lua) | 1 |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Shannah the Clad Dragon Researcher](/examples/rush-cards/120304017) | `120304017` | [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Lullalabind](/examples/rush-cards/120246073) | `120246073` | [Rush/Scripts/c120246073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246073.lua) | 1 |
| [False Sun](/examples/rush-cards/120264033) | `120264033` | [Rush/Scripts/c120264033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264033.lua) | 1 |
| [Bluetech Burst Rex](/examples/rush-cards/120261044) | `120261044` | [Rush/Scripts/c120261044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261044.lua) | 1 |
| [Red-Reboot Enhanced Boost Dragon](/examples/rush-cards/120253037) | `120253037` | [Rush/Scripts/c120253037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253037.lua) | 1 |
| [Fist the Contractor of the Imprisoned Dragon](/examples/rush-cards/120306037) | `120306037` | [Rush/Scripts/c120306037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306037.lua) | 1 |
| [Madrhea Amelo](/examples/rush-cards/120300028) | `120300028` | [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua) | 1 |
| [Chemicalizer Wing](/examples/rush-cards/120272057) | `120272057` | [Rush/Scripts/c120272057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272057.lua) | 1 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Galactica Supreme Oblivion | `120245003` | [Rush/Scripts/c120245003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245003.lua) | 1 |
| Voidvelg Divine Requiem | `120109037` | [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua) | 1 |
| Ether Escape | `120235062` | [Rush/Scripts/c120235062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235062.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken \[L\] | `120239016` | [Rush/Scripts/c120239016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239016.lua) | 1 |
| Poet Fairy | `120208021` | [Rush/Scripts/c120208021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208021.lua) | 1 |
| Skysavior Defense | `120301054` | [Rush/Scripts/c120301054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301054.lua) | 1 |
| Jointech Joint | `120257058` | [Rush/Scripts/c120257058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257058.lua) | 1 |
| Ever-Grace Princess Hina | `120290038` | [Rush/Scripts/c120290038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290038.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix \[L\] | `120249015` | [Rush/Scripts/c120249015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249015.lua) | 1 |
| Siesta Torero | `120170035` | [Rush/Scripts/c120170035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170035.lua) | 1 |
| Vortex of Shattered Light | `120244065` | [Rush/Scripts/c120244065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244065.lua) | 1 |
| ...and 164 more |  |  |  |

## Script Examples

### Dolphin Counterattack (`120199058`)

Source: [Rush/Scripts/c120199058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199058.lua)

```lua
		and c and c:IsControler(tp) and c:IsFaceup() and c:IsRace(RACE_FISH+RACE_SEASERPENT)
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,0,LOCATION_MZONE,1,nil) end
```

### Spice Cross Secret Recipe (`120261060`)

Source: [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil,e,tp) end
```

### Hybridrive Back Fusion (`120261052`)

Source: [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua)

```lua
	return sg:GetClassCount(Card.GetRace)==sg:GetCount()
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,4,4)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(1-tp)>0
```
