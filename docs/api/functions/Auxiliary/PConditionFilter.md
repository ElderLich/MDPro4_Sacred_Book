# Auxiliary.PConditionFilter

## Signature

```lua
Auxiliary.PConditionFilter(Card c, Effect e, int tp, int lscale, int rscale, table eset) -> bool
```

## Description

Pendulum Summon candidate filter. It checks location, Level or pendulum_level, scales, Special Summon legality, forbidden state, and extra Pendulum Summon permissions.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `lscale` `int`
- `rscale` `int`
- `eset` `table`

## Returns

- `bool` - true if c can be Pendulum Summoned.

## Source

- `Utilities/procedure.lua:1991`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PConditionFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 2 |
| Harmonic Oscillation | `31531170` | [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua) | 4 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		if lscale>rscale then lscale,rscale=rscale,lscale end
		local g=Duel.GetFieldGroup(tp,loc,0)
		local res=g:IsExists(aux.PConditionFilter,1,nil,e,tp,lscale,rscale,eset)
		e1:Reset()
		return res
```

### Harmonic Oscillation (`31531170`)

Source: [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua)

```lua
	if ft<=0 then return false end
	if og then
		return og:IsExists(aux.PConditionFilter,1,nil,e,tp,lscale,rscale,eset)
	else
		return Duel.IsExistingMatchingCard(aux.PConditionFilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,lscale,rscale,eset)
```
