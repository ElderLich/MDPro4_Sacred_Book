# Duel.ReleaseRitualMaterial

## Signature

```lua
Duel.ReleaseRitualMaterial(Group g) -> void
```

## Description

Moves the selected Ritual Materials in g using Ritual-material rules.
Standard hand or field materials are Tributed, while materials such as suitable Graveyard Ritual Materials are banished instead.
Call Card.SetMaterial before this function, then Special Summon with SUMMON_TYPE_RITUAL and call Card.CompleteProcedure after the Summon succeeds. The function does not return a count.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4999`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ReleaseRitualMaterial) with `Duel.ReleaseRitualMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 2 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 2 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua) | 1 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua) | 1 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| Magikey Duo | `51510279` | [Scripts/c51510279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51510279.lua) | 1 |
| Blessing of the Voiceless Voice | `39114494` | [Scripts/c39114494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39114494.lua) | 1 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 1 |
| Magikey Maftea | `99426088` | [Scripts/c99426088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99426088.lua) | 1 |
| Nekroz Divinemirror | `50596425` | [Scripts/c50596425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50596425.lua) | 1 |
| Revendread Evolution | `7986397` | [Scripts/c7986397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7986397.lua) | 1 |
| Megalith Phuloch | `8805651` | [Scripts/c8805651.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8805651.lua) | 1 |
| Dogmatikaturgy | `42158279` | [Scripts/c42158279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42158279.lua) | 1 |
| Dogmatikalamity | `31002402` | [Scripts/c31002402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31002402.lua) | 1 |
| Megalith Och | `36849933` | [Scripts/c36849933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36849933.lua) | 1 |
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18988396.lua) | 1 |
| Rise of the Salamangreat | `38784726` | [Scripts/c38784726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38784726.lua) | 1 |
| Megalith Ophiel | `63056220` | [Scripts/c63056220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63056220.lua) | 1 |
| Megalith Unformed | `69003792` | [Scripts/c69003792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69003792.lua) | 1 |
| Underworld Ritual of Prediction | `8428836` | [Scripts/c8428836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8428836.lua) | 1 |
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90444325.lua) | 1 |
| Fire Formation - Domei | `93754402` | [Scripts/c93754402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93754402.lua) | 1 |
| ...and 12 more |  |  |  |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
		if not mat then goto cancel end
		tc:SetMaterial(mat)
		Duel.ReleaseRitualMaterial(mat)
		Duel.BreakEffect()
		Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
```

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
		tc:SetMaterial(mat)
		if not mc:IsLocation(LOCATION_EXTRA) then
			Duel.ReleaseRitualMaterial(mat)
		else
			Duel.SendtoGrave(mat,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)
```

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
			if not mat then goto cancel end
			tc:SetMaterial(mat)
			Duel.ReleaseRitualMaterial(mat)
		else
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
```
