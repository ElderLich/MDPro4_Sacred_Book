# bit.lshift

## Signature

```lua
bit.lshift(int a, int b) -> int
```

## Description

Returns a shifted left by b bits.

## Parameters

- `a` `int`
- `b` `int`

## Returns

- `int`

## Source

- `Utilities/utility.lua:24`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=bit.lshift) with `bit.lshift`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87871125.lua) | 1 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95372220.lua) | 1 |
| Knightmare Goblin | `39064822` | [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39064822.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| Vampire Duke | `58947797` | [Scripts/c58947797.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58947797.lua) | 1 |
| Gouki Thunder Ogre | `30010480` | [Scripts/c30010480.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30010480.lua) | 2 |

## Script Examples

### Salamangreat Sunlight Wolf (`87871125`)

Source: [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87871125.lua)

```lua
		return ec:GetLinkedGroup():IsContains(c)
	else
		return bit.band(ec:GetLinkedZone(c:GetPreviousControler()),bit.lshift(0x1,c:GetPreviousSequence()))~=0
	end
end
```

### Flash Charge Dragon (`95372220`)

Source: [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95372220.lua)

```lua
		return ec:GetLinkedGroup():IsContains(c)
	else
		return bit.band(ec:GetLinkedZone(c:GetPreviousControler()),bit.lshift(0x1,c:GetPreviousSequence()))~=0
	end
end
```

### Knightmare Goblin (`39064822`)

Source: [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39064822.lua)

```lua
	local c=e:GetHandler()
	local sumzone=c:GetLinkedZone()
	local relzone=-bit.lshift(1,c:GetSequence())
	return 0,sumzone,relzone
end
```
