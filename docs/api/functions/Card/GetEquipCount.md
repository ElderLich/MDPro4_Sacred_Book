# Card.GetEquipCount

## Signature

```lua
Card.GetEquipCount(Card c) -> int
```

## Description

Returns the number of Equip Cards currently equipped to c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3518`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetEquipCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 56 |
| Full Armored Dark Knight Lancer | `67630394` | [Scripts/c67630394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67630394.lua) | 47 |
| Cyberdark Inferno | `44352516` | [Scripts/c44352516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44352516.lua) | 46 |
| Zaralaam the Dark Palace | `64230128` | [Scripts/c64230128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64230128.lua) | 46 |
| Jupiter the Power Patron of Destruction | `68231287` | [Scripts/c68231287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68231287.lua) | 46 |
| Forest of Lost Flowers | `91228233` | [Scripts/c91228233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91228233.lua) | 43 |
| Thunder Discharge | `27623932` | [Scripts/c27623932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27623932.lua) | 43 |
| Yellow Dragon Ninja | `90247311` | [Scripts/c90247311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90247311.lua) | 42 |
| Infernoble Knight Turpin | `89809665` | [Scripts/c89809665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89809665.lua) | 41 |
| DMZ Dragon | `98371278` | [Scripts/c98371278.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98371278.lua) | 41 |
| Ultimate Great Insect | `87804747` | [Scripts/c87804747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804747.lua) | 41 |
| Fateful Adventure | `39568067` | [Scripts/c39568067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39568067.lua) | 40 |
| Cocoon of Ultra Evolution | `77840540` | [Scripts/c77840540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77840540.lua) | 38 |
| Fire Lake of the Burning Abyss | `36006208` | [Scripts/c36006208.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36006208.lua) | 38 |
| Angelica's Angelic Ring | `40678060` | [Scripts/c40678060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40678060.lua) | 37 |
| Maha Vailo, Light of the Heavens | `45796834` | [Scripts/c45796834.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45796834.lua) | 35 |
| Heavenly Gate of the Mikanko | `17255673` | [Scripts/c17255673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17255673.lua) | 33 |
| Dark Highlander | `75326861` | [Scripts/c75326861.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75326861.lua) | 33 |
| Soul Devouring Bamboo Sword | `51670553` | [Scripts/c51670553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51670553.lua) | 33 |
| Trismagistus | `61159609` | [Scripts/c61159609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61159609.lua) | 32 |
| Heritage of the Chalice | `51412776` | [Scripts/c51412776.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51412776.lua) | 29 |
| Flint Missile | `16437822` | [Scripts/c16437822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16437822.lua) | 28 |
| Vylon Vanguard | `87836938` | [Scripts/c87836938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87836938.lua) | 23 |
| Really Eternal Rest | `28121403` | [Scripts/c28121403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28121403.lua) | 14 |
| ...and 5 more |  |  |  |

## Script Examples

### Emperor Charles the Great (`97864322`)

Source: [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua)

```lua
end
function s.matfilter(c)
	return c:IsLevel(9) and c:IsLinkCode(77656797) and c:GetEquipCount()>0
end
function s.copycon(e)
```

### Full Armored Dark Knight Lancer (`67630394`)

Source: [Scripts/c67630394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67630394.lua)

```lua
end
function s.atkval(e,c)
	return (c:GetOverlayCount()+c:GetEquipCount())*300
end
function s.thfilter(c)
```

### Cyberdark Inferno (`44352516`)

Source: [Scripts/c44352516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44352516.lua)

```lua
end
function c44352516.indestg(e,c)
	return c:IsSetCard(0x4093) and c:IsType(TYPE_EFFECT) and c:GetEquipCount()>0
end
function c44352516.filter(c)
```
