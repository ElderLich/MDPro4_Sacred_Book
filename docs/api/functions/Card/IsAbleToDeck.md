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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3640`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **615** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToDeck) with `Card.IsAbleToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 2 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 2 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua) | 2 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 1 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66518509.lua) | 1 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua) | 2 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65514302.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16306932.lua) | 2 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74586817.lua) | 3 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37517035.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua) | 3 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83528184.lua) | 5 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42125140.lua) | 3 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22283204.lua) | 2 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Witchcrafter Celebration | `6958567` | [Scripts/c6958567.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6958567.lua) | 1 |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c572850.lua) | 1 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36982581.lua) | 2 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2390019.lua) | 1 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78397661.lua) | 4 |
| ...and 591 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
end
function s.filter0(c)
	return c:IsType(TYPE_MONSTER) and c:IsAbleToDeck()
end
function s.filter1(c,e)
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.filter0(c,e)
	return c:IsLocation(LOCATION_MZONE) and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToDeck() and not c:IsImmuneToEffect(e)
end
function s.filter1(c,e)
```

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
end
function s.filter0(c,e)
	return c:IsLocation(LOCATION_MZONE) and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToDeck() and not c:IsImmuneToEffect(e)
end
function s.filter1(c,e)
```
