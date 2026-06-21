# Card.IsRankBelow

## Signature

```lua
Card.IsRankBelow(Card c, int rank) -> bool
```

## Description

Check whether c is below the rank rank (at least 1)

## Parameters

- `c` `Card`
- `rank` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3614`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRankBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Galaxy-Eyes Cipher X Dragon | `28346136` | [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28346136.lua) | 54 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 52 |
| Hyper-Rank-Up-Magic Ultimate Force | `87818869` | [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua) | 51 |
| Hyper Rank-Up-Magic Utopiforce | `67517351` | [Scripts/c67517351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67517351.lua) | 49 |
| Tailwind of Gusto | `1187243` | [Scripts/c1187243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1187243.lua) | 49 |
| Xyz Revive Splash | `32764863` | [Scripts/c32764863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32764863.lua) | 49 |
| Rank-Down-Magic Numeron Fall | `71345905` | [Scripts/c71345905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71345905.lua) | 48 |
| Virtual World Gate - Chuche | `13364097` | [Scripts/c13364097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13364097.lua) | 47 |
| Raidraptor - Revolution Falcon - Air Raid | `79985120` | [Scripts/c79985120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79985120.lua) | 46 |
| Madolche Puddingcess Chocolat-a-la-Mode | `44311445` | [Scripts/c44311445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44311445.lua) | 46 |
| Eclipse Twins | `45852939` | [Scripts/c45852939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45852939.lua) | 44 |
| Full Armored Utopic Ray Lancer | `1269512` | [Scripts/c1269512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1269512.lua) | 38 |
| Reincarnation of the Seventh Emperors | `57499304` | [Scripts/c57499304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57499304.lua) | 37 |
| Dragon Gate | `9567495` | [Scripts/c9567495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9567495.lua) | 35 |
| Cat Shark | `84224627` | [Scripts/c84224627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84224627.lua) | 35 |
| Bahamut Shark | `440556` | [Scripts/c440556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c440556.lua) | 28 |
| Xyz Xtreme !! | `57319935` | [Scripts/c57319935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57319935.lua) | 26 |
| Downerd Magician | `72167543` | [Scripts/c72167543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72167543.lua) | 19 |
| Blind Obliteration | `22802010` | [Scripts/c22802010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22802010.lua) | 17 |
| Planckton | `10282757` | [Scripts/c10282757.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10282757.lua) | 16 |

## Script Examples

### Galaxy-Eyes Cipher X Dragon (`28346136`)

Source: [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28346136.lua)

```lua
end
function c28346136.filter(c)
	return c:IsType(TYPE_XYZ) and c:IsRankBelow(9) and c:IsRace(RACE_DRAGON) and c:IsAbleToExtra()
end
function c28346136.tg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Number 93: Utopia Kaiser (`23187256`)

Source: [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua)

```lua
end
function c23187256.filter(c,e,tp)
	return c:IsRankBelow(9) and c:IsAttackBelow(3000) and c:IsSetCard(0x48)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

### Hyper-Rank-Up-Magic Ultimate Force (`87818869`)

Source: [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua)

```lua
end
function s.filter1(c,e,tp)
	return c:IsFaceup() and c:IsSetCard(0x7f) and c:IsType(TYPE_XYZ) and c:IsRankBelow(9) and c:GetOriginalAttribute()&ATTRIBUTE_LIGHT~=0
		and Duel.IsExistingMatchingCard(s.filter2,tp,LOCATION_EXTRA,0,1,nil,e,tp,c)
		and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_XMATERIAL)
```
