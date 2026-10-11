# bit.bor

## Signature

```lua
bit.bor(int a, int b) -> int
```

## Description

Returns the bitwise OR of a and b.

## Parameters

- `a` `int`
- `b` `int`

## Returns

- `int`

## Source

- `Utilities/utility.lua:18`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=bit.bor) with `bit.bor`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 3 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 1 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Hyperinvoked Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57761191.lua) | 1 |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua) | 1 |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 2 |
| Chaofeng, Phantom of the Yang Zing | `19048328` | [Scripts/c19048328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19048328.lua) | 2 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua) | 3 |
| Folgo, Justice Fur Hire | `66023650` | [Scripts/c66023650.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66023650.lua) | 1 |
| Clown Crew Matinee Operatics | `57847269` | [Scripts/c57847269.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57847269.lua) | 1 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 1 |
| Distrust Paranoia | `81965543` | [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81965543.lua) | 1 |
| Tindangle Base Gardna | `94365540` | [Scripts/c94365540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94365540.lua) | 1 |
| Master Peace, the True Dracoslaying King | `21377582` | [Scripts/c21377582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21377582.lua) | 1 |
| Angelechy Enlisted | `81797573` | [Scripts/c81797573.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81797573.lua) | 4 |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 1 |
| Elementsaber Lapauila Mana | `71797713` | [Scripts/c71797713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71797713.lua) | 3 |
| Mekk-Knight Red Moon | `56809158` | [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua) | 2 |
| Mekk-Knight Blue Sky | `20537097` | [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua) | 2 |
| Ancient Gear Reactor Dragon | `44874522` | [Scripts/c44874522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44874522.lua) | 2 |
| Mekk-Knight Green Horizon | `66022706` | [Scripts/c66022706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66022706.lua) | 2 |
| Rokket Caliber | `67127799` | [Scripts/c67127799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67127799.lua) | 1 |
| ...and 30 more |  |  |  |

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

### Genex Ally Triforce (`52709508`)

Source: [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua)

```lua
	while tc do
		if not tc:IsType(TYPE_TUNER) then
			att=bit.bor(att,tc:GetAttribute())
		end
		tc=g:GetNext()
```
