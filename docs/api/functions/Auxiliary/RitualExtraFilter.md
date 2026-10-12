# Auxiliary.RitualExtraFilter

## Signature

```lua
Auxiliary.RitualExtraFilter(Card c, function f) -> bool
```

## Description

Graveyard Ritual Material filter; c must be a Level monster accepted by f and able to be banished.

## Parameters

- `c` `Card`
- `f` `function`

## Returns

- `bool` - true if c is valid extra Graveyard Ritual Material.

## Source

- `Utilities/procedure.lua:1842`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.RitualExtraFilter) with `Auxiliary.RitualExtraFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| A.I.'s Ritual | `85327820` | [Scripts/c85327820.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85327820.lua) | 2 |

## Script Examples

### A.I.'s Ritual (`85327820`)

Source: [Scripts/c85327820.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85327820.lua)

```lua
		local mg2=nil
		if Duel.IsExistingMatchingCard(c85327820.cfilter,tp,LOCATION_MZONE,0,1,nil) then
			mg2=Duel.GetMatchingGroup(aux.RitualExtraFilter,tp,LOCATION_GRAVE,0,nil,c85327820.mfilter)
		end
		return Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,LOCATION_HAND,0,1,nil,c85327820.filter,e,tp,mg,mg2,Card.GetLevel,"Greater")
```
