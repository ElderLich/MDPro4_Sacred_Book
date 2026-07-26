# Auxiliary.PlaceCardsOnDeckTop

## Signature

```lua
Auxiliary.PlaceCardsOnDeckTop(int p, Group g, [int reason]) -> int
```

## Description

Sends g to the top of the Deck by reason, lets p order cards that reached either Deck when needed, and returns the number of operated cards.

## Parameters

- `p` `int`
- `g` `Group`
- `reason` `int` optional - Defaults to REASON_EFFECT.

## Returns

- `int` - The number of operated cards.

## Source

- `Utilities/utility.lua:1601`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PlaceCardsOnDeckTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dimension Conjurer | `77683371` | [Scripts/c77683371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77683371.lua) | 1 |
| Sylvan Charity | `82016179` | [Scripts/c82016179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82016179.lua) | 2 |

## Script Examples

### Dimension Conjurer (`77683371`)

Source: [Scripts/c77683371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77683371.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,p,HINTMSG_TODECK)
		local sg=tg:Select(p,ct,ct,nil)
		aux.PlaceCardsOnDeckTop(p,sg)
	end
end
```

### Sylvan Charity (`82016179`)

Source: [Scripts/c82016179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82016179.lua)

```lua
			sg1:Merge(sg2)
			Duel.ConfirmCards(1-p,sg1)
			aux.PlaceCardsOnDeckTop(p,sg1)
		else
			local hg=Duel.GetFieldGroup(p,LOCATION_HAND,0)
```
