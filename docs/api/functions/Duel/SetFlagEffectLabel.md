# Duel.SetFlagEffectLabel

## Signature

```lua
Duel.SetFlagEffectLabel(int player, int code, int label) -> bool|nil
```

## Description

Sets the first matching player flag effect's label to label and returns whether one was found.

## Parameters

- `player` `int`
- `code` `int`
- `label` `int`

## Returns

- `bool|nil` - True if a matching flag effect was updated; false if none exists; nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4856`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetFlagEffectLabel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mayakashi Mayhem | `41867019` | [Scripts/c41867019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41867019.lua) | 41 |
| You and A.I. | `32056070` | [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua) | 37 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 36 |
| New Frontier | `56787189` | [Scripts/c56787189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56787189.lua) | 33 |
| Dimensional Barrier | `83326048` | [Scripts/c83326048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83326048.lua) | 26 |

## Script Examples

### Mayakashi Mayhem (`41867019`)

Source: [Scripts/c41867019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41867019.lua)

```lua
	if sel==1 then
		Duel.Draw(tp,1,REASON_EFFECT)
		Duel.SetFlagEffectLabel(tp,41867019,flag|0x1)
	elseif sel==2 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SET)
```

### You and A.I. (`32056070`)

Source: [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua)

```lua
	end
	used=used|att
	Duel.SetFlagEffectLabel(tp,32056070,used)
	if att&(ATTRIBUTE_EARTH+ATTRIBUTE_WATER)>0 then
		e:SetCategory(CATEGORY_ATKCHANGE)
```

### Cairngorgon, Antiluminescent Knight (`21501505`)

Source: [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua)

```lua
	local val=ct+bit.lshift(ev+1,16)
	if label then
		Duel.SetFlagEffectLabel(0,21501505,val)
	else
		Duel.RegisterFlagEffect(0,21501505,RESET_CHAIN,0,1,val)
```
