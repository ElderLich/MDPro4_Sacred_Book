# Card.GetPreviousRankOnField

## Signature

```lua
Card.GetPreviousRankOnField(Card c) -> int
```

## Description

Returns the Rank value c had while it was previously on the field.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3501`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousRankOnField) with `Card.GetPreviousRankOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua) | 1 |

## Script Examples

### Seven Stars Slash - Army Annihilator Hagun (`65114115`)

Source: [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua)

```lua
end
function s.thcfilter(c,tp)
	return (c:GetPreviousLevelOnField()>=8 or c:GetPreviousRankOnField()>=8) and c:IsPreviousControler(1-tp)
end
function s.thcon2(e,tp,eg,ep,ev,re,r,rp)
```
