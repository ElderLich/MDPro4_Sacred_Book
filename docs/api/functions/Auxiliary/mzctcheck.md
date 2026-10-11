# Auxiliary.mzctcheck

## Signature

```lua
Auxiliary.mzctcheck(Group g, int tp) -> bool
```

## Description

Returns true if tp would have an open Monster Zone after releasing g.

## Parameters

- `g` `Group`
- `tp` `int`

## Returns

- `bool` - true if tp has an open Monster Zone after releasing g.

## Source

- `Utilities/utility.lua:1166`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.mzctcheck) with `Auxiliary.mzctcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 2 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua) | 2 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 2 |
| D/D/D Vice King Requiem | `25857977` | [Scripts/c25857977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25857977.lua) | 2 |
| Indiora Doom Volt the Cubic Emperor | `3775068` | [Scripts/c3775068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3775068.lua) | 2 |
| Vulcan Dragni the Cubic King | `77387463` | [Scripts/c77387463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77387463.lua) | 2 |
| Armed Dragon LV10 White | `84425220` | [Scripts/c84425220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84425220.lua) | 1 |
| Metaphys Executor | `45148985` | [Scripts/c45148985.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45148985.lua) | 2 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 1 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 2 |
| Blade Garoodia the Cubic Beast | `78509901` | [Scripts/c78509901.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78509901.lua) | 2 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4068622.lua) | 1 |
| Buster Gundil the Cubic Behemoth | `4998619` | [Scripts/c4998619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4998619.lua) | 2 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 2 |
| Infernoid Seitsemas | `51316684` | [Scripts/c51316684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51316684.lua) | 2 |
| Awakening of the Possessed - Nefariouser Archfiend | `65268179` | [Scripts/c65268179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65268179.lua) | 1 |
| Infernoid Onuncu | `14799437` | [Scripts/c14799437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14799437.lua) | 2 |
| Awakening of the Possessed - Gagigobyte | `74426895` | [Scripts/c74426895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74426895.lua) | 1 |
| Dystopia the Despondent | `52085072` | [Scripts/c52085072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52085072.lua) | 2 |
| The Atmosphere | `14466224` | [Scripts/c14466224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14466224.lua) | 1 |
| Conduction Warrior Linear Magnum Plus Minus | `44839512` | [Scripts/c44839512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44839512.lua) | 2 |
| Awakening of the Possessed - Greater Inari Fire | `92652813` | [Scripts/c92652813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92652813.lua) | 1 |
| Transcendosaurus Meteorus | `31241087` | [Scripts/c31241087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31241087.lua) | 3 |
| Infernoid Devyaty | `23440231` | [Scripts/c23440231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23440231.lua) | 2 |
| ...and 30 more |  |  |  |

## Script Examples

### Mecha Phantom Beast Auroradon (`44097050`)

Source: [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua)

```lua
	local g=Duel.GetReleaseGroup(tp)
	local b1=Duel.CheckReleaseGroup(tp,c44097050.costfilter,1,nil,tp)
	local b2=g:GetCount()>1 and g:CheckSubGroup(aux.mzctcheck,2,2,tp)
		and Duel.IsExistingMatchingCard(c44097050.spfilter,tp,LOCATION_DECK,0,1,nil,e,tp)
	local b3=Duel.CheckReleaseGroup(tp,nil,3,nil) and Duel.IsExistingMatchingCard(c44097050.thfilter,tp,LOCATION_GRAVE,0,1,nil)
```

### Berserkion the Electromagna Warrior (`42901635`)

Source: [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua)

```lua
	local tp=c:GetControler()
	local g=Duel.GetMatchingGroup(c42901635.spcostfilter,tp,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,nil)
	return g:CheckSubGroupEach(c42901635.spchecks,aux.mzctcheck,tp)
end
function c42901635.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### Arcana Force EX - The Light Ruler (`5861892`)

Source: [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua)

```lua
	local tp=c:GetControler()
	local mg=Duel.GetMatchingGroup(c5861892.spfilter,tp,LOCATION_MZONE,0,nil)
	return mg:CheckSubGroup(aux.mzctcheck,3,3,tp)
end
function c5861892.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```
