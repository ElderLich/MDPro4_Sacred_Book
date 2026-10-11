# Card.GetOriginalRightScale

## Signature

```lua
Card.GetOriginalRightScale(Card c) -> int
```

## Description

Returns c's printed right Pendulum Scale.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3467`

## Guided Examples

Learn how to use this function in context:

- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetOriginalRightScale) with `Card.GetOriginalRightScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Wisdom-Eye Magician | `72714461` | [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua) | 1 |

## Script Examples

### Wisdom-Eye Magician (`72714461`)

Source: [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua)

```lua
		local e2=e1:Clone()
		e2:SetCode(EFFECT_CHANGE_RSCALE)
		e2:SetValue(tc:GetOriginalRightScale())
		tc:RegisterEffect(e2)
	end
```
