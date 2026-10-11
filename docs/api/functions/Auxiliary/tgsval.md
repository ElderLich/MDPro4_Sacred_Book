# Auxiliary.tgsval

## Signature

```lua
Auxiliary.tgsval(Effect e, Effect re, int rp) -> bool
```

## Description

Value helper for self-targeting protection; it returns true when the reason player is the handler's player.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:835`

## Guided Examples

Learn how to use this function in context:

- [Negation And Immunity](/learn/negation-and-immunity)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.tgsval) with `Auxiliary.tgsval`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magical Mid-Breaker Field | `71650854` | [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua) | 1 |
| Defense Zone | `59687381` | [Scripts/c59687381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59687381.lua) | 1 |

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
