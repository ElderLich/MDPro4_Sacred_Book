# bit.rshift

## Signature

```lua
bit.rshift(int a, int b) -> int
```

## Description

Returns a shifted right by b bits.

## Parameters

- `a` `int`
- `b` `int`

## Returns

- `int`

## Source

- `Utilities/utility.lua:27`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `bit.rshift`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| S-Force Mystify | `4611341` | [Scripts/c4611341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4611341.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| Dueltaining | `19162134` | [Scripts/c19162134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19162134.lua) | 1 |
| Remote Rebirth | `54658815` | [Scripts/c54658815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54658815.lua) | 2 |
| Wattkinetic Puppeteer | `88392300` | [Scripts/c88392300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88392300.lua) | 1 |
| Dai Dance | `50696588` | [Scripts/c50696588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50696588.lua) | 1 |
| Dice Re-Roll | `83241722` | [Scripts/c83241722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83241722.lua) | 1 |

## Script Examples

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
	if mlv==mc:GetLevel() then return false end
	local lv=c:GetLevel()
	return lv==bit.band(mlv,0xffff) or lv==bit.rshift(mlv,16)
end
function c51124303.filter(c,e,tp)
```

### S-Force Mystify (`4611341`)

Source: [Scripts/c4611341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4611341.lua)

```lua
		local fd=Duel.SelectDisableField(tp,1,0,LOCATION_MZONE,0)
		Duel.Hint(HINT_ZONE,tp,fd)
		local nseq=math.log(bit.rshift(fd,16),2)
		Duel.MoveSequence(tc,nseq)
	end
```

### Cairngorgon, Antiluminescent Knight (`21501505`)

Source: [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua)

```lua
	local label=Duel.GetFlagEffectLabel(0,21501505)
	if label then
		if ev==bit.rshift(label,16) then ct=bit.band(label,0xffff) end
	end
	if chkc then return chkc:IsOnField() and c21501505.filter(chkc,ct) end
```
