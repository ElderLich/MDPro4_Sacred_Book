# Group.SelectSubGroup

## Signature

```lua
Group.SelectSubGroup(Group g, int tp, function f, bool cancelable, [int min], [int max], ... any) -> Group|nil
```

## Description

Lets tp select a subgroup from g with size between min and max that satisfies f. It respects already selected cards and returns nil if no valid selection is completed.

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
