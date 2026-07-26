# Card.GetRank

## Signature

```lua
Card.GetRank(Card c) -> int
```

## Description

Returns c's current Rank.
Non-Xyz cards return 0. Xyz Monsters outside the Monster Zone return their original Rank; in the Monster Zone, Rank-changing effects are applied and the result is at least 1.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3409`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **99** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetRank`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 58 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 58 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88504133.lua) | 57 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 55 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 55 |
| Raider's Knight | `28781003` | [Scripts/c28781003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28781003.lua) | 54 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36224040.lua) | 53 |
| Rank-Up-Magic Numeron Force | `48333324` | [Scripts/c48333324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48333324.lua) | 53 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 52 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 52 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 51 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50797682.lua) | 51 |
| Rank-Up-Magic Argent Chaos Force | `94220427` | [Scripts/c94220427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94220427.lua) | 50 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 49 |
| Tellarknight Ptolemaeus | `18326736` | [Scripts/c18326736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18326736.lua) | 49 |
| Sharv Sarga | `75728539` | [Scripts/c75728539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75728539.lua) | 49 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 49 |
| Xyz Revive Splash | `32764863` | [Scripts/c32764863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32764863.lua) | 49 |
| Infernoid Seitsemas | `51316684` | [Scripts/c51316684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51316684.lua) | 49 |
| Rank-Up-Magic Barian's Force | `47660516` | [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua) | 49 |
| Rank-Down-Magic Numeron Fall | `71345905` | [Scripts/c71345905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71345905.lua) | 48 |
| Outrigger Extension | `96462121` | [Scripts/c96462121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96462121.lua) | 48 |
| ...and 75 more |  |  |  |

## Script Examples

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
	return c:IsFaceup() and c:IsType(TYPE_XYZ)
		and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_XMATERIAL)
		and Duel.IsExistingMatchingCard(c49082032.spfilter2,tp,LOCATION_EXTRA,0,1,nil,e,tp,c,c:GetRace(),c:GetRank()+1)
end
function c49082032.spfilter2(c,e,tp,mc,race,rk)
```

### Rank-Up-Magic Astral Force (`45950291`)

Source: [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua)

```lua
end
function c45950291.cfilter(c,rk)
	return c:IsFaceup() and c:GetRank()>rk
end
function c45950291.filter1(c,e,tp)
```

### Grandpa Demetto (`44190146`)

Source: [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
	e:SetLabelObject(rc)
	local dmg=rc:GetRank()*300
	Duel.SetTargetCard(rc)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
```
