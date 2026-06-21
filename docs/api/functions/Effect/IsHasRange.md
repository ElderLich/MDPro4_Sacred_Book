# Effect.IsHasRange

## Signature

```lua
Effect.IsHasRange(Effect e, int range) -> bool
```

## Description

Checks whether the effect includes range.

## Parameters

- `e` `Effect`
- `range` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:653`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.IsHasRange`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Liberator Eto | `24643913` | [Scripts/c24643913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24643913.lua) | 31 |

## Script Examples

### Liberator Eto (`24643913`)

Source: [Scripts/c24643913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24643913.lua)

```lua
end
function s.quick_filter(e)
	return (e:GetCode()==EVENT_CHAINING or e:GetCode()==EVENT_BECOME_TARGET) and e:IsHasType(EFFECT_TYPE_QUICK_O+EFFECT_TYPE_QUICK_F) and e:IsHasRange(LOCATION_HAND+LOCATION_MZONE)
end
function s.cfilter(c)
```
