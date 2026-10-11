# RushDuel.CostSendGraveSubToDeckBottom

Alias: `RD.CostSendGraveSubToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveSubToDeckBottom(any filter, any check, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组下面 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:473`

```lua
function RushDuel.CostSendGraveSubToDeckBottom(filter, check, min, max, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendGroupToDeckSort(filter, check, LOCATION_GRAVE, min, max, false, SEQ_DECKBOTTOM, false, true,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveSubToDeckBottom) with `RushDuel.CostSendGraveSubToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Vortex Chaos Shooter | `120277006` | [Rush/Scripts/c120277006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277006.lua) | 1 |
| Yoctron | `120150017` | [Rush/Scripts/c120150017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150017.lua) | 1 |
| Hybridrive Screwdriver | `120261006` | [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua) | 1 |
| Icezark the Unequaled | `120170022` | [Rush/Scripts/c120170022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170022.lua) | 1 |
| Cybernetic Overflow | `120278037` | [Rush/Scripts/c120278037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278037.lua) | 1 |
| Over Rush Volcano | `120301076` | [Rush/Scripts/c120301076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301076.lua) | 1 |
| Scarechair Scale | `120151026` | [Rush/Scripts/c120151026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151026.lua) | 1 |
| Galactic Chaos Enforcer | `120277005` | [Rush/Scripts/c120277005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277005.lua) | 1 |
| JAM:P Start! | `120170040` | [Rush/Scripts/c120170040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170040.lua) | 1 |
| Hybridrive Restruct | `120261053` | [Rush/Scripts/c120261053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261053.lua) | 1 |

## Script Examples

### Vortex Chaos Shooter (`120277006`)

Source: [Rush/Scripts/c120277006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277006.lua)

```lua
		or (tc2:IsRace(RACE_GALAXY) and tc1:IsCode(list[1]))
end
cm.cost=RD.CostSendGraveSubToDeckBottom(cm.costfilter,cm.costcheck,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
```

### Yoctron (`120150017`)

Source: [Rush/Scripts/c120150017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150017.lua)

```lua
	return c:IsCode(list[1],list[2],list[3]) and c:IsAbleToDeckOrExtraAsCost()
end
cm.cost=RD.CostSendGraveSubToDeckBottom(cm.costfilter,aux.dncheck,3,3)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToGrave() and Duel.IsPlayerCanDraw(tp,3) end
```

### Hybridrive Screwdriver (`120261006`)

Source: [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua)

```lua
	return g:FilterCount(Card.IsRace,nil,RACE_DRAGON)==2 and g:FilterCount(Card.IsRace,nil,RACE_MACHINE)==2
end
cm.cost=RD.CostSendGraveSubToDeckBottom(cm.costfilter,cm.costcheck,4,4)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
```
