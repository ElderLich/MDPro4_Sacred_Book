# Card.IsAbleToGrave

## Signature

```lua
Card.IsAbleToGrave(Card c) -> bool
```

## Description

Checks whether c can be sent to the Graveyard.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3587`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **592** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua) | 66 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 64 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 63 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua) | 59 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 59 |
| Fusion Destiny | `52947044` | [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52947044.lua) | 59 |
| Mementotlan Shleepy | `50042011` | [Scripts/c50042011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50042011.lua) | 58 |
| Overload Future Fusion | `33099732` | [Scripts/c33099732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33099732.lua) | 58 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 58 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Defense of the Temple | `96687733` | [Scripts/c96687733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96687733.lua) | 58 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| Dinomorphia Frenzy | `78420796` | [Scripts/c78420796.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78420796.lua) | 57 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua) | 57 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 56 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 56 |
| Extinguishing the Ashened | `98828338` | [Scripts/c98828338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98828338.lua) | 56 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 56 |
| ...and 568 more |  |  |  |

## Script Examples

### Gem-Knight Dispersion (`24220368`)

Source: [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua)

```lua
function s.filter0(c)
	return c:IsSetCard(0x1047) and not c:IsRace(RACE_ROCK)
		and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToGrave()
end
function s.filter1(c,e)
```

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
end
function c96570609.tgfilter(c)
	return c:IsSetCard(0xbe) and c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsAbleToGrave()
end
function c96570609.spfilter(c,e,tp)
```

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
end
function s.matdeckfilter(c)
	return c:IsSetCard(0x1dd) and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial() and c:IsAbleToGrave()
end
function s.matfilter1(c,e)
```
