# Auxiliary.FilterBoolFunction

## Signature

```lua
Auxiliary.FilterBoolFunction(function f, ... any) -> void
```

## Description

Returns a filter function that calls f(target, ...) with the extra arguments captured now.
Use this when another API expects a one-argument Card filter but the real filter needs fixed extra values.

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/utility.lua:466`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **859** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.FilterBoolFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 68 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 66 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua) | 62 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 62 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 61 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua) | 59 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59934749.lua) | 59 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 58 |
| Gem-Knight Phantom Quartz | `24484270` | [Scripts/c24484270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24484270.lua) | 58 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 57 |
| ...and 835 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1cd),2,true)
	--splimit
	local e0=Effect.CreateEffect(c)
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
function s.initial_effect(c)
	--fusion material
	aux.AddFusionProcFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0xaf),2,true)
	c:EnableReviveLimit()
	--fusion
```

### Invoked Sorath (`43989315`)

Source: [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1e1),aux.FilterBoolFunction(Card.IsFusionAttribute,ATTRIBUTE_FIRE+ATTRIBUTE_WIND),true)
	--disable
	local e1=Effect.CreateEffect(c)
```
