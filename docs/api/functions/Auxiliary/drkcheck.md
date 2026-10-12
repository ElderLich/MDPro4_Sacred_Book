# Auxiliary.drkcheck

## Signature

```lua
Auxiliary.drkcheck(Group g) -> void
```

## Description

Returns true if every card in g has a different Rank.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:1137`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.drkcheck) with `Auxiliary.drkcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23187256.lua) | 1 |
| Garbage Golem | `28968609` | [Scripts/c28968609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28968609.lua) | 1 |

## Script Examples

### Number 93: Utopia Kaiser (`23187256`)

Source: [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23187256.lua)

```lua
	if g1:GetCount()>0 and ct>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		aux.GCheckAdditional=aux.drkcheck
		local g2=g1:SelectSubGroup(tp,aux.TRUE,false,1,ct)
		aux.GCheckAdditional=nil
```

### Garbage Golem (`28968609`)

Source: [Scripts/c28968609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28968609.lua)

```lua
	if chk==0 then return g:GetClassCount(Card.GetRank)>2 end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local sg=g:SelectSubGroup(tp,aux.drkcheck,false,3,3)
	Duel.ConfirmCards(1-tp,sg)
end
```
