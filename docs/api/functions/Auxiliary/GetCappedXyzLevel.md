# Auxiliary.GetCappedXyzLevel

## Signature

```lua
Auxiliary.GetCappedXyzLevel(Card c) -> void
```

## Description

Returns c's current Level, capped at MAX_XYZ_LEVEL.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1528`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetCappedXyzLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Satellarknight Capella | `86466163` | [Scripts/c86466163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86466163.lua) | 1 |

## Script Examples

### Satellarknight Capella (`86466163`)

Source: [Scripts/c86466163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86466163.lua)

```lua
end
function c86466163.xyzlv(e,c,rc)
	return 0x30050000|aux.GetCappedXyzLevel(c)
end
```
