# Card.GetCounter

## Signature

```lua
Card.GetCounter(Card c, int countertype) -> int
```

## Description

Returns counters on c for countertype.
When countertype is 0, this core returns the number of different counter types currently present on c, not the total number of all counters.

## Parameters

- `c` `Card`
- `countertype` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3685`

## Guided Examples

Learn how to use this function in context:

- [Counters](/learn/counters)
- [Applying The Latest Engine And Script Changes](/learn/engine-updates)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **123** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetCounter) with `Card.GetCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3611830.lua) | 4 |
| Veda Kalarcanum | `40785230` | [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40785230.lua) | 1 |
| Predaplanet | `51858200` | [Scripts/c51858200.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51858200.lua) | 1 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Bunny Ear Enthusiast | `39643167` | [Scripts/c39643167.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39643167.lua) | 2 |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39000945.lua) | 3 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30432463.lua) | 1 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73218989.lua) | 1 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Predaplant Daredevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82370493.lua) | 3 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2606417.lua) | 2 |
| Predaplant Chlamydosundew | `89181134` | [Scripts/c89181134.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89181134.lua) | 3 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24104865.lua) | 1 |
| Enneapolis | `17621695` | [Scripts/c17621695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17621695.lua) | 2 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27104921.lua) | 1 |
| Corrosive Scales | `13235258` | [Scripts/c13235258.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13235258.lua) | 1 |
| Zushin the Sleeping Giant | `67547370` | [Scripts/c67547370.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67547370.lua) | 1 |
| Cubic Causality | `38606913` | [Scripts/c38606913.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38606913.lua) | 2 |
| Alien Shocktrooper M-Frame | `74974229` | [Scripts/c74974229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74974229.lua) | 1 |
| Predaplant Longinephila | `44994712` | [Scripts/c44994712.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44994712.lua) | 2 |
| Vaalmonica Ereditare | `14972952` | [Scripts/c14972952.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14972952.lua) | 2 |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77751766.lua) | 1 |
| Endymion, the Master Magician | `40732515` | [Scripts/c40732515.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40732515.lua) | 1 |
| Aiza the Dragoness of Deranged Devotion | `63378869` | [Scripts/c63378869.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63378869.lua) | 2 |
| ...and 99 more |  |  |  |

## Script Examples

### Endymion, the Mighty Master of Magic (`3611830`)

Source: [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3611830.lua)

```lua
end
function c3611830.thfilter(c)
	return c:GetCounter(0x1)>0 and c:IsAbleToHand()
end
function c3611830.negtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Veda Kalarcanum (`40785230`)

Source: [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40785230.lua)

```lua
end
function c40785230.scval(e,c)
	return c:GetCounter(0x69)
end
function c40785230.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Predaplanet (`51858200`)

Source: [Scripts/c51858200.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51858200.lua)

```lua
}
function c51858200.cfilter(c)
	return c:IsLocation(LOCATION_MZONE) and c:GetCounter(0x1041)>0
end
function c51858200.regop(e,tp,eg,ep,ev,re,r,rp)
```
