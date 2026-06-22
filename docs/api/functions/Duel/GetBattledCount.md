# Duel.GetBattledCount

## Signature

```lua
Duel.GetBattledCount(int player) -> int
```

## Description

Returns how many battles player has conducted in the current Battle Phase tracking state.

## Parameters

- `player` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5070`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetBattledCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Zap Mustung | `29951323` | [Scripts/c29951323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29951323.lua) | 20 |

## Script Examples

### Zap Mustung (`29951323`)

Source: [Scripts/c29951323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29951323.lua)

```lua
end
function c29951323.limittg(e,c,tp)
	return Duel.GetTurnPlayer()==tp and Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)>=Duel.GetBattledCount(tp)
end
function c29951323.countcon1(e)
```
