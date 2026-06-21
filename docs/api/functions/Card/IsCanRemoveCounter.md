# Card.IsCanRemoveCounter

## Signature

```lua
Card.IsCanRemoveCounter(Card c, int player, int countertype, int count, int reason) -> bool
```

## Description

Check if the player player can remove count counters of type c on c for reason

## Parameters

- `c` `Card`
- `player` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3636`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanRemoveCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 51 |
| Chaos Core | `54040484` | [Scripts/c54040484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54040484.lua) | 45 |
| Mythical Institution | `94599451` | [Scripts/c94599451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94599451.lua) | 45 |
| Endymion, the Master Magician | `40732515` | [Scripts/c40732515.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40732515.lua) | 45 |
| Beat Cop from the Underworld | `99011763` | [Scripts/c99011763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99011763.lua) | 44 |
| Link Turret | `55034079` | [Scripts/c55034079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55034079.lua) | 42 |
| Full Moon Mirror | `44857722` | [Scripts/c44857722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44857722.lua) | 42 |
| Ursarctic Radiation | `32692693` | [Scripts/c32692693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32692693.lua) | 42 |
| Duralume, Vaalmonican Heathen Hallow | `76821171` | [Scripts/c76821171.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76821171.lua) | 41 |
| Thelematech Clatis | `98986900` | [Scripts/c98986900.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98986900.lua) | 38 |
| Magical Exemplar | `6061630` | [Scripts/c6061630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6061630.lua) | 36 |
| F.A. Shining Star GT | `37414347` | [Scripts/c37414347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37414347.lua) | 35 |
| BOXer | `61156777` | [Scripts/c61156777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61156777.lua) | 32 |
| Pitch-Black Power Stone | `34029630` | [Scripts/c34029630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34029630.lua) | 32 |
| Hinezumi Hanabi | `71459017` | [Scripts/c71459017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71459017.lua) | 30 |
| Blast Magician | `21051146` | [Scripts/c21051146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21051146.lua) | 28 |
| Magical Citadel of Endymion | `39910367` | [Scripts/c39910367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39910367.lua) | 26 |

## Script Examples

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	local exg=nil
	if fc and fc:IsHasEffect(81788994) and fc:IsCanRemoveCounter(tp,0x16,3,REASON_EFFECT) then
		local fe=fc:IsHasEffect(81788994)
		exg=Duel.GetMatchingGroup(c50907446.FShaddollExFilter,tp,0,LOCATION_MZONE,mg,c,fe)
```

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
	local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	local exg=nil
	if fc and fc:IsHasEffect(81788994) and fc:IsCanRemoveCounter(tp,0x16,3,REASON_EFFECT) then
		local fe=fc:IsHasEffect(81788994)
		exg=Duel.GetMatchingGroup(s.FShaddollExFilter,tp,0,LOCATION_MZONE,mg,c,fe)
```

### Zebufera, Vaalmonican Hallow Heathen (`2815176`)

Source: [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua)

```lua
		local ct=0
		for i=1,3 do
			if tc:IsCanRemoveCounter(tp,0x6a,i,REASON_COST) then ct=i end
		end
		tl=tl+ct
```
