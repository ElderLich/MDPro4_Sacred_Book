# Auxiliary.AddFusionProcFun2

## Signature

```lua
Auxiliary.AddFusionProcFun2(Card c, function|table f1, function|table f2, bool insf) -> void
```

## Description

Registers a Fusion Summon procedure on c that requires one material satisfying f1 and one material satisfying f2.

## Parameters

- `c` `Card`
- `f1` `function|table`
- `f2` `function|table`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1275`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **143** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddFusionProcFun2) with `Auxiliary.AddFusionProcFun2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80843006.lua) | 1 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 1 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 1 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71159974.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua) | 1 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 1 |
| Destiny HERO - Dusktopia | `93657021` | [Scripts/c93657021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93657021.lua) | 1 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79755671.lua) | 1 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua) | 1 |
| Possessed Destiny - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 1 |
| Predaplant Daredevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82370493.lua) | 1 |
| Witchcrafter Pupils | `69964858` | [Scripts/c69964858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69964858.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Melffys' Joyful Surprise | `79561872` | [Scripts/c79561872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79561872.lua) | 1 |
| Ritual Beast Ulti-Cannahawk | `48063985` | [Scripts/c48063985.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48063985.lua) | 1 |
| Invoked Baybarron | `70383419` | [Scripts/c70383419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70383419.lua) | 1 |
| Borreload Fatalflare Dragon | `84464389` | [Scripts/c84464389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84464389.lua) | 1 |
| Predaplant Chimerafflesia | `25586143` | [Scripts/c25586143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25586143.lua) | 1 |
| Dinomorphia Rexterm | `92798873` | [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua) | 1 |
| ...and 119 more |  |  |  |

## Script Examples

### Mixousia the Confounder (`80843006`)

Source: [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80843006.lua)

```lua
	c:EnableReviveLimit()
	--material
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsRace,RACE_SPELLCASTER),aux.FilterBoolFunction(aux.NOT(Card.IsRace),RACE_SPELLCASTER),true)
	--attr change
	local e1=Effect.CreateEffect(c)
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

### Dracotail Shaulas (`42125140`)

Source: [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua)

```lua
function s.initial_effect(c)
	--fusion material
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1c9),aux.FilterBoolFunction(Card.IsLocation,LOCATION_HAND),true)
	c:EnableReviveLimit()
	--to deck
```
