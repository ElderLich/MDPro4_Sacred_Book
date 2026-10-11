# Auxiliary.DimensionalFissureTarget

## Signature

```lua
Auxiliary.DimensionalFissureTarget(Effect e, Card c) -> void
```

## Description

Target filter for Dimensional Fissure-style replacement effects. It matches cards whose original type includes Monster, excluding Xyz Materials and cards currently treated as Spell/Trap Cards.

## Parameters

- `e` `Effect`
- `c` `Card`

## Source

- `Utilities/utility.lua:1998`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.DimensionalFissureTarget) with `Auxiliary.DimensionalFissureTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 1 |
| Invoked Oceanus | `6772168` | [Scripts/c6772168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6772168.lua) | 1 |
| Different Dimension Ground | `31849106` | [Scripts/c31849106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31849106.lua) | 1 |
| Dimensional Fissure | `81674782` | [Scripts/c81674782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81674782.lua) | 1 |

## Script Examples

### Awakening of the Sacred Beasts (`53701259`)

Source: [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua)

```lua
end
function c53701259.rmtg(e,c)
	return c:GetOwner()~=e:GetHandlerPlayer() and aux.DimensionalFissureTarget(e,c)
end
function c53701259.rmcon(e)
```

### Invoked Oceanus (`6772168`)

Source: [Scripts/c6772168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6772168.lua)

```lua
end
function s.rmtg(e,c)
	return c:GetOwner()~=e:GetHandlerPlayer() and aux.DimensionalFissureTarget(e,c)
end
function s.filter(c)
```

### Different Dimension Ground (`31849106`)

Source: [Scripts/c31849106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31849106.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE+EFFECT_FLAG_IGNORE_RANGE+EFFECT_FLAG_IGNORE_IMMUNE)
	e1:SetCode(EFFECT_TO_GRAVE_REDIRECT)
	e1:SetTarget(aux.DimensionalFissureTarget)
	e1:SetTargetRange(LOCATION_DECK,LOCATION_DECK)
	e1:SetValue(LOCATION_REMOVED)
```
