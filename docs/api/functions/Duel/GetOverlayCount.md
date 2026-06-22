# Duel.GetOverlayCount

## Signature

```lua
Duel.GetOverlayCount(int player, int s, int o) -> int|nil
```

## Description

Returns the number of Xyz Materials attached to cards in player-relative locations s and o.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`

## Returns

- `int|nil` - Overlay count, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5016`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetOverlayCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rank-Up-Magic Barian's Force | `47660516` | [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua) | 49 |
| Xyz Lay | `43150717` | [Scripts/c43150717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43150717.lua) | 38 |
| Neo Galaxy-Eyes Photon Dragon | `39272762` | [Scripts/c39272762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39272762.lua) | 38 |
| Goblin Biker Troika Griare | `44241999` | [Scripts/c44241999.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44241999.lua) | 37 |
| Prima Materiactor | `57448410` | [Scripts/c57448410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57448410.lua) | 36 |
| Empress of Prophecy | `770365` | [Scripts/c770365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c770365.lua) | 35 |
| Stoic Challenge | `37364101` | [Scripts/c37364101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37364101.lua) | 32 |
| Overlay Sentinel | `39229392` | [Scripts/c39229392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39229392.lua) | 32 |
| Overlay Eater | `81816475` | [Scripts/c81816475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81816475.lua) | 23 |
| Night Papilloperative | `2191144` | [Scripts/c2191144.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2191144.lua) | 20 |

## Script Examples

### Rank-Up-Magic Barian's Force (`47660516`)

Source: [Scripts/c47660516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47660516.lua)

```lua
		Duel.SpecialSummon(sc,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)
		sc:CompleteProcedure()
		if Duel.GetOverlayCount(tp,0,1)~=0 then
			Duel.BreakEffect()
			local g1=Duel.GetOverlayGroup(tp,0,1)
```

### Xyz Lay (`43150717`)

Source: [Scripts/c43150717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43150717.lua)

```lua
end
function s.atkval(e,c)
	return Duel.GetOverlayCount(e:GetHandlerPlayer(),1,1)*200
end
```

### Neo Galaxy-Eyes Photon Dragon (`39272762`)

Source: [Scripts/c39272762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39272762.lua)

```lua
end
function c39272762.attg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetOverlayCount(tp,0,1)~=0 end
end
function c39272762.atop(e,tp,eg,ep,ev,re,r,rp)
```
