# Group.SelectSubGroupEach

## Signature

```lua
Group.SelectSubGroupEach(Group g, int tp, table checks, [bool cancelable], [function f], ... any) -> Group|nil
```

## Description

Lets tp select one card for each filter in checks, optionally cancelable. If f is omitted, Auxiliary.TRUE is used for the final group check.

## Parameters

- `g` `Group`
- `tp` `int`
- `checks` `table`
- `cancelable` `bool` optional
- `f` `function` optional
- `...` `any`

## Returns

- `Group|nil` - The selected subgroup, or nil if no valid selection is completed.

## Source

- `Utilities/utility.lua:1356`
