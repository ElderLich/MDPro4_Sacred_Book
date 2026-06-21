# Card.IsLinkAttribute

## Signature

```lua
Card.IsLinkAttribute(Card c, int attribute, [int player]) -> bool
```

## Description

Check if card c, when used as Link Material \[for a Link Summon by player\], has Attribute attribute

## Parameters

- `c` `Card`
- `attribute` `int`
- `player` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3496`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **56** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 68 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57134592.lua) | 53 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 53 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87871125.lua) | 52 |
| Harpie Conductor | `85696777` | [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua) | 50 |
| Fiendsmith's Requiem | `2463794` | [Scripts/c2463794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2463794.lua) | 50 |
| Hi-Speedroid Rubber Band Shooter | `72813401` | [Scripts/c72813401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72813401.lua) | 49 |
| Salamangreat Pyro Phoenix | `31313405` | [Scripts/c31313405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31313405.lua) | 49 |
| Marincess Wonder Heart | `94207108` | [Scripts/c94207108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94207108.lua) | 49 |
| Miasma Necromancer | `69176851` | [Scripts/c69176851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69176851.lua) | 47 |
| Breachborrel Dragon | `90011273` | [Scripts/c90011273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90011273.lua) | 47 |
| Marincess Aqua Argonaut | `20934852` | [Scripts/c20934852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20934852.lua) | 46 |
| Ancient Warriors Oath - Double Dragon Lords | `65711558` | [Scripts/c65711558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65711558.lua) | 46 |
| Galaxy-Eyes Solflare Dragon | `3356494` | [Scripts/c3356494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3356494.lua) | 46 |
| Marincess Great Bubble Reef | `47910940` | [Scripts/c47910940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47910940.lua) | 46 |
| Ancient Gear Ballista | `10547580` | [Scripts/c10547580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10547580.lua) | 46 |
| G Golem Invalid Dolmen | `24151924` | [Scripts/c24151924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24151924.lua) | 46 |
| X-Krawler Synaphysis | `39998992` | [Scripts/c39998992.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39998992.lua) | 45 |
| Salamangreat Heatleo | `41463181` | [Scripts/c41463181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41463181.lua) | 45 |
| Dillingerous Dragon | `23732205` | [Scripts/c23732205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23732205.lua) | 44 |
| Ukanomitsune-no-Onari | `49451215` | [Scripts/c49451215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49451215.lua) | 44 |
| Fiendsmith's Agnumday | `32991300` | [Scripts/c32991300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32991300.lua) | 44 |
| Trisborrel Dragon | `3957130` | [Scripts/c3957130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3957130.lua) | 44 |
| ...and 32 more |  |  |  |

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

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.matfilter(c)
	return c:IsLinkAttribute(ATTRIBUTE_LIGHT) and c:IsLinkRace(RACE_BEAST) and c:IsLevelBelow(4)
end
function s.stfilter(c,tp)
```

### Salamangreat Raging Phoenix (`57134592`)

Source: [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57134592.lua)

```lua
end
function s.matfilter(c)
	return c:IsLinkType(TYPE_EFFECT) and c:IsLinkAttribute(ATTRIBUTE_FIRE)
end
function s.valcheck(e,c)
```
