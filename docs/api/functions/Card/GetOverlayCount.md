# Card.GetOverlayCount

## Signature

```lua
Card.GetOverlayCount(Card c) -> int
```

## Description

Returns the number of cards currently stacked

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3525`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **82** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOverlayCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 52 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 52 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53054164.lua) | 52 |
| Mimighoul Throne | `42940335` | [Scripts/c42940335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42940335.lua) | 51 |
| Laevatein, Generaider Boss of Shadows | `74615388` | [Scripts/c74615388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74615388.lua) | 49 |
| Bujin Regalia - The Jewel | `63049052` | [Scripts/c63049052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63049052.lua) | 48 |
| Traptrix Pinguicula | `1688285` | [Scripts/c1688285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1688285.lua) | 47 |
| Full Armored Dark Knight Lancer | `67630394` | [Scripts/c67630394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67630394.lua) | 47 |
| Overlay Network | `67378935` | [Scripts/c67378935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67378935.lua) | 47 |
| Melffy Mommy | `76833149` | [Scripts/c76833149.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76833149.lua) | 46 |
| Number 79: Battlin' Boxer Nova Kaiser | `71921856` | [Scripts/c71921856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71921856.lua) | 46 |
| Evoltile Megachirella | `13046291` | [Scripts/c13046291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13046291.lua) | 46 |
| Number C5: Chaos Chimera Dragon | `69757518` | [Scripts/c69757518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69757518.lua) | 46 |
| Number C79: Battlin' Boxer General Kaiser | `10300821` | [Scripts/c10300821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10300821.lua) | 45 |
| Number S38: Titanic Galaxy | `16110708` | [Scripts/c16110708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16110708.lua) | 45 |
| Mereologic Aggregator | `9940036` | [Scripts/c9940036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9940036.lua) | 44 |
| Tantrum Toddler | `7020743` | [Scripts/c7020743.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7020743.lua) | 44 |
| Transcendosaurus Drillygnathus | `30128445` | [Scripts/c30128445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30128445.lua) | 43 |
| Expurrely Happiness | `51822687` | [Scripts/c51822687.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51822687.lua) | 42 |
| Rank-Up-Magic Revolution Force | `43476205` | [Scripts/c43476205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43476205.lua) | 42 |
| Springans Merrymaker | `48285768` | [Scripts/c48285768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48285768.lua) | 42 |
| Cyber Dragon Infinity | `10443957` | [Scripts/c10443957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10443957.lua) | 42 |
| ...and 58 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
end
function s.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_XYZ) and c:GetOverlayCount()>0
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Galaxy-Eyes Photon Dragon (`93717133`)

Source: [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua)

```lua
	local g=Group.FromCards(c,tc)
	local mcount=0
	if tc:IsFaceup() then mcount=tc:GetOverlayCount() end
	if Duel.Remove(g,0,REASON_EFFECT+REASON_TEMPORARY)~=0 then
		local og=Duel.GetOperatedGroup()
```

### Number 93: Utopia Kaiser (`23187256`)

Source: [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua)

```lua
aux.xyz_number[23187256]=93
function c23187256.mfilter(c,xyzc)
	return c:IsXyzType(TYPE_XYZ) and c:IsSetCard(0x48) and c:GetOverlayCount()>0
end
function c23187256.xyzcheck(g)
```
