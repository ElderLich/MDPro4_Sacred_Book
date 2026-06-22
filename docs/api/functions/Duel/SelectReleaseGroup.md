# Duel.SelectReleaseGroup

## Signature

```lua
Duel.SelectReleaseGroup(int sel_player, [function|nil f], int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player select min to max releasable cards matching f, excluding ex, and returns the selected Group.
Extra arguments after ex are passed to f after the Card argument.

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4977`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **430** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectReleaseGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 59 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71340250.lua) | 59 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58004362.lua) | 56 |
| D/D Vice Typhon | `59123937` | [Scripts/c59123937.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59123937.lua) | 55 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 54 |
| Dangers of the Divine | `22082432` | [Scripts/c22082432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22082432.lua) | 53 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 53 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 53 |
| Infernity Paranoia | `86547356` | [Scripts/c86547356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86547356.lua) | 53 |
| Master Spirit Tech Force - Pendulum Ruler | `68508433` | [Scripts/c68508433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68508433.lua) | 52 |
| Neiroy, the Dream Mirror Traitor | `90176467` | [Scripts/c90176467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90176467.lua) | 52 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Abyss Actor - Superstar | `25629622` | [Scripts/c25629622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25629622.lua) | 52 |
| Soul of the Supreme Celestial King | `76840111` | [Scripts/c76840111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76840111.lua) | 52 |
| Prompthorn | `50548657` | [Scripts/c50548657.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50548657.lua) | 52 |
| Oh Tokenbaum! | `97173708` | [Scripts/c97173708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97173708.lua) | 52 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28651380.lua) | 51 |
| Ancient Gear Advance | `4064925` | [Scripts/c4064925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4064925.lua) | 51 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 51 |
| Assault Reboot | `74431740` | [Scripts/c74431740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74431740.lua) | 51 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 51 |
| ...and 406 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	local g=eg:Filter(c59255742.filter,nil,tp)
	if chk==0 then return Duel.CheckReleaseGroup(tp,c59255742.costfilter,1,nil,tp,g) end
	local g=Duel.SelectReleaseGroup(tp,c59255742.costfilter,1,1,nil,tp,g)
	Duel.Release(g,REASON_COST)
end
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckReleaseGroup(tp,s.rlfilter,1,nil) end
	local g=Duel.SelectReleaseGroup(tp,s.rlfilter,1,1,nil)
	Duel.Release(g,REASON_COST)
end
```

### Frightfur Meister (`77522571`)

Source: [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua)

```lua
function c77522571.spcost1(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckReleaseGroup(tp,c77522571.costfilter1,1,nil,e,tp) end
	local rg=Duel.SelectReleaseGroup(tp,c77522571.costfilter1,1,1,nil,e,tp)
	e:SetLabel(rg:GetFirst():GetLevel())
	e:SetValue(rg:GetFirst():GetCode())
```
