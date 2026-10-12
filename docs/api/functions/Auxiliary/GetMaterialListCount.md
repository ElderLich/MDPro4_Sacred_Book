# Auxiliary.GetMaterialListCount

## Signature

```lua
Auxiliary.GetMaterialListCount(Card c) -> int,int
```

## Description

Returns c's stored minimum and maximum material counts. If c has no material_count table, returns 0,0.

## Parameters

- `c` `Card`

## Returns

- `int` - Minimum material count.
- `int` - Maximum material count.

## Source

- `Utilities/utility.lua:529`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetMaterialListCount) with `Auxiliary.GetMaterialListCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Neos Fusion | `14088859` | [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14088859.lua) | 1 |

## Script Examples

### Neos Fusion (`14088859`)

Source: [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14088859.lua)

```lua
end
function c14088859.filter2(c,e,tp,m,chkf)
	local min,max=aux.GetMaterialListCount(c)
	return min==2 and max==2 and aux.IsMaterialListCode(c,89943723)
		and c:IsCanBeSpecialSummoned(e,0,tp,true,false) and c:CheckFusionMaterial(m,nil,chkf,true)
```
