# Duel.RockPaperScissors

## Signature

```lua
Duel.RockPaperScissors([bool repeat]) -> int
```

## Description

Runs the Rock-Paper-Scissors selector and returns the winning player; repeat defaults to true.

## Parameters

- `repeat` `bool` optional - default: true

## Returns

- `int` - Winning player.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5038`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RockPaperScissors`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transmission Gear | `58297729` | [Scripts/c58297729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58297729.lua) | 1 |

## Script Examples

### Transmission Gear (`58297729`)

Source: [Scripts/c58297729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58297729.lua)

```lua
	if not a:IsRelateToBattle() or not d:IsRelateToBattle() then return end
	if a:IsControler(1-tp) then a,d=d,a end
	local res=Duel.RockPaperScissors()
	if res==tp then
		Duel.Remove(d,POS_FACEDOWN,REASON_RULE)
```
