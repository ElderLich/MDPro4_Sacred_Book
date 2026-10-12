# Auxiliary.EffectCategoryFilter

## Signature

```lua
Auxiliary.EffectCategoryFilter(int category) -> function
```

## Description

Returns a predicate that checks whether an Effect has category.

## Parameters

- `category` `int`

## Returns

- `function`

## Source

- `Utilities/utility.lua:2024`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EffectCategoryFilter) with `Auxiliary.EffectCategoryFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30964246.lua) | 1 |

## Script Examples

### Argostars - Giantslaying (`30964246`)

Source: [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30964246.lua)

```lua
	return c:IsAllTypes(TYPE_CONTINUOUS|TYPE_TRAP) and c:IsFaceup() and
		(c:IsLocation(LOCATION_MZONE) or
			c:IsEffectProperty(aux.EffectCategoryFilter(CATEGORY_SPECIAL_SUMMON)) and
			(c:GetOriginalLevel()>0
			or bit.band(c:GetOriginalRace(),0x3fffffff)~=0
```
