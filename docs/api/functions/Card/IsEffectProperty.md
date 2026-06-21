# Card.IsEffectProperty

## Signature

```lua
Card.IsEffectProperty(Card c, function filter) -> bool
```

## Description

Checks whether c has an effect matching filter.

## Parameters

- `c` `Card`
- `filter` `function` - filter(Effect)

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3508`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsEffectProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 49 |
| Desperado Barrel Dragon | `76728962` | [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua) | 48 |
| Heosvarog the Mechanical Dawn | `8963089` | [Scripts/c8963089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8963089.lua) | 43 |
| Goddess of the Two Sides | `50915474` | [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50915474.lua) | 41 |
| Arcana Force XIX - The Sun | `39761418` | [Scripts/c39761418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39761418.lua) | 37 |
| Arcana Spread | `76302448` | [Scripts/c76302448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76302448.lua) | 34 |
| Arcana Reading | `11819473` | [Scripts/c11819473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11819473.lua) | 32 |
| Dimension Dice | `47292920` | [Scripts/c47292920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47292920.lua) | 28 |
| Diced Dice | `93078761` | [Scripts/c93078761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93078761.lua) | 21 |

## Script Examples

### Argostars - Giantslaying (`30964246`)

Source: [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua)

```lua
	return c:IsAllTypes(TYPE_CONTINUOUS|TYPE_TRAP) and c:IsFaceup() and
		(c:IsLocation(LOCATION_MZONE) or
			c:IsEffectProperty(aux.EffectCategoryFilter(CATEGORY_SPECIAL_SUMMON)) and
			(c:GetOriginalLevel()>0
			or bit.band(c:GetOriginalRace(),0x3fffffff)~=0
```

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
