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

- Detected in **865** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.FilterBoolFunction) with `Auxiliary.FilterBoolFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua) | 2 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43989315.lua) | 2 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua) | 2 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87746184.lua) | 1 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42125140.lua) | 2 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua) | 2 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8690387.lua) | 1 |
| [Stars Align Above the Shrine](/examples/cards/15306543) | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 2 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83793721.lua) | 2 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7382007.lua) | 1 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44097050.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| ...and 841 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1cd),2,true)
	--splimit
	local e0=Effect.CreateEffect(c)
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
function s.initial_effect(c)
	--fusion material
	aux.AddFusionProcFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0xaf),2,true)
	c:EnableReviveLimit()
	--fusion
```

### Mixousia the Confounder (`80843006`)

Source: [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua)

```lua
	c:EnableReviveLimit()
	--material
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsRace,RACE_SPELLCASTER),aux.FilterBoolFunction(aux.NOT(Card.IsRace),RACE_SPELLCASTER),true)
	--attr change
	local e1=Effect.CreateEffect(c)
```
