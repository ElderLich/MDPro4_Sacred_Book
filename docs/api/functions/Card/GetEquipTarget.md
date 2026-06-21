# Card.GetEquipTarget

## Signature

```lua
Card.GetEquipTarget(Card c) -> Card
```

## Description

Returns the current artefact object

## Parameters

- `c` `Card`

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3519`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **150** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetEquipTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 65 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| [Fiendsmith Kyrie](/examples/cards/26434972) | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26434972.lua) | 61 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 56 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55749927.lua) | 56 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua) | 55 |
| Nephe Shaddoll Fusion | `60226558` | [Scripts/c60226558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60226558.lua) | 55 |
| Dragunity Arma Gram | `53184342` | [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53184342.lua) | 54 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 52 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 52 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 51 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 51 |
| Immortal Phoenix Gearfried | `22091647` | [Scripts/c22091647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22091647.lua) | 51 |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua) | 51 |
| Tragic Twin Twined Jewels | `81143465` | [Scripts/c81143465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81143465.lua) | 51 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 51 |
| Meklord Emperor Granel | `4545683` | [Scripts/c4545683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4545683.lua) | 50 |
| Plunder Patroll Parrrty | `43004235` | [Scripts/c43004235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43004235.lua) | 49 |
| Tailwind of Gusto | `1187243` | [Scripts/c1187243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1187243.lua) | 49 |
| Marincess Wonder Heart | `94207108` | [Scripts/c94207108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94207108.lua) | 49 |
| ZS - Ouroboros Sage | `32281491` | [Scripts/c32281491.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32281491.lua) | 49 |
| Super Strident Blaze | `81193865` | [Scripts/c81193865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81193865.lua) | 49 |
| ...and 126 more |  |  |  |

## Script Examples

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
end
function s.fcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():GetEquipTarget()
end
function s.filter1(c,e)
```

### Converging Wishes (`20007374`)

Source: [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua)

```lua
end
function c20007374.cacon(e,tp,eg,ep,ev,re,r,rp)
	local ec=e:GetHandler():GetEquipTarget()
	return ec and eg:IsContains(ec)
end
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
