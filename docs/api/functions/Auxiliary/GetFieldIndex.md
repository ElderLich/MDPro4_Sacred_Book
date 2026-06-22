# Auxiliary.GetFieldIndex

## Signature

```lua
Auxiliary.GetFieldIndex(Card c) -> int,int
```

## Description

Returns c's global row and column indexes from player 0's field viewpoint.

## Parameters

- `c` `Card`

## Returns

- `int`
- `int`

## Source

- `Utilities/utility.lua:670`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetFieldIndex`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gold Pride - Nytro Blaster | `58884063` | [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58884063.lua) | 47 |

## Script Examples

### Gold Pride - Nytro Blaster (`58884063`)

Source: [Scripts/c58884063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58884063.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) and tc:IsType(TYPE_MONSTER) then
		local row,column=aux.GetFieldIndex(tc)
		if Duel.Destroy(tc,REASON_EFFECT)==0 or row<0 or column<0 then
			return
```
