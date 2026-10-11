# RushDuel.CostSendGraveToDeckTop

Alias: `RD.CostSendGraveToDeckTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveToDeckTop(any filter, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组上面
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

`Rush/Utilities/RDCost.lua:455`

```lua
function RushDuel.CostSendGraveToDeckTop(filter, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_GRAVE, min, max, false, SEQ_DECKTOP, false, true,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveToDeckTop) with `RushDuel.CostSendGraveToDeckTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| Prime Roast Beef Horseman | `120205042` | [Rush/Scripts/c120205042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205042.lua) | 1 |
| JAM:P Set! | `120183041` | [Rush/Scripts/c120183041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183041.lua) | 1 |
| Flame Archer the Super Graphagas | `120257042` | [Rush/Scripts/c120257042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257042.lua) | 1 |
| Cyber Assault Dragon | `120231022` | [Rush/Scripts/c120231022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231022.lua) | 1 |
| Flapun | `120238041` | [Rush/Scripts/c120238041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238041.lua) | 1 |
| Autumn Leaves of Blisstopia | `120253053` | [Rush/Scripts/c120253053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253053.lua) | 1 |

## Script Examples

### Tamabot King Golem (`120285039`)

Source: [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua)

```lua
	return c:IsCode(list[1]) and c:IsAbleToDeckOrExtraAsCost()
end
cm.cost=RD.CostSendGraveToDeckTop(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,LOCATION_MZONE,0,1,nil) end
```

### Prime Roast Beef Horseman (`120205042`)

Source: [Rush/Scripts/c120205042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205042.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendGraveToDeckTop(cm.costfilter,4,4)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
```

### JAM:P Set! (`120183041`)

Source: [Rush/Scripts/c120183041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183041.lua)

```lua
	return c:IsType(TYPE_MONSTER) and c:IsAbleToDeck()
end
cm.cost=RD.CostSendGraveToDeckTop(cm.costfilter,1,1,nil,nil,function(g)
	return g:GetFirst():GetCode()
end)
```
