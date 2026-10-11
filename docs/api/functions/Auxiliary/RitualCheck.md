# Auxiliary.RitualCheck

## Signature

```lua
Auxiliary.RitualCheck(Group g, int tp, Card c, int lv, string greater_or_equal) -> bool
```

## Description

Ritual material group predicate that checks zone availability, the requested Greater/Equal level rule, custom mat_group_check, and RCheckAdditional.

## Parameters

- `g` `Group`
- `tp` `int`
- `c` `Card`
- `lv` `int`
- `greater_or_equal` `string`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:1786`

## Guided Examples

Learn how to use this function in context:

- [Ritual Summon Choices](/learn/ritual-summon-choices)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.RitualCheck) with `Auxiliary.RitualCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 1 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 1 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua) | 1 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua) | 1 |
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
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18988396.lua) | 2 |
| Rise of the Salamangreat | `38784726` | [Scripts/c38784726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38784726.lua) | 1 |
| Megalith Ophiel | `63056220` | [Scripts/c63056220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63056220.lua) | 1 |
| Megalith Unformed | `69003792` | [Scripts/c69003792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69003792.lua) | 2 |
| Underworld Ritual of Prediction | `8428836` | [Scripts/c8428836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8428836.lua) | 2 |
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90444325.lua) | 1 |
| Fire Formation - Domei | `93754402` | [Scripts/c93754402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93754402.lua) | 1 |
| Ravenous Vendread | `13386407` | [Scripts/c13386407.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13386407.lua) | 1 |
| Archfiend's Usurpation | `82997779` | [Scripts/c82997779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82997779.lua) | 1 |
| High Ritual Art | `36350300` | [Scripts/c36350300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36350300.lua) | 1 |
| ...and 6 more |  |  |  |

## Script Examples

### Sonic Tracker (`17888577`)

Source: [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
		aux.GCheckAdditional=aux.RitualCheckAdditional(tc,tc:GetLevel(),"Greater")
		local mat=mg:SelectSubGroup(tp,aux.RitualCheck,true,1,tc:GetLevel(),tp,tc,tc:GetLevel(),"Greater")
		aux.GCheckAdditional=nil
		if not mat then goto cancel end
```

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
			aux.GCheckAdditional=aux.RitualCheckAdditional(tc,tc:GetLevel(),"Equal")
			local mat=mg:SelectSubGroup(tp,aux.RitualCheck,true,1,tc:GetLevel(),tp,tc,tc:GetLevel(),"Equal")
			aux.GCheckAdditional=nil
			if not mat then goto cancel end
```

### Secrets of Dark Magic (`59514116`)

Source: [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua)

```lua
			aux.GCheckAdditional=aux.RitualCheckAdditional(tc,tc:GetLevel(),"Greater")
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
			local mat=mg:SelectSubGroup(tp,aux.RitualCheck,true,1,tc:GetLevel(),tp,tc,tc:GetLevel(),"Greater")
			aux.GCheckAdditional=nil
			if not mat then
```
