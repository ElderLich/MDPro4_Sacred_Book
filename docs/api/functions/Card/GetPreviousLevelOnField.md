# Card.GetPreviousLevelOnField

## Signature

```lua
Card.GetPreviousLevelOnField(Card c) -> int
```

## Description

Returns the Level value c had while it was previously on the field.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3448`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousLevelOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65114115.lua) | 57 |
| Imperial Princess Quinquery | `29510428` | [Scripts/c29510428.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29510428.lua) | 44 |
| The World Legacy | `92562411` | [Scripts/c92562411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92562411.lua) | 32 |
| Revival Rose | `12469386` | [Scripts/c12469386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12469386.lua) | 24 |

## Script Examples

### Seven Stars Slash - Army Annihilator Hagun (`65114115`)

Source: [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65114115.lua)

```lua
end
function s.thcfilter(c,tp)
	return (c:GetPreviousLevelOnField()>=8 or c:GetPreviousRankOnField()>=8) and c:IsPreviousControler(1-tp)
end
function s.thcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Imperial Princess Quinquery (`29510428`)

Source: [Scripts/c29510428.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29510428.lua)

```lua
function s.cfilter(c,tp)
	return c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousControler(tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and c:GetPreviousLevelOnField()==5 and (c:IsReason(REASON_BATTLE) or c:IsReason(REASON_EFFECT) and c:GetReasonPlayer()==1-tp)
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### The World Legacy (`92562411`)

Source: [Scripts/c92562411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92562411.lua)

```lua
end
function c92562411.ctfilter(c)
	return c:IsPreviousLocation(LOCATION_MZONE) and c:IsPreviousPosition(POS_FACEUP) and c:GetPreviousLevelOnField()>=5
end
function c92562411.ctop(e,tp,eg,ep,ev,re,r,rp)
```
