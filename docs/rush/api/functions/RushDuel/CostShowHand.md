# RushDuel.CostShowHand

Alias: `RD.CostShowHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowHand(any filter, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡给对方观看
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:206`

```lua
function RushDuel.CostShowHand(filter, min, max, set_label, set_object)
    return RushDuel._private_cost_select_match(HINTMSG_CONFIRM, filter, LOCATION_HAND, 0, min, max, true,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
            Duel.ShuffleHand(tp)
        end)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostShowHand) with `RushDuel.CostShowHand`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Miracle Pick](/examples/rush-cards/120253052) | `120253052` | [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| [Lovely Rabbit](/examples/rush-cards/120300018) | `120300018` | [Rush/Scripts/c120300018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300018.lua) | 1 |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| [Road Servant Flare](/examples/rush-cards/120109050) | `120109050` | [Rush/Scripts/c120109050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109050.lua) | 1 |
| Lua, the Fairy of Skysavior | `120235021` | [Rush/Scripts/c120235021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235021.lua) | 1 |
| Chemipet Chirp | `120261009` | [Rush/Scripts/c120261009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261009.lua) | 1 |
| Celeb Rose Wiz | `120253008` | [Rush/Scripts/c120253008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253008.lua) | 1 |
| Dark Matter String | `120261024` | [Rush/Scripts/c120261024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261024.lua) | 1 |
| Intersprime | `120257003` | [Rush/Scripts/c120257003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257003.lua) | 1 |
| Plectclive the Dynamauve Deadly Dirge | `120253043` | [Rush/Scripts/c120253043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253043.lua) | 1 |
| Quick Attack Knight | `120293037` | [Rush/Scripts/c120293037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293037.lua) | 1 |
| Legendary Hunter | `120271046` | [Rush/Scripts/c120271046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271046.lua) | 1 |
| Hybridrive Orbuster | `120264007` | [Rush/Scripts/c120264007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264007.lua) | 1 |
| Zombie Fireworks | `120217082` | [Rush/Scripts/c120217082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217082.lua) | 1 |
| Voidvelg Logisticos | `120244007` | [Rush/Scripts/c120244007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244007.lua) | 1 |
| Reifu the Dimensional Sworn Ally | `120309028` | [Rush/Scripts/c120309028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309028.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 1 |
| Legendary Shooter | `120271045` | [Rush/Scripts/c120271045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271045.lua) | 1 |
| Space Call | `120260018` | [Rush/Scripts/c120260018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260018.lua) | 1 |
| Super Electromagnetic Maximum | `120239024` | [Rush/Scripts/c120239024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239024.lua) | 1 |
| Lovely Dove | `120260047` | [Rush/Scripts/c120260047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260047.lua) | 1 |
| ...and 22 more |  |  |  |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	return not c:IsPublic() and c:IsRace(RACE_WARRIOR+RACE_FAIRY)
end
cm.cost=RD.CostShowHand(cm.costfilter,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
```

### Miracle Pick (`120253052`)

Source: [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua)

```lua
	return not c:IsPublic() and c:IsLevel(7) and c:IsAttribute(ATTRIBUTE_LIGHT+ATTRIBUTE_DARK) and c:IsRace(RACE_PSYCHO) and RD.IsDefense(c,0)
end
cm.cost=RD.CostShowHand(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
```

### Lovely Wolf (`120260046`)

Source: [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua)

```lua
	return c:IsCode(list[1]) and c:IsAbleToHand()
end
cm.cost=RD.CostShowHand(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil,e,tp) end
```
