# Card.GetPreviousControler

## Signature

```lua
Card.GetPreviousControler(Card c) -> int
```

## Description

Returns c's previous controller value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3457`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **68** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousControler`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua) | 59 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71159974.lua) | 59 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 56 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 56 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 56 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 55 |
| Timebreaker Magician | `80335817` | [Scripts/c80335817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80335817.lua) | 54 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 53 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11674673.lua) | 53 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87871125.lua) | 52 |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 52 |
| Yummyusment★Acroquey | `93360904` | [Scripts/c93360904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93360904.lua) | 51 |
| Unchained Soul Lord of Yama | `24269961` | [Scripts/c24269961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24269961.lua) | 51 |
| Ghost Mourner &amp; Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038441.lua) | 50 |
| Stardust Dragon - Victim Sanctuary | `76636978` | [Scripts/c76636978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76636978.lua) | 49 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 49 |
| Qliphort Genius | `22423493` | [Scripts/c22423493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22423493.lua) | 49 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 48 |
| Majestic Absorption | `63144961` | [Scripts/c63144961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63144961.lua) | 48 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95372220.lua) | 47 |
| Subterror Behemoth Fiendess | `74937659` | [Scripts/c74937659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74937659.lua) | 45 |
| Vaylantz Mad Marquess | `87897777` | [Scripts/c87897777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87897777.lua) | 44 |
| ...and 44 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
	g:DeleteGroup()
	local tc=sg:GetFirst()
	Duel.SendtoHand(tc,tc:GetPreviousControler(),REASON_EFFECT)
end
```

### PSY-Framelord Omega (`74586817`)

Source: [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua)

```lua
			Duel.ReturnToField(tc)
		else
			Duel.SendtoHand(tc,tc:GetPreviousControler(),REASON_EFFECT)
		end
		tc=sg:GetNext()
```

### Hojo the Vaylantz Warrior (`88919365`)

Source: [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua)

```lua
	local ph=Duel.GetCurrentPhase()
	return c:IsPreviousLocation(LOCATION_MZONE) and c:IsLocation(LOCATION_MZONE)
		and (c:GetPreviousSequence()~=c:GetSequence() or c:GetPreviousControler()~=tp)
		and ph~=PHASE_DAMAGE and ph~=PHASE_DAMAGE_CAL
end
```
