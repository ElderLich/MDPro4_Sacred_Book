# Card.GetPreviousPosition

## Signature

```lua
Card.GetPreviousPosition(Card c) -> int
```

## Description

Returns c's previously recorded position value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3467`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 1 |
| Loki, Lord of the Aesir | `67098114` | [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua) | 1 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 3 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 1 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 1 |
| Odin, Father of the Aesir | `93483212` | [Scripts/c93483212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93483212.lua) | 1 |
| Thor, Lord of the Aesir | `30604579` | [Scripts/c30604579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30604579.lua) | 1 |
| Digital Bug Corebage | `58600555` | [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58600555.lua) | 1 |
| Karakuri Super Shogun mdl 00N "Bureibu" | `25904894` | [Scripts/c25904894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25904894.lua) | 1 |
| Ninjitsu Art of Shadow Sealing | `13629812` | [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13629812.lua) | 1 |
| Karakuri Gama Oil | `11699941` | [Scripts/c11699941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11699941.lua) | 1 |
| Karakuri Steel Shogun mdl 00X "Bureido" | `66976526` | [Scripts/c66976526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66976526.lua) | 1 |
| Morphtronic Map | `56074358` | [Scripts/c56074358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56074358.lua) | 1 |
| Madolche Chickolates | `26570480` | [Scripts/c26570480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26570480.lua) | 1 |
| Karakuri Anatomy | `85541675` | [Scripts/c85541675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85541675.lua) | 1 |
| Morpho Butterspy | `43573231` | [Scripts/c43573231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43573231.lua) | 1 |
| Attack the Moon! | `83715234` | [Scripts/c83715234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83715234.lua) | 1 |
| Karakuri Trick House | `33184236` | [Scripts/c33184236.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33184236.lua) | 1 |
| Earthquake Giant | `61864793` | [Scripts/c61864793.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61864793.lua) | 1 |
| Time Machine | `80987696` | [Scripts/c80987696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80987696.lua) | 2 |

## Script Examples

### Chevreuil, Hunting Scout of the Deep Forest (`13023431`)

Source: [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua)

```lua
			and bc:IsType(TYPE_MONSTER) and bc:IsRace(RACE_WARRIOR) and bc:IsAttribute(ATTRIBUTE_EARTH)
	else
		return bc:GetPreviousPosition()&POS_FACEUP>0 and bc:GetPreviousLocation()&LOCATION_MZONE==LOCATION_MZONE and bc:IsPreviousControler(tp)
			and bc:GetPreviousTypeOnField()&TYPE_MONSTER==TYPE_MONSTER and c:GetPreviousRaceOnField()&RACE_WARRIOR==RACE_WARRIOR
			and bc:GetPreviousAttributeOnField()&ATTRIBUTE_EARTH==ATTRIBUTE_EARTH
```

### Loki, Lord of the Aesir (`67098114`)

Source: [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua)

```lua
function c67098114.regop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local pos=c:GetPreviousPosition()
	if c:IsReason(REASON_BATTLE) then pos=c:GetBattlePosition() end
	if rp==1-tp and c:IsPreviousControler(tp) and c:IsReason(REASON_DESTROY)
```

### Red-Eyes Retro Dragon (`53485634`)

Source: [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua)

```lua
		and (c:IsReason(REASON_EFFECT) and c:GetReasonPlayer()==1-tp or c:IsReason(REASON_BATTLE) and Duel.GetAttacker():IsControler(1-tp))
		and c:IsSetCard(0x3b) and c:IsLevelBelow(7) and c:IsControler(tp)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false,c:GetPreviousPosition())
end
function c53485634.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
