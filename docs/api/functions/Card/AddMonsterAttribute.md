# Card.AddMonsterAttribute

## Signature

```lua
Card.AddMonsterAttribute(Card c, int type, [int attribute], [int race], [int level], [int atk], [int def]) -> void
```

## Description

Adds temporary monster properties to c through effects.
The binding clears STATUS_NO_LEVEL, applies EFFECT_PRE_MONSTER with type, and applies Attribute, Race, Level, base ATK, and base DEF changes for nonzero supplied values.

## Parameters

- `c` `Card`
- `type` `int`
- `attribute` `int` optional - default: 0
- `race` `int` optional - default: 0
- `level` `int` optional - default: 0
- `atk` `int` optional - default: 0
- `def` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3705`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **76** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.AddMonsterAttribute) with `Card.AddMonsterAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sentence of Doom | `40771118` | [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40771118.lua) | 1 |
| Dimension Reflector | `54297661` | [Scripts/c54297661.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54297661.lua) | 1 |
| Diamond Duston | `96857854` | [Scripts/c96857854.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96857854.lua) | 1 |
| Argostars - Lightning Tydeu | `65889305` | [Scripts/c65889305.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65889305.lua) | 1 |
| Distrust Paranoia | `81965543` | [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81965543.lua) | 1 |
| Metalhold the Moving Blockade | `42237854` | [Scripts/c42237854.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42237854.lua) | 1 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85257384.lua) | 1 |
| The Door of Destiny | `27062594` | [Scripts/c27062594.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27062594.lua) | 1 |
| Ragnaraika Wisteria of Woe | `77573354` | [Scripts/c77573354.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77573354.lua) | 1 |
| Speedroid Dupligate | `58543073` | [Scripts/c58543073.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58543073.lua) | 1 |
| The Phantom Knights of Mist Claws | `9336190` | [Scripts/c9336190.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9336190.lua) | 1 |
| Metamorphortress | `43959432` | [Scripts/c43959432.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43959432.lua) | 1 |
| Tiki Soul | `49514333` | [Scripts/c49514333.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49514333.lua) | 1 |
| Ashtra Divine Domain | `37839434` | [Scripts/c37839434.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37839434.lua) | 1 |
| The Prime Monarch | `54241725` | [Scripts/c54241725.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54241725.lua) | 1 |
| Ashtra Cursed Roar | `91444835` | [Scripts/c91444835.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91444835.lua) | 1 |
| Prey of the Jirai Gumo | `33055499` | [Scripts/c33055499.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33055499.lua) | 1 |
| Destiny Board | `94212438` | [Scripts/c94212438.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94212438.lua) | 1 |
| Eldlixir of the Glorious Golden Land | `22669793` | [Scripts/c22669793.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22669793.lua) | 1 |
| Argostars - Slayer Eteo | `38379052` | [Scripts/c38379052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38379052.lua) | 1 |
| Kuebiko | `20087414` | [Scripts/c20087414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20087414.lua) | 1 |
| Statue of Anguish Pattern | `23626223` | [Scripts/c23626223.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23626223.lua) | 1 |
| Ashtra Insect Poison | `64455720` | [Scripts/c64455720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64455720.lua) | 1 |
| Silhouhatte Trick | `24440742` | [Scripts/c24440742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24440742.lua) | 1 |
| ...and 52 more |  |  |  |

## Script Examples

### Sentence of Doom (`40771118`)

Source: [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40771118.lua)

```lua
		and Duel.IsPlayerCanSpecialSummonMonster(tp,tc:GetCode(),0,TYPES_TOKEN_MONSTER,0,0,1,RACE_FIEND,ATTRIBUTE_DARK,POS_FACEUP,tp,SUMMON_VALUE_DARK_SANCTUARY)
		and Duel.SelectYesNo(tp,aux.Stringid(16625614,0)) then
		tc:AddMonsterAttribute(TYPE_NORMAL,ATTRIBUTE_DARK,RACE_FIEND,1,0,0)
		Duel.SpecialSummonStep(tc,SUMMON_VALUE_DARK_SANCTUARY,tp,tp,true,false,POS_FACEUP)
		--immune
```

### Dimension Reflector (`54297661`)

Source: [Scripts/c54297661.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54297661.lua)

```lua
	local def=tc:GetDefense()
	if not Duel.IsPlayerCanSpecialSummonMonster(tp,54297661,0,TYPES_EFFECT_TRAP_MONSTER,atk,def,4,RACE_SPELLCASTER,ATTRIBUTE_DARK,POS_FACEUP_ATTACK) then return end
	c:AddMonsterAttribute(TYPE_EFFECT+TYPE_TRAP)
	if Duel.SpecialSummonStep(c,SUMMON_VALUE_SELF,tp,tp,true,false,POS_FACEUP_ATTACK) then
		local e1=Effect.CreateEffect(c)
```

### Diamond Duston (`96857854`)

Source: [Scripts/c96857854.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96857854.lua)

```lua
	if c:IsRelateToEffect(e)
		and Duel.IsPlayerCanSpecialSummonMonster(tp,96857854,0,TYPES_NORMAL_TRAP_MONSTER,0,1000,1,RACE_FIEND,ATTRIBUTE_DARK,POS_FACEUP_DEFENSE,1-tp) then
		c:AddMonsterAttribute(TYPE_NORMAL)
		Duel.SpecialSummonStep(c,0,tp,1-tp,true,false,POS_FACEUP_DEFENSE)
		local e1=Effect.CreateEffect(c)
```
