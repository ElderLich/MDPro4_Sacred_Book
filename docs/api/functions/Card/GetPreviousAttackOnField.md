# Card.GetPreviousAttackOnField

## Signature

```lua
Card.GetPreviousAttackOnField(Card c) -> int
```

## Description

Returns the ATK value recorded for c's previous on-field state.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3504`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousAttackOnField) with `Card.GetPreviousAttackOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| Performapal Smile Sorcerer | `7799906` | [Scripts/c7799906.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7799906.lua) | 1 |
| Solving for Pendulum | `5208118` | [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua) | 1 |
| Performapal Laugh Maker | `44944304` | [Scripts/c44944304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44944304.lua) | 1 |
| Ecole de Zone | `60514625` | [Scripts/c60514625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60514625.lua) | 1 |
| Jigen Bakudan | `90020065` | [Scripts/c90020065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90020065.lua) | 1 |
| Time Wizard | `71625222` | [Scripts/c71625222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71625222.lua) | 1 |
| Reptilianne Scylla | `16909657` | [Scripts/c16909657.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16909657.lua) | 1 |

## Script Examples

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
		if rc>0 then
			local rg=Duel.GetOperatedGroup()
			local atk=rg:GetSum(Card.GetPreviousAttackOnField)
			local def=rg:GetSum(Card.GetPreviousDefenseOnField)
			local tc=sg:GetFirst()
```

### Performapal Smile Sorcerer (`7799906`)

Source: [Scripts/c7799906.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7799906.lua)

```lua
function c7799906.cfilter(c,tp)
	return c:IsReason(REASON_BATTLE+REASON_EFFECT) and c:IsPreviousControler(tp)
		and c:IsPreviousLocation(LOCATION_MZONE) and c:GetPreviousAttackOnField()>c:GetBaseAttack()
end
function c7799906.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### Solving for Pendulum (`5208118`)

Source: [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua)

```lua
			Duel.Destroy(g,REASON_EFFECT)
			local og=Duel.GetOperatedGroup()
			local dam=og:GetSum(Card.GetPreviousAttackOnField)
			if dam>0 then
				Duel.Damage(1-tp,dam,REASON_EFFECT)
```
