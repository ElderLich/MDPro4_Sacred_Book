# Card.GetAttackableTarget

## Signature

```lua
Card.GetAttackableTarget(Card c) -> Group,bool
```

## Description

Returns the Group of cards c can attack and a boolean indicating whether c can attack directly.

## Parameters

- `c` `Card`

## Returns

- `Group` - Attackable monsters.
- `bool` - Whether c can attack directly.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3709`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetAttackableTarget) with `Card.GetAttackableTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Apple Magician Girl | `56132807` | [Scripts/c56132807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56132807.lua) | 1 |
| Chocolate Magician Girl | `7198399` | [Scripts/c7198399.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7198399.lua) | 1 |
| Mutant Mindmaster | `11508758` | [Scripts/c11508758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11508758.lua) | 1 |
| Ultimate Tyranno | `15894048` | [Scripts/c15894048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15894048.lua) | 1 |

## Script Examples

### Apple Magician Girl (`56132807`)

Source: [Scripts/c56132807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56132807.lua)

```lua
	if tc and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)~=0 then
		local a=Duel.GetAttacker()
		local ag=a:GetAttackableTarget()
		if a:IsAttackable() and not a:IsImmuneToEffect(e) and ag:IsContains(tc) then
			Duel.BreakEffect()
```

### Chocolate Magician Girl (`7198399`)

Source: [Scripts/c7198399.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7198399.lua)

```lua
	if tc:IsRelateToEffect(e) and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)>0 then
		local a=Duel.GetAttacker()
		local ag=a:GetAttackableTarget()
		if a:IsAttackable() and not a:IsImmuneToEffect(e) and ag:IsContains(tc) then
			Duel.BreakEffect()
```

### Mutant Mindmaster (`11508758`)

Source: [Scripts/c11508758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11508758.lua)

```lua
			tc:RegisterEffect(e1)
			if tc:IsAttackable() and not tc:IsImmuneToEffect(e) then
				local ats=tc:GetAttackableTarget()
				if #ats==0 then return end
				Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(11508758,1))
```
