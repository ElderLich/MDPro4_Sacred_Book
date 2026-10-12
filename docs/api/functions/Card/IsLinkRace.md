# Card.IsLinkRace

## Signature

```lua
Card.IsLinkRace(Card c, int race, [int player]) -> bool
```

## Description

Checks whether c's Race while used as Link Material for player contains race. player defaults to the current reason player.

## Parameters

- `c` `Card`
- `race` `int`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3548`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **139** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsLinkRace) with `Card.IsLinkRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua) | 2 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44097050.lua) | 1 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51476410.lua) | 1 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58004362.lua) | 1 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21903613.lua) | 1 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48183890.lua) | 1 |
| Unchained Soul Rage Abominator | `21419436` | [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21419436.lua) | 1 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35606858.lua) | 1 |
| Helping Robo for Underwater Combat | `77856460` | [Scripts/c77856460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77856460.lua) | 1 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11674673.lua) | 1 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35306215.lua) | 1 |
| Tri-Brigade Rugal the Silver Sheller | `52331012` | [Scripts/c52331012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52331012.lua) | 1 |
| Unchained Soul Lord of Yama | `24269961` | [Scripts/c24269961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24269961.lua) | 1 |
| Mermail Abyssalacia | `23545031` | [Scripts/c23545031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23545031.lua) | 1 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64454614.lua) | 1 |
| Thunder Dragon Thunderstormech | `12081875` | [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12081875.lua) | 1 |
| Endymion, the Crescent Magistus | `20714553` | [Scripts/c20714553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20714553.lua) | 1 |
| Protector of The Agents - Moon | `90290572` | [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90290572.lua) | 1 |
| Fiendsmith's Requiem | `2463794` | [Scripts/c2463794.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2463794.lua) | 1 |
| ...and 115 more |  |  |  |

## Script Examples

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
end
function s.mfilter(c)
	return c:IsLinkRace(RACE_FIEND) and c:IsLinkAttribute(ATTRIBUTE_LIGHT)
end
function s.filter0(c)
```

### Destratification Dino Stratiae (`3841104`)

Source: [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua)

```lua
end
function s.lcheck(g)
	return g:IsExists(Card.IsLinkRace,1,nil,RACE_DINOSAUR)
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
```

### A Bao A Qu, the Lightless Shadow (`4731783`)

Source: [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua)

```lua
end
function s.lcheck(g,lc)
	return g:IsExists(Card.IsLinkRace,1,nil,RACE_FIEND)
end
function s.accon(e,tp,eg,ep,ev,re,r,rp)
```
