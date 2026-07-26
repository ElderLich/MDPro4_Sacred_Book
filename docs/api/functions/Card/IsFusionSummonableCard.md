# Card.IsFusionSummonableCard

## Signature

```lua
Card.IsFusionSummonableCard(Card c, [int sum_type]) -> bool
```

## Description

Checks whether c can be Fusion Summoned as a Fusion Monster for summon type sum_type, defaulting to 0.

## Parameters

- `c` `Card`
- `sum_type` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3577`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsFusionSummonableCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua) | 55 |

## Script Examples

### Future Fusion (`77565204`)

Source: [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua)

```lua
end
function c77565204.filter2(c,m)
	return c:IsFusionSummonableCard() and c:CheckFusionMaterial(m)
end
function c77565204.tgop(e,tp,eg,ep,ev,re,r,rp)
```
