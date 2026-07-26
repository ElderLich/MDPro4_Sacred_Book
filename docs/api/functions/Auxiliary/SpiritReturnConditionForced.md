# Auxiliary.SpiritReturnConditionForced

## Signature

```lua
Auxiliary.SpiritReturnConditionForced(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the mandatory Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does not have the optional-return permission effect.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Returns

- `bool` - true if the mandatory Spirit return effect should apply.

## Source

- `Utilities/utility.lua:200`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SpiritReturnConditionForced`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua) | 1 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua) | 1 |
| Sacred Spirit of the Ice Barrier | `44877690` | [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua) | 1 |

## Script Examples

### Shinobaroness Peacock (`25415052`)

Source: [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua)

```lua
	e1:SetCountLimit(1)
	e1:SetReset(RESET_EVENT+0x1ee0000+RESET_PHASE+PHASE_END)
	e1:SetCondition(aux.SpiritReturnConditionForced)
	e1:SetTarget(c25415052.rettg)
	e1:SetOperation(c25415052.retop)
```

### Shinobaron Peacock (`52900000`)

Source: [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua)

```lua
	e1:SetCountLimit(1)
	e1:SetReset(RESET_EVENT+0x1ee0000+RESET_PHASE+PHASE_END)
	e1:SetCondition(aux.SpiritReturnConditionForced)
	e1:SetTarget(c52900000.rettg)
	e1:SetOperation(c52900000.retop)
```

### Sacred Spirit of the Ice Barrier (`44877690`)

Source: [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua)

```lua
	if Duel.IsExistingMatchingCard(c44877690.cfilter,tp,LOCATION_MZONE,0,1,e:GetHandler()) then return false end
	if e:IsHasType(EFFECT_TYPE_TRIGGER_F) then
		return aux.SpiritReturnConditionForced(e,tp,eg,ep,ev,re,r,rp)
	else
		return aux.SpiritReturnConditionOptional(e,tp,eg,ep,ev,re,r,rp)
```
