# Card.IsAbleToDeck

## Signature

```lua
Card.IsAbleToDeck(Card c) -> bool
```

## Description

Checks whether c can be returned to the Deck.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3585`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **598** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 75 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 71 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 68 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 68 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 67 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua) | 65 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 63 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83528184.lua) | 62 |
| [Ecclesia and the Dark Dragon](/examples/cards/78397661) | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 61 |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua) | 59 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua) | 59 |
| Tearlaments Havnis | `37961969` | [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua) | 58 |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua) | 58 |
| ...and 574 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
end
function s.filter0(c)
	return c:IsType(TYPE_MONSTER) and c:IsAbleToDeck()
end
function s.filter1(c,e)
```

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.filter0(c,e)
	return c:IsLocation(LOCATION_MZONE) and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToDeck() and not c:IsImmuneToEffect(e)
end
function s.filter1(c,e)
```

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
end
function s.filter0(c,e)
	return c:IsLocation(LOCATION_MZONE) and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToDeck() and not c:IsImmuneToEffect(e)
end
function s.filter1(c,e)
```
