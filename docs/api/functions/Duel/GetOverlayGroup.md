# Duel.GetOverlayGroup

## Signature

```lua
Duel.GetOverlayGroup(int player, int s, int o) -> Group|nil
```

## Description

Returns the Xyz Materials attached to cards in player-relative locations s and o.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`

## Returns

- `Group|nil` - Overlay group, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5015`

## Guided Examples

Learn how to use this function in context:

- [Xyz Procedure Guide](/learn/xyz-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetOverlayGroup) with `Duel.GetOverlayGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rank-Up-Magic Barian's Force | `47660516` | [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua) | 1 |
| Heroic Call | `32175429` | [Scripts/c32175429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32175429.lua) | 2 |
| Neo Galaxy-Eyes Photon Dragon | `39272762` | [Scripts/c39272762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39272762.lua) | 1 |
| Xyz Revenge | `10275411` | [Scripts/c10275411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10275411.lua) | 1 |
| Overlay Eater | `81816475` | [Scripts/c81816475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81816475.lua) | 1 |

## Script Examples

### Rank-Up-Magic Barian's Force (`47660516`)

Source: [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua)

```lua
		if Duel.GetOverlayCount(tp,0,1)~=0 then
			Duel.BreakEffect()
			local g1=Duel.GetOverlayGroup(tp,0,1)
			Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(47660516,0))
			local mg2=g1:Select(tp,1,1,nil)
```

### Heroic Call (`32175429`)

Source: [Scripts/c32175429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32175429.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(tp) and chkc:IsFaceup() end
	local ct1=Duel.GetMatchingGroupCount(s.afilter,tp,LOCATION_ONFIELD,0,nil)
	local ct2=Duel.GetOverlayGroup(tp,1,0):FilterCount(Card.IsSetCard,nil,0x6f)
	if chk==0 then return Duel.IsExistingTarget(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
		and ct1+ct2>0 end
```

### Neo Galaxy-Eyes Photon Dragon (`39272762`)

Source: [Scripts/c39272762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39272762.lua)

```lua
end
function c39272762.atop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetOverlayGroup(tp,0,1)
	if g:GetCount()==0 then return end
	Duel.SendtoGrave(g,REASON_EFFECT)
```
