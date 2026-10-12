# Card.GetSummonLocation

## Signature

```lua
Card.GetSummonLocation(Card c) -> int
```

## Description

Returns the location c was Summoned from, decoded from its summon information.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3523`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetSummonLocation) with `Card.GetSummonLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ursarctic Septentrion | `53087962` | [Scripts/c53087962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53087962.lua) | 1 |
| Psychic Eraser Laser | `9322133` | [Scripts/c9322133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9322133.lua) | 1 |

## Script Examples

### Ursarctic Septentrion (`53087962`)

Source: [Scripts/c53087962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53087962.lua)

```lua
end
function c53087962.distg(e,c)
	return c:GetSummonLocation()==LOCATION_EXTRA and c:IsLevel(0)
end
function c53087962.thcon(e,tp,eg,ep,ev,re,r,rp)
```

### Psychic Eraser Laser (`9322133`)

Source: [Scripts/c9322133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9322133.lua)

```lua
end
function c9322133.filter(c)
	return c:GetSummonLocation()==LOCATION_EXTRA and c:IsAbleToGrave()
end
function c9322133.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
