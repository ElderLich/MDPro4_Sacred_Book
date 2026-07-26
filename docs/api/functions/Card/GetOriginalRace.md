# Card.GetOriginalRace

## Signature

```lua
Card.GetOriginalRace(Card c) -> int
```

## Description

Returns c's original Race from card data, or 0 while c is marked with STATUS_NO_LEVEL.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3440`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **83** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOriginalRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| World Legacy Monstrosity | `14604710` | [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14604710.lua) | 2 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 2 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 1 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 1 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 3 |
| Card 24056179 | `24056179` | [Scripts/c24056179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24056179.lua) | 2 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43502497.lua) | 3 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 1 |
| Endymion, the Crescent Magistus | `20714553` | [Scripts/c20714553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20714553.lua) | 1 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39973386.lua) | 2 |
| Union Carrier | `83152482` | [Scripts/c83152482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83152482.lua) | 3 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 2 |
| Silhouhatte Rabbit | `1528054` | [Scripts/c1528054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1528054.lua) | 1 |
| Traptrix Pinguicula | `1688285` | [Scripts/c1688285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1688285.lua) | 1 |
| Galaxy Satellite Dragon | `92362073` | [Scripts/c92362073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92362073.lua) | 1 |
| Crystal Aegis | `58371671` | [Scripts/c58371671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58371671.lua) | 3 |
| Ryu-Ge Realm - Sea Spires | `28669235` | [Scripts/c28669235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28669235.lua) | 1 |
| Aussa the Earth Channeler | `62803464` | [Scripts/c62803464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62803464.lua) | 5 |
| The League of Uniform Nomenclature Strikes | `29265962` | [Scripts/c29265962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29265962.lua) | 2 |
| Ryu-Ge Realm - Wyrm Winds | `55154344` | [Scripts/c55154344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55154344.lua) | 1 |
| Mysterion the Dragon Crown | `13735899` | [Scripts/c13735899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13735899.lua) | 4 |
| ...and 59 more |  |  |  |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local def=tc:GetTextDefense()
	local lv=tc:GetOriginalLevel()
	local race=tc:GetOriginalRace()
	local att=tc:GetOriginalAttribute()
	if Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)<=0
```

### World Legacy Monstrosity (`14604710`)

Source: [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14604710.lua)

```lua
end
function c14604710.spfilter2(c,e,tp,tc)
	return c:IsLevel(9) and c:GetOriginalRace()~=tc:GetOriginalRace() and c:GetOriginalAttribute()~=tc:GetOriginalAttribute()
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

### Link into the VRAINS! (`28827503`)

Source: [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua)

```lua
end
function c28827503.thfilter(c,race)
	return c:GetOriginalRace()&race>0 and c:IsAbleToHand()
end
function c28827503.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
