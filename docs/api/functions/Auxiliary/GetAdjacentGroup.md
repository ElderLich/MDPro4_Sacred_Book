# Auxiliary.GetAdjacentGroup

## Signature

```lua
Auxiliary.GetAdjacentGroup(int tp, int location1, int location2, int i, int j) -> Group
```

## Description

Get the card group adjacent to (i,j)

## Parameters

- `tp` `int`
- `location1` `int`
- `location2` `int`
- `i` `int`
- `j` `int`

## Returns

- `Group`

## Source

- `Utilities/utility.lua:695`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetAdjacentGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gold Pride - Nytro Blaster | `58884063` | [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58884063.lua) | 47 |

## Script Examples

### Gold Pride - Nytro Blaster (`58884063`)

Source: [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58884063.lua)

```lua
			return
		end
		local cg=aux.GetAdjacentGroup(tp,LOCATION_ONFIELD,LOCATION_ONFIELD,row,column)
		if Duel.GetLP(tp)<Duel.GetLP(1-tp) and #cg>0 and Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
			Duel.BreakEffect()
```
