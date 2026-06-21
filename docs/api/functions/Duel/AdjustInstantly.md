# Duel.AdjustInstantly

## Signature

```lua
Duel.AdjustInstantly([Card c]) -> void
```

## Description

Manually refreshing the card's inactive state on card \[affected by card c\]

## Parameters

- `c` `Card` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4963`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **40** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.AdjustInstantly`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Destruction Chant of the Sacred Beast | `50147815` | [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua) | 59 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 53 |
| Red Cocoon | `2542230` | [Scripts/c2542230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2542230.lua) | 52 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Scourge of the White Forest | `93723936` | [Scripts/c93723936.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93723936.lua) | 51 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81418467.lua) | 50 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 49 |
| Rank-Down-Magic Numeron Fall | `71345905` | [Scripts/c71345905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71345905.lua) | 48 |
| Baelgrill de Nouvelles | `88890658` | [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88890658.lua) | 47 |
| Update Jammer | `88093706` | [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua) | 47 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 47 |
| Realm Eulogy | `54851325` | [Scripts/c54851325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54851325.lua) | 47 |
| Flower Cardian Lightflare | `87460579` | [Scripts/c87460579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87460579.lua) | 46 |
| Ultimate Leo Utopia Ray | `68679595` | [Scripts/c68679595.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68679595.lua) | 46 |
| Magnificent Machine Angel | `27331568` | [Scripts/c27331568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27331568.lua) | 46 |
| Cosmo Queen the Queen of Prayers | `85314178` | [Scripts/c85314178.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85314178.lua) | 45 |
| Primite Drillbeam | `29095457` | [Scripts/c29095457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29095457.lua) | 45 |
| Dracotail Flame | `5431722` | [Scripts/c5431722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5431722.lua) | 43 |
| Fist of Fate | `79868386` | [Scripts/c79868386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79868386.lua) | 42 |
| Stare of the Snake Hair | `54077752` | [Scripts/c54077752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54077752.lua) | 42 |
| Tearlaments Sulliek | `74920585` | [Scripts/c74920585.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74920585.lua) | 42 |
| Samurai Destroyer | `40509732` | [Scripts/c40509732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40509732.lua) | 41 |
| Artmage Finmel | `34541940` | [Scripts/c34541940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34541940.lua) | 40 |
| ...and 16 more |  |  |  |

## Script Examples

### Destruction Chant of the Sacred Beast (`50147815`)

Source: [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua)

```lua
						nc:RegisterEffect(e3)
					end
					Duel.AdjustInstantly()
					Duel.NegateRelatedChain(nc,RESET_TURN_SET)
					Duel.Destroy(nc,REASON_EFFECT)
```

### Traptrix Atypus (`48183890`)

Source: [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua)

```lua
		tc=g:GetNext()
	end
	Duel.AdjustInstantly(c)
	if Duel.IsExistingMatchingCard(aux.NecroValleyFilter(s.rmfilter),tp,LOCATION_GRAVE,0,1,nil)
		and Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
```

### Borrelshroud Dragon (`66452432`)

Source: [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua)

```lua
			sc:RegisterEffect(e4)
		end
		Duel.AdjustInstantly(sc)
		if tc:IsRelateToChain() and tc:IsType(TYPE_MONSTER) then
			Duel.BreakEffect()
```
