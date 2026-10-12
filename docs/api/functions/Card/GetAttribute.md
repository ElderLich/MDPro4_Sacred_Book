# Card.GetAttribute

## Signature

```lua
Card.GetAttribute(Card c) -> int
```

## Description

Returns c's current Attribute bitmask.
Cards treated as having multiple Attributes can return a bitwise combination of ATTRIBUTE_* values.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3482`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **172** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetAttribute) with `Card.GetAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua) | 4 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 2 |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua) | 3 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71939275.lua) | 3 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua) | 2 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41908872.lua) | 2 |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65195679.lua) | 2 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71159974.lua) | 6 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45950291.lua) | 2 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10424147.lua) | 2 |
| Shaddoll Schism | `21011044` | [Scripts/c21011044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21011044.lua) | 1 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10780049.lua) | 2 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Hyperinvoked Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33166263.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Rescue Hedgehog | `99742859` | [Scripts/c99742859.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99742859.lua) | 1 |
| Psychic Arsenal | `16238373` | [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16238373.lua) | 3 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89812483.lua) | 2 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67359907.lua) | 2 |
| R-Genex Undine | `34568783` | [Scripts/c34568783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34568783.lua) | 2 |
| ...and 148 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
end
function s.rafilter(c)
	return c:IsFaceup() and ((RACE_ALL&~c:GetRace())~=0 or (ATTRIBUTE_ALL&~c:GetAttribute())~=0)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(s.thfilter,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,nil)
	if chk==0 then return g:GetClassCount(Card.GetAttribute)>=4 end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,4,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,nil,2,tp,LOCATION_HAND)
```

### Mixousia the Confounder (`80843006`)

Source: [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua)

```lua
end
function s.cosfilter(c)
	return c:IsFaceup() and c:GetAttribute()~=ATTRIBUTE_ALL
end
function s.costg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
