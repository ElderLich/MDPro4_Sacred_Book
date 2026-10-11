# Card.IsSummonLocation

## Signature

```lua
Card.IsSummonLocation(Card c, int loc) -> bool
```

## Description

Checks whether c's recorded Summon location contains loc. This reads the Summon information, not c's current location.

## Parameters

- `c` `Card` - Card whose recorded Summon location is checked.
- `loc` `int` - Location mask to test against the stored Summon location, such as LOCATION_EXTRA or LOCATION_GRAVE.

## Returns

- `bool` - True if any bit in loc is present in c's recorded Summon location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3557`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **212** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsSummonLocation) with `Card.IsSummonLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 1 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 1 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 1 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 1 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 1 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 2 |
| Veda Kalarcanum | `40785230` | [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40785230.lua) | 1 |
| Clear Wing Fast Dragon | `90036274` | [Scripts/c90036274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90036274.lua) | 1 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 1 |
| Fydraulis Harmonia | `70088809` | [Scripts/c70088809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70088809.lua) | 1 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua) | 1 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54725177.lua) | 1 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 1 |
| Masked HERO Furnace | `58288218` | [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58288218.lua) | 1 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 1 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 3 |
| Rapid Trigger | `67526112` | [Scripts/c67526112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67526112.lua) | 2 |
| Branded Fusion | `44362883` | [Scripts/c44362883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44362883.lua) | 1 |
| ...and 188 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
end
function c55795155.checkfilter(c)
	return c:IsType(TYPE_PENDULUM) and c:IsPreviousPosition(POS_FACEDOWN) and c:IsSummonLocation(LOCATION_EXTRA)
end
function c55795155.checkop(e,tp,eg,ep,ev,re,r,rp)
```

### Melffy Playtime Surprise (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
end
function s.tg(e,c)
	return c:IsSummonLocation(LOCATION_EXTRA) and c:IsSetCard(0x146)
end
function s.efilter(e,re)
```

### Tohushaddoll Grysta (`95072744`)

Source: [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua)

```lua
end
function s.counterfilter(c)
	return not c:IsSummonLocation(LOCATION_EXTRA) or c:IsSetCard(0x9d) and c:IsFaceup()
end
function s.rfilter(c)
```
