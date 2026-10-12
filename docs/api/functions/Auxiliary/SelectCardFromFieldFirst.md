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

- `Utilities/utility.lua:1382`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SelectCardFromFieldFirst) with `Auxiliary.SelectCardFromFieldFirst`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ekhajar, Descendant Dragon of the Ice Barrier | `65424481` | [Scripts/c65424481.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65424481.lua) | 2 |
| Majestic Mirage | `98020526` | [Scripts/c98020526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98020526.lua) | 1 |
| Dark Contract with the Entities | `60168186` | [Scripts/c60168186.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60168186.lua) | 1 |
| Barian's Seal | `38001022` | [Scripts/c38001022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38001022.lua) | 1 |
| Doomking Balerdroch | `39185163` | [Scripts/c39185163.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39185163.lua) | 1 |
| Kozmojo | `90452877` | [Scripts/c90452877.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90452877.lua) | 1 |

## Script Examples

### Ekhajar, Descendant Dragon of the Ice Barrier (`65424481`)

Source: [Scripts/c65424481.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65424481.lua)

```lua
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=aux.SelectCardFromFieldFirst(tp,aux.NecroValleyFilter(Card.IsAbleToHand),tp,LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE,1,1,nil)
	if g:GetCount()>0 then
		Duel.HintSelection(g)
```

### Majestic Mirage (`98020526`)

Source: [Scripts/c98020526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98020526.lua)

```lua
	elseif opval[op]==2 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		local rg=aux.SelectCardFromFieldFirst(tp,aux.NecroValleyFilter(c98020526.rfilter),tp,0,LOCATION_MZONE+LOCATION_GRAVE,1,1,nil)
		Duel.HintSelection(rg)
		Duel.Remove(rg,POS_FACEUP,REASON_EFFECT)
```

### Dark Contract with the Entities (`60168186`)

Source: [Scripts/c60168186.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60168186.lua)

```lua
function c60168186.rmop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g=aux.SelectCardFromFieldFirst(tp,Card.IsAbleToRemove,tp,LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE,1,1,nil)
	if g:GetCount()>0 then
		Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
```
