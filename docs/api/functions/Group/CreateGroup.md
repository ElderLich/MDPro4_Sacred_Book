# Group.CreateGroup

## Signature

```lua
Group.CreateGroup() -> Group
```

## Description

Creates and returns a new empty Group.

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:900`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **174** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.CreateGroup) with `Group.CreateGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 2 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71801447.lua) | 3 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42125140.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Black Dragon Ninja | `56562619` | [Scripts/c56562619.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56562619.lua) | 1 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38129297.lua) | 2 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53330789.lua) | 1 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53701259.lua) | 1 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38572779.lua) | 1 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33760966.lua) | 1 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17188206.lua) | 1 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81794107.lua) | 1 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57761191.lua) | 1 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3441553.lua) | 2 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79755671.lua) | 1 |
| Helping Robo for Underwater Combat | `77856460` | [Scripts/c77856460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77856460.lua) | 1 |
| ...and 150 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		return
	end
	local sg=Group.CreateGroup()
	sg:Merge(g)
	Duel.HintSelection(Group.FromCards(lpz))
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	local g=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)
	local tc=g:GetFirst()
	local tg=Group.CreateGroup()
	local tc=g:GetFirst()
	while tc do
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	local ect2=aux.ExtraDeckSummonCountLimit and Duel.IsPlayerAffectedByEffect(tp,92345028)
		and aux.ExtraDeckSummonCountLimit[tp]
	local g=Group.CreateGroup()
	if c:IsSetCard(0xa3) then g:Merge(Duel.GetMatchingGroup(c30983281.excostfilter,tp,LOCATION_GRAVE,0,nil,tp)) end
	local chkrel=c:IsReleasable()
```
