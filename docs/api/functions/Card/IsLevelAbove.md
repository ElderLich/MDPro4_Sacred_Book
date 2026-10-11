# Card.IsLevelAbove

## Signature

```lua
Card.IsLevelAbove(Card c, int level) -> bool
```

## Description

Checks whether c has a Level greater than 0 and greater than or equal to level.

## Parameters

- `c` `Card`
- `level` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3668`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **773** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsLevelAbove) with `Card.IsLevelAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 2 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 2 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 1 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 2 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 2 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 1 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua) | 1 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 1 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 2 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua) | 1 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 1 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 1 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26534688.lua) | 1 |
| Extinguishing the Ashened | `98828338` | [Scripts/c98828338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98828338.lua) | 1 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 1 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 1 |
| Primite Fusion | `99161253` | [Scripts/c99161253.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99161253.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 2 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 3 |
| ...and 749 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
end
function s.spfilter(c,tp,sc)
	return c:IsFusionSetCard(0x1cd) and c:IsLevelAbove(7)
		and (c:IsControler(tp) or c:IsFaceup())
		and Duel.GetLocationCountFromEx(tp,tp,c,sc)>0
```

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if c==nil then return true end
	local mg=Duel.GetMatchingGroup(c96570609.otfilter,0,LOCATION_MZONE,LOCATION_MZONE,nil)
	return c:IsLevelAbove(7) and minc<=1 and Duel.CheckTribute(c,1,1,mg)
end
function c96570609.otop(e,tp,eg,ep,ev,re,r,rp,c)
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
s.fusion_effect=true
function s.eqlimit(e,c)
	return c:IsLevelAbove(5) and c:IsRace(RACE_FIEND+RACE_ZOMBIE)
end
function s.filter(c)
```
