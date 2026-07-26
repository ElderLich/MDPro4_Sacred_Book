# Duel.AnnounceRace

## Signature

```lua
Duel.AnnounceRace(int player, int count, int available) -> int
```

## Description

Lets player declare count Races from available and returns the selected RACE_* bitmask.

## Parameters

- `player` `int`
- `count` `int`
- `available` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5029`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.AnnounceRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 2 |
| Theorealize | `48739627` | [Scripts/c48739627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48739627.lua) | 2 |
| Spiritual Art Familiars | `45538320` | [Scripts/c45538320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45538320.lua) | 2 |
| Archnemeses Eschatos | `33212663` | [Scripts/c33212663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33212663.lua) | 1 |
| Shipping Archfiend | `57256127` | [Scripts/c57256127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57256127.lua) | 1 |
| Metal Illusionist | `29157292` | [Scripts/c29157292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29157292.lua) | 1 |
| Herald of the Abyss | `94016752` | [Scripts/c94016752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94016752.lua) | 1 |
| Mimesis Elephant | `10632284` | [Scripts/c10632284.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10632284.lua) | 1 |
| Propa Gandake | `61681816` | [Scripts/c61681816.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61681816.lua) | 1 |
| Genomix Fighter | `42155488` | [Scripts/c42155488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42155488.lua) | 1 |
| Specimen Inspection | `12292422` | [Scripts/c12292422.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12292422.lua) | 1 |
| Reprodocus | `34989413` | [Scripts/c34989413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34989413.lua) | 1 |
| Sword Breaker | `64689404` | [Scripts/c64689404.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64689404.lua) | 1 |
| Baby Mudragon | `40380686` | [Scripts/c40380686.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40380686.lua) | 1 |
| Symphonic Warrior Piaano | `31826057` | [Scripts/c31826057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31826057.lua) | 2 |
| Tribe-Infecting Virus | `33184167` | [Scripts/c33184167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33184167.lua) | 1 |
| Rebirth Judgment | `45064756` | [Scripts/c45064756.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45064756.lua) | 1 |
| Gishki Psychelone | `30334522` | [Scripts/c30334522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30334522.lua) | 1 |
| The Regulation of Tribe | `296499` | [Scripts/c296499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c296499.lua) | 1 |
| Abyssal Designator | `89801755` | [Scripts/c89801755.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89801755.lua) | 1 |
| Shien's Advisor | `98126725` | [Scripts/c98126725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98126725.lua) | 1 |
| Quantum Cat | `87772572` | [Scripts/c87772572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87772572.lua) | 1 |
| Swamp Mirrorer | `50277973` | [Scripts/c50277973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50277973.lua) | 1 |
| Dimensional Allotrope Varis | `52254878` | [Scripts/c52254878.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52254878.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RACE)
	if ATTRIBUTE_ALL&~tc:GetAttribute()==0 then
		race=Duel.AnnounceRace(tp,1,RACE_ALL&~tc:GetRace())
	else
		race=Duel.AnnounceRace(tp,1,RACE_ALL)
```

### Theorealize (`48739627`)

Source: [Scripts/c48739627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48739627.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RACE)
	if ATTRIBUTE_ALL&~tc:GetAttribute()==0 then
		race=Duel.AnnounceRace(tp,1,RACE_ALL&~tc:GetRace())
	else
		race=Duel.AnnounceRace(tp,1,RACE_ALL)
```

### Spiritual Art Familiars (`45538320`)

Source: [Scripts/c45538320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45538320.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RACE)
	if ATTRIBUTE_ALL&~c:GetAttribute()==0 then
		race=Duel.AnnounceRace(tp,1,RACE_ALL&~c:GetRace())
	else
		race=Duel.AnnounceRace(tp,1,RACE_ALL)
```
