# Duel.GetRitualMaterial

## Signature

```lua
Duel.GetRitualMaterial(int player) -> Group
```

## Description

Returns the cards player can use as basic Ritual Material.
The group includes cards in the hand or field that can be Tributed, plus Ritual-material exceptions such as suitable cards in the Graveyard.
This is only the starting pool. After a Ritual Monster is chosen, filter the group with Card.IsCanBeRitualMaterial and then perform the exact or greater-or-equal material total check.

## Parameters

- `player` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4997`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetRitualMaterial) with `Duel.GetRitualMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 2 |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua) | 2 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36982581.lua) | 2 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59514116.lua) | 2 |
| Magikey Duo | `51510279` | [Scripts/c51510279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51510279.lua) | 1 |
| Blessing of the Voiceless Voice | `39114494` | [Scripts/c39114494.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39114494.lua) | 2 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20071842.lua) | 2 |
| Magikey Maftea | `99426088` | [Scripts/c99426088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99426088.lua) | 2 |
| Nekroz Divinemirror | `50596425` | [Scripts/c50596425.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50596425.lua) | 2 |
| Revendread Evolution | `7986397` | [Scripts/c7986397.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7986397.lua) | 2 |
| Megalith Phuloch | `8805651` | [Scripts/c8805651.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8805651.lua) | 2 |
| Dogmatikaturgy | `42158279` | [Scripts/c42158279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42158279.lua) | 2 |
| Dogmatikalamity | `31002402` | [Scripts/c31002402.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31002402.lua) | 2 |
| Megalith Och | `36849933` | [Scripts/c36849933.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36849933.lua) | 2 |
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18988396.lua) | 2 |
| Rise of the Salamangreat | `38784726` | [Scripts/c38784726.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38784726.lua) | 2 |
| Megalith Ophiel | `63056220` | [Scripts/c63056220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63056220.lua) | 2 |
| Megalith Unformed | `69003792` | [Scripts/c69003792.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69003792.lua) | 2 |
| Underworld Ritual of Prediction | `8428836` | [Scripts/c8428836.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8428836.lua) | 2 |
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90444325.lua) | 2 |
| Fire Formation - Domei | `93754402` | [Scripts/c93754402.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93754402.lua) | 1 |
| Ravenous Vendread | `13386407` | [Scripts/c13386407.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13386407.lua) | 2 |
| Archfiend's Usurpation | `82997779` | [Scripts/c82997779.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82997779.lua) | 2 |
| High Ritual Art | `36350300` | [Scripts/c36350300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36350300.lua) | 2 |
| ...and 6 more |  |  |  |

## Script Examples

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
		local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
		if ft<0 then return false end
		local mg=Duel.GetRitualMaterial(tp)
		if ft>0 then
			local mg2=Duel.GetMatchingGroup(c51124303.mfilter,tp,LOCATION_EXTRA,0,nil)
```

### Sonic Tracker (`17888577`)

Source: [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua)

```lua
function c17888577.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local mg=Duel.GetRitualMaterial(tp)
		return Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,c17888577.filter,e,tp,mg,nil,Card.GetLevel,"Greater")
	end
```

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
function c36982581.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local mg1=Duel.GetRitualMaterial(tp)
		local mg2=Duel.GetReleaseGroup(1-tp,false,REASON_EFFECT):Filter(c36982581.cfilter,nil,e,1-tp)
		return Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,c36982581.rfilter1,e,tp,mg1,nil,Card.GetLevel,"Equal")
```
