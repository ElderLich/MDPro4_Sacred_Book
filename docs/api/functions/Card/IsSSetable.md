# Card.IsSSetable

## Signature

```lua
Card.IsSSetable(Card c, [bool ignore_field]) -> bool
```

## Description

Checks whether c can be Set in a Spell & Trap Zone. If ignore_field is true, available zone checks are ignored.

## Parameters

- `c` `Card`
- `ignore_field` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3636`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **314** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsSSetable) with `Card.IsSSetable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua) | 2 |
| K9-EW Special Release Experiment | `26585784` | [Scripts/c26585784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26585784.lua) | 1 |
| Dracotail Mululu | `7375867` | [Scripts/c7375867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7375867.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90809975.lua) | 1 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 1 |
| Dracotail Faimena | `1498449` | [Scripts/c1498449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1498449.lua) | 1 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 1 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57775790.lua) | 1 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 1 |
| Azamina Determination | `42201897` | [Scripts/c42201897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42201897.lua) | 1 |
| Zenet Revelator Nefertari | `84512726` | [Scripts/c84512726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84512726.lua) | 1 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 1 |
| Mementomictlan | `43338320` | [Scripts/c43338320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43338320.lua) | 1 |
| Abyss Actor - Superstar | `25629622` | [Scripts/c25629622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25629622.lua) | 1 |
| Dark Spell Regeneration | `12930501` | [Scripts/c12930501.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12930501.lua) | 1 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 1 |
| D/D/D Duo-Dawn King Kali Yuga | `15939229` | [Scripts/c15939229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15939229.lua) | 1 |
| Scourge of the White Forest | `93723936` | [Scripts/c93723936.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93723936.lua) | 1 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 1 |
| Sloppy Stasher Squirrel | `42081767` | [Scripts/c42081767.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42081767.lua) | 1 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 1 |
| ...and 290 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
end
function s.setfilter(c)
	return c:IsSetCard(0x1cd) and c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsSSetable()
end
function s.settg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
function s.setfilter(c,e,tp)
	return c:IsType(TYPE_MONSTER) and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEDOWN) and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		or c:IsType(TYPE_TRAP) and c:IsSSetable()
end
function s.cspfilter(c)
```

### Albion the Branded Dragon (`87746184`)

Source: [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua)

```lua
function c87746184.thfilter(c)
	if not (c:IsSetCard(0x15d) and c:IsType(TYPE_SPELL+TYPE_TRAP)) then return false end
	return c:IsAbleToHand() or c:IsSSetable()
end
function c87746184.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
