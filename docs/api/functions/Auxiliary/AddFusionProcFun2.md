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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **139** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcFun2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 66 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71159974.lua) | 59 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 57 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 56 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua) | 54 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| Destiny HERO - Dusktopia | `93657021` | [Scripts/c93657021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93657021.lua) | 54 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79755671.lua) | 54 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua) | 53 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 52 |
| Possessed Resonance - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 52 |
| Predaplant Dheadevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82370493.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| Excited Melffys | `79561872` | [Scripts/c79561872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79561872.lua) | 51 |
| Ritual Beast Ulti-Cannahawk | `48063985` | [Scripts/c48063985.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48063985.lua) | 50 |
| Invoked Babalon | `70383419` | [Scripts/c70383419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70383419.lua) | 50 |
| Borreload Fatalflare Dragon | `84464389` | [Scripts/c84464389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84464389.lua) | 50 |
| Predaplant Chimerafflesia | `25586143` | [Scripts/c25586143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25586143.lua) | 49 |
| Dinomorphia Rexterm | `92798873` | [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua) | 48 |
| Tearlaments Kitkallos | `92731385` | [Scripts/c92731385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92731385.lua) | 48 |
| Hecahands Jauzah | `67021206` | [Scripts/c67021206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67021206.lua) | 48 |
| ...and 115 more |  |  |  |

## Script Examples

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

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
	c:EnableReviveLimit()
	aux.EnablePendulumAttribute(c,false)
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsFusionAttribute,ATTRIBUTE_DARK),aux.FilterBoolFunction(Card.IsFusionType,TYPE_PENDULUM),true)
	--counter
	local e1=Effect.CreateEffect(c)
```
