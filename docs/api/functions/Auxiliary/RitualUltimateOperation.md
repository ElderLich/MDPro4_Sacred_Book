# Auxiliary.RitualUltimateOperation

## Signature

```lua
Auxiliary.RitualUltimateOperation(function|nil filter, function level_function, string greater_or_equal, int summon_location, function|nil grave_filter, function|nil mat_filter, function|nil extra_operation) -> function
```

## Description

Returns the operation function for configurable Ritual Summon effects. It selects the Ritual Monster and materials, releases or banishes the materials, Special Summons the monster, and runs extra callbacks.

## Parameters

- `filter` `function|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `summon_location` `int`
- `grave_filter` `function|nil`
- `mat_filter` `function|nil`
- `extra_operation` `function|nil`

## Returns

- `function` - Operation function for a configurable Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1865`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.RitualUltimateOperation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Stars Align Above the Shrine | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15306543.lua) | 42 |
| Mitsurugi Magatama | `76725398` | [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua) | 38 |

## Script Examples

### Stars Align Above the Shrine (`15306543`)

Source: [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15306543.lua)

```lua
	e2:SetCountLimit(1)
	e2:SetTarget(aux.RitualUltimateTarget(table.unpack(t)))
	e2:SetOperation(aux.RitualUltimateOperation(table.unpack(t)))
	c:RegisterEffect(e2)
	--retrieve/sset, on bounce
```

### Mitsurugi Magatama (`76725398`)

Source: [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua)

```lua
		end
	elseif e:GetLabel()==2 then
		aux.RitualUltimateOperation(s.ritual_filter,Card.GetLevel,"Greater",LOCATION_HAND,nil,s.mfilter)(e,tp,eg,ep,ev,re,r,rp)
	end
end
```
