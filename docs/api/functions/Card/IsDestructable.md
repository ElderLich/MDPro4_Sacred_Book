# Card.IsDestructable

## Signature

```lua
Card.IsDestructable(Card c, [Effect e]) -> bool
```

## Description

Checks whether c can be destroyed.
Without e, the core only rejects Xyz Materials and cards already in the GY or banished. With e, it checks whether c is affected by e and whether effect-destruction protection applies for the current reason player.

## Parameters

- `c` `Card`
- `e` `Effect` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3571`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **86** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDestructable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 56 |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 53 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 52 |
| Rapid Trigger | `67526112` | [Scripts/c67526112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67526112.lua) | 52 |
| Odd-Eyes Pendulum Dragon of the Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 51 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 51 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 51 |
| Odd-Eyes Lancer Dragon | `83347294` | [Scripts/c83347294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83347294.lua) | 51 |
| Harpie Conductor | `85696777` | [Scripts/c85696777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85696777.lua) | 50 |
| Mythical Beast Master Cerberus | `53842431` | [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua) | 49 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 48 |
| Mythical Beast Garuda | `28570310` | [Scripts/c28570310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28570310.lua) | 48 |
| Rokket Barrage | `53481938` | [Scripts/c53481938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53481938.lua) | 48 |
| Underground Arachnid | `63465535` | [Scripts/c63465535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63465535.lua) | 48 |
| Empire of Endymion | `34041788` | [Scripts/c34041788.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34041788.lua) | 47 |
| Abyss Actor - Sassy Rookie | `51028231` | [Scripts/c51028231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51028231.lua) | 45 |
| Hollowrokket Dragon | `51548207` | [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51548207.lua) | 45 |
| ReSolfachord Dreamia | `92610868` | [Scripts/c92610868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92610868.lua) | 45 |
| Gwenhwyfar, Queen of Noble Arms | `19748583` | [Scripts/c19748583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19748583.lua) | 45 |
| Dragunity Senatus | `92868896` | [Scripts/c92868896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92868896.lua) | 45 |
| Mythical Beast Bashilisk | `80959027` | [Scripts/c80959027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80959027.lua) | 44 |
| ...and 62 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
function s.ptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsDestructable()
		and Duel.IsExistingMatchingCard(s.pfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,tp) end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,c,1,0,0)
```

### Camelot, Realm of Noble Knights and Noble Arms (`15635751`)

Source: [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua)

```lua
end
function s.dfilter(c,e)
	return c:GetEquipTarget() and c:IsDestructable(e) and not c:IsStatus(STATUS_DESTROY_CONFIRMED)
end
function s.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Heavy Interlock (`20071842`)

Source: [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua)

```lua
end
function c20071842.mfilter(c,e)
	return c:IsLevelAbove(0) and c:IsSetCard(0x102) and c:IsDestructable(e)
end
function c20071842.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
