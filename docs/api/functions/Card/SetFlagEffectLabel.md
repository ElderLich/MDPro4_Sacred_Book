# Card.SetFlagEffectLabel

## Signature

```lua
Card.SetFlagEffectLabel(Card c, int code, int label) -> bool
```

## Description

Returns whether or not c has an identifier of type code, and sets its Label property to label

## Parameters

- `c` `Card`
- `code` `int`
- `label` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3555`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetFlagEffectLabel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua) | 51 |
| Sky Striker Mecha Modules - Multirole | `24010609` | [Scripts/c24010609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24010609.lua) | 49 |
| Ultimate Divine-Beast | `32247099` | [Scripts/c32247099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32247099.lua) | 45 |
| Van'Dalgyon the Dark Dragon Lord | `24857466` | [Scripts/c24857466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24857466.lua) | 42 |
| Evilswarm Ouroboros | `38273745` | [Scripts/c38273745.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38273745.lua) | 38 |
| Gaia Blaze, the Force of the Sun | `9709452` | [Scripts/c9709452.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9709452.lua) | 36 |
| Shootingcode Talker | `33897356` | [Scripts/c33897356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33897356.lua) | 35 |
| Lair of Darkness | `59160188` | [Scripts/c59160188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59160188.lua) | 34 |
| Super Rush Headlong | `48422921` | [Scripts/c48422921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48422921.lua) | 31 |
| Blockman | `48115277` | [Scripts/c48115277.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48115277.lua) | 28 |
| Greed | `89405199` | [Scripts/c89405199.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89405199.lua) | 21 |
| Dark Snake Syndrome | `47233801` | [Scripts/c47233801.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47233801.lua) | 20 |
| Reversal of Fate | `36690018` | [Scripts/c36690018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36690018.lua) | 19 |

## Script Examples

### Groza, Tyrant of Thunder (`45420955`)

Source: [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua)

```lua
			c:RegisterFlagEffect(45420955,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
		end
		c:SetFlagEffectLabel(45420955,bit.bor(c:GetFlagEffectLabel(45420955),0x1))
		local e1=Effect.CreateEffect(c)
		e1:SetDescription(aux.Stringid(45420955,2))
```

### Sky Striker Mecha Modules - Multirole (`24010609`)

Source: [Scripts/c24010609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24010609.lua)

```lua
		local flag=c:GetFlagEffectLabel(24010609)
		if flag then
			c:SetFlagEffectLabel(24010609,flag+1)
		else
			c:RegisterFlagEffect(24010609,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,1)
```

### Ultimate Divine-Beast (`32247099`)

Source: [Scripts/c32247099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32247099.lua)

```lua
			rc:RegisterFlagEffect(32247099,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,1)
		else
			rc:SetFlagEffectLabel(32247099,ct+1)
		end
	end
```
