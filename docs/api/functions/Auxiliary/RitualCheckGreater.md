# Auxiliary.RitualCheckGreater

## Signature

```lua
Auxiliary.RitualCheckGreater(Group g, Card c, int lv) -> bool
```

## Description

Checks whether g's Ritual Levels are greater than or equal to lv for c.

## Parameters

- `g` `Group`
- `c` `Card`
- `lv` `int`

## Returns

- `bool` - true if g reaches at least lv.

## Source

- `Utilities/procedure.lua:1767`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.RitualCheckGreater`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua) | 1 |

## Script Examples

### Emperor Tanuki's Critter Count (`20560620`)

Source: [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua)

```lua
			return tc:IsHasEffect(EFFECT_EXTRA_RITUAL_MATERIAL,tc:GetControler()) and tc:IsLocation(LOCATION_EXTRA)
		end
		function aux.RitualCheckGreater(g,rc,lv)
			if g:FilterCount(aux.rit_mat_hack_exmat_filter,nil)>1 then return false end
			Duel.SetSelectedCard(g)
```
