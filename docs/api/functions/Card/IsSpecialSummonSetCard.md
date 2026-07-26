# Card.IsSpecialSummonSetCard

## Signature

```lua
Card.IsSpecialSummonSetCard(Card c, ... int) -> bool
```

## Description

Checks whether c was Special Summoned by a card whose name includes setname.

## Parameters

- `c` `Card`
- `...` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3401`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSpecialSummonSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92332424.lua) | 1 |
| Hyper Rank-Up-Magic Utopiforce | `67517351` | [Scripts/c67517351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67517351.lua) | 1 |
| Baelgrill de Nouvelles | `88890658` | [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88890658.lua) | 1 |
| World of Prophecy | `29146185` | [Scripts/c29146185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29146185.lua) | 1 |
| Barian Untopia | `30761649` | [Scripts/c30761649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30761649.lua) | 1 |
| Balameuniere de Nouvelles | `52495649` | [Scripts/c52495649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52495649.lua) | 2 |
| Phantasos, the Dream Mirror Friend | `62393472` | [Scripts/c62393472.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62393472.lua) | 1 |
| Neiroy, the Dream Mirror Disciple | `18189187` | [Scripts/c18189187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18189187.lua) | 1 |
| P.U.N.K. JAM Dragon Drive | `28403802` | [Scripts/c28403802.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28403802.lua) | 1 |
| Chef's Special Recipe | `87955518` | [Scripts/c87955518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87955518.lua) | 1 |
| Morpheus, the Dream Mirror Black Knight | `38267552` | [Scripts/c38267552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38267552.lua) | 1 |
| Brotherhood of the Fire Fist - Ram | `62694833` | [Scripts/c62694833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62694833.lua) | 1 |
| Morpheus, the Dream Mirror White Knight | `1872843` | [Scripts/c1872843.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1872843.lua) | 1 |
| Raidraptor - Rudder Strix | `6552938` | [Scripts/c6552938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6552938.lua) | 1 |
| K9-X "Ripper/M" | `31286915` | [Scripts/c31286915.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31286915.lua) | 1 |
| Ikelos, the Dream Mirror Sprite | `49389190` | [Scripts/c49389190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49389190.lua) | 1 |
| Fortune Lady Fire | `71870152` | [Scripts/c71870152.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71870152.lua) | 1 |
| Phantasos, the Dream Mirror Foe | `99792080` | [Scripts/c99792080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99792080.lua) | 1 |
| Brotherhood of the Fire Fist - Rooster | `30929786` | [Scripts/c30929786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30929786.lua) | 1 |
| Metaphys Nephthys | `72355272` | [Scripts/c72355272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72355272.lua) | 1 |
| Ikelos, the Dream Mirror Mara | `75888208` | [Scripts/c75888208.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75888208.lua) | 1 |
| Metaphys Daedalus | `45960523` | [Scripts/c45960523.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45960523.lua) | 1 |
| Mermail Abyssdine | `74298287` | [Scripts/c74298287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74298287.lua) | 1 |
| Evo-Price | `14154221` | [Scripts/c14154221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14154221.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### Majesty Pegasus, the Dracoslayer (`92332424`)

Source: [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92332424.lua)

```lua
function c92332424.thcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsSummonType(SUMMON_TYPE_PENDULUM) or c:IsSpecialSummonSetCard(0xc7)
end
function c92332424.thfilter(c)
```

### Hyper Rank-Up-Magic Utopiforce (`67517351`)

Source: [Scripts/c67517351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67517351.lua)

```lua
	local typ,rk=c:GetSpecialSummonInfo(SUMMON_INFO_TYPE,SUMMON_INFO_RANK)
	return c:IsFaceup() and c:IsType(TYPE_XYZ) and c:IsCanBeEffectTarget(e)
		and typ&TYPE_XYZ~=0 and rk>=10 and c:IsSpecialSummonSetCard(0x7f)
end
function c67517351.matcon(e,tp,eg,ep,ev,re,r,rp)
```

### Baelgrill de Nouvelles (`88890658`)

Source: [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88890658.lua)

```lua
	if chk==0 then return Duel.IsExistingMatchingCard(aux.NegateAnyFilter,tp,0,LOCATION_ONFIELD,1,nil) end
	local c=e:GetHandler()
	local res=c:GetSpecialSummonInfo(SUMMON_INFO_TYPE)&TYPE_MONSTER~=0 and c:IsSpecialSummonSetCard(0x196) and 1 or 0
	e:SetLabel(res)
	local g=Duel.GetMatchingGroup(aux.NegateAnyFilter,tp,0,LOCATION_ONFIELD,nil)
```
