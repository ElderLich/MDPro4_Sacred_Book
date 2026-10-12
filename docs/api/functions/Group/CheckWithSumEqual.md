# Group.CheckWithSumEqual

## Signature

```lua
Group.CheckWithSumEqual(Group g, function f, int acc, int min, int max, [... any]) -> bool
```

## Description

Checks whether a subset of g, including any must-select cards, can make the f-sum exactly acc using between min and max cards.

## Parameters

- `g` `Group`
- `f` `function`
- `acc` `int`
- `min` `int`
- `max` `int`
- `...` `any` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:920`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)
- [Ritual Procedure Guide](/learn/ritual-procedure)
- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.CheckWithSumEqual) with `Group.CheckWithSumEqual`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 2 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 2 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 2 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 2 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89818984.lua) | 2 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55749927.lua) | 2 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33541430.lua) | 2 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21915012.lua) | 2 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61052897.lua) | 2 |
| Prompthorn | `50548657` | [Scripts/c50548657.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50548657.lua) | 1 |
| Blackwing - Gofu the Vague Shadow | `9929398` | [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9929398.lua) | 1 |
| Rampaging Smashtank Rhynosaber | `82197831` | [Scripts/c82197831.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82197831.lua) | 1 |
| Rescue Ferret | `56343672` | [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56343672.lua) | 2 |
| Benghalancer the Resurgent | `73345237` | [Scripts/c73345237.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73345237.lua) | 1 |
| T.G. Cyber Magician | `64910482` | [Scripts/c64910482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64910482.lua) | 1 |
| Blackwing - Vata the Emblem of Wandering | `71187462` | [Scripts/c71187462.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71187462.lua) | 1 |
| Starliege Seyfert | `15381421` | [Scripts/c15381421.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15381421.lua) | 1 |
| Variety Comes Out | `65196094` | [Scripts/c65196094.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65196094.lua) | 1 |
| Vendread Reunion | `2266498` | [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2266498.lua) | 1 |
| Block Dragon | `94689206` | [Scripts/c94689206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94689206.lua) | 1 |
| Tatsunoko | `55863245` | [Scripts/c55863245.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55863245.lua) | 1 |
| Tatsunecro | `3096468` | [Scripts/c3096468.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3096468.lua) | 1 |
| ...and 13 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
function s.LCheckGoal(sg,tp,lc,gf,lmat)
	return (Duel.IsPlayerAffectedByEffect(tp,38391684)
		and sg:CheckWithSumEqual(s.GetLinkCount,2,#sg,#sg)
		or sg:CheckWithSumEqual(s.GetLinkCount,lc:GetLink(),#sg,#sg))
		and Duel.GetLocationCountFromEx(tp,tp,sg,lc)>0 and (not gf or gf(sg,lc,tp))
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
function s.LCheckGoal(sg,tp,lc,gf,lmat)
	return (Duel.IsPlayerAffectedByEffect(tp,38391684)
		and sg:CheckWithSumEqual(s.GetLinkCount,3,#sg,#sg)
		or sg:CheckWithSumEqual(s.GetLinkCount,lc:GetLink(),#sg,#sg))
		and Duel.GetLocationCountFromEx(tp,tp,sg,lc)>0 and (not gf or gf(sg,lc,tp))
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
function s.RitualCheckEqual(g,c,atk)
	if atk==0 then return false end
	return g:CheckWithSumEqual(aux.GetCappedAttack,atk,#g,#g)
end
function s.RitualCheck(g,tp,c,atk,greater_or_equal)
```
