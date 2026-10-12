# RushDuel.Select

Alias: `RD.Select`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Select(int hint, int player, Group group, function|nil check, bool cancelable, int min, int max, ... any) -> Group|nil
```

## Description

Displays the supplied selection hint, then selects cards from group. Without check it uses Select or CancelableSelect; with check it uses SelectSubGroup. Always guard a cancelable result before dereferencing it.

## Parameters

- `hint` `int`: Selection hint identifier.
- `player` `int`: Selecting player, 0 or 1.
- `group` `Group`: Candidate cards.
- `check` `function|nil`: Optional whole-group predicate; pass nil for an ordinary selection.
- `cancelable` `bool`: Whether cancellation is permitted.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum selected count.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `Group|nil`: Selected cards; nil on cancellation.

## Example

```lua
local sg = RD.Select(HINTMSG_TOGRAVE, tp, g, nil, true, 1, 1)
if not sg then return end
Duel.SendtoGrave(sg, REASON_EFFECT)
```

## Source

`Rush/Utilities/RDFunction.lua:32`

```lua
function RushDuel.Select(hint, player, group, check, cancelable, min, max, ...)
    Duel.Hint(HINT_SELECTMSG, player, hint)
    if check == nil then
        if cancelable then
            return group:CancelableSelect(player, min, max, nil)
        else
            return group:Select(player, min, max, nil)
        end
    else
        return group:SelectSubGroup(player, check, cancelable, min, max, ...)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.Select) with `RushDuel.Select`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Elemental Circulation](/examples/rush-cards/120263030) | `120263030` | [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua) | 1 |
| I Hear Footsteps | `120217085` | [Rush/Scripts/c120217085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217085.lua) | 1 |

## Script Examples

### Elemental Circulation (`120263030`)

Source: [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua)

```lua
	local g=Duel.GetMatchingGroup(cm.costfilter,tp,LOCATION_EXTRA+LOCATION_HAND,0,nil)
	if chk==0 then return g:CheckSubGroup(cm.check,2,2) end
	local sg=RD.Select(aux.Stringid(m,1),tp,g,cm.check,false,2,2)
	local mc,fc=sg:GetFirst(),sg:GetNext()
	if mc:IsLocation(LOCATION_EXTRA) then mc,fc=fc,mc end
```

### I Hear Footsteps (`120217085`)

Source: [Rush/Scripts/c120217085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217085.lua)

```lua
		local og=g:Filter(cm.setfilter,nil)
		if ft>0 and og:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
			local sg=RD.Select(HINTMSG_SET,tp,og,cm.setcheck,false,1,3,ft)
			local dam=Duel.SSet(1-tp,sg)
			Duel.Damage(1-tp,dam*300,REASON_EFFECT)
```
