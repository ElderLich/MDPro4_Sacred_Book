# bit.bnot

## Signature

```lua
bit.bnot(int a) -> int
```

## Description

Returns the bitwise NOT of a.

## Parameters

- `a` `int`

## Returns

- `int` - Bitwise NOT of a.

## Source

- `Utilities/utility.lua:30`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=bit.bnot) with `bit.bnot`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54527349.lua) | 1 |
| Disablaster the Negation Fortress | `58707981` | [Scripts/c58707981.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58707981.lua) | 1 |
| Red Hared Hasty Horse | `19636995` | [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19636995.lua) | 1 |

## Script Examples

### Darklord Uprising (`54527349`)

Source: [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54527349.lua)

```lua
		e:SetCategory(bit.bor(cat,CATEGORY_RECOVER))
	else
		e:SetCategory(bit.band(cat,bit.bnot(CATEGORY_RECOVER)))
	end
end
```

### Disablaster the Negation Fortress (`58707981`)

Source: [Scripts/c58707981.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58707981.lua)

```lua
		zone=bit.bor(zone,tc:GetColumnZone(LOCATION_MZONE,tp))
	end
	return bit.bnot(zone)
end
function s.hspcon(e,c)
```

### Red Hared Hasty Horse (`19636995`)

Source: [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19636995.lua)

```lua
		zone=bit.bor(zone,tc:GetColumnZone(LOCATION_MZONE,tp))
	end
	return bit.bnot(zone)
end
function c19636995.hspcon(e,c)
```
