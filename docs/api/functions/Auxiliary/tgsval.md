# Auxiliary.tgsval

## Signature

```lua
Auxiliary.tgsval(Effect e, Effect re, int rp) -> void
```

## Description

Simplified method for the filter function preventing being targeted by your own card effects, used in effect registration for SetValue
function aux.tgsval(e, re, rp)
  return rp==e:GetHandlerPlayer()
end

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:832`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.tgsval`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magical Mid-Breaker Field | `71650854` | [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua) | 23 |
| Defense Zone | `59687381` | [Scripts/c59687381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59687381.lua) | 20 |

## Script Examples

### Magical Mid-Breaker Field (`71650854`)

Source: [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua)

```lua
	local e4=e2:Clone()
	e4:SetTargetRange(0,LOCATION_MZONE)
	e4:SetValue(aux.tgsval)
	c:RegisterEffect(e4)
	local e5=e4:Clone()
```

### Defense Zone (`59687381`)

Source: [Scripts/c59687381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59687381.lua)

```lua
	local e3=e1:Clone()
	e3:SetTargetRange(0,LOCATION_SZONE)
	e3:SetValue(aux.tgsval)
	c:RegisterEffect(e3)
	local e4=e3:Clone()
```
