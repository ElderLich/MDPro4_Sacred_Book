# Auxiliary.MonsterEffectPropertyFilter

## Signature

```lua
Auxiliary.MonsterEffectPropertyFilter(int flag) -> function
```

## Description

Returns a predicate that checks whether an Effect has property flag and is not ranged to the Pendulum Zone.

## Parameters

- `flag` `int`

## Returns

- `function`

## Source

- `Utilities/utility.lua:2028`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.MonsterEffectPropertyFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dimension Dice | `47292920` | [Scripts/c47292920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47292920.lua) | 1 |

## Script Examples

### Dimension Dice (`47292920`)

Source: [Scripts/c47292920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47292920.lua)

```lua
end
function c47292920.spfilter(c,e,tp)
	return c:IsType(TYPE_MONSTER) and c:IsEffectProperty(aux.MonsterEffectPropertyFilter(EFFECT_FLAG_DICE))
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```
