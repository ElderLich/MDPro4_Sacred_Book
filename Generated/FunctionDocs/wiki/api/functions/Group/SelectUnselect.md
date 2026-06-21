# Group.SelectUnselect

## Signature

```lua
Group.SelectUnselect(Group cg, [Group|nil sg], int player, bool btok, bool cancelable, int minc, int maxc) -> Card|nil
```

## Description

Have player select 1 card from cg to add to sg and return the selected card
btok indicates whether the confirm selection button is available, cancelable indicates whether selected cards can be canceled
minc and maxc are client-side text buffer prompts indicating the need to select minc-maxc cards, but this only affects visual display and does not enforce the selection count

## Parameters

- `cg` `Group`
- `sg` `Group|nil` optional - already selected cards that can be unselected
- `player` `int`
- `btok` `bool` - default: false
- `cancelable` `bool` - default: false
- `minc` `int`
- `maxc` `int`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:916`
