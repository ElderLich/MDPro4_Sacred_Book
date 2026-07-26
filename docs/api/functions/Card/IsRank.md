# Card.IsRank

## Signature

```lua
Card.IsRank(Card c, int rank1, [int rank2], [... int]) -> bool
```

## Description

Checks whether c:GetRank() equals any supplied rank value.
Nil rank arguments are skipped. The binding compares the numeric Rank directly; it does not separately require c to be an Xyz Monster, so non-Xyz cards compare as Rank 0.

## Parameters

- `c` `Card`
- `rank1` `int`
- `rank2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3491`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **106** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRank`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 1 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua) | 1 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 1 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 1 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 1 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 1 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 1 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 1 |
| Raider's Knight | `28781003` | [Scripts/c28781003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28781003.lua) | 1 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36224040.lua) | 1 |
| Rank-Up-Magic Numeron Force | `48333324` | [Scripts/c48333324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48333324.lua) | 1 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 1 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 1 |
| K9-LC Release Restraint | `27308231` | [Scripts/c27308231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27308231.lua) | 1 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 1 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 1 |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30350202.lua) | 1 |
| Dark Rebellion Xyz Dragon of the Four Heavenly Dragons | `90091224` | [Scripts/c90091224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90091224.lua) | 1 |
| Rank-Up-Magic Argent Chaos Force | `94220427` | [Scripts/c94220427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94220427.lua) | 1 |
| Tellarknight Ptolemaeus | `18326736` | [Scripts/c18326736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18326736.lua) | 1 |
| Xyz Revive Splash | `32764863` | [Scripts/c32764863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32764863.lua) | 1 |
| Materiactor Meltdown | `38669664` | [Scripts/c38669664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38669664.lua) | 1 |
| Rank-Up-Magic Barian's Force | `47660516` | [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua) | 1 |
| ...and 82 more |  |  |  |

## Script Examples

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
end
function c49082032.spfilter2(c,e,tp,mc,race,rk)
	return c:IsRace(race) and c:IsRank(rk) and c:IsSetCard(0x1048,0x1073) and mc:IsCanBeXyzMaterial(c)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
end
```

### Power Patron DoomZ (`81650695`)

Source: [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua)

```lua
end
function s.spfilter(c,e,tp,mc)
	return c:IsRank(mc:GetLevel()) and (c:IsSetCard(0x1d2) or c:IsCode(68231287)) and c:IsAllTypes(TYPE_XYZ+TYPE_MONSTER)
		and mc:IsCanBeXyzMaterial(c) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false)
		and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
```

### Rank-Up-Magic Astral Force (`45950291`)

Source: [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua)

```lua
function c45950291.filter2(c,e,tp,mc,rk,rc,att,code)
	if c:GetOriginalCode()==6165656 and code~=48995978 then return false end
	return c:IsRank(rk) and c:IsRace(rc) and c:IsAttribute(att) and mc:IsCanBeXyzMaterial(c)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false)
		and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
```
