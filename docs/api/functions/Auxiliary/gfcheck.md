# Auxiliary.gfcheck

## Signature

```lua
Auxiliary.gfcheck(Group g, function f, any a1, any a2) -> bool
```

## Description

Checks a 2-card group against one filter in either order: one card must satisfy f(c,a1) and the other f(c,a2).

## Parameters

- `g` `Group`
- `f` `function`
- `a1` `any`
- `a2` `any`

## Returns

- `bool` - true if the two cards satisfy the filter in either order.

## Source

- `Utilities/utility.lua:1153`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.gfcheck) with `Auxiliary.gfcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 1 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua) | 2 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 1 |
| Dinomorphia Frenzy | `78420796` | [Scripts/c78420796.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78420796.lua) | 1 |
| Thunder Dragonduo | `55591586` | [Scripts/c55591586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55591586.lua) | 2 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82301904.lua) | 2 |
| Vanquish Soul Heavy Borger | `92895501` | [Scripts/c92895501.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92895501.lua) | 2 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 1 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 2 |
| Concours de Cuisine (Culinary Confrontation) | `14283055` | [Scripts/c14283055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14283055.lua) | 1 |
| Vanquish Soul Hollie Sue | `93156774` | [Scripts/c93156774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93156774.lua) | 4 |
| Envoy of Chaos | `38695361` | [Scripts/c38695361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38695361.lua) | 2 |
| Chaos Ruler, the Chaotic Magical Dragon | `3040496` | [Scripts/c3040496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3040496.lua) | 2 |
| Master of Chaos | `85059922` | [Scripts/c85059922.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85059922.lua) | 2 |
| EN - Engage Neo Space | `80170678` | [Scripts/c80170678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80170678.lua) | 1 |
| Vanquish Soul Dr. Mad Love | `29280200` | [Scripts/c29280200.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280200.lua) | 2 |
| Evil Eyes Unleashed | `8775395` | [Scripts/c8775395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8775395.lua) | 1 |
| Tellarknight Constellar Caduceus | `58858807` | [Scripts/c58858807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58858807.lua) | 1 |
| The Chaos Creator | `90488465` | [Scripts/c90488465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90488465.lua) | 2 |
| Chaos End Ruler - Ruler of the Beginning and the End | `41424250` | [Scripts/c41424250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41424250.lua) | 2 |
| Chaos Beast | `49565413` | [Scripts/c49565413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49565413.lua) | 2 |
| Black Luster Soldier - Envoy of the Beginning | `72989439` | [Scripts/c72989439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72989439.lua) | 2 |
| Master Peace, the True Dracoslayer | `34079868` | [Scripts/c34079868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34079868.lua) | 1 |
| EN Shuffle | `10186633` | [Scripts/c10186633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10186633.lua) | 1 |
| ...and 17 more |  |  |  |

## Script Examples

### Tellusion the Magna Warrior (`24431911`)

Source: [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua)

```lua
end
function s.gcheck(g,tp)
	return aux.gfcheck(g,Card.IsCode,51826619,87814728)
		and Duel.GetMZoneCount(tp,g)>0
end
```

### Chaos Emperor, the Dragon of Armageddon (`4538826`)

Source: [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua)

```lua
	return ((c:IsLocation(LOCATION_HAND) and Duel.GetLocationCount(tp,LOCATION_MZONE)>0) or
		(c:IsLocation(LOCATION_EXTRA) and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0))
		and g:CheckSubGroup(aux.gfcheck,2,2,Card.IsAttribute,ATTRIBUTE_LIGHT,ATTRIBUTE_DARK)
end
function c4538826.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### A-to-Z-Dragon Buster Cannon (`65172015`)

Source: [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua)

```lua
end
function c65172015.fselect(g,tp,sc)
	return aux.gfcheck(g,Card.IsOriginalCodeRule,1561110,91998119)
		and Duel.GetLocationCountFromEx(tp,tp,g,sc)>0
end
```
