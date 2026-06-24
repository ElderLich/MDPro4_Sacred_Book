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

- Detected in **77** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.NOT`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63136489.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 62 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| Cyberload Fusion | `55704856` | [Scripts/c55704856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55704856.lua) | 57 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 56 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 56 |
| Tobari the Sky Ninja | `31887806` | [Scripts/c31887806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31887806.lua) | 53 |
| Heavy Polymerization | `58570206` | [Scripts/c58570206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58570206.lua) | 52 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 51 |
| Salamangreat Burst Gryphon | `10140443` | [Scripts/c10140443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10140443.lua) | 50 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90884403.lua) | 49 |
| Ultimaya Tzolkin | `1686814` | [Scripts/c1686814.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1686814.lua) | 49 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua) | 49 |
| Concours de Cuisine (Culinary Confrontation) | `14283055` | [Scripts/c14283055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14283055.lua) | 49 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 49 |
| Fusion Draft | `55158350` | [Scripts/c55158350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55158350.lua) | 49 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 49 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 49 |
| Rasterliger | `88000953` | [Scripts/c88000953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88000953.lua) | 49 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 48 |
| Ritual Beast Inheritance | `22501005` | [Scripts/c22501005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22501005.lua) | 48 |
| ...and 53 more |  |  |  |

## Script Examples

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
function c27693363.fselect(g,tp,sc)
	return g:GetCount()==2
		and g:IsExists(Card.IsType,1,nil,TYPE_TUNER) and g:IsExists(aux.NOT(Card.IsType),1,nil,TYPE_TUNER)
		and g:IsExists(c27693363.mnfilter,1,nil,g)
		and Duel.GetLocationCountFromEx(tp,tp,g,sc)>0
```

### Chimera Fusion (`63136489`)

Source: [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63136489.lua)

```lua
function s.fsop(e,tp,eg,ep,ev,re,r,rp)
	local chkf=tp
	local mg1=Duel.GetFusionMaterial(tp):Filter(aux.NOT(Card.IsImmuneToEffect),nil,e)
	aux.FCheckAdditional=s.check
	local sg1=Duel.GetMatchingGroup(s.filter,tp,LOCATION_EXTRA,0,nil,e,tp,mg1,nil,chkf)
```

### Ursarctic Polar Star (`62714453`)

Source: [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua)

```lua
end
function s.fselect(g,tp,sc)
	return g:GetCount()==2 and g:IsExists(Card.IsType,1,nil,TYPE_TUNER) and g:IsExists(aux.NOT(Card.IsType),1,nil,TYPE_TUNER)
		and g:IsExists(s.mnfilter,1,nil,g) and Duel.GetLocationCountFromEx(tp,tp,g,sc)>0
end
```
