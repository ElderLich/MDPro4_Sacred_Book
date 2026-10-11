# RushDuel.CostSendHandToDeckTop

Alias: `RD.CostSendHandToDeckTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToDeckTop(any filter, any min, any max, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡返回卡组上面
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

`Rush/Utilities/RDCost.lua:425`

```lua
function RushDuel.CostSendHandToDeckTop(filter, min, max, confirm, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_HAND, min, max, true, SEQ_DECKTOP, false, confirm,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandToDeckTop) with `RushDuel.CostSendHandToDeckTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cyber Search Dragon | `120109022` | [Rush/Scripts/c120109022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109022.lua) | 1 |

## Script Examples

### Cyber Search Dragon (`120109022`)

Source: [Rush/Scripts/c120109022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109022.lua)

```lua
	return c:IsCode(list[1]) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendHandToDeckTop(Card.IsAbleToDeckAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
```
