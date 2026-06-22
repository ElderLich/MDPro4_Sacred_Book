# Auxiliary.IsMaterialListCode

## Signature

```lua
Auxiliary.IsMaterialListCode(Card c, int code) -> bool|nil
```

## Description

Checks whether code is present in c.material, normally populated by AddMaterialCodeList; returns true or nil.

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `bool|nil`

## Source

- `Utilities/utility.lua:512`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **44** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsMaterialListCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua) | 59 |
| Overload Future Fusion | `33099732` | [Scripts/c33099732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33099732.lua) | 58 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 57 |
| Ultimate Fusion | `71143015` | [Scripts/c71143015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71143015.lua) | 56 |
| Contact Gate | `41933425` | [Scripts/c41933425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41933425.lua) | 52 |
| Branded Fusion | `44362883` | [Scripts/c44362883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44362883.lua) | 52 |
| Neos Fusion | `14088859` | [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14088859.lua) | 49 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 49 |
| Fusion Draft | `55158350` | [Scripts/c55158350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55158350.lua) | 49 |
| Destruction Swordsman Fusion | `41940225` | [Scripts/c41940225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41940225.lua) | 49 |
| Branded Retribution | `17751597` | [Scripts/c17751597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17751597.lua) | 48 |
| Keeper of Dragon Magic | `48048590` | [Scripts/c48048590.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48048590.lua) | 48 |
| Xtra HERO Infernal Devicer | `19324993` | [Scripts/c19324993.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19324993.lua) | 45 |
| Branded Expulsion | `1041278` | [Scripts/c1041278.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1041278.lua) | 45 |
| Springans Call! | `83199011` | [Scripts/c83199011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83199011.lua) | 43 |
| Springans Merrymaker | `48285768` | [Scripts/c48285768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48285768.lua) | 42 |
| The Golden Swordsoul | `82489470` | [Scripts/c82489470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82489470.lua) | 40 |
| XYZ Hyper Cannon | `21723081` | [Scripts/c21723081.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21723081.lua) | 40 |
| Brightest, Blazing, Branded King | `19271881` | [Scripts/c19271881.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19271881.lua) | 40 |
| Springans Kitt | `45484331` | [Scripts/c45484331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45484331.lua) | 38 |
| The Eye of Timaeus | `1784686` | [Scripts/c1784686.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1784686.lua) | 38 |
| Decisive Battle of Golgonda | `70485614` | [Scripts/c70485614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70485614.lua) | 37 |
| ...and 20 more |  |  |  |

## Script Examples

### The Gaze of Timaeus (`22283204`)

Source: [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua)

```lua
end
function s.fusfilter(c,e,tp,code,mc)
	return c:IsType(TYPE_FUSION) and aux.IsMaterialListCode(c,code)
		and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0 and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)
end
```

### Ojamassimilation (`2390019`)

Source: [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua)

```lua
end
function c2390019.spfilter(c,e,tp,fc)
	return aux.IsMaterialListCode(fc,c:GetCode()) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c2390019.fselect(cg,tp,tg)
```

### Overload Future Fusion (`33099732`)

Source: [Scripts/c33099732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33099732.lua)

```lua
end
function s.sfilter(c,tc)
	return aux.IsMaterialListCode(tc,c:GetCode()) and c:IsAbleToGrave()
end
function s.tgtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
