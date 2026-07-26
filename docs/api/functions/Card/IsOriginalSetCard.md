# Card.IsOriginalSetCard

## Signature

```lua
Card.IsOriginalSetCard(Card c, int setcode1, [int setcode2], [... int]) -> bool
```

## Description

Checks whether c's original set data matches any supplied set code.

## Parameters

- `c` `Card`
- `setcode1` `int`
- `setcode2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3397`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsOriginalSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Heraldic Beast Stad Whale | `97662494` | [Scripts/c97662494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97662494.lua) | 1 |
| Obliterate!!! Blaze | `402416` | [Scripts/c402416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c402416.lua) | 1 |
| Final Cross | `35756798` | [Scripts/c35756798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35756798.lua) | 1 |
| Riryoku Guardian | `96661780` | [Scripts/c96661780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96661780.lua) | 1 |
| Scrap Warrior | `42711820` | [Scripts/c42711820.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42711820.lua) | 1 |
| Lyrilusc - Independent Nightingale | `76815942` | [Scripts/c76815942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76815942.lua) | 1 |
| Heraldic Beast Gryphon | `60268386` | [Scripts/c60268386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60268386.lua) | 1 |
| Synchro Chase | `23442438` | [Scripts/c23442438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23442438.lua) | 1 |
| Junk Armor | `91215724` | [Scripts/c91215724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91215724.lua) | 1 |
| Full-Speed Warrior | `17201951` | [Scripts/c17201951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17201951.lua) | 1 |
| Scrap Synchron | `16449363` | [Scripts/c16449363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16449363.lua) | 1 |
| Satellite Synchron | `57458399` | [Scripts/c57458399.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57458399.lua) | 1 |
| Junk Mail | `39520293` | [Scripts/c39520293.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39520293.lua) | 1 |

## Script Examples

### Heraldic Beast Stad Whale (`97662494`)

Source: [Scripts/c97662494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97662494.lua)

```lua
end
function s.tlmtg(e,c)
	return not c:IsOriginalSetCard(0x76,0x48)
end
function s.tlmval(e,c)
```

### Obliterate!!! Blaze (`402416`)

Source: [Scripts/c402416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c402416.lua)

```lua
end
function s.filter(c)
	return c:IsFaceup() and c:IsOriginalSetCard(0xde) and c:IsLevelAbove(10) and c:GetFlagEffect(id)==0
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Final Cross (`35756798`)

Source: [Scripts/c35756798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35756798.lua)

```lua
	local g=Duel.SelectTarget(tp,c35756798.filter,tp,LOCATION_MZONE,0,1,1,nil)
	local tc=g:GetFirst()
	if tc:IsOriginalSetCard(0x66,0x1017,0xa3) then
		Duel.SetTargetParam(1)
	end
```
