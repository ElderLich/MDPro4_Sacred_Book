# Auxiliary.EnableBESRemove

## Signature

```lua
Auxiliary.EnableBESRemove(Card c) -> void
```

## Description

Registers the shared B.E.S. maintenance trigger on c. After c battles, it removes one 0x1f counter if possible; otherwise it destroys c.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1791`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableBESRemove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| B.E.S. Big Core MK-3 | `82821760` | [Scripts/c82821760.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82821760.lua) | 32 |
| B.E.S. Crystal Core | `22790789` | [Scripts/c22790789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22790789.lua) | 27 |
| B.E.S. Tetran | `44954628` | [Scripts/c44954628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44954628.lua) | 26 |
| B.E.S. Blaster Cannon Core | `84257883` | [Scripts/c84257883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84257883.lua) | 23 |
| B.E.S. Big Core MK-2 | `75937826` | [Scripts/c75937826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75937826.lua) | 20 |
| B.E.S. Big Core | `14148099` | [Scripts/c14148099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14148099.lua) | 14 |

## Script Examples

### B.E.S. Big Core MK-3 (`82821760`)

Source: [Scripts/c82821760.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82821760.lua)

```lua
	c:RegisterEffect(e4)
	--remove counter
	aux.EnableBESRemove(c)
	--to deck
	local e6=Effect.CreateEffect(c)
```

### B.E.S. Crystal Core (`22790789`)

Source: [Scripts/c22790789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22790789.lua)

```lua
	c:RegisterEffect(e2)
	--remove counter
	aux.EnableBESRemove(c)
	--pos
	local e5=Effect.CreateEffect(c)
```

### B.E.S. Tetran (`44954628`)

Source: [Scripts/c44954628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44954628.lua)

```lua
	c:RegisterEffect(e2)
	--remove counter
	aux.EnableBESRemove(c)
	--destroy
	local e5=Effect.CreateEffect(c)
```
