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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3616`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.ClearEffectRelation) with `Card.ClearEffectRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |

## Script Examples

### Magical Hats (`81210420`)

Source: [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua)

```lua
	if tc:IsFaceup() then
		Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
		tc:ClearEffectRelation()
	end
	local tg=sg:GetFirst()
```
