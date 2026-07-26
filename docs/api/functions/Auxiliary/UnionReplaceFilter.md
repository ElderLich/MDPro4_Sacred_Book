# Auxiliary.UnionReplaceFilter

## Signature

```lua
Auxiliary.UnionReplaceFilter(Effect e, Effect re, int r, int rp) -> bool
```

## Description

Destroy-substitute value function for modern Union monsters; returns true for destruction by battle or card effect.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool` - true for destruction by battle or card effect.

## Source

- `Utilities/utility.lua:342`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.UnionReplaceFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Buster Blaster | `63676256` | [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua) | 1 |
| Spirit of the Six Samurai | `65685470` | [Scripts/c65685470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65685470.lua) | 1 |
| Oilman | `31768112` | [Scripts/c31768112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31768112.lua) | 1 |
| Trigon | `48568432` | [Scripts/c48568432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48568432.lua) | 1 |
| Vylon Pentachloro | `47228077` | [Scripts/c47228077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47228077.lua) | 1 |
| Vylon Tesseract | `84313685` | [Scripts/c84313685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84313685.lua) | 1 |

## Script Examples

### Buster Blaster (`63676256`)

Source: [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua)

```lua
	e3:SetCode(EFFECT_DESTROY_SUBSTITUTE)
	e3:SetCondition(aux.IsUnionState)
	e3:SetValue(aux.UnionReplaceFilter)
	c:RegisterEffect(e3)
	--eqlimit
```

### Spirit of the Six Samurai (`65685470`)

Source: [Scripts/c65685470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65685470.lua)

```lua
	e5:SetCode(EFFECT_DESTROY_SUBSTITUTE)
	e5:SetCondition(aux.IsUnionState)
	e5:SetValue(aux.UnionReplaceFilter)
	c:RegisterEffect(e5)
	--draw
```

### Oilman (`31768112`)

Source: [Scripts/c31768112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31768112.lua)

```lua
	e3:SetCode(EFFECT_DESTROY_SUBSTITUTE)
	e3:SetCondition(aux.IsUnionState)
	e3:SetValue(aux.UnionReplaceFilter)
	c:RegisterEffect(e3)
	--draw
```
