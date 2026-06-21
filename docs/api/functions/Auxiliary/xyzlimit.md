# Auxiliary.xyzlimit

## Signature

```lua
Auxiliary.xyzlimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Xyz Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.xyzlimit(e, se, sp, st)
  return st&SUMMON_TYPE_XYZ==SUMMON_TYPE_XYZ
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2301`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.xyzlimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 22: Zombiestein | `73445448` | [Scripts/c73445448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73445448.lua) | 40 |

## Script Examples

### Number 22: Zombiestein (`73445448`)

Source: [Scripts/c73445448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73445448.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.xyzlimit)
	c:RegisterEffect(e1)
	--negate
```
