# Auxiliary.nzatk

## Signature

```lua
Auxiliary.nzatk(Card c) -> bool
```

## Description

Filter helper that is true for face-up cards with current ATK greater than 0.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:840`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.nzatk`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 1 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 2 |
| Reptilianne Melusine | `32138660` | [Scripts/c32138660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32138660.lua) | 3 |
| Gate Guardian of Water and Thunder | `97783338` | [Scripts/c97783338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97783338.lua) | 3 |
| Dark Requiem Xyz Dragon | `1621413` | [Scripts/c1621413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1621413.lua) | 3 |
| Wattkingdom | `41790641` | [Scripts/c41790641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41790641.lua) | 1 |
| Sinful Spoils of Doom - Rciela | `16240772` | [Scripts/c16240772.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16240772.lua) | 1 |
| Ryu-Ge Realm - Wyrm Winds | `55154344` | [Scripts/c55154344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55154344.lua) | 3 |
| Conduction Warrior Linear Magnum Plus Minus | `44839512` | [Scripts/c44839512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44839512.lua) | 1 |
| Apparition | `91392974` | [Scripts/c91392974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91392974.lua) | 1 |
| Water Leviathan @Ignister | `37061511` | [Scripts/c37061511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37061511.lua) | 4 |
| Heroic Champion - Claivesolish | `97453744` | [Scripts/c97453744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97453744.lua) | 3 |
| Reptilianne Echidna | `8602351` | [Scripts/c8602351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8602351.lua) | 3 |
| Ancient Warriors Saga - Borrowing of Arrows | `33609093` | [Scripts/c33609093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33609093.lua) | 2 |
| Reptilianne Lamia | `57647597` | [Scripts/c57647597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57647597.lua) | 4 |
| Dragocytos Corrupted Nethersoul Dragon | `21435914` | [Scripts/c21435914.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21435914.lua) | 3 |
| Queen Butterfly Danaus | `13302026` | [Scripts/c13302026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13302026.lua) | 1 |
| Vision HERO Poisoner | `83414006` | [Scripts/c83414006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83414006.lua) | 2 |
| Argostars - Glorious Adra | `91438674` | [Scripts/c91438674.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91438674.lua) | 2 |
| Black-Winged Dragon | `9012916` | [Scripts/c9012916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9012916.lua) | 2 |
| Dark Anthelion Dragon | `95685352` | [Scripts/c95685352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95685352.lua) | 3 |
| You and A.I. | `32056070` | [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua) | 2 |
| Daruma Dropper | `35394356` | [Scripts/c35394356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35394356.lua) | 3 |
| ...and 11 more |  |  |  |

## Script Examples

### Earthbound Servant Geo Gremlin (`8690387`)

Source: [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua)

```lua
	local op=aux.SelectFromOptions(1-tp,
		{true,aux.Stringid(id,2)},
		{aux.nzatk(tc),aux.Stringid(id,3)})
	if op==1 then
		Duel.Destroy(tc,REASON_EFFECT)
```

### Number 99: Utopia Dragonar (`95134948`)

Source: [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua)

```lua
end
function c95134948.atkcon(e,tp,eg,ep,ev,re,r,rp)
	return tp~=Duel.GetTurnPlayer() and aux.nzatk(Duel.GetAttacker())
end
function c95134948.atkop(e,tp,eg,ep,ev,re,r,rp)
```

### Gagaga Girl - Cell Phone Subtraction (`48393693`)

Source: [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua)

```lua
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(aux.nzatk,tp,0,LOCATION_MZONE,nil)
	if chk==0 then return #g>0 end
	Duel.SetOperationInfo(0,CATEGORY_ATKCHANGE,g,1,0,0)
```
