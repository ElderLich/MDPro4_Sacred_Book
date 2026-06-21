# Card.GetOriginalAttribute

## Signature

```lua
Card.GetOriginalAttribute(Card c) -> int
```

## Description

Returns the attributes of the card that c is describing

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3432`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **71** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOriginalAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua) | 58 |
| World Legacy Monstrosity | `14604710` | [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14604710.lua) | 56 |
| Elfnotes: Rhapsodia of Madness | `24092792` | [Scripts/c24092792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24092792.lua) | 54 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 53 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 53 |
| Chaos Allure Queen | `29925614` | [Scripts/c29925614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29925614.lua) | 53 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27632520.lua) | 52 |
| Chaofeng, Phantom of the Yang Zing | `19048328` | [Scripts/c19048328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19048328.lua) | 51 |
| Hyper-Rank-Up-Magic Ultimate Force | `87818869` | [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua) | 51 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Gagaga Utopic Tactics | `75956913` | [Scripts/c75956913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75956913.lua) | 51 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39973386.lua) | 50 |
| Myutant Blast | `79072916` | [Scripts/c79072916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79072916.lua) | 49 |
| Speedroid Wing Synchron | `2254222` | [Scripts/c2254222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2254222.lua) | 48 |
| Mirage Swordsman | `73936388` | [Scripts/c73936388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73936388.lua) | 48 |
| Union Carrier | `83152482` | [Scripts/c83152482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83152482.lua) | 48 |
| Sacred Fire King Garunix | `66431519` | [Scripts/c66431519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66431519.lua) | 47 |
| Silhouhatte Rabbit | `1528054` | [Scripts/c1528054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1528054.lua) | 47 |
| Galaxy Satellite Dragon | `92362073` | [Scripts/c92362073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92362073.lua) | 47 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 47 |
| Crystal Aegis | `58371671` | [Scripts/c58371671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58371671.lua) | 47 |
| Simorgh Sky Battle | `57823578` | [Scripts/c57823578.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57823578.lua) | 46 |
| Elemental Training | `11167052` | [Scripts/c11167052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11167052.lua) | 46 |
| ...and 47 more |  |  |  |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local lv=tc:GetOriginalLevel()
	local race=tc:GetOriginalRace()
	local att=tc:GetOriginalAttribute()
	if Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)<=0
		or not Duel.IsPlayerCanSpecialSummonMonster(tp,60025884,0,TYPES_TOKEN_MONSTER,atk,def,lv,race,att) then return end
```

### Vanquish Soul Trinity Burst (`53330789`)

Source: [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua)

```lua
function c53330789.spfilter(c,e,tp,attr)
	return c:IsSetCard(0x195) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and c:GetOriginalAttribute()~=attr
end
function c53330789.filter(c,e,tp)
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
