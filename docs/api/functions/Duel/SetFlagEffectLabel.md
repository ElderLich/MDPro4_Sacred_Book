# Duel.SetFlagEffectLabel

## Signature

```lua
Duel.SetFlagEffectLabel(int player, int code, int label) -> bool|nil
```

## Description

Sets the first matching player flag effect's label to label and returns whether one was found.

## Parameters

- `player` `int` - Player whose matching flag effect is updated.
- `code` `int` - Flag-effect code to find.
- `label` `int` - New integer label stored on the first matching player flag effect.

## Returns

- `bool|nil` - True if a matching flag effect was updated; false if none exists; nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4856`

## Guided Examples

Learn how to use this function in context:

- [Flag Effects](/learn/flag-effects)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetFlagEffectLabel) with `Duel.SetFlagEffectLabel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| Mayakashi Mayhem | `41867019` | [Scripts/c41867019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41867019.lua) | 4 |
| You and A.I. | `32056070` | [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| New Frontier | `56787189` | [Scripts/c56787189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56787189.lua) | 2 |
| Dimensional Barrier | `83326048` | [Scripts/c83326048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83326048.lua) | 1 |

## Script Examples

### Trirealm Rift Judgment (`65195679`)

Source: [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua)

```lua
				local label=Duel.GetFlagEffectLabel(tp,id)
				if label then
					Duel.SetFlagEffectLabel(tp,id,label|att)
				else
					Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1,att)
```

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
