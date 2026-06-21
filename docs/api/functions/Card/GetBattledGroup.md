# Card.GetBattledGroup

## Signature

```lua
Card.GetBattledGroup(Card c) -> Group
```

## Description

Returns the deck of the card that fought this turn
Fighting has occurred in the calculation of the damage occurred, for the sword and other animals, animal judgments

## Parameters

- `c` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3532`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBattledGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reptilianne Naga | `79491903` | [Scripts/c79491903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79491903.lua) | 25 |

## Script Examples

### Reptilianne Naga (`79491903`)

Source: [Scripts/c79491903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79491903.lua)

```lua
end
function c79491903.filter(c,bc)
	return c:IsFaceup() and c:GetBattledGroup():IsContains(bc)
end
function c79491903.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
```
