# Auxiliary.FilterEqualFunction

## Signature

```lua
Auxiliary.FilterEqualFunction(function f, any value, [... any]) -> function
```

## Description

Returns a card filter that calls f on the card and extra arguments, then checks whether the result equals value.

## Parameters

- `f` `function`
- `value` `any`
- `...` `any` optional

## Returns

- `function`

## Source

- `Utilities/utility.lua:460`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.FilterEqualFunction) with `Auxiliary.FilterEqualFunction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Starry Dragon's Cycle | `6278008` | [Scripts/c6278008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6278008.lua) | 2 |
| Sextet Summon | `99162753` | [Scripts/c99162753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99162753.lua) | 1 |

## Script Examples

### Starry Dragon's Cycle (`6278008`)

Source: [Scripts/c6278008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6278008.lua)

```lua
	local f=aux.FALSE
	local typ=tc:GetType()&TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ+TYPE_LINK
	if typ==TYPE_FUSION then f=aux.FilterEqualFunction(Card.GetAttribute,tc:GetAttribute())
	elseif typ==TYPE_SYNCHRO then f=aux.FilterBoolFunction(Card.IsLevelBelow,tc:GetLevel()-1)
	elseif typ==TYPE_XYZ then f=aux.FilterBoolFunction(Card.IsLevel,tc:GetRank())
```

### Sextet Summon (`99162753`)

Source: [Scripts/c99162753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99162753.lua)

```lua
end
function c99162753.spfilter(c,e,tp,g)
	return g:IsExists(aux.FilterEqualFunction(Card.GetOriginalRace,c:GetOriginalRace()),1,nil) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and (c:IsLocation(LOCATION_DECK) and Duel.GetMZoneCount(tp,g)>0
			or c:IsLocation(LOCATION_EXTRA) and Duel.GetLocationCountFromEx(tp,tp,g,c)>0)
```
