# RushDuel.CostSendGroupToDeckSort

Alias: `RD.CostSendGroupToDeckSort`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGroupToDeckSort(any filter, any check, any field, any min, any max, any except_self, any sequence, any hint_selection, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 选择子卡片组, 返回卡组 (排序)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
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

`Rush/Utilities/RDCost.lua:167`

```lua
function RushDuel.CostSendGroupToDeckSort(filter, check, field, min, max, except_self, sequence, hint_selection,
    confirm, set_label_before, set_object_before, set_label_after, set_object_after)
    local action = RushDuel._private_action_send_deck_sort(sequence, REASON_COST, hint_selection, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel._private_cost_select_group(HINTMSG_TODECK, filter, check, field, 0, min, max, except_self, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGroupToDeckSort) with `RushDuel.CostSendGroupToDeckSort`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Invitation to a Delirious Dream](/examples/rush-cards/120261066) | `120261066` | [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| Celeb Revelation | `120254022` | [Rush/Scripts/c120254022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254022.lua) | 1 |
| Elite Agent Mystery | `120249022` | [Rush/Scripts/c120249022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249022.lua) | 1 |

## Script Examples

### Invitation to a Delirious Dream (`120261066`)

Source: [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendGroupToDeckSort(Card.IsAbleToDeckOrExtraAsCost,cm.costcheck,LOCATION_MZONE+LOCATION_HAND,2,2,true,SEQ_DECKBOTTOM,true,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return (e:IsCostChecked() or Duel.GetMZoneCount(tp,nil,tp,LOCATION_REASON_CONTROL)>0)
```

### Moonforce Timo (`120300015`)

Source: [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua)

```lua
	return RD.IsSummonTurn(e:GetHandler()) and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9
end
cm.cost=RD.CostSendGroupToDeckSort(cm.costfilter,cm.check,LOCATION_HAND+LOCATION_GRAVE,2,2,true,SEQ_DECKBOTTOM,true,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
```

### Celeb Revelation (`120254022`)

Source: [Rush/Scripts/c120254022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254022.lua)

```lua
		and Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,nil)
end
cm.cost=RD.CostSendGroupToDeckSort(cm.costfilter,cm.costcheck,LOCATION_ONFIELD+LOCATION_GRAVE,1,4,false,SEQ_DECKSHUFFLE,false,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil) end
```
