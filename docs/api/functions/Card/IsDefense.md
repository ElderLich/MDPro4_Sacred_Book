# Card.IsDefense

## Signature

```lua
Card.IsDefense(Card c, int def, [int atk2], [... int]) -> bool
```

## Description

Check if c's DEF is def1 \[, or def2...\]; returns false if c is not a monster card or not in LOCATION_MZONE

## Parameters

- `c` `Card`
- `def` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3491`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **97** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 54 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 53 |
| Jiaotu, Darkness of the Yang Zing | `25935625` | [Scripts/c25935625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25935625.lua) | 52 |
| Multiplying Kuriboh! | `14965712` | [Scripts/c14965712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14965712.lua) | 51 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 51 |
| Box of Friends | `81587028` | [Scripts/c81587028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81587028.lua) | 50 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 49 |
| Nightmare Throne | `93729896` | [Scripts/c93729896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729896.lua) | 48 |
| Possessed Partnerships | `65046521` | [Scripts/c65046521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65046521.lua) | 48 |
| Gizmek Inaba, the Hopping Hare of Hakuto | `50901852` | [Scripts/c50901852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50901852.lua) | 47 |
| Mannadium Prime-Heart | `90465153` | [Scripts/c90465153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90465153.lua) | 47 |
| Demiurge Ema | `26364381` | [Scripts/c26364381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26364381.lua) | 47 |
| Spiritual Art Familiars | `45538320` | [Scripts/c45538320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45538320.lua) | 46 |
| Branded in High Spirits | `29948294` | [Scripts/c29948294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29948294.lua) | 46 |
| Antidote Nurse | `31539614` | [Scripts/c31539614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31539614.lua) | 45 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 45 |
| Mannadium Breakheart | `71164684` | [Scripts/c71164684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71164684.lua) | 45 |
| Regenesis | `31786838` | [Scripts/c31786838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31786838.lua) | 45 |
| Replicard LAD | `1665819` | [Scripts/c1665819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1665819.lua) | 45 |
| Shiranui Style Samsara | `78765160` | [Scripts/c78765160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78765160.lua) | 45 |
| ...and 73 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
end
function c96570609.spfilter(c,e,tp)
	return c:IsAttackAbove(2400) and c:IsDefense(1000) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c96570609.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
function s.thfilter(c)
	return c:IsSetCard(0xaf) and c:IsType(TYPE_MONSTER)
		and (c:IsAttack(0) or c:IsDefense(0)) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Grandpa Demetto (`44190146`)

Source: [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua)

```lua
end
function c44190146.filter(c,e,tp)
	return c:IsType(TYPE_NORMAL) and (c:IsAttack(0) or c:IsDefense(0)) and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP_DEFENSE)
end
function c44190146.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
