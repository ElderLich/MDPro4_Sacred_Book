# Auxiliary.TargetBoolFunction

## Signature

```lua
Auxiliary.TargetBoolFunction(function f, ... any) -> function
```

## Description

Returns an effect target callback that calls f(target, ...) with the extra arguments captured now.
Use this when SetTarget or similar APIs expect a function with parameters (effect, target).

## Parameters

- `f` `function`
- `...` `any`

## Returns

- `function` - A target callback with parameters (effect, target).

## Source

- `Utilities/utility.lua:454`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **415** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.TargetBoolFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38572779.lua) | 56 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 55 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 55 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua) | 53 |
| Mementomictlan | `43338320` | [Scripts/c43338320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43338320.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53054164.lua) | 52 |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua) | 51 |
| Qliphort Disk | `64496451` | [Scripts/c64496451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64496451.lua) | 50 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 50 |
| Salamangreat Burst Gryphon | `10140443` | [Scripts/c10140443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10140443.lua) | 50 |
| Legendary Lord Six Samurai - Enishi | `70634245` | [Scripts/c70634245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70634245.lua) | 50 |
| The Bystial Alba Los | `69120785` | [Scripts/c69120785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69120785.lua) | 50 |
| DoomZ Destruction | `80320877` | [Scripts/c80320877.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80320877.lua) | 50 |
| D/D/D Super Doom King Dark Armageddon | `18897163` | [Scripts/c18897163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18897163.lua) | 49 |
| Concours de Cuisine (Culinary Confrontation) | `14283055` | [Scripts/c14283055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14283055.lua) | 49 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 49 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17269895.lua) | 48 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 48 |
| Tri-Brigade Kitt | `56196385` | [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua) | 48 |
| Primite Lordly Lode | `56506740` | [Scripts/c56506740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56506740.lua) | 48 |
| ...and 391 more |  |  |  |

## Script Examples

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
	e2:SetRange(LOCATION_SZONE)
	e2:SetTargetRange(LOCATION_MZONE,0)
	e2:SetTarget(aux.TargetBoolFunction(Card.IsType,TYPE_XYZ))
	e2:SetValue(800)
	c:RegisterEffect(e2)
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
	e1:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
	e1:SetTargetRange(LOCATION_ONFIELD,0)
	e1:SetTarget(aux.TargetBoolFunction(Card.IsType,TYPE_SPELL+TYPE_TRAP))
	e1:SetValue(aux.indoval)
	e1:SetReset(RESET_PHASE+PHASE_END)
```

### Miscellaneousaurus (`38572779`)

Source: [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38572779.lua)

```lua
	e1:SetCode(EFFECT_IMMUNE_EFFECT)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetTarget(aux.TargetBoolFunction(Card.IsRace,RACE_DINOSAUR))
	e1:SetValue(c38572779.efilter)
	if Duel.GetCurrentPhase()==PHASE_MAIN1 then
```
