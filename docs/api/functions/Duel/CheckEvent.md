# Duel.CheckEvent

## Signature

```lua
Duel.CheckEvent(int event, [bool get_info]) -> bool,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Without get_info, returns whether event is present in the current event state.
With get_info true, returns true plus event cards, event player, event value, reason effect, reason, and reason player when found; otherwise returns false.

## Parameters

- `event` `int`
- `get_info` `bool` optional - default: false

## Returns

- `bool`
- `Group|nil` - Event cards when get_info succeeds.
- `int|nil` - Event player.
- `int|nil` - Event value.
- `Effect|nil` - Reason effect.
- `int|nil` - Reason.
- `int|nil` - Reason player.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4894`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckEvent`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 73 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 71 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua) | 56 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79755671.lua) | 54 |
| U.A. Penalty Box | `70043345` | [Scripts/c70043345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70043345.lua) | 46 |
| Kunai with Chain | `37390589` | [Scripts/c37390589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37390589.lua) | 44 |
| Eye of Illusion | `23446369` | [Scripts/c23446369.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23446369.lua) | 40 |
| Crusadia Testament | `87497553` | [Scripts/c87497553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87497553.lua) | 37 |
| Beast King Unleashed | `50675040` | [Scripts/c50675040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50675040.lua) | 34 |
| Depth Amulet | `8279188` | [Scripts/c8279188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8279188.lua) | 32 |
| Prepare to Strike Back | `4483989` | [Scripts/c4483989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4483989.lua) | 31 |
| Lose 1 Turn | `24348804` | [Scripts/c24348804.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24348804.lua) | 30 |
| Dice-nied | `31863912` | [Scripts/c31863912.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31863912.lua) | 27 |
| Dimension Slice | `73632127` | [Scripts/c73632127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73632127.lua) | 26 |
| Gishki Vanity | `93506862` | [Scripts/c93506862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93506862.lua) | 25 |
| Chow Chow Chan | `99902789` | [Scripts/c99902789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99902789.lua) | 23 |
| Zolga | `16268841` | [Scripts/c16268841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16268841.lua) | 20 |
| Dust Storm of Gusto | `8414337` | [Scripts/c8414337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8414337.lua) | 18 |

## Script Examples

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
end
function s.cedop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.CheckEvent(EVENT_SPSUMMON_SUCCESS) and e:GetLabelObject():GetLabel()==1 and e:GetHandler():GetFlagEffect(id)~=0 then
		Duel.SetChainLimitTillChainEnd(aux.FALSE)
	end
```

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
end
function s.cedop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.CheckEvent(EVENT_SPSUMMON_SUCCESS) and e:GetLabelObject():GetLabel()==1 and e:GetHandler():GetFlagEffect(id)~=0 then
		Duel.SetChainLimitTillChainEnd(s.chainlm)
	end
```

### Dracotail Shaulas (`42125140`)

Source: [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua)

```lua
	local c=e:GetOwner()
	g:Merge(eg)
	if Duel.CheckEvent(EVENT_MOVE) then
		local _,meg=Duel.CheckEvent(EVENT_MOVE,true)
		if meg:IsContains(c) and (c:IsFaceup() or c:IsPublic()) then
```
