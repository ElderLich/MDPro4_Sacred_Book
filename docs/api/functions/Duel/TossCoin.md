# Duel.TossCoin

## Signature

```lua
Duel.TossCoin(int player, int count) -> ...
```

## Description

Let the player player cast count (&lt;= 5) coins, the return value for the count results, 0 or 1.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5036`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.TossCoin`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 49 |
| Desperado Barrel Dragon | `76728962` | [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua) | 48 |
| Arcana Force V - The Hierophant | `3376703` | [Scripts/c3376703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3376703.lua) | 46 |
| Light Force | `30913809` | [Scripts/c30913809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30913809.lua) | 45 |
| Saion the Vaylantz Archer | `15130912` | [Scripts/c15130912.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15130912.lua) | 43 |
| Goddess of the Two Sides | `50915474` | [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50915474.lua) | 41 |
| Bettan Bat | `84079032` | [Scripts/c84079032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84079032.lua) | 39 |
| VIP Whale | `14556954` | [Scripts/c14556954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14556954.lua) | 39 |
| Elemental HERO Chaos Neos | `17032740` | [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17032740.lua) | 38 |
| Arcana Force XIX - The Sun | `39761418` | [Scripts/c39761418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39761418.lua) | 37 |
| Ancient Warriors Saga - East-by-South Winds | `62528292` | [Scripts/c62528292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62528292.lua) | 36 |
| Arcana Spread | `76302448` | [Scripts/c76302448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76302448.lua) | 34 |
| Arcana Reading | `11819473` | [Scripts/c11819473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11819473.lua) | 32 |
| Arcana Force VII - The Chariot | `34568403` | [Scripts/c34568403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34568403.lua) | 32 |
| Time Wizard of Tomorrow | `26273196` | [Scripts/c26273196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26273196.lua) | 31 |
| Light Barrier | `73206827` | [Scripts/c73206827.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73206827.lua) | 31 |
| Prepare to Strike Back | `4483989` | [Scripts/c4483989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4483989.lua) | 31 |
| Toon Barrel Dragon | `28112535` | [Scripts/c28112535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28112535.lua) | 31 |
| Origami Goddess | `7930346` | [Scripts/c7930346.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7930346.lua) | 31 |
| Vortex of Time | `42138622` | [Scripts/c42138622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42138622.lua) | 29 |
| Head Judging | `38143903` | [Scripts/c38143903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38143903.lua) | 28 |
| Fairy Box | `21598948` | [Scripts/c21598948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21598948.lua) | 28 |
| Tempura of Fortune - EBI | `86304179` | [Scripts/c86304179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86304179.lua) | 26 |
| Couple of Aces | `26259179` | [Scripts/c26259179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26259179.lua) | 24 |
| ...and 23 more |  |  |  |

## Script Examples

### Arcana Force EX - The Chaos Ruler (`12686296`)

Source: [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua)

```lua
				{b2,61,0})
		end
	else res=Duel.TossCoin(tp,1) end
	if res==1 then
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
```

### Desperado Barrel Dragon (`76728962`)

Source: [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua)

```lua
	local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	if g:GetCount()==0 then return end
	local c1,c2,c3=Duel.TossCoin(tp,3)
	local ct=c1+c2+c3
	if ct==0 then return end
```

### Arcana Force V - The Hierophant (`3376703`)

Source: [Scripts/c3376703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3376703.lua)

```lua
		end
	else
		res=Duel.TossCoin(tp,1)
	end
	if res==1 then
```
