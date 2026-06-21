# Card.GetOriginalRightScale

## Signature

```lua
Card.GetOriginalRightScale(Card c) -> int
```

## Description

Returns the original right pendulum scale of c

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3416`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOriginalRightScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Wisdom-Eye Magician | `72714461` | [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua) | 40 |

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
