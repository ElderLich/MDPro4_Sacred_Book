# Card.IsPosition

## Signature

```lua
Card.IsPosition(Card c, int pos) -> bool
```

## Description

Check whether c is the representation pos

## Parameters

- `c` `Card`
- `pos` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3605`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **222** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 63 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Performage Trapeze Magician | `17016362` | [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17016362.lua) | 56 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 53 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 51 |
| Arbitration of White | `57964143` | [Scripts/c57964143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57964143.lua) | 51 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19743887.lua) | 50 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 47 |
| D/D/D Super Doom King Purple Armageddon | `84569886` | [Scripts/c84569886.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84569886.lua) | 46 |
| Mermail Abyssbalaen | `75180828` | [Scripts/c75180828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75180828.lua) | 46 |
| The Undying Legion | `43355214` | [Scripts/c43355214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43355214.lua) | 46 |
| Melffy Mommy | `76833149` | [Scripts/c76833149.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76833149.lua) | 46 |
| WAKE CUP! Macchia | `71410542` | [Scripts/c71410542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71410542.lua) | 46 |
| Dice Roll Battle | `88482761` | [Scripts/c88482761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88482761.lua) | 45 |
| Gagaga Escape | `9591819` | [Scripts/c9591819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9591819.lua) | 45 |
| Rocket Hand | `13317419` | [Scripts/c13317419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13317419.lua) | 45 |
| Digital Bug Corebage | `58600555` | [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58600555.lua) | 44 |
| Kagero the Cannon Ninja | `20065259` | [Scripts/c20065259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20065259.lua) | 44 |
| Zubababa Knight | `62006866` | [Scripts/c62006866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62006866.lua) | 44 |
| GMX Chairman Kimridge | `56034579` | [Scripts/c56034579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56034579.lua) | 44 |
| Riot's Reason | `51612489` | [Scripts/c51612489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51612489.lua) | 44 |
| Mermail Abyssleed | `37781520` | [Scripts/c37781520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37781520.lua) | 44 |
| Heart of Gaia | `73129314` | [Scripts/c73129314.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73129314.lua) | 43 |
| ...and 198 more |  |  |  |

## Script Examples

### Dark End Evaporation Dragon (`62002838`)

Source: [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua)

```lua
end
function s.atkfilter(c)
	return c:IsFaceup() and c:IsPosition(POS_ATTACK)
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### PSY-Framelord Zeta (`37192109`)

Source: [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua)

```lua
end
function c37192109.rmfilter(c)
	return c:IsPosition(POS_FACEUP_ATTACK) and c:IsAbleToRemove()
		and c:IsSummonType(SUMMON_TYPE_SPECIAL)
end
```

### Magical Hats (`81210420`)

Source: [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua)

```lua
end
function c81210420.filter(c)
	return c:GetSequence()<5 and (c:IsPosition(POS_FACEDOWN_DEFENSE) or c:IsCanTurnSet())
end
function c81210420.spfilter(c,e,tp)
```
