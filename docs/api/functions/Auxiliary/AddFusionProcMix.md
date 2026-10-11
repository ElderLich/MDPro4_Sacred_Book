# Auxiliary.AddFusionProcMix

## Signature

```lua
Auxiliary.AddFusionProcMix(Card fcard, bool sub, bool insf, ... int|function|table) -> void
```

## Description

Registers a fixed-count mixed Fusion Material procedure on fcard.
Each extra argument is a required material slot and may be a card code, filter function, or table of alternatives. Numeric material slots update listed-material metadata.

## Parameters

- `fcard` `Card`
- `sub` `bool`
- `insf` `bool`
- `...` `int|function|table`

## Source

- `Utilities/procedure.lua:862`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddFusionProcMix) with `Auxiliary.AddFusionProcMix`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 1 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13331639.lua) | 1 |
| Despian Proskenion | `18666161` | [Scripts/c18666161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18666161.lua) | 1 |
| Coordius the Triphasic Dealmon | `70219023` | [Scripts/c70219023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70219023.lua) | 1 |
| The Dragon that Devours the Dogma | `76666602` | [Scripts/c76666602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76666602.lua) | 1 |
| Ritual Beast Ulti-Gaiapelio | `56655675` | [Scripts/c56655675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56655675.lua) | 1 |

## Script Examples

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcMix(c,false,true,s.fusfilter1,s.fusfilter2,s.fusfilter3,s.fusfilter4)
	aux.AddContactFusionProcedure(c,s.fsmfiler(c),LOCATION_MZONE+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_SPSUMMON)
	aux.EnablePendulumAttribute(c,false)
```

### Odd-Eyes Arcray Dragon (`6218704`)

Source: [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua)

```lua
	--fusion summon
	c:EnableReviveLimit()
	aux.AddFusionProcMix(c,false,true,c6218704.fusfilter1,c6218704.fusfilter2,c6218704.fusfilter3,c6218704.fusfilter4)
	--pendulum summon
	aux.EnablePendulumAttribute(c,false)
```

### Master Spirit Tech Force - Pendulum Ruler (`68508433`)

Source: [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcMix(c,true,true,s.matfilter1,s.matfilter2)
	aux.EnablePendulumAttribute(c,false)
	--Pendulum Effect
```
