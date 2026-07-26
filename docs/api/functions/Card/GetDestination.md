# Card.GetDestination

## Signature

```lua
Card.GetDestination(Card c) -> int
```

## Description

Returns the destination location currently stored in c's send-to parameters.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3477`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetDestination`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Neos Fusion | `14088859` | [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14088859.lua) | 49 |
| Madolche Chateau | `14001430` | [Scripts/c14001430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14001430.lua) | 45 |
| Tiki Soul | `49514333` | [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua) | 43 |
| Archlord Kristya | `59509952` | [Scripts/c59509952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59509952.lua) | 32 |
| Storm Caller | `15935204` | [Scripts/c15935204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15935204.lua) | 32 |
| Evigishki Merrowgeist | `76372778` | [Scripts/c76372778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76372778.lua) | 21 |
| Spirit Elimination | `69832741` | [Scripts/c69832741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69832741.lua) | 20 |

## Script Examples

### Neos Fusion (`14088859`)

Source: [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14088859.lua)

```lua
function c14088859.repfilter2(c,tp,re)
	return c:IsControler(tp) and c:IsLocation(LOCATION_MZONE) and aux.IsMaterialListCode(c,89943723) and c:IsType(TYPE_FUSION)
		and c:GetDestination()==LOCATION_DECK and re:GetOwner()==c
end
function c14088859.reptg2(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Madolche Chateau (`14001430`)

Source: [Scripts/c14001430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14001430.lua)

```lua
end
function c14001430.repfilter(c,tp)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE) and c:GetDestination()==LOCATION_DECK and c:IsType(TYPE_MONSTER)
		and c:IsAbleToHand()
end
```

### Tiki Soul (`49514333`)

Source: [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua)

```lua
end
function c49514333.repfilter(c,tp)
	return c:IsLocation(LOCATION_MZONE) and c:IsFaceup() and c:GetDestination()==LOCATION_GRAVE and c:GetLeaveFieldDest()==0 and c:IsReason(REASON_DESTROY)
		and c:GetReasonPlayer()==1-tp and c:GetOwner()==tp and bit.band(c:GetOriginalType(),TYPE_TRAP)~=0 and c:IsCanTurnSet()
end
```
