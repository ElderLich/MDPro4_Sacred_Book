# Duel.GetFlagEffectLabel

## Signature

```lua
Duel.GetFlagEffectLabel(int player, int code) -> int|nil,int...
```

## Description

Returns the label values stored on player flag effects with code.
If no matching flag effect exists, the core returns nil; if multiple matching flag effects exist, it returns one label value for each. A matching flag effect with no label returns 0 for that slot.

## How To Use It

Use this to read integer labels stored on player markers.

```lua
local label=Duel.GetFlagEffectLabel(tp,id)
```

If no marker exists, this returns nil. If several matching markers exist, the local binding returns one label value for each marker.

## Related Functions

- [Duel.RegisterFlagEffect](/api/functions/Duel/RegisterFlagEffect)
- [Duel.GetFlagEffect](/api/functions/Duel/GetFlagEffect)
- [Duel.ResetFlagEffect](/api/functions/Duel/ResetFlagEffect)

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

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetFlagEffectLabel) with `Duel.GetFlagEffectLabel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua) | 2 |
| Mayakashi Mayhem | `41867019` | [Scripts/c41867019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41867019.lua) | 2 |
| You and A.I. | `32056070` | [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| New Frontier | `56787189` | [Scripts/c56787189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56787189.lua) | 1 |
| Dimensional Barrier | `83326048` | [Scripts/c83326048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83326048.lua) | 2 |

## Script Examples

### Trirealm Rift Judgment (`65195679`)

Source: [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua)

```lua
end
function s.spfilter(c,e,tp,ec,ft)
	return c:IsFacedown() and c:IsSetCard(0x1ed) and c:IsAttribute(ec:GetAttribute()) and not c:IsAttribute(Duel.GetFlagEffectLabel(tp,id))
		and (c:IsAbleToHand() or (ft>0 and c:IsCanBeSpecialSummoned(e,0,tp,false,false)))
end
```

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
