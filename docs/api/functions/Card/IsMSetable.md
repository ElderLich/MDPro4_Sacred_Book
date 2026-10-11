# Card.IsMSetable

## Signature

```lua
Card.IsMSetable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

Checks whether c can be Normal Set in a Monster Zone for the current reason player.
ignore_count skips the Normal Summon/Set count check. e checks Set legality for that effect, min is the minimum number of releases required, and zone restricts usable Monster Zones.

## Parameters

- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3635`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsMSetable) with `Card.IsMSetable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 2 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 5 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 2 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 2 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 2 |
| Fairy Tale Tails | `91957038` | [Scripts/c91957038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91957038.lua) | 1 |
| Tessera the Primal Squire | `67584223` | [Scripts/c67584223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67584223.lua) | 2 |
| Samsara Dragon | `33750025` | [Scripts/c33750025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33750025.lua) | 2 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 3 |
| Proof of Pruflas | `85847157` | [Scripts/c85847157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85847157.lua) | 2 |
| Spell Card "Soul Exchange" | `15735108` | [Scripts/c15735108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15735108.lua) | 2 |
| Gemini Summoner | `19041767` | [Scripts/c19041767.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19041767.lua) | 2 |
| Cry Havoc! | `39712330` | [Scripts/c39712330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39712330.lua) | 2 |
| Ultimate Offering | `80604091` | [Scripts/c80604091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80604091.lua) | 2 |
| Escalation of the Monarchs | `18235309` | [Scripts/c18235309.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18235309.lua) | 2 |
| Free-Range Monsters | `75025112` | [Scripts/c75025112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75025112.lua) | 2 |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
function c96570609.sumtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsSummonable(true,nil,1) or c:IsMSetable(true,nil,1) end
	Duel.SetOperationInfo(0,CATEGORY_SUMMON,c,1,0,0)
end
```

### Quick Summon (`10086952`)

Source: [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua)

```lua
end
function s.sumfilter(c,res,se)
	return (c:IsSummonable(true,nil) or c:IsMSetable(true,nil))
		or (res and c:IsLevelAbove(5) and c:IsSummonable(true,se))
end
```

### Clown Crew Biancaviso (`82159583`)

Source: [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua)

```lua
end
function s.sumfilter(c)
	return c:IsSummonable(true,nil,1) or c:IsMSetable(true,nil,1)
end
function s.sumtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
