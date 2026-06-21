# Auxiliary.MaskChangeLimit

## Signature

```lua
Auxiliary.MaskChangeLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for Masked HERO/Mask Change effects; allows the Mask Change summon value or effects activated by card code 21143940.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches Mask Change conditions.

## Source

- `Utilities/procedure.lua:2317`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.MaskChangeLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Masked HERO Koga | `50608164` | [Scripts/c50608164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50608164.lua) | 38 |
| Masked HERO Atomic | `85672957` | [Scripts/c85672957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85672957.lua) | 36 |
| Masked HERO Blast | `89870349` | [Scripts/c89870349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89870349.lua) | 34 |
| Masked HERO Anki | `59642500` | [Scripts/c59642500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59642500.lua) | 32 |
| Masked HERO Dark Law | `58481572` | [Scripts/c58481572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58481572.lua) | 31 |
| Masked HERO Divine Wind | `22093873` | [Scripts/c22093873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22093873.lua) | 30 |
| Masked HERO Dian | `62624486` | [Scripts/c62624486.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62624486.lua) | 30 |
| Masked HERO Acid | `29095552` | [Scripts/c29095552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29095552.lua) | 23 |
| Masked HERO Goka | `58147549` | [Scripts/c58147549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58147549.lua) | 13 |
| Masked HERO Vapor | `10920352` | [Scripts/c10920352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10920352.lua) | 9 |

## Script Examples

### Masked HERO Koga (`50608164`)

Source: [Scripts/c50608164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50608164.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.MaskChangeLimit)
	c:RegisterEffect(e1)
	--atkup
```

### Masked HERO Atomic (`85672957`)

Source: [Scripts/c85672957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85672957.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.MaskChangeLimit)
	c:RegisterEffect(e1)
	--spsummon
```

### Masked HERO Blast (`89870349`)

Source: [Scripts/c89870349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89870349.lua)

```lua
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(aux.MaskChangeLimit)
	c:RegisterEffect(e1)
	--atk
```
