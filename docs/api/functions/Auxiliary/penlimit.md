# Auxiliary.penlimit

## Signature

```lua
Auxiliary.penlimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Pendulum Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.penlimit(e, se, sp, st)
  return st&SUMMON_TYPE_PENDULUM==SUMMON_TYPE_PENDULUM
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2305`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.penlimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mayosenju Hitot | `21364070` | [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua) | 46 |
| Mayosenju Daibak | `93368494` | [Scripts/c93368494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93368494.lua) | 38 |

## Script Examples

### Mayosenju Hitot (`21364070`)

Source: [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua)

```lua
	e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e3:SetCode(EFFECT_SPSUMMON_CONDITION)
	e3:SetValue(aux.penlimit)
	c:RegisterEffect(e3)
	--tohand
```

### Mayosenju Daibak (`93368494`)

Source: [Scripts/c93368494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93368494.lua)

```lua
	e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e3:SetCode(EFFECT_SPSUMMON_CONDITION)
	e3:SetValue(aux.penlimit)
	c:RegisterEffect(e3)
	--cannot disable
```
