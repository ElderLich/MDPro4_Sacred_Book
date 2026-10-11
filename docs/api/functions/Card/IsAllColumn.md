# Card.IsAllColumn

## Signature

```lua
Card.IsAllColumn(Card c) -> bool
```

## Description

Checks whether c is treated as occupying or applying to all columns.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3481`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAllColumn) with `Card.IsAllColumn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Bingo Card | `99505609` | [Scripts/c99505609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99505609.lua) | 1 |

## Script Examples

### Bingo Card (`99505609`)

Source: [Scripts/c99505609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99505609.lua)

```lua
		return c:GetColumnGroupCount()==4
	end
	return c:IsAllColumn()
end
function s.zonefilter(c)
```
