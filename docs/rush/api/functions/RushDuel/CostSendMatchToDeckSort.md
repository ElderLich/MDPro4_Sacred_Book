# RushDuel.CostSendMatchToDeckSort

Alias: `RD.CostSendMatchToDeckSort`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMatchToDeckSort(any filter, any field, any min, any max, any except_self, any sequence, any hint_selection, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 选择匹配卡片, 返回卡组 (排序)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `field` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `sequence` `any`: Type and behavior are not yet reviewed; see the source.
- `hint_selection` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:160`

```lua
function RushDuel.CostSendMatchToDeckSort(filter, field, min, max, except_self, sequence, hint_selection, confirm,
    set_label_before, set_object_before, set_label_after, set_object_after)
    local action = RushDuel._private_action_send_deck_sort(sequence, REASON_COST, hint_selection, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel._private_cost_select_match(HINTMSG_TODECK, filter, field, 0, min, max, except_self, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendMatchToDeckSort) with `RushDuel.CostSendMatchToDeckSort`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Moonforce Piyopi | `120300011` | [Rush/Scripts/c120300011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300011.lua) | 1 |
| The Lauan Adventurers Are Go!! | `120306050` | [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua) | 1 |
| Luna Moonforce Mochi | `120300039` | [Rush/Scripts/c120300039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300039.lua) | 1 |
| Solciere, the Radiant Skysavior | `120235038` | [Rush/Scripts/c120235038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235038.lua) | 1 |
| Sanmarth the Skysavior Bright Brilliance | `120301043` | [Rush/Scripts/c120301043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301043.lua) | 1 |
| The Very Kind Human | `120309052` | [Rush/Scripts/c120309052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309052.lua) | 1 |

## Script Examples

### Moonforce Piyopi (`120300011`)

Source: [Rush/Scripts/c120300011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300011.lua)

```lua
	end
end
cm.cost=RD.CostSendMatchToDeckSort(cm.costfilter,LOCATION_HAND+LOCATION_ONFIELD,1,cm.max,true,SEQ_DECKBOTTOM,false,true,nil,nil,Group.GetCount)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
```

### The Lauan Adventurers Are Go!! (`120306050`)

Source: [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua)

```lua
		and RD.CheckUnionEquip(e,tc,c)
end
cm.cost=RD.CostSendMatchToDeckSort(cm.costfilter,LOCATION_ONFIELD,1,1,true,SEQ_DECKBOTTOM,true,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_MZONE,0,1,nil,e,tp) end
```

### Luna Moonforce Mochi (`120300039`)

Source: [Rush/Scripts/c120300039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300039.lua)

```lua
	return c:IsType(TYPE_SPELL+TYPE_TRAP)
end
cm.cost=RD.CostSendMatchToDeckSort(cm.costfilter,LOCATION_MZONE+LOCATION_GRAVE,3,3,true,SEQ_DECKBOTTOM,false,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_MZONE,1,nil) end
```
