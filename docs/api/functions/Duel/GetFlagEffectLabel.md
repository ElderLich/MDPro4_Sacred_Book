# Duel.GetFlagEffectLabel

## Signature

```lua
Duel.GetFlagEffectLabel(int player, int code) -> int|nil,int...
```

## Description

Returns the label values stored on player flag effects with code.
If no matching flag effect exists, the core returns nil; if multiple matching flag effects exist, it returns one label value for each. A matching flag effect with no label returns 0 for that slot.

## Parameters

- `player` `int` - Player whose player flag effects are inspected.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - First matching label, or nil if player is invalid or no matching flag effect exists.
- `int...` - Additional matching labels; a matching effect with no label contributes 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4857`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetFlagEffectLabel`.

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
			Duel.RegisterFlagEffect(tp,41867019,RESET_PHASE+PHASE_END,0,1)
		end
		local flag=Duel.GetFlagEffectLabel(tp,41867019)
		local b1=Duel.IsPlayerCanDraw(tp,1) and bit.band(flag,0x1)==0
		local b2=Duel.IsExistingMatchingCard(c41867019.setfilter,tp,LOCATION_DECK,0,1,nil) and bit.band(flag,0x2)==0
```

### You and A.I. (`32056070`)

Source: [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua)

```lua
	local b3=Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsPlayerCanSpecialSummonMonster(tp,11738490,0,TYPES_TOKEN_MONSTER,0,0,1,RACE_CYBERSE,ATTRIBUTE_DARK)
	local used=Duel.GetFlagEffectLabel(tp,32056070)
	if used==nil then
		used=0
```

### Cairngorgon, Antiluminescent Knight (`21501505`)

Source: [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua)

```lua
function c21501505.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local ct=ev
	local label=Duel.GetFlagEffectLabel(0,21501505)
	if label then
		if ev==bit.rshift(label,16) then ct=bit.band(label,0xffff) end
```
