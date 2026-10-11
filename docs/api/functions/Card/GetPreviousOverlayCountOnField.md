# Card.GetPreviousOverlayCountOnField

## Signature

```lua
Card.GetPreviousOverlayCountOnField(Card c) -> int
```

## Description

Returns the number of cards that were overlaid on c while it was previously on the field.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3506`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousOverlayCountOnField) with `Card.GetPreviousOverlayCountOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Stealth Kragen Spawn | `94942656` | [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua) | 1 |
| Rikka Queen Strenna | `3828844` | [Scripts/c3828844.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3828844.lua) | 1 |
| Number C101: Silent Honor DARK | `12744567` | [Scripts/c12744567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12744567.lua) | 1 |
| Number 79: Battlin' Boxer Nova Kaiser | `71921856` | [Scripts/c71921856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71921856.lua) | 1 |
| Number C1000: Numerounius | `89477759` | [Scripts/c89477759.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89477759.lua) | 1 |
| Number 53: Heart-eartH | `23998625` | [Scripts/c23998625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23998625.lua) | 1 |
| Number C103: Ragnafinity | `20785975` | [Scripts/c20785975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20785975.lua) | 1 |
| Cipher Spectrum | `98905` | [Scripts/c98905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98905.lua) | 1 |

## Script Examples

### Number 4: Stealth Kragen (`67557908`)

Source: [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua)

```lua
function c67557908.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local ct=c:GetPreviousOverlayCountOnField()
	e:SetLabel(ct)
	return c:IsPreviousLocation(LOCATION_MZONE) and c:IsSummonType(SUMMON_TYPE_XYZ) and ct>0
```

### Stealth Kragen Spawn (`94942656`)

Source: [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua)

```lua
function c94942656.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local ct=c:GetPreviousOverlayCountOnField()
	e:SetLabel(ct)
	return c:IsPreviousLocation(LOCATION_MZONE) and c:GetFlagEffect(94942656)>0 and ct>0
```

### Rikka Queen Strenna (`3828844`)

Source: [Scripts/c3828844.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3828844.lua)

```lua
function c3828844.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_MZONE) and c:GetPreviousOverlayCountOnField()>0
end
function c3828844.spfilter(c,e,tp)
```
