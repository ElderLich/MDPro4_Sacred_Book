# Duel.GetSZoneCount

## Signature

```lua
Duel.GetSZoneCount(int player, [Group|Card targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns the number of available Spell & Trap Zones for player after targets leave, optionally restricted by zone. The Field Zone is not included.
The additional use_player and reason parameters are used by effects that restrict zones, such as Kaiser Colosseum.

## Parameters

- `player` `int`
- `targets` `Group|Card` optional
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`
- `int` - zone

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4937`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetSZoneCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 51 |
| Paleozoic Cambroraster | `36346532` | [Scripts/c36346532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36346532.lua) | 50 |
| Parametalfoes Melcaster | `10024317` | [Scripts/c10024317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10024317.lua) | 47 |
| Amazement Precious Park | `33773528` | [Scripts/c33773528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33773528.lua) | 44 |
| The Weather Painter Sun | `54895237` | [Scripts/c54895237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54895237.lua) | 42 |
| Sunvine Shrine | `27946124` | [Scripts/c27946124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27946124.lua) | 42 |
| That's 10! | `97223101` | [Scripts/c97223101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97223101.lua) | 42 |
| Raremetalfoes Bismugear | `18716735` | [Scripts/c18716735.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18716735.lua) | 40 |
| The Weather Painter Thunder | `91299846` | [Scripts/c91299846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91299846.lua) | 40 |
| Crystal Tree | `47408488` | [Scripts/c47408488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47408488.lua) | 40 |
| Artifact Ignition | `29223325` | [Scripts/c29223325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29223325.lua) | 39 |
| Trap Holic | `22377092` | [Scripts/c22377092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22377092.lua) | 37 |
| Metalfoes Silverd | `7868571` | [Scripts/c7868571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7868571.lua) | 30 |
| Metalfoes Volflame | `69351984` | [Scripts/c69351984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69351984.lua) | 30 |
| Metalfoes Steelen | `60473572` | [Scripts/c60473572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60473572.lua) | 30 |
| Metalfoes Goldriver | `33256280` | [Scripts/c33256280.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33256280.lua) | 30 |
| Terrors of the Overroot | `63086455` | [Scripts/c63086455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63086455.lua) | 27 |

## Script Examples

### Hrimnir the Divine Follower (`49904658`)

Source: [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua)

```lua
end
function s.rcheck(g,tp)
	return Duel.GetSZoneCount(tp,g)>0 and Duel.CheckReleaseGroupEx(tp,Auxiliary.IsInGroup,#g,REASON_COST,true,nil,g)
end
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Paleozoic Cambroraster (`36346532`)

Source: [Scripts/c36346532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36346532.lua)

```lua
end
function c36346532.cfilter(c,tp)
	return c:GetSequence()<5 and c:IsFacedown() and c:IsAbleToGrave() and Duel.GetSZoneCount(tp,c)>0
		and Duel.IsExistingMatchingCard(c36346532.setfilter,tp,LOCATION_DECK,0,1,nil,c,tp)
end
```

### Parametalfoes Melcaster (`10024317`)

Source: [Scripts/c10024317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10024317.lua)

```lua
function c10024317.desfilter(c,tp)
	if c:IsFacedown() then return false end
	return Duel.GetSZoneCount(tp,c)>0 and Duel.IsExistingMatchingCard(c10024317.filter,tp,LOCATION_DECK,0,1,nil,true)
end
function c10024317.filter(c,ignore)
```
