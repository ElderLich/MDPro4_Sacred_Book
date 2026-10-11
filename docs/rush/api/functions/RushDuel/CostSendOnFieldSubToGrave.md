# RushDuel.CostSendOnFieldSubToGrave

Alias: `RD.CostSendOnFieldSubToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendOnFieldSubToGrave(any filter, any check, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把场上的卡送去墓地 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
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

`Rush/Utilities/RDCost.lua:331`

```lua
function RushDuel.CostSendOnFieldSubToGrave(filter, check, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendGroupToGrave(filter, check, LOCATION_ONFIELD, min, max, except_self, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendOnFieldSubToGrave) with `RushDuel.CostSendOnFieldSubToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rising HERO Reglam | `120304024` | [Rush/Scripts/c120304024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304024.lua) | 1 |
| Ultimate Flag Beast Aim Eagle | `120193003` | [Rush/Scripts/c120193003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120193003.lua) | 1 |

## Script Examples

### Rising HERO Reglam (`120304024`)

Source: [Rush/Scripts/c120304024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304024.lua)

```lua
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendOnFieldSubToGrave(cm.costfilter,cm.costcheck,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp,e:GetHandler())>0
```

### Ultimate Flag Beast Aim Eagle (`120193003`)

Source: [Rush/Scripts/c120193003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120193003.lua)

```lua
	return Duel.IsExistingMatchingCard(cm.confilter,tp,0,LOCATION_MZONE,1,nil)
end
cm.cost=RD.CostSendOnFieldSubToGrave(cm.costfilter,cm.costcheck,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp,e:GetHandler())>0
```
