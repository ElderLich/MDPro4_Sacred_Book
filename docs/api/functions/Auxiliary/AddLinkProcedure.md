# Auxiliary.AddLinkProcedure

## Signature

```lua
Auxiliary.AddLinkProcedure(Card c, function|nil f, int min, [int max], [function|nil gf]) -> Effect
```

## Description

Registers the standard Link Summon procedure for c and returns the created Effect.
f filters each Link Material, min/max constrain the number of selected material cards, and gf optionally checks the selected group as a whole.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_LINK, uses Auxiliary.GetLinkCount to match the Link Rating, records materials with Card.SetMaterial, and sends them to the GY with REASON_MATERIAL+REASON_LINK.

## Parameters

- `c` `Card` - Link Monster receiving the procedure.
- `f` `function|nil` - Optional per-material filter. nil means no extra filter beyond normal Link Material legality.
- `min` `int` - Minimum number of material cards that must be selected.
- `max` `int` optional - Maximum number of material cards. Defaults to c:GetLink() when omitted.
- `gf` `function|nil` optional - Optional whole-group validator called as gf(selected_group, link_monster, player).

## Returns

- `Effect` - The registered Special Summon procedure effect.

## Source

- `Utilities/procedure.lua:2128`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **469** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddLinkProcedure) with `Auxiliary.AddLinkProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua) | 1 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 1 |
| Gem-Knight Phantom Quartz | `24484270` | [Scripts/c24484270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24484270.lua) | 1 |
| The Weather Painter Moonbow | `95515518` | [Scripts/c95515518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515518.lua) | 1 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 1 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58004362.lua) | 1 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 1 |
| ...and 445 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
	--link summon
	c:EnableReviveLimit()
	--aux.AddLinkProcedure(c,s.mfilter,2,3,s.glcheck)
	local e0=Effect.CreateEffect(c)
	e0:SetDescription(aux.Stringid(id,0))
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
	--link summon
	c:EnableReviveLimit()
	--aux.AddLinkProcedure(c,nil,3,4,s.glcheck)
	local e0=Effect.CreateEffect(c)
	e0:SetDescription(aux.Stringid(id,0))
```

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.AddLinkProcedure(c,nil,2,2,s.lcheck)
	c:EnableReviveLimit()
	--
```
