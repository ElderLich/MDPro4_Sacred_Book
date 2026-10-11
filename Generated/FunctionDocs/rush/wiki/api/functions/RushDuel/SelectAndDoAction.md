# RushDuel.SelectAndDoAction

Alias: `RD.SelectAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndDoAction(int hint, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, function action) -> any
```

## Description

Finds matching cards in the specified locations, asks tp to select a non-cancelable Group of min to max cards, and immediately calls action(selected_group). Use during resolution, not during a chk==0 legality test. This helper does not select activation targets or store a target relation.
The public wrapper passes only a Card to filter and only the selected Group to action; capture other values in closures or compose a filter with RD.Filter. It emits a selection hint for public-location searches. If there are too few candidates or the selected Group is empty, it returns numeric 0 without calling action.
On a nonempty selection it forwards every return value from action unchanged. A callback with no return makes this helper return no values (nil in a single-value assignment); it does not automatically return the selected count or success.

## Parameters

- `hint` `int`: Selection prompt identifier, such as HINTMSG_TOGRAVE or aux.Stringid(id, n).
- `filter` `function`: Card predicate. Include the needed operation-legality checks.
- `tp` `int`: Selecting player; 0 or 1.
- `s_range` `int`: Locations on tp's side.
- `o_range` `int`: Locations on the opponent's side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum selected count.
- `expect` `Card|Group|nil`: Card(s) excluded from matching; pass nil for no exclusion. The upstream parameter is spelled expect.
- `action` `function`: Called as action(selected_group) immediately after a nonempty selection.

## Returns

- `any`: Exactly the callback's return values when invoked; otherwise numeric 0. A callback may return no values.

## Example

```lua
local moved = RD.SelectAndDoAction(HINTMSG_TOGRAVE,
    Card.IsAbleToGrave, tp, LOCATION_MZONE, 0, 1, 1, nil,
    function(g) return Duel.SendtoGrave(g, REASON_EFFECT) end)
if moved > 0 then
    -- The returned movement count is positive.
end
```

## Source

`Rush/Utilities/RDAction.lua:102`

```lua
function RushDuel.SelectAndDoAction(hint, filter, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_select_match(hint, filter, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```
