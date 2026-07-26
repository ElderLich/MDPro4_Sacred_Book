# Card.IsSpecialSummonableCard

## Signature

```lua
Card.IsSpecialSummonableCard(Card c) -> bool
```

## Description

Checks whether c can be Special Summoned by a proper procedure.
c must have an available Special Summon procedure. This is useful for cards that look for monsters in the GY that already satisfy their revive-limit requirements and still have a legal procedure-style Special Summon path.

## Parameters

- `c` `Card` - Card being checked.

## Returns

- `bool` - True if c has an available proper Special Summon procedure in the current game state.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSpecialSummonableCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| The Deep Grave | `17688543` | [Scripts/c17688543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17688543.lua) | 37 |
| Reanimation Wave | `60312997` | [Scripts/c60312997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60312997.lua) | 30 |

## Script Examples

### The Deep Grave (`17688543`)

Source: [Scripts/c17688543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17688543.lua)

```lua
end
function c17688543.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_GRAVE) and chkc:IsSpecialSummonableCard() end
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingTarget(Card.IsSpecialSummonableCard,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,nil) end
```

### Reanimation Wave (`60312997`)

Source: [Scripts/c60312997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60312997.lua)

```lua
end
function c60312997.filter(c,lv)
	return c:IsLevelBelow(lv) and c:IsType(TYPE_SYNCHRO) and c:IsSpecialSummonableCard()
end
function c60312997.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
