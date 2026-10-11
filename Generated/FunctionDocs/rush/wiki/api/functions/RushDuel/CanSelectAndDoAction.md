# RushDuel.CanSelectAndDoAction

Alias: `RD.CanSelectAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndDoAction(int desc, int hint, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, function action) -> any
```

## Description

Optional resolution action: finds candidates, asks a yes/no question, then selects a Group and calls action(selected_group). Despite its name, this helper performs selection and the action; do not use it as a legality predicate or inside chk==0.
Declining the yes/no question, having too few candidates, or selecting an empty Group returns numeric 0 without running action. Canceling card selection returns to the yes/no question through RD.CanSelect. Once the player completes a nonempty selection, every callback return value is forwarded unchanged, including no values.
Like RD.SelectAndDoAction, it creates no activation target relation, passes no extra arguments to the filter/action, and emits a selection hint for public-location searches.

## Parameters

- `desc` `int`: Yes/no question description identifier.
- `hint` `int`: Card-selection prompt identifier.
- `filter` `function`: Card predicate including required action-legality checks.
- `tp` `int`: Selecting player; 0 or 1.
- `s_range` `int`: Locations on tp's side.
- `o_range` `int`: Locations on the opponent's side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum selected count.
- `expect` `Card|Group|nil`: Card(s) excluded from matching; pass nil for none.
- `action` `function`: Called as action(selected_group) after the player accepts and completes selection.

## Returns

- `any`: Exactly the callback's return values when invoked; otherwise numeric 0. A callback may return no values.

## Source

`Rush/Utilities/RDAction.lua:107`

```lua
function RushDuel.CanSelectAndDoAction(desc, hint, filter, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_can_select_match(desc, hint, filter, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```
