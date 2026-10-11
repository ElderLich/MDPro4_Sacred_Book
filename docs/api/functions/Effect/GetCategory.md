# Effect.GetCategory

## Signature

```lua
Effect.GetCategory(Effect e) -> int
```

## Description

Returns e's category bitmask.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:637`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetCategory) with `Effect.GetCategory`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 2 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 2 |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua) | 1 |
| Tally-ho! Springans | `9175957` | [Scripts/c9175957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9175957.lua) | 2 |
| Gunkan Suship Shirauo-class Carrier | `21293424` | [Scripts/c21293424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21293424.lua) | 1 |
| Evigishki Neremanas | `88926295` | [Scripts/c88926295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88926295.lua) | 2 |
| Virakam, the Divine Spirit of Artifice | `10673071` | [Scripts/c10673071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10673071.lua) | 2 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua) | 1 |
| Awakening of the Crystal Ultimates | `12877076` | [Scripts/c12877076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12877076.lua) | 1 |
| Tri-Edge Master | `52445243` | [Scripts/c52445243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52445243.lua) | 1 |
| Linguriboh | `24842059` | [Scripts/c24842059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24842059.lua) | 2 |
| Recette de Poisson (Fish Recipe) | `87778106` | [Scripts/c87778106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87778106.lua) | 1 |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
	end
	if re:GetActivateLocation()==LOCATION_GRAVE then
		e:SetCategory(e:GetCategory()|CATEGORY_GRAVE_ACTION)
	else
		e:SetCategory(e:GetCategory()&~CATEGORY_GRAVE_ACTION)
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	end
	if re:GetActivateLocation()==LOCATION_GRAVE then
		e:SetCategory(e:GetCategory()|CATEGORY_GRAVE_ACTION)
	else
		e:SetCategory(e:GetCategory()&~CATEGORY_GRAVE_ACTION)
```

### Darklord Uprising (`54527349`)

Source: [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua)

```lua
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
	local cat=e:GetCategory()
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) and label==100 and rec>0 then
		e:SetCategory(bit.bor(cat,CATEGORY_RECOVER))
```
