# Duel.GetUsableMZoneCount

## Signature

```lua
Duel.GetUsableMZoneCount(int player, [int use_player]) -> int|nil
```

## Description

Returns how many Monster Zones player can use for a monster entering the field.
use_player defaults to the current reason player and is used for zone-limit checks involving the acting player.

## Parameters

- `player` `int`
- `use_player` `int` optional - default: current reason player

## Returns

- `int|nil` - Usable Monster Zone count, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4939`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetUsableMZoneCount) with `Duel.GetUsableMZoneCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| Soul of the Supreme King | `92428405` | [Scripts/c92428405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92428405.lua) | 1 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 1 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 1 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 1 |
| Gem-Knight Master Diamond Dispersion | `25342956` | [Scripts/c25342956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25342956.lua) | 1 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 1 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 2 |
| Supreme Rage | `84869738` | [Scripts/c84869738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84869738.lua) | 1 |
| Virtual World City - Kauwloon | `14886190` | [Scripts/c14886190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14886190.lua) | 1 |
| A.I.'s Show | `54374642` | [Scripts/c54374642.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54374642.lua) | 1 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	local ft1=Duel.GetLocationCount(tp,LOCATION_MZONE)
	local ft2=Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_PENDULUM)
	local ft=Duel.GetUsableMZoneCount(tp)
	local ect=c29724053 and Duel.IsPlayerAffectedByEffect(tp,29724053) and c29724053[tp]
	if ect and ect<ft2 then ft2=ect end
```

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
		local ft2=Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ)
		local ft3=Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_PENDULUM+TYPE_LINK)
		local ft=Duel.GetUsableMZoneCount(tp)
		if ect1 and ect1>ft2 then ft2=ect1 end
		if ect1 and ect1>ft3 then ft3=ect1 end
```

### Soul of the Supreme King (`92428405`)

Source: [Scripts/c92428405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92428405.lua)

```lua
	local ft2=Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ)
	local ft3=Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_PENDULUM+TYPE_LINK)
	local ft=Duel.GetUsableMZoneCount(tp)
	if Duel.IsPlayerAffectedByEffect(tp,59822133) then
		if ft1>0 then ft1=1 end
```
