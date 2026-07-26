# Card.GetRaceInGrave

## Signature

```lua
Card.GetRaceInGrave(Card c, [int reasonPlayer]) -> int
```

## Description

Returns the Race c is treated as having in the GY for player, defaulting to the current reason player.

## Parameters

- `c` `Card`
- `reasonPlayer` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3442`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetRaceInGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transmodify | `5288597` | [Scripts/c5288597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5288597.lua) | 37 |

## Script Examples

### Transmodify (`5288597`)

Source: [Scripts/c5288597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5288597.lua)

```lua
function c5288597.cfilter(c,e,tp)
	local lv=c:GetOriginalLevel()
	local rc=c:GetRaceInGrave()
	local att=c:GetAttributeInGrave()
	return bit.band(c:GetOriginalType(),TYPE_MONSTER)~=0 and lv>0 and c:IsFaceup() and c:IsAbleToGraveAsCost()
```
