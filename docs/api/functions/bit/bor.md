# bit.bor

## Signature

```lua
bit.bor(any a, any b) -> void
```

## Description

A or b

## Parameters

- `a` `any`
- `b` `any`

## Source

- `Utilities/utility.lua:18`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **52** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `bit.bor`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 55 |
| Invoked Transcendence Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 55 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 55 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 55 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57761191.lua) | 54 |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua) | 54 |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 53 |
| Chaofeng, Phantom of the Yang Zing | `19048328` | [Scripts/c19048328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19048328.lua) | 51 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua) | 51 |
| Folgo, Justice Fur Hire | `66023650` | [Scripts/c66023650.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66023650.lua) | 48 |
| Clown Crew Matinee Operatics | `57847269` | [Scripts/c57847269.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57847269.lua) | 47 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 47 |
| Tindangle Base Gardna | `94365540` | [Scripts/c94365540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94365540.lua) | 46 |
| Master Peace, the True Dracoslaying King | `21377582` | [Scripts/c21377582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21377582.lua) | 46 |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 44 |
| Elementsaber Lapauila Mana | `71797713` | [Scripts/c71797713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71797713.lua) | 42 |
| Mekk-Knight Red Moon | `56809158` | [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua) | 41 |
| Mekk-Knight Blue Sky | `20537097` | [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua) | 39 |
| Ancient Gear Reactor Dragon | `44874522` | [Scripts/c44874522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44874522.lua) | 38 |
| Mekk-Knight Green Horizon | `66022706` | [Scripts/c66022706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66022706.lua) | 38 |
| Rokket Caliber | `67127799` | [Scripts/c67127799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67127799.lua) | 38 |
| Mekk-Knight Yellow Star | `29415459` | [Scripts/c29415459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29415459.lua) | 38 |
| Ancient Warriors Saga - Sun-Liu Alliance | `58116537` | [Scripts/c58116537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58116537.lua) | 37 |
| ...and 28 more |  |  |  |

## Script Examples

### Mecha Phantom Beast Auroradon (`44097050`)

Source: [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua)

```lua
	if sel==1 then
		local dg=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
		e:SetCategory(bit.bor(cat,CATEGORY_DESTROY))
		Duel.SetOperationInfo(0,CATEGORY_DESTROY,dg,1,0,0)
	elseif sel==2 then
```

### Link into the VRAINS! (`28827503`)

Source: [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua)

```lua
		local tc=g:GetFirst()
		while tc do
			race=bit.bor(race,tc:GetOriginalRace())
			tc=g:GetNext()
		end
```

### Invoked Transcendence Aeon (`33166263`)

Source: [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua)

```lua
	local att=0
	for tc in aux.Next(g) do
		att=bit.bor(att,(0x7f-tc:GetAttribute()))
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATTRIBUTE)
```
