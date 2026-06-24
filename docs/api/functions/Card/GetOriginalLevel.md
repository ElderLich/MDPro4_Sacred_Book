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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3410`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **116** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOriginalLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| Destruction Chant of the Sacred Beast | `50147815` | [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua) | 59 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 56 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 56 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 53 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 53 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 53 |
| Card 24056179 | `24056179` | [Scripts/c24056179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24056179.lua) | 52 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16719140.lua) | 51 |
| Pendulum Dimension | `84274024` | [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua) | 50 |
| Salamangreat Burst Gryphon | `10140443` | [Scripts/c10140443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10140443.lua) | 50 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 50 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 50 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39973386.lua) | 50 |
| Void Imagination | `31444249` | [Scripts/c31444249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31444249.lua) | 49 |
| Speedroid Wing Synchron | `2254222` | [Scripts/c2254222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2254222.lua) | 48 |
| Titaniklad the Ash Dragon | `41373230` | [Scripts/c41373230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41373230.lua) | 47 |
| Silhouhatte Rabbit | `1528054` | [Scripts/c1528054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1528054.lua) | 47 |
| Jade Dragon Mech | `69191257` | [Scripts/c69191257.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69191257.lua) | 47 |
| Greedy Venom Fusion Dragon | `51570882` | [Scripts/c51570882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51570882.lua) | 47 |
| ...and 92 more |  |  |  |

## Script Examples

### Vidolium the Unstable Power Patron of Unity (`70488851`)

Source: [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua)

```lua
end
function s.atktg(e,c)
	return c:IsSetCard(0x1ce) and c:GetOriginalLevel()==12
end
function s.spfilter2(c)
```

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local atk=tc:GetTextAttack()
	local def=tc:GetTextDefense()
	local lv=tc:GetOriginalLevel()
	local race=tc:GetOriginalRace()
	local att=tc:GetOriginalAttribute()
```

### Destruction Chant of the Sacred Beast (`50147815`)

Source: [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua)

```lua
end
function s.cfilter(c)
	return c:IsFaceup() and c:GetOriginalLevel()==10 and c:IsSetCard(0x1144)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
```
