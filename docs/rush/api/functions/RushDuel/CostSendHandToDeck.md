# RushDuel.CostSendHandToDeck

Alias: `RD.CostSendHandToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToDeck(any filter, any min, any max, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡返回卡组
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

`Rush/Utilities/RDCost.lua:419`

```lua
function RushDuel.CostSendHandToDeck(filter, min, max, confirm, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_HAND, min, max, true, SEQ_DECKSHUFFLE, false, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandToDeck) with `RushDuel.CostSendHandToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Jointech Nesstrydar Tank | `120257017` | [Rush/Scripts/c120257017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257017.lua) | 1 |
| Supreme Dog Ropero | `120239022` | [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua) | 1 |
| Celeb Rose Enchanter | `120254050` | [Rush/Scripts/c120254050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254050.lua) | 1 |
| Clashing Twin Tides | `120264051` | [Rush/Scripts/c120264051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264051.lua) | 1 |

## Script Examples

### Jointech Nesstrydar Tank (`120257017`)

Source: [Rush/Scripts/c120257017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257017.lua)

```lua
	return c:IsLevel(7,8) and c:IsAttribute(ATTRIBUTE_DARK) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendHandToDeck(Card.IsAbleToDeckAsCost,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
```

### Supreme Dog Ropero (`120239022`)

Source: [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua)

```lua
end
cm.cost1=RD.CostPayLP(500)
cm.cost2=RD.CostSendHandToDeck(Card.IsAbleToDeckAsCost,2,2,false)
cm.cost=RD.CostMerge(cm.cost1,cm.cost2)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Celeb Rose Enchanter (`120254050`)

Source: [Rush/Scripts/c120254050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254050.lua)

```lua
	return c:IsCode(list[1]) and c:IsAbleToHand()
end
cm.cost=RD.CostSendHandToDeck(Card.IsAbleToDeckAsCost,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
```
