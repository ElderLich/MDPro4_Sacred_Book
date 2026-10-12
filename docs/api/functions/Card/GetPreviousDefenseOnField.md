# Card.GetPreviousDefenseOnField

## Signature

```lua
Card.GetPreviousDefenseOnField(Card c) -> int
```

## Description

Returns the DEF value c had while it was previously on the field.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3505`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousDefenseOnField) with `Card.GetPreviousDefenseOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| Ecole de Zone | `60514625` | [Scripts/c60514625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60514625.lua) | 1 |

## Script Examples

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
			local rg=Duel.GetOperatedGroup()
			local atk=rg:GetSum(Card.GetPreviousAttackOnField)
			local def=rg:GetSum(Card.GetPreviousDefenseOnField)
			local tc=sg:GetFirst()
			local e1=Effect.CreateEffect(e:GetHandler())
```

### Ecole de Zone (`60514625`)

Source: [Scripts/c60514625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60514625.lua)

```lua
		and Duel.IsPlayerCanSpecialSummonMonster(p,60514626,0,TYPES_TOKEN_MONSTER,-2,-2,1,RACE_SPELLCASTER,ATTRIBUTE_DARK) then
		local atk=tc:GetPreviousAttackOnField()
		local def=tc:GetPreviousDefenseOnField()
		local token=Duel.CreateToken(tp,60514626)
		if Duel.SpecialSummonStep(token,0,p,p,false,false,POS_FACEUP) then
```
