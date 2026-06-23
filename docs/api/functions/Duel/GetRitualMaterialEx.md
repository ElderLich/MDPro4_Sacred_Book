# Duel.GetRitualMaterialEx

## Signature

```lua
Duel.GetRitualMaterialEx(int player) -> Group
```

## Description

Returns an extended Ritual Material pool, including monsters without a Level.
Local Drytron-style scripts use this when the Ritual procedure compares something other than ordinary Levels, such as an ATK-based value.
After collecting the group, still apply the script's own race, card text, and Ritual Monster material checks.

## Parameters

- `player` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4998`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetRitualMaterialEx`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local mg=Duel.GetRitualMaterialEx(tp):Filter(Card.IsRace,nil,RACE_MACHINE)
		return Duel.IsExistingMatchingCard(s.RitualUltimateFilter,tp,LOCATION_HAND+LOCATION_GRAVE,0,1,nil,s.rfilter,e,tp,mg,nil,aux.GetCappedAttack,"Greater")
	end
```

### Meteonis Drytron (`22398665`)

Source: [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua)

```lua
function c22398665.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local mg=Duel.GetRitualMaterialEx(tp):Filter(Card.IsRace,nil,RACE_MACHINE)
		return Duel.IsExistingMatchingCard(c22398665.RitualUltimateFilter,tp,LOCATION_HAND+LOCATION_GRAVE,0,1,nil,nil,e,tp,mg,nil,aux.GetCappedAttack,"Greater")
	end
```
