# Auxiliary.RitualCheckEqual

## Signature

```lua
Auxiliary.RitualCheckEqual(Group g, Card c, int lv) -> bool
```

## Description

Checks whether g's Ritual Levels exactly equal lv for c.

## Parameters

- `g` `Group`
- `c` `Card`
- `lv` `int`

## Returns

- `bool` - true if g exactly matches lv.

## Source

- `Utilities/procedure.lua:1775`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.RitualCheckEqual`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Advanced Ritual Art | `46052429` | [Scripts/c46052429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46052429.lua) | 34 |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua) | 24 |

## Script Examples

### Advanced Ritual Art (`46052429`)

Source: [Scripts/c46052429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46052429.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
		aux.GCheckAdditional=function(sg) return sg:GetSum(Card.GetRitualLevel,tc)<=lv end
		local mat=mg:SelectSubGroup(tp,aux.RitualCheckEqual,true,1,99,tc,lv)
		aux.GCheckAdditional=nil
		if not mat then goto cancel end
```

### Emperor Tanuki's Critter Count (`20560620`)

Source: [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua)

```lua
			return g:CheckWithSumGreater(Card.GetRitualLevel,lv,rc)
		end
		function aux.RitualCheckEqual(g,rc,lv)
			if g:FilterCount(aux.rit_mat_hack_exmat_filter,nil)>1 then return false end
			return g:CheckWithSumEqual(Card.GetRitualLevel,lv,#g,#g,rc)
```
