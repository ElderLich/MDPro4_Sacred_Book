# Duel.GetOperationCount

## Signature

```lua
Duel.GetOperationCount(int chainc) -> int
```

## Description

Returns the number of operation categories recorded for chainc.

## Parameters

- `chainc` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5010`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetOperationCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Muko | `80863132` | [Scripts/c80863132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80863132.lua) | 1 |

## Script Examples

### Muko (`80863132`)

Source: [Scripts/c80863132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80863132.lua)

```lua
function c80863132.condition(e,tp,eg,ep,ev,re,r,rp)
	if not re:IsHasProperty(EFFECT_FLAG_PLAYER_TARGET) then return false end
	if Duel.GetOperationCount(ev)~=1 then return false end
	local ex,cg,cc,cp,cv=Duel.GetOperationInfo(ev,CATEGORY_DRAW)
	return ex and cv>0
```
