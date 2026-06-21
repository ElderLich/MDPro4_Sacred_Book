# Effect.SetAbsoluteRange

## Signature

```lua
Effect.SetAbsoluteRange(Effect e, int playerid, int s_range, int o_range) -> void
```

## Description

Set the target range property and set the EFFECT_FLAG_ABSOLUTE_RANGE flag
Playerid! = 0 s_range and o_range invert

## Parameters

- `e` `Effect`
- `playerid` `int`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:616`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.SetAbsoluteRange`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua) | 59 |
| Performage Wind Drainer | `70417076` | [Scripts/c70417076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70417076.lua) | 46 |
| Readying of Rites | `71771004` | [Scripts/c71771004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71771004.lua) | 43 |
| Swordsoul Assessment | `78836195` | [Scripts/c78836195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78836195.lua) | 42 |
| Assault Synchron | `77202120` | [Scripts/c77202120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77202120.lua) | 42 |
| Gouki Machine Suprex | `29099860` | [Scripts/c29099860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29099860.lua) | 42 |
| Elfnotes: Quatrain of Succession | `58809685` | [Scripts/c58809685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58809685.lua) | 41 |
| Outburst Dragon | `87263576` | [Scripts/c87263576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87263576.lua) | 40 |
| K9-04 Noroi | `47960073` | [Scripts/c47960073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47960073.lua) | 40 |
| Swordsoul of Mo Ye | `20001443` | [Scripts/c20001443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20001443.lua) | 40 |
| NEXT | `74414885` | [Scripts/c74414885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74414885.lua) | 39 |
| Thunder Dragons' Hundred Thunders | `82045034` | [Scripts/c82045034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82045034.lua) | 39 |
| Astral Kuriboh | `64591429` | [Scripts/c64591429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64591429.lua) | 38 |
| Numbers Eveil | `20994205` | [Scripts/c20994205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20994205.lua) | 38 |
| Swordsoul Strategist Longyuan | `93490856` | [Scripts/c93490856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93490856.lua) | 38 |
| Lunalight Silver Hound | `35763582` | [Scripts/c35763582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35763582.lua) | 38 |
| Odd-Eyes Solblaze Dragon | `29325276` | [Scripts/c29325276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29325276.lua) | 38 |
| Unchained Soul of Sharvara | `41165831` | [Scripts/c41165831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41165831.lua) | 38 |
| Libromancer Realized | `15590355` | [Scripts/c15590355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15590355.lua) | 37 |
| Super Hippo Carnival | `11050415` | [Scripts/c11050415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11050415.lua) | 36 |
| Swordsoul Blackout | `14821890` | [Scripts/c14821890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14821890.lua) | 36 |
| Nordic Relic Hlidskjalf | `7320132` | [Scripts/c7320132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7320132.lua) | 36 |
| Guard Mantis | `53754104` | [Scripts/c53754104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53754104.lua) | 36 |
| Icejade Ran Aegirine | `18494511` | [Scripts/c18494511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18494511.lua) | 35 |
| ...and 17 more |  |  |  |

## Script Examples

### Gouki Sheik Ogre (`7382007`)

Source: [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua)

```lua
			e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_CLIENT_HINT)
			e1:SetRange(LOCATION_MZONE)
			e1:SetAbsoluteRange(tp,1,0)
			e1:SetTarget(s.splimit)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_CONTROL)
```

### Performage Wind Drainer (`70417076`)

Source: [Scripts/c70417076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70417076.lua)

```lua
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE)
		e1:SetRange(LOCATION_MZONE)
		e1:SetAbsoluteRange(tp,1,0)
		e1:SetTarget(s.splimit)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
```

### Readying of Rites (`71771004`)

Source: [Scripts/c71771004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71771004.lua)

```lua
			e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
			e1:SetRange(LOCATION_MZONE)
			e1:SetAbsoluteRange(tp,1,0)
			e1:SetTarget(s.splimit)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_CONTROL)
```
