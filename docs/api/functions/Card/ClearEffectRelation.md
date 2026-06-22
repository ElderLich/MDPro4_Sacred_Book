# Card.ClearEffectRelation

## Signature

```lua
Card.ClearEffectRelation(Card c) -> void
```

## Description

Clears all effect relations currently stored on c.

## Parameters

- `c` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3561`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ClearEffectRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |

## Script Examples

### Magical Hats (`81210420`)

Source: [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua)

```lua
	if tc:IsFaceup() then
		Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
		tc:ClearEffectRelation()
	end
	local tg=sg:GetFirst()
```
