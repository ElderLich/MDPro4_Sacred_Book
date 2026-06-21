# Duel.GetMZoneCount

## Signature

```lua
Duel.GetMZoneCount(int player, [Group|Card targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Return the number of available \[zone slots\] in the Monster Zone on player's field \[after targets leave\]

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4936`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **702** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetMZoneCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 62 |
| [Ecclesia and the Dark Dragon](/examples/cards/78397661) | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 62 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [Cyber Pharos](/examples/cards/29719112) | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 61 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 59 |
| Soul of the Supreme King | `92428405` | [Scripts/c92428405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92428405.lua) | 59 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua) | 59 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua) | 58 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 57 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| ...and 678 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
function s.cfilter(c,tp,chk)
	return c:IsType(TYPE_FUSION) and c:IsReleasableByEffect() and (not chk
		or (Duel.GetMZoneCount(tp,c)>1 and not Duel.IsPlayerAffectedByEffect(tp,59822133)
			and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,0,0,c:GetLevel(),RACE_SPELLCASTER,ATTRIBUTE_DARK)))
end
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.costfilter(c,tp,g)
	return c59255742.ffilter(c) and Duel.GetMZoneCount(tp,c,tp,LOCATION_REASON_CONTROL)>0 and g:IsExists(aux.TRUE,1,c)
end
function c59255742.cost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.RitualCheck(g,tp,c,atk,greater_or_equal)
	return s["RitualCheck"..greater_or_equal](g,c,atk) and Duel.GetMZoneCount(tp,g,tp)>0 and (not c.mat_group_check or c.mat_group_check(g,tp))
		and (not aux.RCheckAdditional or aux.RCheckAdditional(tp,g,c))
end
```
