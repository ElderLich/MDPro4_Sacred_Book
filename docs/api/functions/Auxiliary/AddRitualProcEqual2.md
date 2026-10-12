# Auxiliary.AddRitualProcEqual2

## Signature

```lua
Auxiliary.AddRitualProcEqual2(Card c, function filter, int summon_location, [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Registers an exact-Level Ritual Summon procedure using Card.GetLevel and returns the created Effect.

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `int`
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:1922`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcEqual2) with `Auxiliary.AddRitualProcEqual2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Forbidden Ritual Art | `12157563` | [Scripts/c12157563.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12157563.lua) | 1 |
| Recette de Personnel (Staff Recipe) | `40551410` | [Scripts/c40551410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40551410.lua) | 1 |
| Majesty of the White Dragons | `43219114` | [Scripts/c43219114.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43219114.lua) | 1 |
| Gishki Aquamirror | `46159582` | [Scripts/c46159582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46159582.lua) | 1 |
| Nekroz Mirror | `14735698` | [Scripts/c14735698.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14735698.lua) | 1 |
| Nekroz Cycle | `97211663` | [Scripts/c97211663.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97211663.lua) | 1 |
| Zefrasaber, Swordmaster of the Nekroz | `84388461` | [Scripts/c84388461.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84388461.lua) | 1 |
| Chaos Form | `21082832` | [Scripts/c21082832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21082832.lua) | 1 |
| Earth Chant | `59820352` | [Scripts/c59820352.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59820352.lua) | 1 |
| Sprite's Blessing | `37626500` | [Scripts/c37626500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37626500.lua) | 1 |
| Breath of Acclamation | `44221928` | [Scripts/c44221928.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44221928.lua) | 1 |
| Contract with the Abyss | `69035382` | [Scripts/c69035382.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69035382.lua) | 1 |

## Script Examples

### Forbidden Ritual Art (`12157563`)

Source: [Scripts/c12157563.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12157563.lua)

```lua
function s.initial_effect(c)
	--Activate
	local e1=aux.AddRitualProcEqual2(c,aux.TRUE,LOCATION_GRAVE,aux.TRUE,aux.FALSE,false,s.extraop)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCountLimit(1,id)
```

### Recette de Personnel (Staff Recipe) (`40551410`)

Source: [Scripts/c40551410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40551410.lua)

```lua
	c:RegisterEffect(e2)
	--ritual
	local e3=aux.AddRitualProcEqual2(c,s.filter,LOCATION_HAND,nil,nil,true)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_QUICK_O)
```

### Majesty of the White Dragons (`43219114`)

Source: [Scripts/c43219114.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43219114.lua)

```lua
	c:RegisterEffect(e1)
	--spsummon
	local e2=aux.AddRitualProcEqual2(c,nil,nil,nil,s.mfilter,true)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_QUICK_O)
```
