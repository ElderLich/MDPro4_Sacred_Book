# RushDuel.CanSelectAndSet

Alias: `RD.CanSelectAndSet`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndSet(any desc, any filter, any tp, any s_range, any o_range, any min, any max, any expect, any e, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 选择魔法, 陷阱卡盖放
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:196`

```lua
function RushDuel.CanSelectAndSet(desc, filter, tp, s_range, o_range, min, max, expect, e, break_effect)
    local ct = RushDuel.GetSZoneCount(tp, max)
    if ct >= min then
        return RushDuel._private_action_can_select_match(desc, HINTMSG_SET, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._set_spell_trap, e, tp, break_effect)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectAndSet) with `RushDuel.CanSelectAndSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Wish of the Skysavior](/examples/rush-cards/120253064) | `120253064` | [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua) | 1 |
| [Insect Taurus](/examples/rush-cards/120300060) | `120300060` | [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua) | 1 |
| [Grace Princess Hina](/examples/rush-cards/120287020) | `120287020` | [Rush/Scripts/c120287020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287020.lua) | 1 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Skysavior Defense | `120301054` | [Rush/Scripts/c120301054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301054.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Grace Princess Emaki | `120300021` | [Rush/Scripts/c120300021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300021.lua) | 1 |
| Etraynze the Shadow Flower Restricter | `120254041` | [Rush/Scripts/c120254041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254041.lua) | 1 |
| Condurglar the Assisting Anthem | `120293064` | [Rush/Scripts/c120293064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293064.lua) | 1 |
| Celeb Rose Sorcerer | `120244010` | [Rush/Scripts/c120244010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244010.lua) | 1 |
| Cat Claw Girl | `120235016` | [Rush/Scripts/c120235016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235016.lua) | 1 |
| Doushin Kaika the Shadow Flower Full Moon | `120228037` | [Rush/Scripts/c120228037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228037.lua) | 1 |
| Destroyer of Dragon Sorcerers | `120231049` | [Rush/Scripts/c120231049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231049.lua) | 1 |
| Handy Partners | `120290032` | [Rush/Scripts/c120290032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290032.lua) | 1 |
| Hagoromo the Cloudle-Handling Celestial Seamstress | `120246042` | [Rush/Scripts/c120246042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246042.lua) | 1 |
| James the Steam Swallow | `120257020` | [Rush/Scripts/c120257020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257020.lua) | 1 |
| Space Bud Exploit | `120260015` | [Rush/Scripts/c120260015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260015.lua) | 1 |
| Lightning Bringer Wako | `120272024` | [Rush/Scripts/c120272024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272024.lua) | 1 |
| Endoll | `120170018` | [Rush/Scripts/c120170018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170018.lua) | 1 |
| Fortitude Dragon | `120170017` | [Rush/Scripts/c120170017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170017.lua) | 1 |
| Straynge Cat Signal | `120246020` | [Rush/Scripts/c120246020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246020.lua) | 1 |
| Shrine Rhynchus | `120300027` | [Rush/Scripts/c120300027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300027.lua) | 1 |
| Javelin Dux the Shadow Flower Piercer | `120228038` | [Rush/Scripts/c120228038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228038.lua) | 1 |
| Healthie Cafferin | `120306019` | [Rush/Scripts/c120306019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306019.lua) | 1 |
| ...and 5 more |  |  |  |

## Script Examples

### Wish of the Skysavior (`120253064`)

Source: [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_TODECK,Card.IsAbleToDeck,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if RD.SendToDeckBottom(g,e,tp,REASON_EFFECT)~=0 then
			RD.CanSelectAndSet(aux.Stringid(m,1),aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,true)
		end
	end)
```

### Insect Taurus (`120300060`)

Source: [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua)

```lua
			RD.AttachAtkDef(e,tc,atk,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
		RD.CanSelectAndSet(aux.Stringid(m,2),aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e)
	end
end
```

### Grace Princess Hina (`120287020`)

Source: [Rush/Scripts/c120287020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287020.lua)

```lua
		local ex=tc:IsCode(list[1])
		if Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP_DEFENSE)~=0 and ex then
			RD.CanSelectAndSet(aux.Stringid(m,1),aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e)
		end
	end)
```
