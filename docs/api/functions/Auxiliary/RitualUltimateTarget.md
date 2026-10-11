# Auxiliary.RitualUltimateTarget

## Signature

```lua
Auxiliary.RitualUltimateTarget(function|nil filter, function level_function, string greater_or_equal, int summon_location, function|nil grave_filter, function|nil mat_filter, function|nil extra_target) -> function
```

## Description

Returns the target function for configurable Ritual Summon effects. It checks Ritual Monsters and material pools, then registers Special Summon, banish, and extra target information.

## Parameters

- `filter` `function|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `summon_location` `int`
- `grave_filter` `function|nil`
- `mat_filter` `function|nil`
- `extra_target` `function|nil`

## Returns

- `function` - Target function for a configurable Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1845`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.RitualUltimateTarget) with `Auxiliary.RitualUltimateTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Stars Align Above the Shrine | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| Mitsurugi Magatama | `76725398` | [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua) | 2 |

## Script Examples

### Stars Align Above the Shrine (`15306543`)

Source: [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15306543.lua)

```lua
	e2:SetRange(LOCATION_FZONE)
	e2:SetCountLimit(1)
	e2:SetTarget(aux.RitualUltimateTarget(table.unpack(t)))
	e2:SetOperation(aux.RitualUltimateOperation(table.unpack(t)))
	c:RegisterEffect(e2)
```

### Mitsurugi Magatama (`76725398`)

Source: [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua)

```lua
	local c1=not e:IsCostChecked() or Duel.CheckReleaseGroup(tp,s.cfilter,1,nil,tp)
	local b1=c1 and Duel.IsExistingTarget(Card.IsFaceup,tp,0,LOCATION_ONFIELD,1,nil)
	local b2=aux.RitualUltimateTarget(s.ritual_filter,Card.GetLevel,"Greater",LOCATION_HAND,nil,s.mfilter)(e,tp,eg,ep,ev,re,r,rp,0)
	if chkc then
		if e:GetLabel()~=1 then return false end
```
