# Duel.Win

## Signature

```lua
Duel.Win(int player, int reason) -> void
```

## Description

Sets player as the duel winner with reason, but only if no winner has already been set.

## Parameters

- `player` `int`
- `reason` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4899`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Win) with `Duel.Win`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77751766.lua) | 1 |
| Phantasm Spiral Assault | `97795930` | [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97795930.lua) | 1 |
| Exodius the Ultimate Forbidden Lord | `13893596` | [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua) | 1 |
| Destiny Board | `94212438` | [Scripts/c94212438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94212438.lua) | 1 |
| Exodia, the Legendary Defender | `5008836` | [Scripts/c5008836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5008836.lua) | 1 |
| Vennominaga the Deity of Poisonous Snakes | `8062132` | [Scripts/c8062132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8062132.lua) | 1 |
| F.A. Winners | `69553552` | [Scripts/c69553552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69553552.lua) | 1 |
| Number iC1000: Numerounius Numerounia | `15862758` | [Scripts/c15862758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15862758.lua) | 1 |
| Ghostrick Angel of Mischief | `53334641` | [Scripts/c53334641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53334641.lua) | 1 |
| Musical Sumo Dice Games | `96637156` | [Scripts/c96637156.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96637156.lua) | 1 |
| Last Turn | `28566710` | [Scripts/c28566710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28566710.lua) | 3 |
| Number 88: Gimmick Puppet of Leo | `48995978` | [Scripts/c48995978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48995978.lua) | 1 |
| Relay Soul | `42776960` | [Scripts/c42776960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42776960.lua) | 1 |
| Number C88: Gimmick Puppet Disaster Leo | `6165656` | [Scripts/c6165656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6165656.lua) | 1 |
| Holactie the Creator of Light | `10000040` | [Scripts/c10000040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000040.lua) | 1 |
| Jackpot 7 | `81171949` | [Scripts/c81171949.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81171949.lua) | 1 |
| Flying Elephant | `66765023` | [Scripts/c66765023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66765023.lua) | 1 |
| True Exodia | `37984331` | [Scripts/c37984331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37984331.lua) | 1 |
| Final Countdown | `95308449` | [Scripts/c95308449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95308449.lua) | 1 |
| Exodia the Forbidden One | `33396948` | [Scripts/c33396948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33396948.lua) | 3 |

## Script Examples

### Summer Schoolwork Successful! (`77751766`)

Source: [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77751766.lua)

```lua
				if Duel.SSet(tp,g:GetFirst())>0 and Duel.GetMatchingGroupCount(aux.TRUE,tp,LOCATION_DECK,0,nil)<=1 then
					Duel.BreakEffect()
					Duel.Win(tp,0x23)
				end
			end
```

### Phantasm Spiral Assault (`97795930`)

Source: [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97795930.lua)

```lua
	if c:GetFlagEffect(97795930)>2 then
		local WIN_REASON_CELESTIAL_WHIRLPOOL=0x1c
		Duel.Win(tp,WIN_REASON_CELESTIAL_WHIRLPOOL)
	end
end
```

### Exodius the Ultimate Forbidden Lord (`13893596`)

Source: [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua)

```lua
		if c:GetOriginalCode()==13893596 and c:IsFaceup() and g:IsContains(tc) and g:GetClassCount(Card.GetCode)==5 then
			local WIN_REASON_EXODIUS = 0x14
			Duel.Win(tp,WIN_REASON_EXODIUS)
		end
	end
```
