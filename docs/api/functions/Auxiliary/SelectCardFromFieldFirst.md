# Auxiliary.SelectCardFromFieldFirst

## Signature

```lua
Auxiliary.SelectCardFromFieldFirst(int tp, function f, int player, int s, int o, int min, int max, any ex, ... any) -> Group
```

## Description

Selection helper that first offers matching on-field cards with HINTMSG_FIELD_FIRST. If that selection is canceled, it restores the previous hint and falls back to Duel.SelectMatchingCard.

## Parameters

- `tp` `int`
- `f` `function`
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `any`
- `...` `any`

## Returns

- `Group` - The selected cards.

## Source

- `Utilities/utility.lua:1379`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SelectCardFromFieldFirst`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Majestic Mirage | `98020526` | [Scripts/c98020526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98020526.lua) | 46 |
| Dark Contract with the Entities | `60168186` | [Scripts/c60168186.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60168186.lua) | 45 |
| Doomking Balerdroch | `39185163` | [Scripts/c39185163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39185163.lua) | 31 |
| Kozmojo | `90452877` | [Scripts/c90452877.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90452877.lua) | 25 |

## Script Examples

### Majestic Mirage (`98020526`)

Source: [Scripts/c98020526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98020526.lua)

```lua
	elseif opval[op]==2 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		local rg=aux.SelectCardFromFieldFirst(tp,aux.NecroValleyFilter(c98020526.rfilter),tp,0,LOCATION_MZONE+LOCATION_GRAVE,1,1,nil)
		Duel.HintSelection(rg)
		Duel.Remove(rg,POS_FACEUP,REASON_EFFECT)
```

### Dark Contract with the Entities (`60168186`)

Source: [Scripts/c60168186.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60168186.lua)

```lua
function c60168186.rmop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g=aux.SelectCardFromFieldFirst(tp,Card.IsAbleToRemove,tp,LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE,1,1,nil)
	if g:GetCount()>0 then
		Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
```

### Doomking Balerdroch (`39185163`)

Source: [Scripts/c39185163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39185163.lua)

```lua
	else
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		local g=aux.SelectCardFromFieldFirst(tp,c39185163.filter,tp,LOCATION_MZONE+LOCATION_GRAVE,LOCATION_MZONE+LOCATION_GRAVE,1,1,nil)
		Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
		Duel.RegisterFlagEffect(tp,39185164,RESET_PHASE+PHASE_END,0,1)
```
