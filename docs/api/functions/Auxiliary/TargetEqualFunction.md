# Auxiliary.TargetEqualFunction

## Signature

```lua
Auxiliary.TargetEqualFunction(function f, any value, ... any) -> void
```

## Description

Used in effect registration, returns a function with a bool return type; additional parameters start from the third parameter
function Auxiliary.TargetEqualFunction(f, value, ...)
  local ext_params={...}
  return function(effect,target)
    return f(target,table.unpack(ext_params))==value
  end
end

## Parameters

- `f` `function`
- `value` `any`
- `...` `any`

## Source

- `Utilities/utility.lua:448`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.TargetEqualFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| Owner's Seal | `9720537` | [Scripts/c9720537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9720537.lua) | 35 |

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
