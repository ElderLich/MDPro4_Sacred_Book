# RushDuel.CostSendGraveSubToDeckTop

Alias: `RD.CostSendGraveSubToDeckTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveSubToDeckTop(any filter, any check, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组上面 (子卡片组)
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

`Rush/Utilities/RDCost.lua:461`

```lua
function RushDuel.CostSendGraveSubToDeckTop(filter, check, min, max, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendGroupToDeckSort(filter, check, LOCATION_GRAVE, min, max, false, SEQ_DECKTOP, false, true,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveSubToDeckTop) with `RushDuel.CostSendGraveSubToDeckTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Wish of the Skysavior](/examples/rush-cards/120253064) | `120253064` | [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua) | 1 |

## Script Examples

### Wish of the Skysavior (`120253064`)

Source: [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendGraveSubToDeckTop(cm.costfilter,cm.costcheck,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsAbleToDeck,tp,0,LOCATION_MZONE,1,nil) end
```
