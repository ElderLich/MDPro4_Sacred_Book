# Auxiliary.NOT

## Signature

```lua
Auxiliary.NOT(function f) -> function
```

## Description

Returns a predicate that negates f's result.

## Parameters

- `f` `function`

## Returns

- `function` - A predicate that returns not f(...).

## Source

- `Utilities/utility.lua:119`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **82** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.NOT) with `Auxiliary.NOT`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80843006.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 2 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63136489.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 1 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| Cyberload Fusion | `55704856` | [Scripts/c55704856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55704856.lua) | 2 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 1 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 2 |
| Tobari the Sky Ninja | `31887806` | [Scripts/c31887806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31887806.lua) | 1 |
| Zenet Revelator Nefertari | `84512726` | [Scripts/c84512726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84512726.lua) | 2 |
| Heavy Polymerization | `58570206` | [Scripts/c58570206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58570206.lua) | 2 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 1 |
| Salamangreat Burst Gryphon | `10140443` | [Scripts/c10140443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10140443.lua) | 1 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90884403.lua) | 1 |
| Ultimaya Tzolkin | `1686814` | [Scripts/c1686814.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1686814.lua) | 1 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua) | 1 |
| Concours de Cuisine (Culinary Confrontation) | `14283055` | [Scripts/c14283055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14283055.lua) | 1 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 1 |
| Fusion Draft | `55158350` | [Scripts/c55158350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55158350.lua) | 1 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 1 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 1 |
| ...and 58 more |  |  |  |

## Script Examples

### Mixousia the Confounder (`80843006`)

Source: [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80843006.lua)

```lua
	c:EnableReviveLimit()
	--material
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsRace,RACE_SPELLCASTER),aux.FilterBoolFunction(aux.NOT(Card.IsRace),RACE_SPELLCASTER),true)
	--attr change
	local e1=Effect.CreateEffect(c)
```

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
function c27693363.fselect(g,tp,sc)
	return g:GetCount()==2
		and g:IsExists(Card.IsType,1,nil,TYPE_TUNER) and g:IsExists(aux.NOT(Card.IsType),1,nil,TYPE_TUNER)
		and g:IsExists(c27693363.mnfilter,1,nil,g)
		and Duel.GetLocationCountFromEx(tp,tp,g,sc)>0
```

### Artmage Masterwork -Succession- (`37517035`)

Source: [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua)

```lua
	if chk==0 then
		local chkf=tp
		local mg1=Duel.GetFusionMaterial(tp):Filter(aux.NOT(Card.IsImmuneToEffect),nil,e)
		aux.FCheckAdditional=s.check
		local res=Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_EXTRA,0,1,nil,e,tp,mg1,nil,chkf)
```
