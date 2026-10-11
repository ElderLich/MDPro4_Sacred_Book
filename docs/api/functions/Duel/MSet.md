# Duel.MSet

## Signature

```lua
Duel.MSet(int player, Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> void
```

## Description

Makes player Set c by a Normal Summon procedure, optionally using effect e and requiring at least min Tributes.
If e is nil, regular Normal Summon/Set rules are used. If ignore_count is true, the once-per-turn Normal Summon limit is ignored.

## Parameters

- `player` `int`
- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4870`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.MSet) with `Duel.MSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 2 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 1 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 1 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 1 |
| Fairy Tale Tails | `91957038` | [Scripts/c91957038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91957038.lua) | 1 |
| Tessera the Primal Squire | `67584223` | [Scripts/c67584223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67584223.lua) | 1 |
| Samsara Dragon | `33750025` | [Scripts/c33750025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33750025.lua) | 1 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 1 |
| Proof of Pruflas | `85847157` | [Scripts/c85847157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85847157.lua) | 1 |
| Spell Card "Soul Exchange" | `15735108` | [Scripts/c15735108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15735108.lua) | 1 |
| Gemini Summoner | `19041767` | [Scripts/c19041767.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19041767.lua) | 1 |
| Cry Havoc! | `39712330` | [Scripts/c39712330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39712330.lua) | 1 |
| Ultimate Offering | `80604091` | [Scripts/c80604091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80604091.lua) | 1 |
| Escalation of the Monarchs | `18235309` | [Scripts/c18235309.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18235309.lua) | 1 |
| Free-Range Monsters | `75025112` | [Scripts/c75025112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75025112.lua) | 1 |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
		Duel.Summon(tp,c,true,nil,1)
	else
		Duel.MSet(tp,c,true,nil,1)
	end
end
```

### Quick Summon (`10086952`)

Source: [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua)

```lua
				or Duel.SelectPosition(tp,tc,POS_FACEUP_ATTACK+POS_FACEDOWN_DEFENSE)==POS_FACEUP_ATTACK) then
			Duel.Summon(tp,tc,true,ne)
		else Duel.MSet(tp,tc,true,ne) end
	end
end
```

### Clown Crew Biancaviso (`82159583`)

Source: [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua)

```lua
			Duel.Summon(tp,tc,true,nil,1)
		else
			Duel.MSet(tp,tc,true,nil,1)
		end
	end
```
