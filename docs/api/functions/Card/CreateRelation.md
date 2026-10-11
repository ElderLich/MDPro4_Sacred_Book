# Card.CreateRelation

## Signature

```lua
Card.CreateRelation(Card c1, Card c2, int reset) -> void
```

## Description

Creates a relation from c1 to c2 that is cleared by reset.

## Parameters

- `c1` `Card`
- `c2` `Card`
- `reset` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3612`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.CreateRelation) with `Card.CreateRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Smile Action | `47870325` | [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua) | 1 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 1 |
| Victory Viper XX03 | `93130021` | [Scripts/c93130021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93130021.lua) | 1 |
| Overmind Archfiend | `24221808` | [Scripts/c24221808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24221808.lua) | 1 |
| Power Capsule | `54289683` | [Scripts/c54289683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54289683.lua) | 1 |
| Gladiator Beast Darius | `25924653` | [Scripts/c25924653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25924653.lua) | 2 |
| Exodius the Ultimate Forbidden Lord | `13893596` | [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua) | 1 |
| Light Law Medium | `52253888` | [Scripts/c52253888.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52253888.lua) | 1 |
| Morphtronic Vacuumen | `48868994` | [Scripts/c48868994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48868994.lua) | 1 |
| Portable Battery Pack | `61840587` | [Scripts/c61840587.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61840587.lua) | 1 |
| Corrupted Keys | `67949763` | [Scripts/c67949763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67949763.lua) | 1 |
| Future Visions | `87902575` | [Scripts/c87902575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87902575.lua) | 1 |
| Elder Entity Norden | `17412721` | [Scripts/c17412721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17412721.lua) | 2 |
| Morphtronic Repair Unit | `90239723` | [Scripts/c90239723.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90239723.lua) | 1 |
| Kinka-byo | `45452224` | [Scripts/c45452224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45452224.lua) | 2 |
| Escape from the Dark Dimension | `31550470` | [Scripts/c31550470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31550470.lua) | 2 |

## Script Examples

### Smile Action (`47870325`)

Source: [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua)

```lua
			if tc:IsLocation(LOCATION_REMOVED) then
				sg:AddCard(tc)
				tc:CreateRelation(c,RESET_EVENT+RESETS_STANDARD)
			end
			tc=og:GetNext()
```

### Alien Mother (`24104865`)

Source: [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua)

```lua
		Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP)
		tc:RegisterFlagEffect(24104865,RESET_EVENT+RESETS_STANDARD,0,0)
		c:CreateRelation(tc,RESET_EVENT+0x1020000)
		tc=sg:GetNext()
	end
```

### Victory Viper XX03 (`93130021`)

Source: [Scripts/c93130021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93130021.lua)

```lua
			or not Duel.IsPlayerCanSpecialSummonMonster(tp,93130022,0,TYPES_TOKEN_MONSTER,atk,def,lv,race,att) then return end
		local token=Duel.CreateToken(tp,93130022)
		c:CreateRelation(token,RESET_EVENT+RESETS_STANDARD)
		Duel.SpecialSummonStep(token,0,tp,tp,false,false,POS_FACEUP)
		local e1=Effect.CreateEffect(c)
```
