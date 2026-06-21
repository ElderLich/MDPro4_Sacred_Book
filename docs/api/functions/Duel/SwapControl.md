# Duel.SwapControl

## Signature

```lua
Duel.SwapControl(Card|Group targets1, Card|Group targets2, [int reset_phase], [int reset_count]) -> bool
```

## Description

Exchange c1 and c2 control, the return value that is successful

## Parameters

- `targets1` `Card|Group`
- `targets2` `Card|Group`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4907`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SwapControl`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Yummy★Redemption | `65853758` | [Scripts/c65853758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65853758.lua) | 53 |
| Giant Ballgame | `60619435` | [Scripts/c60619435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60619435.lua) | 45 |
| Vampire Red Baron | `6917479` | [Scripts/c6917479.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6917479.lua) | 45 |
| Abyss Actor - Comic Relief | `15308295` | [Scripts/c15308295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15308295.lua) | 41 |
| Evil★Twin Present | `60759087` | [Scripts/c60759087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60759087.lua) | 37 |
| Mind Castlin | `12172567` | [Scripts/c12172567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12172567.lua) | 36 |
| Psychic Jumper | `52430902` | [Scripts/c52430902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52430902.lua) | 35 |
| Geonator Transverser | `52119435` | [Scripts/c52119435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52119435.lua) | 33 |
| Reeze, Whirlwind of Gusto | `36331074` | [Scripts/c36331074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36331074.lua) | 31 |
| Packet Swap | `75153328` | [Scripts/c75153328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75153328.lua) | 24 |
| Xyz Reversal | `66604523` | [Scripts/c66604523.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66604523.lua) | 24 |
| TG1-EM1 | `76641981` | [Scripts/c76641981.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76641981.lua) | 24 |
| Mirror Gate | `43452193` | [Scripts/c43452193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43452193.lua) | 23 |
| Invader of the Throne | `3056267` | [Scripts/c3056267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3056267.lua) | 23 |
| Interdimensional Warp | `57384901` | [Scripts/c57384901.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57384901.lua) | 23 |
| Creature Swap | `31036355` | [Scripts/c31036355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31036355.lua) | 21 |
| Dummy Golem | `13532663` | [Scripts/c13532663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13532663.lua) | 20 |
| Creature Seizure | `15305240` | [Scripts/c15305240.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15305240.lua) | 19 |
| Switcheroroo | `30426226` | [Scripts/c30426226.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30426226.lua) | 17 |

## Script Examples

### Yummy★Redemption (`65853758`)

Source: [Scripts/c65853758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65853758.lua)

```lua
	local b=g:GetNext()
	if a:IsRelateToEffect(e) and b:IsRelateToEffect(e) then
		Duel.SwapControl(a,b)
	end
end
```

### Giant Ballgame (`60619435`)

Source: [Scripts/c60619435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60619435.lua)

```lua
	local tc2=g:Filter(Card.IsControler,nil,1-tp):GetFirst()
	if tc and tc2 then
		if Duel.SwapControl(tc,tc2)~=0 then
			local e1=Effect.CreateEffect(e:GetHandler())
			e1:SetType(EFFECT_TYPE_SINGLE)
```

### Vampire Red Baron (`6917479`)

Source: [Scripts/c6917479.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6917479.lua)

```lua
	local b=g:GetNext()
	if a:IsRelateToEffect(e) and b:IsRelateToEffect(e) then
		Duel.SwapControl(a,b)
	end
end
```
