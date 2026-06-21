# Auxiliary.AddFusionProcMix

## Signature

```lua
Auxiliary.AddFusionProcMix(Card fcard, bool sub, bool insf, ... number|function|table) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 of each card in the additional parameters as Fusion Materials; additional parameters can be function or card code (int code), where passing a code is equivalent to passing function(code) return c:IsFusionCode(code) end
sub indicates whether Fusion Substitute Materials can be used; insf=false means the Fusion Summon must use the specified materials. If this monster can only be Fusion Summoned with the specified cards, both sub and insf must be false

## Parameters

- `fcard` `Card`
- `sub` `bool` - Can be fusion summoned with substitute material
- `insf` `bool` - Can be fusion summoned with no material (Instant Fusion)
- `...` `number|function|table`

## Source

- `Utilities/procedure.lua:862`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcMix`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 63 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 52 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13331639.lua) | 50 |
| Despian Proskenion | `18666161` | [Scripts/c18666161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18666161.lua) | 45 |
| Coordius the Triphasic Dealmon | `70219023` | [Scripts/c70219023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70219023.lua) | 42 |
| The Dragon that Devours the Dogma | `76666602` | [Scripts/c76666602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76666602.lua) | 40 |
| Ritual Beast Ulti-Gaiapelio | `56655675` | [Scripts/c56655675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56655675.lua) | 29 |

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
