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
