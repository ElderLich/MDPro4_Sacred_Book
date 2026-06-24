# Group.SelectSubGroup

## Signature

```lua
Group.SelectSubGroup(Group g, int tp, function f, bool cancelable, [int min], [int max], ... any) -> Group|nil
```

## Description

Lets tp select a subgroup from g with size between min and max that satisfies f. It respects already selected cards and returns nil if no valid selection is completed.
Use Group.CheckSubGroup for the legality check, then SelectSubGroup where the player actually chooses the cards. If the chosen Group is stored for a later callback, call KeepAlive and later DeleteGroup.

## Parameters

- `g` `Group`
- `tp` `int`
- `f` `function`
- `cancelable` `bool`
- `min` `int` optional
- `max` `int` optional
- `...` `any`

## Returns

- `Group|nil` - The selected subgroup, or nil if no valid selection is completed.

## Source

- `Utilities/utility.lua:1255`
