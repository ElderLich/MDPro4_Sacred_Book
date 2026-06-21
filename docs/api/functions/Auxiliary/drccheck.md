# Auxiliary.drccheck

## Signature

```lua
Auxiliary.drccheck(Group g) -> void
```

## Description

Returns true if every card in g has a different Race.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:1146`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.drccheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Bujin Torifune | `29981935` | [Scripts/c29981935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29981935.lua) | 47 |
| Carpiponica, Mystical Beast of the Forest | `85055821` | [Scripts/c85055821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85055821.lua) | 41 |
| Pot of Dichotomy | `98672567` | [Scripts/c98672567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98672567.lua) | 38 |
| Tribe Drive | `90969892` | [Scripts/c90969892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90969892.lua) | 34 |
| Sky Scourge Cidhels | `15792576` | [Scripts/c15792576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15792576.lua) | 34 |

## Script Examples

### Bujin Torifune (`29981935`)

Source: [Scripts/c29981935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29981935.lua)

```lua
	local g=Duel.GetMatchingGroup(c29981935.spfilter,tp,LOCATION_DECK,0,nil,e,tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sg=g:SelectSubGroup(tp,aux.drccheck,false,2,2)
	if sg then
		Duel.SpecialSummon(sg,0,tp,tp,false,false,POS_FACEUP_DEFENSE)
```

### Carpiponica, Mystical Beast of the Forest (`85055821`)

Source: [Scripts/c85055821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85055821.lua)

```lua
	local g=Duel.GetMatchingGroup(c85055821.tdfilter,tp,LOCATION_GRAVE,0,e:GetHandler(),e)
	if chkc then return false end
	if chk==0 then return g:CheckSubGroup(aux.drccheck,2,2)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false) end
```

### Pot of Dichotomy (`98672567`)

Source: [Scripts/c98672567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98672567.lua)

```lua
	local g=Duel.GetMatchingGroup(c98672567.filter,tp,LOCATION_GRAVE,0,nil,e)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g1=g:SelectSubGroup(tp,aux.drccheck,false,3,3)
	Duel.SetTargetCard(g1)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,g1,3,0,0)
```
