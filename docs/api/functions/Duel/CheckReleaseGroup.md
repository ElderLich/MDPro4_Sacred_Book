# Duel.CheckReleaseGroup

## Signature

```lua
Duel.CheckReleaseGroup(int player, [function|nil f], int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether player can release at least count cards matching f, excluding ex.
Extra arguments after ex are passed to f after the Card argument. This helper uses REASON_COST.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4976`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **443** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.CheckReleaseGroup) with `Duel.CheckReleaseGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Mitsurugi Magatama](/examples/cards/76725398) | `76725398` | [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua) | 1 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 2 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 2 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58004362.lua) | 1 |
| D/D Vice Typhon | `59123937` | [Scripts/c59123937.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59123937.lua) | 1 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 1 |
| Dangers of the Divine | `22082432` | [Scripts/c22082432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22082432.lua) | 1 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 1 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 1 |
| Infernity Paranoia | `86547356` | [Scripts/c86547356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86547356.lua) | 1 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 1 |
| Neiroy, the Dream Mirror Traitor | `90176467` | [Scripts/c90176467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90176467.lua) | 1 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 1 |
| Abyss Actor - Superstar | `25629622` | [Scripts/c25629622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25629622.lua) | 1 |
| Soul of the Supreme Celestial King | `76840111` | [Scripts/c76840111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76840111.lua) | 1 |
| Prompthorn | `50548657` | [Scripts/c50548657.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50548657.lua) | 1 |
| Oh Tokenbaum! | `97173708` | [Scripts/c97173708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97173708.lua) | 2 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28651380.lua) | 1 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 2 |
| Ancient Gear Advance | `4064925` | [Scripts/c4064925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4064925.lua) | 1 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 1 |
| ...and 419 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
function c59255742.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=eg:Filter(c59255742.filter,nil,tp)
	if chk==0 then return Duel.CheckReleaseGroup(tp,c59255742.costfilter,1,nil,tp,g) end
	local g=Duel.SelectReleaseGroup(tp,c59255742.costfilter,1,1,nil,tp,g)
	Duel.Release(g,REASON_COST)
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckReleaseGroup(tp,s.rlfilter,1,nil) end
	local g=Duel.SelectReleaseGroup(tp,s.rlfilter,1,1,nil)
	Duel.Release(g,REASON_COST)
```

### Mitsurugi Magatama (`76725398`)

Source: [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua)

```lua
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local c1=not e:IsCostChecked() or Duel.CheckReleaseGroup(tp,s.cfilter,1,nil,tp)
	local b1=c1 and Duel.IsExistingTarget(Card.IsFaceup,tp,0,LOCATION_ONFIELD,1,nil)
	local b2=aux.RitualUltimateTarget(s.ritual_filter,Card.GetLevel,"Greater",LOCATION_HAND,nil,s.mfilter)(e,tp,eg,ep,ev,re,r,rp,0)
```
