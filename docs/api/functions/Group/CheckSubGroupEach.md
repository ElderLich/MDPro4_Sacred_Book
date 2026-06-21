# Group.CheckSubGroupEach

## Signature

```lua
Group.CheckSubGroupEach(Group g, table checks, [function f], ... any) -> bool
```

## Description

Checks whether g can supply one card for each filter in checks. If f is omitted, only the per-position checks are required.

## Parameters

- `g` `Group`
- `checks` `table`
- `f` `function` optional
- `...` `any`

## Returns

- `bool` - true if one card can satisfy each check.

## Source

- `Utilities/utility.lua:1338`
