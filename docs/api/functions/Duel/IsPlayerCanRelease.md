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
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanRelease) with `Duel.IsPlayerCanRelease`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27204311.lua) | 1 |
| Vendread Reunion | `2266498` | [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2266498.lua) | 1 |
| Ame no Habakiri no Mitsurugi | `13332685` | [Scripts/c13332685.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13332685.lua) | 1 |
| Mitsurugi Sacred Boundary | `12210097` | [Scripts/c12210097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12210097.lua) | 1 |
| EMERGENCY! | `61292243` | [Scripts/c61292243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61292243.lua) | 1 |

## Script Examples

### Nibiru, the Primal Being (`27204311`)

Source: [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27204311.lua)

```lua
	local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	if chk==0 then return g:GetCount()>0 and Duel.GetMZoneCount(tp,g)>0 and Duel.GetMZoneCount(1-tp,g,tp)>0
		and Duel.IsPlayerCanRelease(tp)
		and Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
```

### Vendread Reunion (`2266498`)

Source: [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2266498.lua)

```lua
end
function c2266498.filter(c,e,tp)
	return c:IsFaceup() and c:IsSetCard(0x106) and Duel.IsPlayerCanRelease(tp,c,REASON_EFFECT)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEDOWN_DEFENSE)
end
```

### Ame no Habakiri no Mitsurugi (`13332685`)

Source: [Scripts/c13332685.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13332685.lua)

```lua
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_DECK,0,1,nil,e,tp) and Duel.IsPlayerCanRelease(tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK)
end
```
