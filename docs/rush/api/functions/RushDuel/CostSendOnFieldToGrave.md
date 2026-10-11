# RushDuel.CostSendOnFieldToGrave

Alias: `RD.CostSendOnFieldToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendOnFieldToGrave(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把场上的卡送去墓地
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

`Rush/Utilities/RDCost.lua:325`

```lua
function RushDuel.CostSendOnFieldToGrave(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToGrave(filter, LOCATION_ONFIELD, min, max, except_self, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendOnFieldToGrave) with `RushDuel.CostSendOnFieldToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Advance Form | `120261032` | [Rush/Scripts/c120261032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261032.lua) | 1 |
| Sitarloot | `120283047` | [Rush/Scripts/c120283047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283047.lua) | 1 |
| Spell Extraction | `120246085` | [Rush/Scripts/c120246085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246085.lua) | 1 |
| Guardian Eatos | `120290065` | [Rush/Scripts/c120290065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290065.lua) | 1 |
| Abysskite Ultimail | `120239048` | [Rush/Scripts/c120239048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239048.lua) | 1 |
| Cyber Processor | `120244021` | [Rush/Scripts/c120244021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244021.lua) | 1 |
| Ancient Gear Supplier | `120271010` | [Rush/Scripts/c120271010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271010.lua) | 1 |
| Barrel-Up-Magic Liner's Force | `120305039` | [Rush/Scripts/c120305039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305039.lua) | 1 |
| Coredrasil the Spirit Tree Bunrei | `120306018` | [Rush/Scripts/c120306018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306018.lua) | 1 |
| Ancient Gear Medic | `120271009` | [Rush/Scripts/c120271009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271009.lua) | 1 |
| Sacred War of Arthenée | `120306058` | [Rush/Scripts/c120306058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306058.lua) | 1 |
| Benevolent Dragon | `120294011` | [Rush/Scripts/c120294011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294011.lua) | 1 |
| Lostream Gift | `120309042` | [Rush/Scripts/c120309042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309042.lua) | 1 |
| Star Cat Straynya | `120235036` | [Rush/Scripts/c120235036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235036.lua) | 1 |
| Celeb Rose Magician | `120244012` | [Rush/Scripts/c120244012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244012.lua) | 1 |
| Levia-Dragon - Daedalus | `120199000` | [Rush/Scripts/c120199000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199000.lua) | 1 |
| Bendorbreak the Conqueror | `120145018` | [Rush/Scripts/c120145018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145018.lua) | 1 |
| Stratohammer Mjolnir | `120287071` | [Rush/Scripts/c120287071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287071.lua) | 1 |
| Dynamic Dino Dynatyranno | `120274038` | [Rush/Scripts/c120274038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274038.lua) | 1 |
| Gray Storm Reverie | `120229001` | [Rush/Scripts/c120229001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120229001.lua) | 1 |
| Space Yggdrago | `120260009` | [Rush/Scripts/c120260009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260009.lua) | 1 |
| Don A. Corn of the Verdant Vast | `120244023` | [Rush/Scripts/c120244023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244023.lua) | 1 |
| Rampaging Machine Headhorn | `120304013` | [Rush/Scripts/c120304013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304013.lua) | 1 |

## Script Examples

### Advance Form (`120261032`)

Source: [Rush/Scripts/c120261032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261032.lua)

```lua
	return math.min(ct,2)
end
cm.cost=RD.CostSendOnFieldToGrave(Card.IsAbleToGraveAsCost,1,cm.max,false,nil,nil,Group.GetCount)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_GRAVE,1,nil) end
```

### Sitarloot (`120283047`)

Source: [Rush/Scripts/c120283047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283047.lua)

```lua
	return RD.IsSummonTurn(c) and Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,nil)
end
cm.cost=RD.CostSendOnFieldToGrave(Card.IsAbleToGraveAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_ONFIELD,1,nil) end
```

### Spell Extraction (`120246085`)

Source: [Rush/Scripts/c120246085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246085.lua)

```lua
	return c:IsAttribute(ATTRIBUTE_DARK) and c:IsRace(RACE_SPELLCASTER) and c:IsAttack(2000,2500) and not c:IsPublic()
end
cm.cost=RD.CostSendOnFieldToGrave(cm.costfilter,1,1,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
```
