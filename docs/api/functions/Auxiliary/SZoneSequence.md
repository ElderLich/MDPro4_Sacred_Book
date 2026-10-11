# Auxiliary.SZoneSequence

## Signature

```lua
Auxiliary.SZoneSequence(int seq) -> int
```

## Description

Returns the local column for a Spell & Trap Zone sequence from the controller's viewpoint.

## Parameters

- `seq` `int`

## Returns

- `int` - The local column index, or NULL_VALUE for invalid input.

## Source

- `Utilities/utility.lua:725`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SZoneSequence) with `Auxiliary.SZoneSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Broken Line | `88086137` | [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua) | 1 |

## Script Examples

### Broken Line (`88086137`)

Source: [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua)

```lua
	elseif loc&LOCATION_SZONE~=0 then
		if seq>4 then return false end
		col=aux.SZoneSequence(seq)
	else
		return false
```
