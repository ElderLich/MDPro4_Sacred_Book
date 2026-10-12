# Card.IsHasLevel

## Signature

```lua
Card.IsHasLevel(Card c) -> bool
```

## Description

Checks whether c has a Level.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3677`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsHasLevel) with `Card.IsHasLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Returned of the Tistina | `24892828` | [Scripts/c24892828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24892828.lua) | 1 |
| Void Expansion | `34822850` | [Scripts/c34822850.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34822850.lua) | 1 |

## Script Examples

### Returned of the Tistina (`24892828`)

Source: [Scripts/c24892828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24892828.lua)

```lua
end
function s.filter(c,code)
	return c:IsFaceup() and c:IsSetCard(0x1a4) and c:IsHasLevel() and not c:IsCode(code)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Void Expansion (`34822850`)

Source: [Scripts/c34822850.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34822850.lua)

```lua
function c34822850.atlimit(e,c)
	return c:IsFaceup() and c:IsSetCard(0xbb)
		and (not c:IsHasLevel() or Duel.IsExistingMatchingCard(c34822850.filter,c:GetControler(),LOCATION_MZONE,0,1,nil,c:GetLevel()))
end
function c34822850.tglimit(e,c)
```
