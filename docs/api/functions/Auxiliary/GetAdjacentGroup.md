# Auxiliary.GetAdjacentGroup

## Signature

```lua
Auxiliary.GetAdjacentGroup(int tp, int location1, int location2, int i, int j) -> Group
```

## Description

Returns cards from location1/location2 that are orthogonally adjacent to the global field coordinate (i, j).

## Parameters

- `tp` `int`
- `location1` `int`
- `location2` `int`
- `i` `int`
- `j` `int`

## Returns

- `Group`

## Source

- `Utilities/utility.lua:698`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetAdjacentGroup) with `Auxiliary.GetAdjacentGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gold Pride - Nytro Blaster | `58884063` | [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58884063.lua) | 1 |

## Script Examples

### Gold Pride - Nytro Blaster (`58884063`)

Source: [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58884063.lua)

```lua
			return
		end
		local cg=aux.GetAdjacentGroup(tp,LOCATION_ONFIELD,LOCATION_ONFIELD,row,column)
		if Duel.GetLP(tp)<Duel.GetLP(1-tp) and #cg>0 and Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
			Duel.BreakEffect()
```
