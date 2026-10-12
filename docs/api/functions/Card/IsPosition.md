# Card.IsPosition

## Signature

```lua
Card.IsPosition(Card c, int pos) -> bool
```

## Description

Checks whether c's current battle position includes pos.

## Parameters

- `c` `Card`
- `pos` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3660`

## Guided Examples

Learn how to use this function in context:

- [Battle Position Effects](/learn/battle-position-effects)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **225** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsPosition) with `Card.IsPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62002838.lua) | 1 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37192109.lua) | 1 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |
| Performage Trapeze Magician | `17016362` | [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17016362.lua) | 1 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13204145.lua) | 2 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33103459.lua) | 4 |
| Arbitration of White | `57964143` | [Scripts/c57964143.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57964143.lua) | 1 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19743887.lua) | 1 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68987122.lua) | 1 |
| D/D/D Super Doom King Purple Armageddon | `84569886` | [Scripts/c84569886.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84569886.lua) | 3 |
| Mermail Abyssbalaen | `75180828` | [Scripts/c75180828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75180828.lua) | 1 |
| The Undying Legion | `43355214` | [Scripts/c43355214.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43355214.lua) | 1 |
| Melffy Mommy | `76833149` | [Scripts/c76833149.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76833149.lua) | 2 |
| WAKE CUP! Macchia | `71410542` | [Scripts/c71410542.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71410542.lua) | 1 |
| Dice Roll Battle | `88482761` | [Scripts/c88482761.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88482761.lua) | 2 |
| Gagaga Escape | `9591819` | [Scripts/c9591819.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9591819.lua) | 1 |
| Rocket Hand | `13317419` | [Scripts/c13317419.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13317419.lua) | 2 |
| Digital Bug Corebage | `58600555` | [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58600555.lua) | 1 |
| Kagero the Cannon Ninja | `20065259` | [Scripts/c20065259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20065259.lua) | 1 |
| Zubababa Knight | `62006866` | [Scripts/c62006866.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62006866.lua) | 1 |
| GMX Chairman Kimridge | `56034579` | [Scripts/c56034579.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56034579.lua) | 2 |
| Riot's Reason | `51612489` | [Scripts/c51612489.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51612489.lua) | 1 |
| Mermail Abyssleed | `37781520` | [Scripts/c37781520.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37781520.lua) | 1 |
| Heart of Gaia | `73129314` | [Scripts/c73129314.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73129314.lua) | 1 |
| ...and 201 more |  |  |  |

## Script Examples

### Dark End Evaporation Dragon (`62002838`)

Source: [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62002838.lua)

```lua
end
function s.atkfilter(c)
	return c:IsFaceup() and c:IsPosition(POS_ATTACK)
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### PSY-Framelord Zeta (`37192109`)

Source: [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37192109.lua)

```lua
end
function c37192109.rmfilter(c)
	return c:IsPosition(POS_FACEUP_ATTACK) and c:IsAbleToRemove()
		and c:IsSummonType(SUMMON_TYPE_SPECIAL)
end
```

### Magical Hats (`81210420`)

Source: [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua)

```lua
end
function c81210420.filter(c)
	return c:GetSequence()<5 and (c:IsPosition(POS_FACEDOWN_DEFENSE) or c:IsCanTurnSet())
end
function c81210420.spfilter(c,e,tp)
```
