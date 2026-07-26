# Card.IsRankAbove

## Signature

```lua
Card.IsRankAbove(Card c, int rank) -> bool
```

## Description

Checks whether c has a nonzero Rank greater than or equal to rank.

## Parameters

- `c` `Card`
- `rank` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3618`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRankAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hyper-Rank-Up-Magic Ultimate Force | `87818869` | [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua) | 51 |
| Virtual World Roshi - Laolao | `86483512` | [Scripts/c86483512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86483512.lua) | 51 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 51 |
| Rank-Up-Magic Argent Chaos Force | `94220427` | [Scripts/c94220427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94220427.lua) | 50 |
| Hyper Rank-Up-Magic Utopiforce | `67517351` | [Scripts/c67517351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67517351.lua) | 49 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 49 |
| Tailwind of Gusto | `1187243` | [Scripts/c1187243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1187243.lua) | 49 |
| Rikka Queen Strenna | `3828844` | [Scripts/c3828844.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3828844.lua) | 48 |
| Virtual World Xiezhi - Jiji | `12571621` | [Scripts/c12571621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12571621.lua) | 47 |
| Virtual World Mai-Hime - Lulu | `49088914` | [Scripts/c49088914.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49088914.lua) | 47 |
| Gagaga Illusion | `73496100` | [Scripts/c73496100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73496100.lua) | 47 |
| DoomZ Command "A.D.R.A.S.T.E.I.A." | `84054556` | [Scripts/c84054556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84054556.lua) | 45 |
| Virtual World Kirin - Lili | `49966326` | [Scripts/c49966326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49966326.lua) | 44 |
| Gimmick Puppet Rouge Doll | `63825486` | [Scripts/c63825486.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63825486.lua) | 43 |
| QQ Enneagon | `84673574` | [Scripts/c84673574.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84673574.lua) | 42 |
| Number 27: Dreadnought Dreadnoid | `8387138` | [Scripts/c8387138.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8387138.lua) | 41 |
| Tellarknight Constellar Delteros | `32289031` | [Scripts/c32289031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32289031.lua) | 41 |
| Virtual World Hime - Nyannyan | `8736823` | [Scripts/c8736823.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8736823.lua) | 41 |
| Lyrilusc - Phantom Feathers | `8243121` | [Scripts/c8243121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8243121.lua) | 39 |
| Chronomaly Tuspa Rocket | `2089016` | [Scripts/c2089016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2089016.lua) | 37 |
| Wightprincess | `90243945` | [Scripts/c90243945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90243945.lua) | 36 |
| Yellow-Bellied Oni | `53090623` | [Scripts/c53090623.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53090623.lua) | 36 |
| Virtual World Oto-Hime - Toutou | `20799347` | [Scripts/c20799347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20799347.lua) | 32 |
| Planckton | `10282757` | [Scripts/c10282757.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10282757.lua) | 16 |
| ...and 1 more |  |  |  |

## Script Examples

### Hyper-Rank-Up-Magic Ultimate Force (`87818869`)

Source: [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua)

```lua
end
function s.filter2(c,e,tp,mc)
	return c:IsRankAbove(10) and c:IsSetCard(0x48) and mc:IsCanBeXyzMaterial(c)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
end
```

### Virtual World Roshi - Laolao (`86483512`)

Source: [Scripts/c86483512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86483512.lua)

```lua
end
function c86483512.splimit(e,c)
	return not (c:IsLevelAbove(3) or c:IsRankAbove(3))
end
```

### Shichi-Go-San (`11035075`)

Source: [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua)

```lua
	return function(e)
				local tc=e:GetHandler():GetEquipTarget()
				return tc:IsLevelAbove(lv) or tc:IsRankAbove(lv)
			end
end
```
