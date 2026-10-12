# RushDuel.SelectAndSet

Alias: `RD.SelectAndSet`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndSet(any filter, any tp, any s_range, any o_range, any min, any max, any expect, any e, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择魔法, 陷阱卡盖放
```

## Parameters

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

`Rush/Utilities/RDAction.lua:188`

```lua
function RushDuel.SelectAndSet(filter, tp, s_range, o_range, min, max, expect, e, break_effect)
    local ct = RushDuel.GetSZoneCount(tp, max)
    if ct >= min then
        return RushDuel._private_action_select_match(HINTMSG_SET, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._set_spell_trap, e, tp, break_effect)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectAndSet) with `RushDuel.SelectAndSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |
| [Magician's Sense](/examples/rush-cards/120246088) | `120246088` | [Rush/Scripts/c120246088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246088.lua) | 1 |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| Celeb Rose Rich Magicians | `120287040` | [Rush/Scripts/c120287040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287040.lua) | 1 |
| Iris the Rare Shadow Flower | `120228018` | [Rush/Scripts/c120228018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228018.lua) | 1 |
| Looter Force | `120228064` | [Rush/Scripts/c120228064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228064.lua) | 1 |
| Voidvelg Logisticos | `120244007` | [Rush/Scripts/c120244007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244007.lua) | 1 |
| Zuse the Wisdom Vassal | `120244014` | [Rush/Scripts/c120244014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244014.lua) | 1 |
| Light-Calling Griffore | `120280008` | [Rush/Scripts/c120280008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280008.lua) | 1 |
| Shariel, the Novice Sushi Fairy | `120228028` | [Rush/Scripts/c120228028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228028.lua) | 1 |
| Purple-Eyes Star Cat | `120235014` | [Rush/Scripts/c120235014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235014.lua) | 1 |
| Shield in the Right Hand | `120246048` | [Rush/Scripts/c120246048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246048.lua) | 1 |
| Yabume the Frost-Purifying Purebreed | `120298045` | [Rush/Scripts/c120298045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298045.lua) | 1 |
| Necromaid Doctor | `120294015` | [Rush/Scripts/c120294015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294015.lua) | 1 |
| Astrobio Drake | `120235026` | [Rush/Scripts/c120235026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235026.lua) | 1 |
| Wooly Wonderland Planewe | `120208020` | [Rush/Scripts/c120208020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208020.lua) | 1 |
| Matsugumi the Ruler's Squad | `120188006` | [Rush/Scripts/c120188006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120188006.lua) | 1 |
| Double Chill Dragons | `120235034` | [Rush/Scripts/c120235034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235034.lua) | 1 |
| DBF Rebuildra | `120244005` | [Rush/Scripts/c120244005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244005.lua) | 1 |
| Nehime the Dimensional Sworn Ally | `120309029` | [Rush/Scripts/c120309029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309029.lua) | 1 |
| Winged Dragon of Chaos | `120280006` | [Rush/Scripts/c120280006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280006.lua) | 1 |
| Trap Mole | `120238039` | [Rush/Scripts/c120238039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238039.lua) | 1 |
| Charging Remora | `120253018` | [Rush/Scripts/c120253018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253018.lua) | 1 |
| Swordfish Vanguard Gaju | `120208022` | [Rush/Scripts/c120208022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208022.lua) | 1 |
| ...and 6 more |  |  |  |

## Script Examples

### The Black Witch Facing the Temple (`120309048`)

Source: [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndSet(aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e)
end
```

### Magician's Sense (`120246088`)

Source: [Rush/Scripts/c120246088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246088.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndSet(aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,2,nil,e)~=0 then
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetDescription(aux.Stringid(m,1))
```

### Fusionic Defense (`120257064`)

Source: [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndSet(aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e)~=0 then
		local filter=RD.Filter(cm.filter,tp)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),aux.Stringid(m,2),filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
```
