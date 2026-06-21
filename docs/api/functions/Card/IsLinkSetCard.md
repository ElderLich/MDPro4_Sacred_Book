# Card.IsLinkSetCard

## Signature

```lua
Card.IsLinkSetCard(Card c, ... int) -> bool
```

## Description

Check if card c, when used as Link Material, can be treated as a card with setname in its name

## Parameters

- `c` `Card`
- `...` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3397`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **131** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua) | 59 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Gem-Knight Phantom Quartz | `24484270` | [Scripts/c24484270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24484270.lua) | 58 |
| The Weather Painter Moonbow | `95515518` | [Scripts/c95515518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515518.lua) | 57 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 56 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 55 |
| Prank-Kids Dodo-Doodle-Doo | `17382973` | [Scripts/c17382973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17382973.lua) | 55 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 53 |
| Overburst Dragon | `15627227` | [Scripts/c15627227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15627227.lua) | 53 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Ritual Beast Ulti-Kimunfalcos | `58811192` | [Scripts/c58811192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58811192.lua) | 51 |
| X-Krawler Qualiark | `92781606` | [Scripts/c92781606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92781606.lua) | 51 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Wind-Up Zenmaintenance | `1735088` | [Scripts/c1735088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1735088.lua) | 51 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua) | 51 |
| D/D/D Abyss King Gilgamesh | `9024198` | [Scripts/c9024198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9024198.lua) | 50 |
| Sky Striker Ace = Zero | `76072561` | [Scripts/c76072561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76072561.lua) | 50 |
| Paleozoic Cambroraster | `36346532` | [Scripts/c36346532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36346532.lua) | 50 |
| Tri-Brigade Bearbrumm the Rampant Rampager | `47163170` | [Scripts/c47163170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47163170.lua) | 49 |
| Marincess Coral Triangle | `84546257` | [Scripts/c84546257.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84546257.lua) | 49 |
| Zerrziel, Ruler of the Evil Eyed | `17739335` | [Scripts/c17739335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17739335.lua) | 48 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 48 |
| Quadborrel Dragon | `29296344` | [Scripts/c29296344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29296344.lua) | 48 |
| ...and 107 more |  |  |  |

## Script Examples

### Radiant Typhoon Varuroon, the Marine Eidolon (`39341885`)

Source: [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,5318639)
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkSetCard,0x1d1),2,2)
	c:EnableReviveLimit()
	--to hand
```

### Gouki Sheik Ogre (`7382007`)

Source: [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua)

```lua
	--link summon
	c:EnableReviveLimit()
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkSetCard,0xfc),2,2)
	--special summon
	local e1=Effect.CreateEffect(c)
```

### Prank-Kids Bow-Wow-Bark (`43886072`)

Source: [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua)

```lua
	--link summon
	c:EnableReviveLimit()
	aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkSetCard,0x120),2,2)
	--atk gain
	local e1=Effect.CreateEffect(c)
```
