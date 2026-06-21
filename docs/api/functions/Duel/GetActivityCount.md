# Duel.GetActivityCount

## Signature

```lua
Duel.GetActivityCount(int player, int activity_type, ... any) -> int,...
```

## Description

Returns the number of times the player performed the corresponding activity_type operation
The activity_type is of the following type
ACTIVITY_SUMMON call (not including the usual call placed)
ACTIVITY_NORMALSUMMON Usually called (including the usual call placed)
ACTIVITY_SPSUMMON Special call
ACTIVITY_FLIPSUMMON Reverse call
ACTIVITY_ATTACK attack
ACTIVITY_BATTLE_PHASE enters the combat phase

## Parameters

- `player` `int`
- `activity_type` `int`
- `...` `any`

## Returns

- `int`
- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5066`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **83** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetActivityCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 58 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 56 |
| Junk Warrior Extreme | `16327715` | [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua) | 52 |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 52 |
| Red-Eyes Fusion | `6172122` | [Scripts/c6172122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6172122.lua) | 51 |
| Shining Hope Road | `62829077` | [Scripts/c62829077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62829077.lua) | 48 |
| Parallel World Fusion | `54283059` | [Scripts/c54283059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54283059.lua) | 48 |
| Cyber Network | `12670770` | [Scripts/c12670770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12670770.lua) | 47 |
| World of Prophecy | `29146185` | [Scripts/c29146185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29146185.lua) | 46 |
| Rank-Up-Magic Admiration of the Thousands | `96142517` | [Scripts/c96142517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96142517.lua) | 46 |
| Volcanic Queen | `63014935` | [Scripts/c63014935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63014935.lua) | 45 |
| Ties of the Brethren | `40450317` | [Scripts/c40450317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40450317.lua) | 45 |
| Golden Castle of Stromberg | `72283691` | [Scripts/c72283691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72283691.lua) | 44 |
| Shadow's Light | `61322713` | [Scripts/c61322713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61322713.lua) | 44 |
| Destiny End Dragoon | `76263644` | [Scripts/c76263644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76263644.lua) | 43 |
| Floowandereeze & Toccan | `17827173` | [Scripts/c17827173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17827173.lua) | 42 |
| Skull Flame | `99899504` | [Scripts/c99899504.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99899504.lua) | 42 |
| Floowandereeze & Stri | `80433039` | [Scripts/c80433039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80433039.lua) | 41 |
| Blackwing - Silverwind the Ascendant | `33236860` | [Scripts/c33236860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33236860.lua) | 41 |
| Nekroz of Sophia | `21105106` | [Scripts/c21105106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21105106.lua) | 40 |
| Time Maiden | `27107590` | [Scripts/c27107590.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27107590.lua) | 40 |
| Born from Draconis | `96699830` | [Scripts/c96699830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96699830.lua) | 40 |
| Lava Golem | `102380` | [Scripts/c102380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c102380.lua) | 40 |
| Hi-Speedroid Kendama | `97007933` | [Scripts/c97007933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97007933.lua) | 39 |
| ...and 59 more |  |  |  |

## Script Examples

### Rank-Up-Magic Astral Force (`45950291`)

Source: [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua)

```lua
end
function c45950291.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.IsPlayerCanNormalDraw(tp) and Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)==0 end
	local c=e:GetHandler()
	local e1=Effect.CreateEffect(c)
```

### Numeron Calling (`77402960`)

Source: [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua)

```lua
end
function c77402960.getsummoncount(tp)
	return Duel.GetActivityCount(tp,ACTIVITY_SUMMON)+Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)
end
function c77402960.rmfilter(c,fid)
```

### Junk Warrior Extreme (`16327715`)

Source: [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua)

```lua
end
function s.getsummoncount(tp)
	return Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)
end
function s.splimit(e,c,sump,sumtype,sumpos,targetp,se)
```
