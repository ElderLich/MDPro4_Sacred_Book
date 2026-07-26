# Auxiliary.PConditionExtraFilterSpecific

## Signature

```lua
Auxiliary.PConditionExtraFilterSpecific(Card c, Effect e, int tp, int lscale, int rscale, Effect|nil te) -> bool
```

## Description

Checks whether one extra Pendulum Summon effect allows c for the current scales.

## Parameters

- `c` `Card`
- `e` `Effect`
- `tp` `int`
- `lscale` `int`
- `rscale` `int`
- `te` `Effect|nil`

## Returns

- `bool` - true if te allows c or te is nil.

## Source

- `Utilities/procedure.lua:1980`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PConditionExtraFilterSpecific`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| Harmonic Oscillation | `31531170` | [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua) | 1 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	if ft2>0 then loc=loc|LOCATION_EXTRA end
	local tg=Duel.GetMatchingGroup(aux.PConditionFilter,tp,loc,0,nil,e,tp,lscale,rscale,eset)
	tg=tg:Filter(aux.PConditionExtraFilterSpecific,nil,e,tp,lscale,rscale,e1)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	aux.GCheckAdditional=aux.PendOperationCheck(ft1,ft2,ft)
```

### Harmonic Oscillation (`31531170`)

Source: [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua)

```lua
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=tg:FilterSelect(tp,aux.PConditionExtraFilterSpecific,0,ft,nil,e,tp,lscale,rscale,ce)
	if #g==0 then return end
	if ce then
```
