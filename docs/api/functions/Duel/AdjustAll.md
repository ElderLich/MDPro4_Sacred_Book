# Duel.AdjustAll

## Signature

```lua
Duel.AdjustAll() -> void
```

## Description

Immediately refreshes field information.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4964`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **57** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.AdjustAll`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Aiwass the Spirit of the Law](/examples/cards/84288367) | `84288367` | [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua) | 64 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| K9-EW Special Release Experiment | `26585784` | [Scripts/c26585784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26585784.lua) | 59 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 58 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 55 |
| Melffy Rabbys | `46955132` | [Scripts/c46955132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46955132.lua) | 55 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 54 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 53 |
| Worldsea Dragon Zealantis | `45112597` | [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua) | 53 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 52 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 51 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 51 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 51 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50797682.lua) | 51 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 50 |
| Whisker Blitzclique | `85523502` | [Scripts/c85523502.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85523502.lua) | 50 |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua) | 50 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 49 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 49 |
| ...and 33 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
		e2:SetReset(RESET_EVENT+RESETS_STANDARD)
		ec:RegisterEffect(e2)
		Duel.AdjustAll()
		if ec:IsControler(1-tp) or not cres then return false end
		local chkf=tp
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	end
	Duel.SpecialSummonComplete()
	Duel.AdjustAll()
	local tg=Duel.GetMatchingGroup(Card.IsSynchroSummonable,tp,LOCATION_EXTRA,0,nil,nil)
	if res and tg:GetCount()>0 then
```

### Aiwass the Spirit of the Law (`84288367`)

Source: [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua)

```lua
	if c:IsRelateToChain() and aux.NecroValleyFilter()(c)
		and Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)>0 then
		Duel.AdjustAll()
		local chkf=tp
		local mg1=Duel.GetFusionMaterial(tp):Filter(s.filter1,nil,e)
```
