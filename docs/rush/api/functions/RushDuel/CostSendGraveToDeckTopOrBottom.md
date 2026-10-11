# RushDuel.CostSendGraveToDeckTopOrBottom

Alias: `RD.CostSendGraveToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveToDeckTopOrBottom(any filter, any min, any max, any top_desc, any bottom_desc, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组上面或下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:479`

```lua
function RushDuel.CostSendGraveToDeckTopOrBottom(filter, min, max, top_desc, bottom_desc, set_label_before,
    set_object_before, set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckTopOrBottom(filter, LOCATION_GRAVE, min, max, false, top_desc, bottom_desc,
        false, true, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveToDeckTopOrBottom) with `RushDuel.CostSendGraveToDeckTopOrBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| Splendid Slash | `120254070` | [Rush/Scripts/c120254070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254070.lua) | 1 |
| Destructor Soldier Canteen | `120264013` | [Rush/Scripts/c120264013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264013.lua) | 1 |
| Hyper Ritzy King Rex | `120196037` | [Rush/Scripts/c120196037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196037.lua) | 1 |
| Galactiara FUSE Eve | `120244034` | [Rush/Scripts/c120244034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244034.lua) | 1 |
| Ether F Striker | `120205044` | [Rush/Scripts/c120205044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205044.lua) | 1 |
| Axtion Melody the Music Princess | `120247020` | [Rush/Scripts/c120247020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247020.lua) | 1 |

## Script Examples

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
	return c:IsType(TYPE_MAXIMUM) and c:IsAbleToDeckOrExtraAsCost()
end
cm.cost=RD.CostSendGraveToDeckTopOrBottom(cm.costfilter,3,3,aux.Stringid(m,1),aux.Stringid(m,2))
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,0,LOCATION_MZONE,1,nil) end
```

### Splendid Slash (`120254070`)

Source: [Rush/Scripts/c120254070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254070.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,tp,rp)
end
cm.cost=RD.CostSendGraveToDeckTopOrBottom(cm.costfilter,1,1,aux.Stringid(m,1),aux.Stringid(m,2))
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsAbleToDeck,tp,0,LOCATION_ONFIELD,1,nil) end
```

### Destructor Soldier Canteen (`120264013`)

Source: [Rush/Scripts/c120264013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264013.lua)

```lua
	return (c:IsCode(list[1]) or (c:IsType(TYPE_NORMAL) and c:IsRace(RACE_WYRM))) and c:IsAbleToHand()
end
cm.cost=RD.CostSendGraveToDeckTopOrBottom(cm.costfilter,1,1,aux.Stringid(m,1),aux.Stringid(m,2),nil,nil,function(g)
	return g:GetFirst():GetCode()
end)
```
