# Duel.IsPlayerCanRelease

## Signature

```lua
Duel.IsPlayerCanRelease(int player, [Card c], [int reason]) -> bool
```

## Description

Checks whether player can release cards at all, or whether player can release c for reason.
When c is supplied and reason is omitted, the core uses REASON_COST.

## Parameters

- `player` `int`
- `c` `Card` optional
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5054`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanRelease`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 47 |
| Mitsurugi Sacred Boundary | `12210097` | [Scripts/c12210097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12210097.lua) | 41 |
| Vendread Reunion | `2266498` | [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2266498.lua) | 41 |
| Ame no Habakiri no Mitsurugi | `13332685` | [Scripts/c13332685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13332685.lua) | 40 |
| EMERGENCY! | `61292243` | [Scripts/c61292243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61292243.lua) | 36 |

## Script Examples

### Nibiru, the Primal Being (`27204311`)

Source: [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua)

```lua
	local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	if chk==0 then return g:GetCount()>0 and Duel.GetMZoneCount(tp,g)>0 and Duel.GetMZoneCount(1-tp,g,tp)>0
		and Duel.IsPlayerCanRelease(tp)
		and Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
```

### Mitsurugi Sacred Boundary (`12210097`)

Source: [Scripts/c12210097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12210097.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_GRAVE) and chkc:IsControler(tp) and s.tdfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.tdfilter,tp,LOCATION_GRAVE,0,4,nil)
		and (Duel.GetFieldGroup(tp,0,LOCATION_MZONE)==0 or Duel.IsPlayerCanRelease(1-tp)) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectTarget(tp,s.tdfilter,tp,LOCATION_GRAVE,0,4,4,nil)
```

### Vendread Reunion (`2266498`)

Source: [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2266498.lua)

```lua
end
function c2266498.filter(c,e,tp)
	return c:IsFaceup() and c:IsSetCard(0x106) and Duel.IsPlayerCanRelease(tp,c,REASON_EFFECT)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEDOWN_DEFENSE)
end
```
