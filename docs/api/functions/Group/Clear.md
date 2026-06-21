# Group.Clear

## Signature

```lua
Group.Clear(Group g) -> void
```

## Description

Empty the deck

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:905`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.Clear`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| Black Dragon Ninja | `56562619` | [Scripts/c56562619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56562619.lua) | 59 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua) | 56 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 56 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79755671.lua) | 54 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Smile Action | `47870325` | [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua) | 51 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 50 |
| Hushed Psychic Cleric | `25343017` | [Scripts/c25343017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25343017.lua) | 49 |
| Artmage Academic Arcane Arts Acropolis | `74733322` | [Scripts/c74733322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74733322.lua) | 48 |
| Overmind Archfiend | `24221808` | [Scripts/c24221808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24221808.lua) | 46 |
| Tiki Soul | `49514333` | [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua) | 43 |
| Battle Survivor | `64178868` | [Scripts/c64178868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64178868.lua) | 38 |
| Destiny HERO - Captain Tenacious | `77608643` | [Scripts/c77608643.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77608643.lua) | 38 |
| Overdoom Line | `87046457` | [Scripts/c87046457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87046457.lua) | 38 |
| Sacred Serpent's Wake | `98850929` | [Scripts/c98850929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98850929.lua) | 36 |
| Contract with Don Thousand | `56673480` | [Scripts/c56673480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56673480.lua) | 35 |
| Pole Position | `73578229` | [Scripts/c73578229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73578229.lua) | 30 |
| Kotodama | `19406822` | [Scripts/c19406822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19406822.lua) | 29 |
| Tornado Bird | `71283180` | [Scripts/c71283180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71283180.lua) | 24 |
| Greenkappa | `61831093` | [Scripts/c61831093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61831093.lua) | 23 |

## Script Examples

### Dracotail Shaulas (`42125140`)

Source: [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua)

```lua
		local _,meg=Duel.CheckEvent(EVENT_MOVE,true)
		if meg:IsContains(c) and (c:IsFaceup() or c:IsPublic()) then
			g:Clear()
		end
	end
```

### Black Dragon Ninja (`56562619`)

Source: [Scripts/c56562619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56562619.lua)

```lua
			Duel.SpecialSummon(sg,0,tp,sg:GetFirst():GetOwner(),false,false,POS_FACEUP)
		end
		rg:Clear()
		return
	end
```

### Dracotail Arthalion (`33760966`)

Source: [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua)

```lua
		local _,meg=Duel.CheckEvent(EVENT_MOVE,true)
		if meg:IsContains(c) and (c:IsFaceup() or c:IsPublic()) then
			g:Clear()
		end
	end
```
