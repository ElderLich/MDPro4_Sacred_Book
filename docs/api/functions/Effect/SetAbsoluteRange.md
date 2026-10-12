# Effect.SetAbsoluteRange

## Signature

```lua
Effect.SetAbsoluteRange(Effect e, int playerid, int s_range, int o_range) -> void
```

## Description

Sets e's target range from an absolute player viewpoint and marks the effect with EFFECT_FLAG_ABSOLUTE_TARGET.
If playerid is 1, the supplied ranges are swapped internally so the stored ranges still line up with player 0/player 1 absolute handling.

## How To Use It

Use this for field effects whose affected side must be fixed to player 0/player 1 instead of relative to the handler's controller.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetAbsoluteRange(tp,0,LOCATION_MZONE)
```

The core stores the ranges with `EFFECT_FLAG_ABSOLUTE_TARGET` set. If `playerid` is 1, it swaps `s_range` and `o_range` internally so the final effect still points at the intended absolute player.

## Related Functions

- [Effect.SetTargetRange](/api/functions/Effect/SetTargetRange)
- [Effect.SetProperty](/api/functions/Effect/SetProperty)

## Parameters

- `e` `Effect`
- `playerid` `int`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:616`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **42** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.SetAbsoluteRange) with `Effect.SetAbsoluteRange`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7382007.lua) | 1 |
| Unchained Firelord of Yama | `94014327` | [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94014327.lua) | 1 |
| Performage Wind Drainer | `70417076` | [Scripts/c70417076.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70417076.lua) | 1 |
| Readying of Rites | `71771004` | [Scripts/c71771004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71771004.lua) | 1 |
| Swordsoul Assessment | `78836195` | [Scripts/c78836195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78836195.lua) | 1 |
| Assault Synchron | `77202120` | [Scripts/c77202120.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77202120.lua) | 1 |
| Gouki Machine Suprex | `29099860` | [Scripts/c29099860.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29099860.lua) | 1 |
| Elfnotes: Quatrain of Succession | `58809685` | [Scripts/c58809685.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58809685.lua) | 1 |
| Outburst Dragon | `87263576` | [Scripts/c87263576.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87263576.lua) | 1 |
| K9-04 Noroi | `47960073` | [Scripts/c47960073.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47960073.lua) | 1 |
| Swordsoul of Mo Ye | `20001443` | [Scripts/c20001443.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20001443.lua) | 1 |
| NEXT | `74414885` | [Scripts/c74414885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74414885.lua) | 1 |
| Thunder Dragons' Hundred Thunders | `82045034` | [Scripts/c82045034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82045034.lua) | 2 |
| Astral Kuriboh | `64591429` | [Scripts/c64591429.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64591429.lua) | 1 |
| Numbers Eveil | `20994205` | [Scripts/c20994205.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20994205.lua) | 2 |
| Swordsoul Strategist Longyuan | `93490856` | [Scripts/c93490856.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93490856.lua) | 1 |
| Lunalight Silver Hound | `35763582` | [Scripts/c35763582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35763582.lua) | 1 |
| Odd-Eyes Solblaze Dragon | `29325276` | [Scripts/c29325276.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29325276.lua) | 1 |
| Unchained Soul of Sharvara | `41165831` | [Scripts/c41165831.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41165831.lua) | 1 |
| Libromancer Realized | `15590355` | [Scripts/c15590355.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15590355.lua) | 1 |
| Super Hippo Carnival | `11050415` | [Scripts/c11050415.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11050415.lua) | 1 |
| Swordsoul Blackout | `14821890` | [Scripts/c14821890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14821890.lua) | 1 |
| Nordic Relic Hlidskjalf | `7320132` | [Scripts/c7320132.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7320132.lua) | 1 |
| Guard Mantis | `53754104` | [Scripts/c53754104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53754104.lua) | 1 |
| ...and 18 more |  |  |  |

## Script Examples

### Gouki Sheik Ogre (`7382007`)

Source: [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7382007.lua)

```lua
			e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_CLIENT_HINT)
			e1:SetRange(LOCATION_MZONE)
			e1:SetAbsoluteRange(tp,1,0)
			e1:SetTarget(s.splimit)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_CONTROL)
```

### Unchained Firelord of Yama (`94014327`)

Source: [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94014327.lua)

```lua
			e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE)
			e1:SetRange(LOCATION_MZONE)
			e1:SetAbsoluteRange(tp,1,0)
			e1:SetTarget(s.splimit)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_CONTROL)
```

### Performage Wind Drainer (`70417076`)

Source: [Scripts/c70417076.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70417076.lua)

```lua
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE)
		e1:SetRange(LOCATION_MZONE)
		e1:SetAbsoluteRange(tp,1,0)
		e1:SetTarget(s.splimit)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
```
