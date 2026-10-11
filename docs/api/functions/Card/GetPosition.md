# Card.GetPosition

## Signature

```lua
Card.GetPosition(Card c) -> int
```

## Description

Returns c's current position value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3515`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPosition) with `Card.GetPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Digital Bug Corebage | `58600555` | [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58600555.lua) | 1 |
| Morphtronic Converter | `90659259` | [Scripts/c90659259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90659259.lua) | 1 |
| Karakuri Super Shogun mdl 00N "Bureibu" | `25904894` | [Scripts/c25904894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25904894.lua) | 1 |
| Karakuri Gama Oil | `11699941` | [Scripts/c11699941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11699941.lua) | 1 |
| Karakuri Steel Shogun mdl 00X "Bureido" | `66976526` | [Scripts/c66976526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66976526.lua) | 1 |
| Morphtronic Map | `56074358` | [Scripts/c56074358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56074358.lua) | 1 |
| Madolche Chickolates | `26570480` | [Scripts/c26570480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26570480.lua) | 1 |
| Karakuri Anatomy | `85541675` | [Scripts/c85541675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85541675.lua) | 1 |
| Morpho Butterspy | `43573231` | [Scripts/c43573231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43573231.lua) | 1 |
| Attack the Moon! | `83715234` | [Scripts/c83715234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83715234.lua) | 1 |
| Karakuri Trick House | `33184236` | [Scripts/c33184236.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33184236.lua) | 1 |
| Earthquake Giant | `61864793` | [Scripts/c61864793.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61864793.lua) | 1 |

## Script Examples

### Digital Bug Corebage (`58600555`)

Source: [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58600555.lua)

```lua
end
function c58600555.cfilter(c)
	local np=c:GetPosition()
	local pp=c:GetPreviousPosition()
	return ((np<3 and pp>3) or (pp<3 and np>3))
```

### Morphtronic Converter (`90659259`)

Source: [Scripts/c90659259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90659259.lua)

```lua
	local g=Duel.SelectTarget(tp,s.tgfilter,tp,LOCATION_MZONE,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	e:SetLabel(tc:GetPosition()|POS_FACEUP)
	if tc:IsAttackPos() then
		Duel.SetOperationInfo(0,CATEGORY_TODECK,g,1,0,0)
```

### Karakuri Super Shogun mdl 00N "Bureibu" (`25904894`)

Source: [Scripts/c25904894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25904894.lua)

```lua
end
function c25904894.cfilter(c,tp)
	local np=c:GetPosition()
	local pp=c:GetPreviousPosition()
	return c:IsSetCard(0x11) and c:IsControler(tp) and ((pp==0x1 and np==0x4) or (pp==0x4 and np==0x1))
```
