# Auxiliary.TargetEqualFunction

## Signature

```lua
Auxiliary.TargetEqualFunction(function f, any value, [... any]) -> function
```

## Description

Returns an effect target-value function that calls f on the target card and extra arguments, then checks whether the result equals value.

## Parameters

- `f` `function`
- `value` `any`
- `...` `any` optional

## Returns

- `function`

## Source

- `Utilities/utility.lua:448`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.TargetEqualFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| Owner's Seal | `9720537` | [Scripts/c9720537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9720537.lua) | 1 |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
	e1:SetTarget(aux.TargetEqualFunction(Card.GetFlagEffect,1,59255742))
	e1:SetLabelObject(tg)
	Duel.RegisterEffect(e1,tp)
```

### Owner's Seal (`9720537`)

Source: [Scripts/c9720537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9720537.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
	e1:SetTarget(aux.TargetEqualFunction(Card.GetFlagEffect,1,9720537))
	e1:SetLabelObject(tg)
	Duel.RegisterEffect(e1,tp)
```
