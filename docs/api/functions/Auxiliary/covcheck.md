# Auxiliary.covcheck

## Signature

```lua
Auxiliary.covcheck(Card c) -> bool|nil
```

## Description

Returns true for a printed Monster Card, or for a non-monster whose recorded Special Summon reason effect belongs to itself. Used when deciding whether an original-value calculation remains meaningful after a self-summoned Trap leaves the field.

## Parameters

- `c` `Card`

## Returns

- `bool|nil` - May return nil when there is no recorded Special Summon reason effect; use as a predicate.

## Source

- `Utilities/utility.lua:2070`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.covcheck) with `Auxiliary.covcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| [Cerynemesia, Mystical Beast of the Forest](/examples/cards/43632709) | `43632709` | [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43632709.lua) | 1 |
| Dark Time Wizard | `40235813` | [Scripts/c40235813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40235813.lua) | 1 |
| Arcana Force XII - The Hangman | `72321198` | [Scripts/c72321198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72321198.lua) | 2 |

## Script Examples

### Destratification Dino Stratiae (`3841104`)

Source: [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3841104.lua)

```lua
	local atk=0
	for tc in aux.Next(g) do
		if tc:IsLinkRace(RACE_DINOSAUR) and aux.covcheck(tc) then
			local tatk=tc:GetTextAttack()
			if tatk>0 then atk=atk+tatk end
```

### Cerynemesia, Mystical Beast of the Forest (`43632709`)

Source: [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43632709.lua)

```lua
function s.rmfilter(c,e,tp)
	return c:IsFaceupEx() and c:IsRace(RACE_BEAST) and c:IsAbleToRemoveAsCost()
		and Duel.GetMZoneCount(tp,c)>0 and (not c:IsLocation(LOCATION_MZONE) or aux.covcheck(c))
		and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_DECK+LOCATION_GRAVE,0,1,nil,e,tp,c:GetOriginalLevel())
end
```

### Dark Time Wizard (`40235813`)

Source: [Scripts/c40235813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40235813.lua)

```lua
function s.calfilter(c)
	if c:GetTextAttack()<0 then return false end
	return aux.covcheck(c)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
```
