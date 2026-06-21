# Auxiliary.AddRitualProcEqual2

## Signature

```lua
Auxiliary.AddRitualProcEqual2(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
filter is the condition the Ritual Monster must satisfy; the sum of the Ritual Levels of the materials must equal the Ritual Monster's Level (which may be altered by other card effects)

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1922`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddRitualProcEqual2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Forbidden Ritual Art | `12157563` | [Scripts/c12157563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12157563.lua) | 40 |
| Recette de Personnel (Staff Recipe) | `40551410` | [Scripts/c40551410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40551410.lua) | 39 |
| Majesty of the White Dragons | `43219114` | [Scripts/c43219114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43219114.lua) | 31 |
| Gishki Aquamirror | `46159582` | [Scripts/c46159582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46159582.lua) | 29 |
| Nekroz Mirror | `14735698` | [Scripts/c14735698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14735698.lua) | 26 |
| Nekroz Cycle | `97211663` | [Scripts/c97211663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97211663.lua) | 26 |
| Zefrasaber, Swordmaster of the Nekroz | `84388461` | [Scripts/c84388461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84388461.lua) | 18 |
| Chaos Form | `21082832` | [Scripts/c21082832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21082832.lua) | 4 |
| Earth Chant | `59820352` | [Scripts/c59820352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59820352.lua) | 3 |
| Sprite's Blessing | `37626500` | [Scripts/c37626500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37626500.lua) | 3 |
| Breath of Acclamation | `44221928` | [Scripts/c44221928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44221928.lua) | 3 |
| Contract with the Abyss | `69035382` | [Scripts/c69035382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69035382.lua) | 3 |

## Script Examples

### Forbidden Ritual Art (`12157563`)

Source: [Scripts/c12157563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12157563.lua)

```lua
function s.initial_effect(c)
	--Activate
	local e1=aux.AddRitualProcEqual2(c,aux.TRUE,LOCATION_GRAVE,aux.TRUE,aux.FALSE,false,s.extraop)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCountLimit(1,id)
```

### Recette de Personnel (Staff Recipe) (`40551410`)

Source: [Scripts/c40551410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40551410.lua)

```lua
	c:RegisterEffect(e2)
	--ritual
	local e3=aux.AddRitualProcEqual2(c,s.filter,LOCATION_HAND,nil,nil,true)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_QUICK_O)
```

### Majesty of the White Dragons (`43219114`)

Source: [Scripts/c43219114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43219114.lua)

```lua
	c:RegisterEffect(e1)
	--spsummon
	local e2=aux.AddRitualProcEqual2(c,nil,nil,nil,s.mfilter,true)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_QUICK_O)
```
