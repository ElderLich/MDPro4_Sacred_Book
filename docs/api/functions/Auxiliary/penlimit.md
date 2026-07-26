# Auxiliary.penlimit

## Signature

```lua
Auxiliary.penlimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon condition helper that returns true only when st contains SUMMON_TYPE_PENDULUM.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:2305`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.penlimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mayosenju Hitot | `21364070` | [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua) | 1 |
| Mayosenju Daibak | `93368494` | [Scripts/c93368494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93368494.lua) | 1 |

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
