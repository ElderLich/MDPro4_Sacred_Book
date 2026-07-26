# Card.GetLeaveFieldDest

## Signature

```lua
Card.GetLeaveFieldDest(Card c) -> int
```

## Description

Returns the location c would be redirected to by leave-field effects for REASON_EFFECT.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3478`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLeaveFieldDest`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tiki Soul | `49514333` | [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua) | 1 |
| Old Mind | `54239282` | [Scripts/c54239282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54239282.lua) | 1 |
| Storm Caller | `15935204` | [Scripts/c15935204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15935204.lua) | 1 |
| Evigishki Merrowgeist | `76372778` | [Scripts/c76372778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76372778.lua) | 1 |

## Script Examples

### Tiki Soul (`49514333`)

Source: [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua)

```lua
end
function c49514333.repfilter(c,tp)
	return c:IsLocation(LOCATION_MZONE) and c:IsFaceup() and c:GetDestination()==LOCATION_GRAVE and c:GetLeaveFieldDest()==0 and c:IsReason(REASON_DESTROY)
		and c:GetReasonPlayer()==1-tp and c:GetOwner()==tp and bit.band(c:GetOriginalType(),TYPE_TRAP)~=0 and c:IsCanTurnSet()
end
```

### Old Mind (`54239282`)

Source: [Scripts/c54239282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54239282.lua)

```lua
	local g=Duel.GetMatchingGroup(c54239282.filter,tp,LOCATION_HAND,0,nil,type)
	local op=0
	if g:GetCount()>0 and tc:IsDiscardable(REASON_EFFECT) and c:IsRelateToEffect(e) and c:GetLeaveFieldDest()==0 and Duel.IsPlayerCanDraw(tp,1) then
		op=Duel.SelectOption(tp,aux.Stringid(54239282,0),aux.Stringid(54239282,1))
	else
```

### Storm Caller (`15935204`)

Source: [Scripts/c15935204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15935204.lua)

```lua
	return c:IsStatus(STATUS_BATTLE_DESTROYED) and not c:IsType(TYPE_TOKEN)
		and c:IsControler(1-tp) and c:IsReason(REASON_BATTLE) and c:GetReasonCard():IsRace(RACE_PSYCHO) and c:GetReasonCard()~=e:GetHandler()
		and c:GetLeaveFieldDest()==0 and c:GetDestination()~=LOCATION_DECK
end
function c15935204.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
