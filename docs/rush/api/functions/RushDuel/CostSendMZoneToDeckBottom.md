# RushDuel.CostSendMZoneToDeckBottom

Alias: `RD.CostSendMZoneToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMZoneToDeckBottom(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让怪兽返回卡组下面
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

`Rush/Utilities/RDCost.lua:395`

```lua
function RushDuel.CostSendMZoneToDeckBottom(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_MZONE, min, max, except_self, SEQ_DECKBOTTOM, true, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendMZoneToDeckBottom) with `RushDuel.CostSendMZoneToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Kaien the Molten Martial Machine | `120294032` | [Rush/Scripts/c120294032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294032.lua) | 1 |
| Power Meter | `120294054` | [Rush/Scripts/c120294054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294054.lua) | 1 |
| Cyber Variation | `120278028` | [Rush/Scripts/c120278028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278028.lua) | 1 |
| Class-Change Mirror | `120238034` | [Rush/Scripts/c120238034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238034.lua) | 1 |

## Script Examples

### Kaien the Molten Martial Machine (`120294032`)

Source: [Rush/Scripts/c120294032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294032.lua)

```lua
		and c:IsType(TYPE_EFFECT) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendMZoneToDeckBottom(cm.costfilter,1,1)
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9
```

### Power Meter (`120294054`)

Source: [Rush/Scripts/c120294054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294054.lua)

```lua
	return c:IsLevel(4) and c:IsRace(RACE_MACHINE) and RD.IsDefense(c,800)
end
cm.cost=RD.CostSendMZoneToDeckBottom(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
```

### Cyber Variation (`120278028`)

Source: [Rush/Scripts/c120278028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278028.lua)

```lua
	return Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9
end
cm.cost=RD.CostSendMZoneToDeckBottom(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
```
