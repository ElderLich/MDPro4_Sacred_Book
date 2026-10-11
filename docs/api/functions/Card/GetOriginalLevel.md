# Card.GetOriginalLevel

## Signature

```lua
Card.GetOriginalLevel(Card c) -> int
```

## Description

Returns c's original Level from card data, or 0 for Xyz Monsters, Link Monsters, and cards marked with STATUS_NO_LEVEL.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3461`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **121** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetOriginalLevel) with `Card.GetOriginalLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 1 |
| [Cerynemesia, Mystical Beast of the Forest](/examples/cards/43632709) | `43632709` | [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43632709.lua) | 3 |
| [Stars Align Above the Shrine](/examples/cards/15306543) | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Sacred Beasts Combined Assault | `50147815` | [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua) | 1 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 2 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 1 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 1 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 3 |
| Capsule Monster Chess | `24056179` | [Scripts/c24056179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24056179.lua) | 3 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 1 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16719140.lua) | 4 |
| Pendulum Dimension | `84274024` | [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua) | 3 |
| Salamangreat Burst Gryphon | `10140443` | [Scripts/c10140443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10140443.lua) | 1 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 1 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 2 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 2 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39973386.lua) | 3 |
| Void Imagination | `31444249` | [Scripts/c31444249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31444249.lua) | 2 |
| Speedroid Wing Synchron | `2254222` | [Scripts/c2254222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2254222.lua) | 1 |
| ...and 97 more |  |  |  |

## Script Examples

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
		return c:GetRitualLevel(rc)
	else
		return c:GetOriginalLevel()
	end
end
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
		return c:GetRitualLevel(rc)
	else
		return c:GetOriginalLevel()
	end
end
```

### Vidolium the Unstable Power Patron of Unity (`70488851`)

Source: [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua)

```lua
end
function s.atktg(e,c)
	return c:IsSetCard(0x1ce) and c:GetOriginalLevel()==12
end
function s.spfilter2(c)
```
