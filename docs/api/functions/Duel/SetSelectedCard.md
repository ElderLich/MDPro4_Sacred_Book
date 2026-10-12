# Duel.SetSelectedCard

## Signature

```lua
Duel.SetSelectedCard(Card|Group targets) -> void
```

## Description

Sets the core must-select list to a Card or all cards in a Group for later selection helpers.

## Parameters

- `targets` `Card|Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5002`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetSelectedCard) with `Duel.SetSelectedCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 2 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 2 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85687952.lua) | 1 |
| Megalith Phuloch | `8805651` | [Scripts/c8805651.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8805651.lua) | 1 |
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46033517.lua) | 2 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16719140.lua) | 1 |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28711704.lua) | 1 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5556499.lua) | 1 |
| Megalith Och | `36849933` | [Scripts/c36849933.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36849933.lua) | 1 |
| Kozmo Dark Planet | `85991529` | [Scripts/c85991529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85991529.lua) | 1 |
| Megalith Ophiel | `63056220` | [Scripts/c63056220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63056220.lua) | 1 |
| Megalith Hagith | `90444325` | [Scripts/c90444325.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90444325.lua) | 1 |
| The Fabled Behilmoth | `68897338` | [Scripts/c68897338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68897338.lua) | 1 |
| King Beast Barbaros | `63972571` | [Scripts/c63972571.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63972571.lua) | 1 |
| Armor Dragon Ritual | `58827995` | [Scripts/c58827995.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58827995.lua) | 1 |
| Adamancipator Relief | `9341993` | [Scripts/c9341993.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9341993.lua) | 1 |
| Ten Thousand Dragon | `10000` | [Scripts/c10000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000.lua) | 1 |
| Duck Fighter | `54813225` | [Scripts/c54813225.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54813225.lua) | 1 |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20560620.lua) | 1 |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
				local fg=Duel.GetMustMaterial(tp,EFFECT_MUST_BE_LMATERIAL)
				if fg:IsExists(aux.MustMaterialCounterFilter,1,nil,mg) then return false end
				Duel.SetSelectedCard(fg)
				return mg:CheckSubGroup(s.LCheckGoal,minc,maxc,tp,c,gf,lmat)
			end
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
				local fg=Duel.GetMustMaterial(tp,EFFECT_MUST_BE_LMATERIAL)
				if fg:IsExists(aux.MustMaterialCounterFilter,1,nil,mg) then return false end
				Duel.SetSelectedCard(fg)
				return mg:CheckSubGroup(s.LCheckGoal,minc,maxc,tp,c,gf,lmat)
			end
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
function s.RitualCheckGreater(g,c,atk)
	if atk==0 then return false end
	Duel.SetSelectedCard(g)
	return g:CheckWithSumGreater(aux.GetCappedAttack,atk)
end
```
