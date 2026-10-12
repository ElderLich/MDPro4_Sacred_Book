# RushDuel.CostSendMZoneToHand

Alias: `RD.CostSendMZoneToHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMZoneToHand(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让怪兽返回手卡
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

`Rush/Utilities/RDCost.lua:491`

```lua
function RushDuel.CostSendMZoneToHand(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToHand(filter, LOCATION_MZONE, min, max, except_self, false, true, set_label_before,
        set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendMZoneToHand) with `RushDuel.CostSendMZoneToHand`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| CAN - Melo:D | `120203010` | [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua) | 1 |
| Jointech Spike Centipede | `120249007` | [Rush/Scripts/c120249007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249007.lua) | 1 |
| Harpie Cielo | `120102003` | [Rush/Scripts/c120102003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120102003.lua) | 1 |
| Giant Tiger Strike | `120247037` | [Rush/Scripts/c120247037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247037.lua) | 1 |

## Script Examples

### CAN - Melo:D (`120203010`)

Source: [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua)

```lua
	return c:IsType(TYPE_NORMAL) and c:IsLevel(1) and c:IsRace(RACE_PSYCHO) and c:IsAbleToHand()
end
cm.cost=RD.CostSendMZoneToHand(cm.costfilter,1,1,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.tdfilter,tp,0,LOCATION_ONFIELD,1,nil) end
```

### Jointech Spike Centipede (`120249007`)

Source: [Rush/Scripts/c120249007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249007.lua)

```lua
		and c:IsRace(RACE_MACHINE) and RD.IsAbleToHandOrExtraAsCost(c)
end
cm.cost=RD.CostSendMZoneToHand(cm.costfilter,1,1,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_MZONE,1,nil) end
```

### Harpie Cielo (`120102003`)

Source: [Rush/Scripts/c120102003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120102003.lua)

```lua
	return c:IsCode(list[3]) and c:IsAbleToHand()
end
cm.cost=RD.CostSendMZoneToHand(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,3) end
```
