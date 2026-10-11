# Duel.SetSynchroMaterial

## Signature

```lua
Duel.SetSynchroMaterial(Group g) -> void
```

## Description

Stores g as the Synchro Material group for the current Synchro Material custom procedure.
Local standard Synchro helpers usually keep their selected material group on the procedure effect instead; this function appears in custom material-provider scripts such as Flower Cardian Synchro helpers.
This records the selected group for the core. It does not move those cards and returns no value.

## Parameters

- `g` `Group` - Selected Synchro Material group to store for the custom procedure.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4991`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetSynchroMaterial) with `Duel.SetSynchroMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33541430.lua) | 1 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 1 |
| T.G. Cyber Magician | `64910482` | [Scripts/c64910482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64910482.lua) | 1 |
| Tatsunoko | `55863245` | [Scripts/c55863245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55863245.lua) | 1 |
| Tatsunecro | `3096468` | [Scripts/c3096468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3096468.lua) | 1 |

## Script Examples

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
		g:Merge(sg)
	end
	Duel.SetSynchroMaterial(g)
end
```

### Flower Cardian Willow with Calligrapher (`89818984`)

Source: [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua)

```lua
		g:Merge(sg)
	end
	Duel.SetSynchroMaterial(g)
end
```

### Flower Cardian Moonflowerviewing (`33541430`)

Source: [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33541430.lua)

```lua
		g:Merge(sg)
	end
	Duel.SetSynchroMaterial(g)
end
```
