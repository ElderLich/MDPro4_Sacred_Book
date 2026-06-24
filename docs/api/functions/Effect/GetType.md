# Effect.GetType

## Signature

```lua
Effect.GetType(Effect e) -> int
```

## Description

Returns e's effect type mask, such as EFFECT_TYPE_SINGLE, EFFECT_TYPE_FIELD, or EFFECT_TYPE_TRIGGER_O.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:633`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **247** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.GetType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 63 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 62 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 61 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Cyberse Sage | `65037172` | [Scripts/c65037172.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65037172.lua) | 59 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 58 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 56 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55749927.lua) | 56 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua) | 55 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 55 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 54 |
| Sosei Ryu-Ge Mistva | `92487128` | [Scripts/c92487128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92487128.lua) | 54 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| The Continuing Epic of Charles | `11802691` | [Scripts/c11802691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11802691.lua) | 54 |
| Ryu-Ge Rivalry | `81549048` | [Scripts/c81549048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81549048.lua) | 54 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 53 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Witchcrafter Pupils | `69964858` | [Scripts/c69964858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69964858.lua) | 52 |
| Virtual World Roshi - Laolao | `86483512` | [Scripts/c86483512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86483512.lua) | 51 |
| ...and 223 more |  |  |  |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.RitualUltimateFilter(c,filter,e,tp,m1,m2,attack_function,greater_or_equal,chk)
	if bit.band(c:GetType(),0x81)~=0x81 or (filter and not filter(c,e,tp,chk)) or not c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true) then return false end
	local mg=m1:Filter(Card.IsCanBeRitualMaterial,c,c)
	if m2 then
```

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
end
function c97769122.cpfilter(c)
	return c:GetType()==TYPE_SPELL and c:IsSetCard(0x175) and c:IsAbleToGraveAsCost()
		and c:CheckActivateEffect(true,true,false)~=nil
end
```

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
function c51124303.spfilter(c,e,tp,mc)
	local mg=Group.FromCards(mc)
	return c:IsSetCard(0xb4) and bit.band(c:GetType(),0x81)==0x81 and (not c.mat_filter or c.mat_filter(mc,tp)) and (not c.mat_group_check or c.mat_group_check(mg,tp))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true)
		and mc:IsCanBeRitualMaterial(c)
```
