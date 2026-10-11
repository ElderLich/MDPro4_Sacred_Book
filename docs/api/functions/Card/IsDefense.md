# Card.IsDefense

## Signature

```lua
Card.IsDefense(Card c, int def1, [int def2], [... int]) -> bool
```

## Description

Checks whether c is not a Link Monster, is a monster or currently treated as one, and has current DEF equal to any supplied def value.
Nil def arguments are skipped. Unlike the old imported text, the binding does not explicitly require c to be in the Monster Zone.

## Parameters

- `c` `Card`
- `def1` `int`
- `def2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3546`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **99** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsDefense) with `Card.IsDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 1 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 1 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 1 |
| Jiaotu, Darkness of the Yang Zing | `25935625` | [Scripts/c25935625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25935625.lua) | 1 |
| Kuriboh - Multiply! | `14965712` | [Scripts/c14965712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14965712.lua) | 1 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 1 |
| Box of Friends | `81587028` | [Scripts/c81587028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81587028.lua) | 1 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 2 |
| Nightmare Throne | `93729896` | [Scripts/c93729896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729896.lua) | 1 |
| Possessed Partnerships | `65046521` | [Scripts/c65046521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65046521.lua) | 1 |
| Gizmek Inaba, the Hopping Hare of Hakuto | `50901852` | [Scripts/c50901852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50901852.lua) | 1 |
| Mannadium Prime-Heart | `90465153` | [Scripts/c90465153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90465153.lua) | 1 |
| Garbage Golem | `28968609` | [Scripts/c28968609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28968609.lua) | 2 |
| Demiurge Ema | `26364381` | [Scripts/c26364381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26364381.lua) | 1 |
| Spiritual Art Familiars | `45538320` | [Scripts/c45538320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45538320.lua) | 1 |
| Branded in High Spirits | `29948294` | [Scripts/c29948294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29948294.lua) | 1 |
| Antidote Nurse | `31539614` | [Scripts/c31539614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31539614.lua) | 1 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 1 |
| Mannadium Breakheart | `71164684` | [Scripts/c71164684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71164684.lua) | 1 |
| Regenesis | `31786838` | [Scripts/c31786838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31786838.lua) | 1 |
| Replicard LAD | `1665819` | [Scripts/c1665819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1665819.lua) | 1 |
| ...and 75 more |  |  |  |

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
