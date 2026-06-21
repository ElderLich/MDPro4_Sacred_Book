# Duel.RockPaperScissors

## Signature

```lua
Duel.RockPaperScissors([bool repeated]) -> int
```

## Description

Perform Rock-Paper-Scissors; if repeat=false, perform once; otherwise, continue until a winner is determined. Return the winning player's number

## Parameters

- `repeated` `bool` optional - default: true

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5038`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RockPaperScissors`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transmission Gear | `58297729` | [Scripts/c58297729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58297729.lua) | 14 |

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
