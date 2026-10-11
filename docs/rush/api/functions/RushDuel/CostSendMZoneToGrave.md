# RushDuel.CostSendMZoneToGrave

Alias: `RD.CostSendMZoneToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMZoneToGrave(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把怪兽送去墓地
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

`Rush/Utilities/RDCost.lua:313`

```lua
function RushDuel.CostSendMZoneToGrave(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToGrave(filter, LOCATION_MZONE, min, max, except_self, false, false, set_label_before,
        set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **68** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendMZoneToGrave) with `RushDuel.CostSendMZoneToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nativity of the Monarchs](/examples/rush-cards/120244063) | `120244063` | [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua) | 1 |
| [Star Protector's Protection](/examples/rush-cards/120253065) | `120253065` | [Rush/Scripts/c120253065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253065.lua) | 1 |
| [Dark Renewal](/examples/rush-cards/120285066) | `120285066` | [Rush/Scripts/c120285066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285066.lua) | 1 |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| Voidvelg Kyrie | `120244006` | [Rush/Scripts/c120244006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244006.lua) | 1 |
| Multiple Adapter Unit | `120231030` | [Rush/Scripts/c120231030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231030.lua) | 1 |
| Heavy Cavalry Tactics | `120155046` | [Rush/Scripts/c120155046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155046.lua) | 1 |
| Takeout Attack | `120290060` | [Rush/Scripts/c120290060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290060.lua) | 1 |
| Art Angel Metal Position | `120228014` | [Rush/Scripts/c120228014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228014.lua) | 1 |
| Launcher Catapult Turtle | `120249030` | [Rush/Scripts/c120249030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249030.lua) | 1 |
| Celeb Rose Sorcerer | `120244010` | [Rush/Scripts/c120244010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244010.lua) | 1 |
| Frenzied Panda of the Bamboo Forest | `120294028` | [Rush/Scripts/c120294028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294028.lua) | 1 |
| Dark Matter Jelly | `120261022` | [Rush/Scripts/c120261022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261022.lua) | 1 |
| Plasmatic Model Another Rising Lystella | `120290034` | [Rush/Scripts/c120290034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290034.lua) | 1 |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Blue-Fang Enhanced Burst Dragon | `120244037` | [Rush/Scripts/c120244037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244037.lua) | 1 |
| Sevens Road Sorcerer | `120205011` | [Rush/Scripts/c120205011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205011.lua) | 1 |
| Destructor Integration Scrap Gate | `120264053` | [Rush/Scripts/c120264053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264053.lua) | 1 |
| Fish Depth Charge | `120253062` | [Rush/Scripts/c120253062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253062.lua) | 1 |
| Dragonlion Pit Trap | `120231068` | [Rush/Scripts/c120231068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231068.lua) | 1 |
| Corruption of the Blaze Fiends | `120231016` | [Rush/Scripts/c120231016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231016.lua) | 1 |
| Sacrificial Summon | `120217094` | [Rush/Scripts/c120217094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217094.lua) | 1 |
| Sarcophagus of Isyria | `120300048` | [Rush/Scripts/c120300048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300048.lua) | 1 |
| ...and 44 more |  |  |  |

## Script Examples

### Nativity of the Monarchs (`120244063`)

Source: [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return (e:IsCostChecked() or Duel.GetMZoneCount(tp)>0)
```

### Star Protector's Protection (`120253065`)

Source: [Rush/Scripts/c120253065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253065.lua)

```lua
	return Duel.GetTurnPlayer()==1-tp and eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendMZoneToGrave(Card.IsAbleToGraveAsCost,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetFlagEffect(tp,m)==0 end
```

### Dark Renewal (`120285066`)

Source: [Rush/Scripts/c120285066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285066.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```
