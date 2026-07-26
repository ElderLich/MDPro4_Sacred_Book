# Card.GetAttributeInGrave

## Signature

```lua
Card.GetAttributeInGrave(Card c, [int player]) -> int
```

## Description

Returns the Attribute c is treated as having in the GY for player, defaulting to the current reason player.

## Parameters

- `c` `Card`
- `player` `int` optional - default: current reason player

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3438`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetAttributeInGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Aerial Eater | `28143384` | [Scripts/c28143384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28143384.lua) | 43 |
| Transmodify | `5288597` | [Scripts/c5288597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5288597.lua) | 37 |

## Script Examples

### Aerial Eater (`28143384`)

Source: [Scripts/c28143384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28143384.lua)

```lua
end
function s.rselect(g)
	return g:GetClassCount(Card.GetAttributeInGrave)==1
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Transmodify (`5288597`)

Source: [Scripts/c5288597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5288597.lua)

```lua
	local lv=c:GetOriginalLevel()
	local rc=c:GetRaceInGrave()
	local att=c:GetAttributeInGrave()
	return bit.band(c:GetOriginalType(),TYPE_MONSTER)~=0 and lv>0 and c:IsFaceup() and c:IsAbleToGraveAsCost()
		and Duel.IsExistingMatchingCard(c5288597.spfilter,tp,LOCATION_DECK,0,1,nil,lv+1,rc,att,e,tp)
```
