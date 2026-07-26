# Auxiliary.EffectPropertyFilter

## Signature

```lua
Auxiliary.EffectPropertyFilter(int flag) -> function
```

## Description

Returns a predicate that checks whether an Effect has property flag.

## Parameters

- `flag` `int`

## Returns

- `function`

## Source

- `Utilities/utility.lua:2020`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EffectPropertyFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Desperado Barrel Dragon | `76728962` | [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua) | 1 |
| Heosvarog the Mechanical Dawn | `8963089` | [Scripts/c8963089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8963089.lua) | 1 |
| Goddess of the Two Sides | `50915474` | [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50915474.lua) | 1 |
| Arcana Force XIX - The Sun | `39761418` | [Scripts/c39761418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39761418.lua) | 2 |
| Arcana Spread | `76302448` | [Scripts/c76302448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76302448.lua) | 2 |
| Arcana Reading | `11819473` | [Scripts/c11819473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11819473.lua) | 1 |
| Dimension Dice | `47292920` | [Scripts/c47292920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47292920.lua) | 1 |
| Diced Dice | `93078761` | [Scripts/c93078761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93078761.lua) | 1 |

## Script Examples

### Arcana Force EX - The Chaos Ruler (`12686296`)

Source: [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua)

```lua
end
function s.thfilter(c)
	return c:IsEffectProperty(aux.EffectPropertyFilter(EFFECT_FLAG_COIN)) and c:IsAbleToHand()
end
function s.coinop(e,tp,eg,ep,ev,re,r,rp)
```

### Desperado Barrel Dragon (`76728962`)

Source: [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua)

```lua
end
function c76728962.thfilter(c)
	return c:IsEffectProperty(aux.EffectPropertyFilter(EFFECT_FLAG_COIN)) and c:IsType(TYPE_MONSTER) and c:IsLevelBelow(7) and c:IsAbleToHand()
end
function c76728962.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Heosvarog the Mechanical Dawn (`8963089`)

Source: [Scripts/c8963089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8963089.lua)

```lua
end
function s.thfilter(c)
	return c:IsEffectProperty(aux.EffectPropertyFilter(EFFECT_FLAG_FUSION_SUMMON)) and c:IsAbleToHand()
end
function s.thop2(e,tp,eg,ep,ev,re,r,rp)
```
