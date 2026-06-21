# Auxiliary.RitualUltimateFilter

## Signature

```lua
Auxiliary.RitualUltimateFilter(Card c, function|nil filter, Effect e, int tp, Group m1, Group|nil m2, function level_function, string greater_or_equal, bool|nil chk) -> bool
```

## Description

Checks whether c is a valid Ritual Monster that can be Ritual Summoned with the available material groups and the selected Equal or Greater level rule.

## Parameters

- `c` `Card`
- `filter` `function|nil`
- `e` `Effect`
- `tp` `int`
- `m1` `Group`
- `m2` `Group|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `chk` `bool|nil`

## Returns

- `bool` - true if c can be Ritual Summoned.

## Source

- `Utilities/procedure.lua:1825`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.RitualUltimateFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua) | 59 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua) | 59 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 58 |
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
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90444325.lua) | 46 |
| Fire Formation - Domei | `93754402` | [Scripts/c93754402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93754402.lua) | 46 |
| Archfiend's Usurpation | `82997779` | [Scripts/c82997779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82997779.lua) | 46 |
| High Ritual Art | `36350300` | [Scripts/c36350300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36350300.lua) | 44 |
| Forbidden Arts of the Gishki | `28429121` | [Scripts/c28429121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28429121.lua) | 44 |
| Throne of the Archfiends | `63679166` | [Scripts/c63679166.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63679166.lua) | 41 |
| Mitsurugi Ritual | `81560239` | [Scripts/c81560239.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81560239.lua) | 40 |
| Odd-Eyes Advent | `16494704` | [Scripts/c16494704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16494704.lua) | 40 |
| ...and 2 more |  |  |  |

## Script Examples

### Gishki Nekromirror (`36982581`)

Source: [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua)

```lua
		local mg1=Duel.GetRitualMaterial(tp)
		local mg2=Duel.GetReleaseGroup(1-tp,false,REASON_EFFECT):Filter(c36982581.cfilter,nil,e,1-tp)
		return Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,c36982581.rfilter1,e,tp,mg1,nil,Card.GetLevel,"Equal")
			or (mg2:GetCount()>0 and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
				and Duel.IsExistingMatchingCard(c36982581.rfilter2,tp,LOCATION_HAND,0,1,nil,e,tp))
```

### Secrets of Dark Magic (`59514116`)

Source: [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua)

```lua
	aux.RCheckAdditional=c59514116.rcheck
	local res2=mg3:IsExists(Card.IsCode,1,nil,46986414,38033121)
		and Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,aux.TRUE,e,tp,mg3,nil,Card.GetLevel,"Greater")
	aux.RCheckAdditional=nil
	if chk==0 then return res1 or res2 end
```

### Double Interlock (`38129297`)

Source: [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua)

```lua
	aux.RCheckAdditional=s.rcheck
	local rg=Duel.GetMatchingGroup(s.filter2,tp,LOCATION_GRAVE,0,nil,tp)
	local b2=Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,aux.TRUE,e,tp,Group.CreateGroup(),rg,Card.GetLevel,"Greater")
		and (not e:IsCostChecked() or Duel.GetFlagEffect(tp,id+o)==0)
	aux.RCheckAdditional=nil
```
