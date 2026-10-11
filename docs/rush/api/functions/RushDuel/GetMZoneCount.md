# RushDuel.GetMZoneCount

Alias: `RD.GetMZoneCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetMZoneCount(int player, int max) -> int
```

## Description

Returns the available Monster Zone count capped by max, with the helper's special one-zone restriction applied when effect 59822133 affects the player.

## Parameters

- `player` `int`: Player, 0 or 1.
- `max` `int`: Upper bound; required by math.min.

## Returns

- `int`: Capped available zone count.

## Source

`Rush/Utilities/RDFunction.lua:125`

```lua
function RushDuel.GetMZoneCount(player, max)
    local ct = Duel.GetLocationCount(player, LOCATION_MZONE)
    if Duel.IsPlayerAffectedByEffect(player, 59822133) then
        ct = math.min(ct, 1)
    end
    return math.min(ct, max)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.GetMZoneCount) with `RushDuel.GetMZoneCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| Plectclive the Dynamauve Deadly Dirge | `120253043` | [Rush/Scripts/c120253043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253043.lua) | 1 |
| Night Before the Big March | `120238023` | [Rush/Scripts/c120238023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238023.lua) | 1 |

## Script Examples

### Devil Foolish (`120244026`)

Source: [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua)

```lua
end
function cm.max(e,tp,eg,ep,ev,re,r,rp)
	local ct1=RD.GetMZoneCount(tp,2)
	local ct2=Duel.GetMatchingGroupCount(cm.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
	return math.min(ct1,ct2)
```

### Plectclive the Dynamauve Deadly Dirge (`120253043`)

Source: [Rush/Scripts/c120253043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253043.lua)

```lua
end
function cm.max(e,tp,eg,ep,ev,re,r,rp)
	local ct1=RD.GetMZoneCount(tp,2)
	local ct2=Duel.GetMatchingGroupCount(cm.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
	return math.min(ct1,ct2)
```

### Night Before the Big March (`120238023`)

Source: [Rush/Scripts/c120238023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238023.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<3 then return end
	local ct=RD.GetMZoneCount(tp,2)
	local sg,g=RD.RevealDeckTopAndCanSelect(tp,3,aux.Stringid(m,1),HINTMSG_SPSUMMON,cm.spfilter,1,ct,e,tp,ct)
	if sg:GetCount()>0 then
```
