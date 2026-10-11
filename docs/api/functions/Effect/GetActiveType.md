# Effect.GetActiveType

## Signature

```lua
Effect.GetActiveType(Effect e) -> int
```

## Description

Returns the active effect type, such as monster, Spell, or Trap. This can differ from the type of the card that activated the effect, such as Pendulum effects being treated as Spell effects.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:646`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetActiveType) with `Effect.GetActiveType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 1 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua) | 1 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 1 |
| Artifact Durendal | `69840739` | [Scripts/c69840739.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69840739.lua) | 2 |
| Myutant Synthesis | `79194594` | [Scripts/c79194594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79194594.lua) | 1 |
| Krishnerd Witch | `37006702` | [Scripts/c37006702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37006702.lua) | 1 |
| Grapha, Dragon Overlord of Dark World | `39552584` | [Scripts/c39552584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39552584.lua) | 2 |
| Exosister Karmael | `77675029` | [Scripts/c77675029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77675029.lua) | 2 |
| Baromet the Sacred Sheep Shrub | `62967433` | [Scripts/c62967433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62967433.lua) | 1 |
| Van'Dalgyon the Dark Dragon Lord | `24857466` | [Scripts/c24857466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24857466.lua) | 1 |
| Myutant Ultimus | `6182103` | [Scripts/c6182103.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6182103.lua) | 1 |
| Arias the Labrynth Butler | `73602965` | [Scripts/c73602965.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73602965.lua) | 1 |
| Sacred Tree Beast, Hyperyton | `9349094` | [Scripts/c9349094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9349094.lua) | 3 |
| Abyss Actor - Extras | `88412339` | [Scripts/c88412339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88412339.lua) | 1 |
| Pendulum Call | `53208660` | [Scripts/c53208660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53208660.lua) | 1 |
| Ryu Senshi | `49868263` | [Scripts/c49868263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49868263.lua) | 1 |
| Vylon Alpha | `56768355` | [Scripts/c56768355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56768355.lua) | 1 |
| Invoked Mechaba | `75286621` | [Scripts/c75286621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75286621.lua) | 1 |
| Dark Eradicator Warlock | `29436665` | [Scripts/c29436665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29436665.lua) | 1 |
| Vortex of Time | `42138622` | [Scripts/c42138622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42138622.lua) | 1 |
| Arcana Knight Joker | `6150044` | [Scripts/c6150044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6150044.lua) | 1 |
| Des Volstgalph | `81059524` | [Scripts/c81059524.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81059524.lua) | 1 |
| Dark Balter the Terrible | `80071763` | [Scripts/c80071763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071763.lua) | 1 |
| Serial Spell | `49398568` | [Scripts/c49398568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49398568.lua) | 1 |
| ...and 12 more |  |  |  |

## Script Examples

### Beyond the Pendulum (`22125101`)

Source: [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua)

```lua
function c22125101.disop(e,tp,eg,ep,ev,re,r,rp)
	local p,loc=Duel.GetChainInfo(ev,CHAININFO_TRIGGERING_CONTROLER,CHAININFO_TRIGGERING_LOCATION)
	if re:GetActiveType()==TYPE_PENDULUM+TYPE_SPELL and p==tp and bit.band(loc,LOCATION_PZONE)~=0 then
		Duel.NegateEffect(ev)
	end
```

### Arcana Extra Joker (`64454614`)

Source: [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua)

```lua
end
function c64454614.negcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local rtype=bit.band(re:GetActiveType(),0x7)
	if chk==0 then return Duel.IsExistingMatchingCard(c64454614.costfilter,tp,LOCATION_HAND,0,1,nil,rtype) end
	Duel.DiscardHand(tp,c64454614.costfilter,1,1,REASON_COST+REASON_DISCARD,nil,rtype)
```

### PenduLuMoon (`66150724`)

Source: [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua)

```lua
function c66150724.disop(e,tp,eg,ep,ev,re,r,rp)
	local p,loc=Duel.GetChainInfo(ev,CHAININFO_TRIGGERING_CONTROLER,CHAININFO_TRIGGERING_LOCATION)
	if re:GetActiveType()==TYPE_PENDULUM+TYPE_SPELL and p==tp and bit.band(loc,LOCATION_PZONE)~=0 then
		Duel.NegateEffect(ev)
	end
```
