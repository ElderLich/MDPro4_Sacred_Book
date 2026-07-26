# Auxiliary.AddContactFusionProcedure

## Signature

```lua
Auxiliary.AddContactFusionProcedure(Card c, function filter, [int self_location], [int opponent_location], function mat_operation, ... any) -> Effect
```

## Description

Registers a Contact Fusion Special Summon procedure on c, using material filter locations and the provided material operation, and returns the created procedure effect.

## Parameters

- `c` `Card`
- `filter` `function`
- `self_location` `int` optional
- `opponent_location` `int` optional
- `mat_operation` `function`
- `...` `any`

## Returns

- `Effect` - The created Contact Fusion procedure effect.

## Source

- `Utilities/procedure.lua:1687`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **64** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddContactFusionProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 1 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 1 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Ritual Beast Ulti-Cannahawk | `48063985` | [Scripts/c48063985.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48063985.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 1 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Gladiator Beast Claudius | `48958757` | [Scripts/c48958757.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48958757.lua) | 1 |
| Gate Guardian of Water and Thunder | `97783338` | [Scripts/c97783338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97783338.lua) | 1 |
| Gladiator Beast Andabata | `3779662` | [Scripts/c3779662.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3779662.lua) | 1 |
| Supreme King Dragon Starving Venom | `43387895` | [Scripts/c43387895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43387895.lua) | 1 |
| Gate Guardians Combined | `8505920` | [Scripts/c8505920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8505920.lua) | 1 |
| Ritual Beast Ulti-Apelio | `86274272` | [Scripts/c86274272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86274272.lua) | 1 |
| Gladiator Beast Domitianus | `33652635` | [Scripts/c33652635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33652635.lua) | 1 |
| Gladiator Beast Tamer Editor | `30864377` | [Scripts/c30864377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30864377.lua) | 1 |
| Necroquip Princess | `93860227` | [Scripts/c93860227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93860227.lua) | 1 |
| Trishula, the Dragon of Icy Imprisonment | `15661378` | [Scripts/c15661378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15661378.lua) | 1 |
| Secret Six Samurai - Rihan | `33964637` | [Scripts/c33964637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33964637.lua) | 1 |
| Gladiator Beast Nerokius | `29357956` | [Scripts/c29357956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29357956.lua) | 1 |
| Timaeus the Knight of Destiny | `53315891` | [Scripts/c53315891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53315891.lua) | 1 |
| Meizen the Battle Ninja | `11825276` | [Scripts/c11825276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11825276.lua) | 1 |
| ...and 40 more |  |  |  |

## Script Examples

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
	c:EnableReviveLimit()
	aux.AddFusionProcMix(c,false,true,s.fusfilter1,s.fusfilter2,s.fusfilter3,s.fusfilter4)
	aux.AddContactFusionProcedure(c,s.fsmfiler(c),LOCATION_MZONE+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_SPSUMMON)
	aux.EnablePendulumAttribute(c,false)
	--splimit
```

### XYZ-Hyper Dragon Cannon (`75748977`)

Source: [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua)

```lua
	c:EnableReviveLimit()
	aux.AddFusionProcCode3(c,70860415,6355563,33744268,true,true)
	aux.AddContactFusionProcedure(c,Card.IsAbleToRemoveAsCost,LOCATION_ONFIELD+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_COST)
	--
	local e0=Effect.CreateEffect(c)
```

### Arktos XII - Chronochasm Vaylantz (`50687050`)

Source: [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua)

```lua
	aux.EnablePendulumAttribute(c,false)
	aux.AddFusionProcFunRep(c,s.matfilter,2,true)
	aux.AddContactFusionProcedure(c,aux.FilterBoolFunction(Card.IsReleasable,REASON_SPSUMMON),LOCATION_MZONE,0,Duel.Release,REASON_SPSUMMON+REASON_MATERIAL)
	c:EnableReviveLimit()
	--spsummon condition
```
