# Duel.IsPlayerCanSpecialSummonCount

## Signature

```lua
Duel.IsPlayerCanSpecialSummonCount(int player, int count) -> bool
```

## Description

Checks whether player can perform count Special Summons under the current remaining Special Summon-count limits.
The core checks EFFECT_LEFT_SPSUMMON_COUNT effects and the player's Special Summon counter.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5053`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **50** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanSpecialSummonCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 58 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 55 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 55 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 55 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 53 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 52 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 51 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 51 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50797682.lua) | 51 |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua) | 50 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 49 |
| Cyber Jormungardr | `19715246` | [Scripts/c19715246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19715246.lua) | 49 |
| Gazer Shark | `23536866` | [Scripts/c23536866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23536866.lua) | 49 |
| Salamangreat Burning Shell | `28534130` | [Scripts/c28534130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28534130.lua) | 48 |
| Shining Hope Road | `62829077` | [Scripts/c62829077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62829077.lua) | 48 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 47 |
| Magician Navigation | `7922915` | [Scripts/c7922915.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7922915.lua) | 47 |
| Crystron Tristaros | `99471856` | [Scripts/c99471856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99471856.lua) | 46 |
| Performapal Miss Director | `92932860` | [Scripts/c92932860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92932860.lua) | 46 |
| ...and 26 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	local b1=chkrel and Duel.IsExistingMatchingCard(c30983281.scfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,c,chkrel,nil)
	local b2=chknotrel and Duel.IsExistingMatchingCard(c30983281.scfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,c,nil,chknotrel)
	if chk==0 then return Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and (not ect1 or ect1>1) and (not ect2 or ect2>1) and (b1 or b2)
		and aux.MustMaterialCheck(nil,tp,EFFECT_MUST_BE_SMATERIAL) end
```

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
	if ft>2 then ft=2 end
	if Duel.IsPlayerAffectedByEffect(tp,59822133) then ft=1 end
	if chk==0 then return Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and mg:CheckSubGroup(c97769122.fselect,1,ft,tp) end
```

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
function c71095768.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(c71095768.spfilter,tp,LOCATION_HAND+LOCATION_GRAVE,0,nil,e,tp)
	if chk==0 then return Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and not Duel.IsPlayerAffectedByEffect(tp,59822133)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>1
```
