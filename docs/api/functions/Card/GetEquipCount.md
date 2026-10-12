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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3573`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **33** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetEquipCount) with `Card.GetEquipCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Tauzenet Wadjet | `73490148` | [Scripts/c73490148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73490148.lua) | 1 |
| D - Burst | `47471667` | [Scripts/c47471667.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47471667.lua) | 1 |
| Zenet-Nakhte Sphinx | `47095439` | [Scripts/c47095439.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47095439.lua) | 1 |
| Full Armored Dark Knight Lancer | `67630394` | [Scripts/c67630394.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67630394.lua) | 1 |
| Cyberdark Inferno | `44352516` | [Scripts/c44352516.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44352516.lua) | 1 |
| Zaralaam the Dark Palace | `64230128` | [Scripts/c64230128.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64230128.lua) | 1 |
| Jupiter the Power Patron of Destruction | `68231287` | [Scripts/c68231287.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68231287.lua) | 1 |
| Zenetmes Nekhbet | `10884847` | [Scripts/c10884847.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10884847.lua) | 1 |
| Forest of Lost Flowers | `91228233` | [Scripts/c91228233.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91228233.lua) | 1 |
| Thunder Discharge | `27623932` | [Scripts/c27623932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27623932.lua) | 1 |
| Yellow Dragon Ninja | `90247311` | [Scripts/c90247311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90247311.lua) | 2 |
| Infernoble Knight Turpin | `89809665` | [Scripts/c89809665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89809665.lua) | 1 |
| DMZ Dragon | `98371278` | [Scripts/c98371278.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98371278.lua) | 1 |
| Ultimate Great Insect | `87804747` | [Scripts/c87804747.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87804747.lua) | 1 |
| Fateful Adventure | `39568067` | [Scripts/c39568067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39568067.lua) | 1 |
| Cocoon of Ultra Evolution | `77840540` | [Scripts/c77840540.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77840540.lua) | 1 |
| Fire Lake of the Burning Abyss | `36006208` | [Scripts/c36006208.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36006208.lua) | 3 |
| Angelica's Angelic Ring | `40678060` | [Scripts/c40678060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40678060.lua) | 2 |
| Maha Vailo, Light of the Heavens | `45796834` | [Scripts/c45796834.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45796834.lua) | 2 |
| Heavenly Gate of the Mikanko | `17255673` | [Scripts/c17255673.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17255673.lua) | 2 |
| Dark Highlander | `75326861` | [Scripts/c75326861.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75326861.lua) | 1 |
| Soul Devouring Bamboo Sword | `51670553` | [Scripts/c51670553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51670553.lua) | 1 |
| Trismagistus | `61159609` | [Scripts/c61159609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61159609.lua) | 1 |
| ...and 9 more |  |  |  |

## Script Examples

### Emperor Charles the Great (`97864322`)

Source: [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua)

```lua
end
function s.matfilter(c)
	return c:IsLevel(9) and c:IsLinkCode(77656797) and c:GetEquipCount()>0
end
function s.copycon(e)
```

### Tauzenet Wadjet (`73490148`)

Source: [Scripts/c73490148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73490148.lua)

```lua
function s.eqcon(e)
	local c=e:GetHandler()
	return c:GetEquipCount()>0
end
function s.cfilter(c)
```

### D - Burst (`47471667`)

Source: [Scripts/c47471667.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47471667.lua)

```lua
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local at=Duel.GetAttacker()
	return (at:GetEquipCount()>0 or at:IsCode(17132130)) and at:IsChainAttackable()
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
```
