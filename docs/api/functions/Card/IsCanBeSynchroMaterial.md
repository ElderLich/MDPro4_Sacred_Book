# Card.IsCanBeSynchroMaterial

## Signature

```lua
Card.IsCanBeSynchroMaterial(Card c, [Card scard], [Card tuner]) -> bool
```

## Description

Checks whether c can be used as Synchro Material for scard, with tuner supplied when the core needs the paired Tuner.

## Parameters

- `c` `Card`
- `scard` `Card` optional
- `tuner` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3640`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanBeSynchroMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33541430.lua) | 56 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 54 |
| Melffy Pinny | `34800281` | [Scripts/c34800281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34800281.lua) | 53 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 51 |
| T.G. Cyber Magician | `64910482` | [Scripts/c64910482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64910482.lua) | 47 |
| Speedroid Maliciousmagnet | `62899696` | [Scripts/c62899696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62899696.lua) | 40 |
| Tatsunoko | `55863245` | [Scripts/c55863245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55863245.lua) | 40 |
| Turbo-Tainted Hot Rod GT19 | `16769305` | [Scripts/c16769305.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16769305.lua) | 38 |
| Tatsunecro | `3096468` | [Scripts/c3096468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3096468.lua) | 37 |
| Synchro Material | `14507213` | [Scripts/c14507213.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14507213.lua) | 25 |

## Script Examples

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
end
function c57261568.synfilter(c,syncard,tuner,f)
	return c:IsFaceupEx() and c:IsCanBeSynchroMaterial(syncard,tuner) and (f==nil or f(c,syncard))
end
function c57261568.syncheck(c,g,mg,tp,lv,syncard,minc,maxc)
```

### Flower Cardian Willow with Calligrapher (`89818984`)

Source: [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua)

```lua
end
function c89818984.synfilter(c,syncard,tuner,f)
	return c:IsFaceupEx() and c:IsCanBeSynchroMaterial(syncard,tuner) and (f==nil or f(c,syncard))
end
function c89818984.syncheck(c,g,mg,tp,lv,syncard,minc,maxc)
```

### Flower Cardian Moonflowerviewing (`33541430`)

Source: [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33541430.lua)

```lua
end
function c33541430.synfilter(c,syncard,tuner,f)
	return c:IsFaceupEx() and c:IsCanBeSynchroMaterial(syncard,tuner) and (f==nil or f(c,syncard))
end
function c33541430.syncheck(c,g,mg,tp,lv,syncard,minc,maxc)
```
