# Card.GetReason

## Signature

```lua
Card.GetReason(Card c) -> int
```

## Description

Returns c's current reason bitmask/value.
This is the reason recorded in c's current state, such as REASON_EFFECT, REASON_COST, or REASON_BATTLE; it is not limited to position changes.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3462`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetReason`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 71 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua) | 60 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23361526.lua) | 56 |
| Astrolasma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 55 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 51 |
| Meklord Emperor Granel | `4545683` | [Scripts/c4545683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4545683.lua) | 50 |
| Meklord Emperor Skiel | `31930787` | [Scripts/c31930787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31930787.lua) | 48 |
| Meklord Emperor Wisel | `68140974` | [Scripts/c68140974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68140974.lua) | 47 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 47 |
| Recovery Sorcerer | `76232522` | [Scripts/c76232522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76232522.lua) | 45 |
| THE Star Ham | `15123983` | [Scripts/c15123983.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15123983.lua) | 44 |
| Guoglim, Spear of the Ghoti | `2405631` | [Scripts/c2405631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2405631.lua) | 43 |
| Ascension Sky Dragon | `37910722` | [Scripts/c37910722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37910722.lua) | 43 |
| Gigathunder Giclops | `17241941` | [Scripts/c17241941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17241941.lua) | 41 |
| T.G. Recipro Dragonfly | `62560742` | [Scripts/c62560742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62560742.lua) | 41 |
| Scrap Orthros | `64550682` | [Scripts/c64550682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64550682.lua) | 39 |
| Speedroid Dominobutterfly | `28151978` | [Scripts/c28151978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28151978.lua) | 38 |
| Kuribohrn | `78355370` | [Scripts/c78355370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78355370.lua) | 38 |
| Seed of Flame | `38041940` | [Scripts/c38041940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38041940.lua) | 36 |
| De-Synchro | `32441317` | [Scripts/c32441317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32441317.lua) | 36 |
| Blink Out | `28279365` | [Scripts/c28279365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28279365.lua) | 36 |
| Scrap Shark | `69155991` | [Scripts/c69155991.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69155991.lua) | 35 |
| Fusion Recycling Plant | `22829942` | [Scripts/c22829942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22829942.lua) | 35 |
| De-Fusion | `95286165` | [Scripts/c95286165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95286165.lua) | 35 |
| ...and 22 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
function c76647978.mgfilter(c,e,tp,fusc,mg)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE)
		and c:GetReason()&(REASON_FUSION+REASON_MATERIAL)==(REASON_FUSION+REASON_MATERIAL) and c:GetReasonCard()==fusc
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and fusc:CheckFusionMaterial(mg,c,PLAYER_NONE,true)
```

### Ostinato (`9113513`)

Source: [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua)

```lua
function c9113513.mgfilter(c,e,tp,fusc,mg)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE)
		and c:GetReason()&(REASON_FUSION+REASON_MATERIAL)==(REASON_FUSION+REASON_MATERIAL) and c:GetReasonCard()==fusc
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and fusc:CheckFusionMaterial(mg,c,PLAYER_NONE,true)
```

### Hi-Speedroid Cork Shooter (`23361526`)

Source: [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23361526.lua)

```lua
function c23361526.spfilter(c,e,tp,sync)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE)
		and bit.band(c:GetReason(),0x80008)==0x80008 and c:GetReasonCard()==sync
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```
