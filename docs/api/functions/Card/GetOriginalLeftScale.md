# Card.GetOriginalLeftScale

## Signature

```lua
Card.GetOriginalLeftScale(Card c) -> int
```

## Description

Returns c's printed left Pendulum Scale.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3465`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetOriginalLeftScale) with `Card.GetOriginalLeftScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Wisdom-Eye Magician | `72714461` | [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua) | 2 |

## Script Examples

### Wisdom-Eye Magician (`72714461`)

Source: [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua)

```lua
end
function c72714461.scfilter(c)
	return c:GetLeftScale()~=c:GetOriginalLeftScale()
end
function c72714461.sctg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
