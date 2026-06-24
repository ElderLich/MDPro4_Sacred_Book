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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3493`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **137** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 68 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59934749.lua) | 59 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 58 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58004362.lua) | 56 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97273514.lua) | 56 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 54 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| Unchained Soul Rage Abominator | `21419436` | [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21419436.lua) | 53 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 53 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11674673.lua) | 53 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua) | 52 |
| Tri-Brigade Rugal the Silver Sheller | `52331012` | [Scripts/c52331012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52331012.lua) | 51 |
| Unchained Soul Lord of Yama | `24269961` | [Scripts/c24269961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24269961.lua) | 51 |
| Mermail Abyssalacia | `23545031` | [Scripts/c23545031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23545031.lua) | 50 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua) | 50 |
| Thunder Dragon Thunderstormech | `12081875` | [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12081875.lua) | 50 |
| Endymion, the Crescent Magistus | `20714553` | [Scripts/c20714553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20714553.lua) | 50 |
| Protector of The Agents - Moon | `90290572` | [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90290572.lua) | 50 |
| Fiendsmith's Requiem | `2463794` | [Scripts/c2463794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2463794.lua) | 50 |
| Clockwork Knight | `41739381` | [Scripts/c41739381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41739381.lua) | 49 |
| Aromalilith Rosemary | `30989084` | [Scripts/c30989084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30989084.lua) | 49 |
| ...and 113 more |  |  |  |

## Script Examples

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
end
function s.mfilter(c)
	return c:IsLinkRace(RACE_FIEND) and c:IsLinkAttribute(ATTRIBUTE_LIGHT)
end
function s.filter0(c)
```

### A Bao A Qu, the Lightless Shadow (`4731783`)

Source: [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua)

```lua
end
function s.lcheck(g,lc)
	return g:IsExists(Card.IsLinkRace,1,nil,RACE_FIEND)
end
function s.accon(e,tp,eg,ep,ev,re,r,rp)
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.matfilter(c)
	return c:IsLinkAttribute(ATTRIBUTE_LIGHT) and c:IsLinkRace(RACE_BEAST) and c:IsLevelBelow(4)
end
function s.stfilter(c,tp)
```
