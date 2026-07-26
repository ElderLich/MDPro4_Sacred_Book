# Card.IsCanBeRitualMaterial

## Signature

```lua
Card.IsCanBeRitualMaterial(Card c, [Card|nil sc]) -> bool
```

## Description

Checks whether c can be used as Ritual Material for sc.
Ritual scripts usually call this after choosing the Ritual Monster, filtering Duel.GetRitualMaterial's result with Card.IsCanBeRitualMaterial so monster-specific material restrictions are respected.
Pass nil for sc only when checking the generic material pool before a specific Ritual Monster is known.

## Parameters

- `c` `Card`
- `sc` `Card|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3644`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanBeRitualMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 63 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua) | 59 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 58 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Magikey Duo | `51510279` | [Scripts/c51510279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51510279.lua) | 57 |
| Blessing of the Voiceless Voice | `39114494` | [Scripts/c39114494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39114494.lua) | 56 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 56 |
| Magikey Maftea | `99426088` | [Scripts/c99426088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99426088.lua) | 55 |
| Nekroz Divinemirror | `50596425` | [Scripts/c50596425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50596425.lua) | 52 |
| Revendread Evolution | `7986397` | [Scripts/c7986397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7986397.lua) | 52 |
| Megalith Phuloch | `8805651` | [Scripts/c8805651.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8805651.lua) | 51 |
| Dogmatikaturgy | `42158279` | [Scripts/c42158279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42158279.lua) | 50 |
| Dogmatikalamity | `31002402` | [Scripts/c31002402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31002402.lua) | 50 |
| Megalith Och | `36849933` | [Scripts/c36849933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36849933.lua) | 49 |
| Rise of the Salamangreat | `38784726` | [Scripts/c38784726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38784726.lua) | 47 |
| Megalith Ophiel | `63056220` | [Scripts/c63056220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63056220.lua) | 47 |
| Megalith Unformed | `69003792` | [Scripts/c69003792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69003792.lua) | 47 |
| Underworld Ritual of Prediction | `8428836` | [Scripts/c8428836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8428836.lua) | 46 |
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90444325.lua) | 46 |
| Fire Formation - Domei | `93754402` | [Scripts/c93754402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93754402.lua) | 46 |
| Ravenous Vendread | `13386407` | [Scripts/c13386407.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13386407.lua) | 46 |
| Archfiend's Usurpation | `82997779` | [Scripts/c82997779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82997779.lua) | 46 |
| ...and 8 more |  |  |  |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
	local tc=tg:GetFirst()
	if tc then
		mg=mg:Filter(Card.IsCanBeRitualMaterial,tc,tc)
		if tc.mat_filter then
			mg=mg:Filter(tc.mat_filter,tc,tp)
```

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
	return c:IsSetCard(0xb4) and bit.band(c:GetType(),0x81)==0x81 and (not c.mat_filter or c.mat_filter(mc,tp)) and (not c.mat_group_check or c.mat_group_check(mg,tp))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true)
		and mc:IsCanBeRitualMaterial(c)
end
function c51124303.rfilter(c,mc)
```

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
	local tc=g:Select(tp,1,1,nil):GetFirst()
	if tc then
		local mg=mg1:Filter(Card.IsCanBeRitualMaterial,tc,tc)
		if tc.mat_filter then
			mg=mg:Filter(tc.mat_filter,tc,tp)
```
