# Auxiliary.EnableNeosReturn

## Signature

```lua
Auxiliary.EnableNeosReturn(Card c, function operation, any set_category) -> void
```

## Description

Registers the shared Elemental HERO Neos Fusion End Phase return effects on c. It creates a mandatory return effect and an optional version used while c is affected by effect code 42015635, then returns both effects.

## Parameters

- `c` `Card`
- `operation` `function`
- `set_category` `any`

## Source

- `Utilities/utility.lua:222`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableNeosReturn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Nebula Neos | `40080312` | [Scripts/c40080312.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40080312.lua) | 1 |
| Elemental HERO Chaos Neos | `17032740` | [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17032740.lua) | 1 |
| Elemental HERO Glow Neos | `85507811` | [Scripts/c85507811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85507811.lua) | 1 |
| Elemental HERO Cosmo Neos | `90050480` | [Scripts/c90050480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90050480.lua) | 1 |
| Elemental HERO Dark Neos | `28677304` | [Scripts/c28677304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28677304.lua) | 1 |
| Elemental HERO Storm Neos | `49352945` | [Scripts/c49352945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49352945.lua) | 1 |
| Elemental HERO Magma Neos | `78512663` | [Scripts/c78512663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78512663.lua) | 1 |
| Elemental HERO Grand Neos | `48996569` | [Scripts/c48996569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48996569.lua) | 1 |
| Elemental HERO Aqua Neos | `55171412` | [Scripts/c55171412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55171412.lua) | 1 |
| Elemental HERO Air Neos | `11502550` | [Scripts/c11502550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11502550.lua) | 1 |
| Elemental HERO Flare Neos | `81566151` | [Scripts/c81566151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81566151.lua) | 1 |

## Script Examples

### Elemental HERO Nebula Neos (`40080312`)

Source: [Scripts/c40080312.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40080312.lua)

```lua
	c:RegisterEffect(e1)
	--return
	aux.EnableNeosReturn(c,c40080312.retop,c40080312.set_category)
	--draw
	local e5=Effect.CreateEffect(c)
```

### Elemental HERO Chaos Neos (`17032740`)

Source: [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17032740.lua)

```lua
	c:RegisterEffect(e1)
	--return
	aux.EnableNeosReturn(c,c17032740.retop,c17032740.set_category)
	--coin
	local e5=Effect.CreateEffect(c)
```

### Elemental HERO Glow Neos (`85507811`)

Source: [Scripts/c85507811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85507811.lua)

```lua
	c:RegisterEffect(e1)
	--return
	aux.EnableNeosReturn(c,c85507811.retop)
	--destroy
	local e5=Effect.CreateEffect(c)
```
