# Card.AddMonsterAttribute

## Signature

```lua
Card.AddMonsterAttribute(Card c, int type, [int attribute], [int race], [int level], [int atk], [int def]) -> void
```

## Description

Add the monster value to the trap card
Note: Values ​​recorded in the database are treated as the original value, and are set to zero here

## Parameters

- `c` `Card`
- `type` `int`
- `attribute` `int` optional
- `race` `int` optional
- `level` `int` optional
- `atk` `int` optional
- `def` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3650`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **72** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.AddMonsterAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sentence of Doom | `40771118` | [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40771118.lua) | 52 |
| Dimension Reflector | `54297661` | [Scripts/c54297661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54297661.lua) | 48 |
| Diamond Duston | `96857854` | [Scripts/c96857854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96857854.lua) | 47 |
| Argostars - Lightning Tydeu | `65889305` | [Scripts/c65889305.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65889305.lua) | 47 |
| Metalhold the Moving Blockade | `42237854` | [Scripts/c42237854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42237854.lua) | 46 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85257384.lua) | 44 |
| The Door of Destiny | `27062594` | [Scripts/c27062594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27062594.lua) | 44 |
| Ragnaraika Wisteria of Woe | `77573354` | [Scripts/c77573354.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77573354.lua) | 44 |
| Speedroid Dupligate | `58543073` | [Scripts/c58543073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58543073.lua) | 44 |
| The Phantom Knights of Mist Claws | `9336190` | [Scripts/c9336190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9336190.lua) | 43 |
| Metamorphortress | `43959432` | [Scripts/c43959432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43959432.lua) | 43 |
| Tiki Soul | `49514333` | [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49514333.lua) | 43 |
| The Prime Monarch | `54241725` | [Scripts/c54241725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54241725.lua) | 42 |
| Prey of the Jirai Gumo | `33055499` | [Scripts/c33055499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33055499.lua) | 41 |
| Destiny Board | `94212438` | [Scripts/c94212438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94212438.lua) | 41 |
| Eldlixir of the Glorious Golden Land | `22669793` | [Scripts/c22669793.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22669793.lua) | 41 |
| Argostars - Slayer Eteo | `38379052` | [Scripts/c38379052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38379052.lua) | 40 |
| Kuebiko | `20087414` | [Scripts/c20087414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20087414.lua) | 40 |
| Statue of Anguish Pattern | `23626223` | [Scripts/c23626223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23626223.lua) | 40 |
| Silhouhatte Trick | `24440742` | [Scripts/c24440742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24440742.lua) | 39 |
| Guardian of the Golden Land | `67007102` | [Scripts/c67007102.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67007102.lua) | 39 |
| Time Thief Power Reserve | `42620460` | [Scripts/c42620460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42620460.lua) | 39 |
| Qlife's End | `20447641` | [Scripts/c20447641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20447641.lua) | 39 |
| Powerhold the Moving Battery | `35100834` | [Scripts/c35100834.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35100834.lua) | 39 |
| ...and 48 more |  |  |  |

## Script Examples

### Sentence of Doom (`40771118`)

Source: [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40771118.lua)

```lua
		and Duel.IsPlayerCanSpecialSummonMonster(tp,tc:GetCode(),0,TYPES_TOKEN_MONSTER,0,0,1,RACE_FIEND,ATTRIBUTE_DARK,POS_FACEUP,tp,SUMMON_VALUE_DARK_SANCTUARY)
		and Duel.SelectYesNo(tp,aux.Stringid(16625614,0)) then
		tc:AddMonsterAttribute(TYPE_NORMAL,ATTRIBUTE_DARK,RACE_FIEND,1,0,0)
		Duel.SpecialSummonStep(tc,SUMMON_VALUE_DARK_SANCTUARY,tp,tp,true,false,POS_FACEUP)
		--immune
```

### Dimension Reflector (`54297661`)

Source: [Scripts/c54297661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54297661.lua)

```lua
	local def=tc:GetDefense()
	if not Duel.IsPlayerCanSpecialSummonMonster(tp,54297661,0,TYPES_EFFECT_TRAP_MONSTER,atk,def,4,RACE_SPELLCASTER,ATTRIBUTE_DARK,POS_FACEUP_ATTACK) then return end
	c:AddMonsterAttribute(TYPE_EFFECT+TYPE_TRAP)
	if Duel.SpecialSummonStep(c,SUMMON_VALUE_SELF,tp,tp,true,false,POS_FACEUP_ATTACK) then
		local e1=Effect.CreateEffect(c)
```

### Diamond Duston (`96857854`)

Source: [Scripts/c96857854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96857854.lua)

```lua
	if c:IsRelateToEffect(e)
		and Duel.IsPlayerCanSpecialSummonMonster(tp,96857854,0,TYPES_NORMAL_TRAP_MONSTER,0,1000,1,RACE_FIEND,ATTRIBUTE_DARK,POS_FACEUP_DEFENSE,1-tp) then
		c:AddMonsterAttribute(TYPE_NORMAL)
		Duel.SpecialSummonStep(c,0,tp,1-tp,true,false,POS_FACEUP_DEFENSE)
		local e1=Effect.CreateEffect(c)
```
