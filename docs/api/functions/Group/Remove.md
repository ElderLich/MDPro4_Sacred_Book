# Group.Remove

## Signature

```lua
Group.Remove(Group g, function f, Card|nil ex, [... any]) -> void
```

## Description

Removes cards from mutable group g that satisfy f and are not ex, passing any extra arguments to f.

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|nil`
- `...` `any` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:928`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.Remove) with `Group.Remove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71442223.lua) | 1 |
| Forbidden Arts of the Gishki | `28429121` | [Scripts/c28429121.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28429121.lua) | 2 |
| Set Rotation | `73468603` | [Scripts/c73468603.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73468603.lua) | 1 |
| Gozen Match | `53334471` | [Scripts/c53334471.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53334471.lua) | 2 |
| Rivalry of Warlords | `90846359` | [Scripts/c90846359.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90846359.lua) | 2 |
| Treaty on Uniform Nomenclature | `13685271` | [Scripts/c13685271.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13685271.lua) | 1 |
| Battle of the Elements | `60530944` | [Scripts/c60530944.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60530944.lua) | 2 |
| Destructive Daruma Karma Cannon | `30748475` | [Scripts/c30748475.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30748475.lua) | 1 |

## Script Examples

### Cubic Rebirth (`71442223`)

Source: [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71442223.lua)

```lua
				Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_SPSUMMON)
				sg=g:Select(1-tp,ft,ft,nil)
				g:Remove(Card.IsLocation,nil,LOCATION_MZONE+LOCATION_GRAVE)
				Duel.SendtoGrave(g,REASON_EFFECT)
			end
```

### Forbidden Arts of the Gishki (`28429121`)

Source: [Scripts/c28429121.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28429121.lua)

```lua
	if chk==0 then
		local mg1=Duel.GetRitualMaterial(tp)
		mg1:Remove(Card.IsLocation,nil,LOCATION_HAND)
		local mg2=Duel.GetMatchingGroup(c28429121.mfilter,tp,0,LOCATION_MZONE,nil,e)
		mg1:Merge(mg2)
```

### Set Rotation (`73468603`)

Source: [Scripts/c73468603.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73468603.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(73468603,0))
	local tg1=g:Select(tp,1,1,nil)
	g:Remove(Card.IsCode,nil,tg1:GetFirst():GetCode())
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(73468603,1))
	local tg2=g:Select(tp,1,1,nil)
```
