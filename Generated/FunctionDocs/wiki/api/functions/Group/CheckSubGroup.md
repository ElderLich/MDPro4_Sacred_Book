# Group.CheckSubGroup

## Signature

```lua
Group.CheckSubGroup(Group g, function f, [int min], [int max], ... any) -> bool
```

## Description

Checks whether g has a subgroup with size between min and max that satisfies f, while respecting already selected cards from Duel.GrabSelectedCard and Auxiliary.GCheckAdditional.

## Parameters

- `g` `Group`
- `f` `function`
- `min` `int` optional
- `max` `int` optional
- `...` `any`

## Returns

- `bool` - true if a valid subgroup exists.

## Source

- `Utilities/utility.lua:1233`
