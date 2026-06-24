# Group.SelectUnselect

## Signature

```lua
Group.SelectUnselect(Group cg, [Group|nil sg], int player, [bool finishable], [bool cancelable], [int min], [int max]) -> Card|nil
```

## Description

Lets player choose one card from cg to add to the current selection or one card from sg to remove from it, then returns the card that was chosen.
sg may be nil. finishable controls whether the selection can finish at its current size, cancelable allows cancellation, and cancellation returns nil. min and max default to 1.
This is a building block for step-by-step material or procedure selections. For ordinary one-shot choices, Group.Select, Group.FilterSelect, or Duel.SelectMatchingCard is usually clearer.

## Parameters

- `cg` `Group`
- `sg` `Group|nil` optional
- `player` `int`
- `finishable` `bool` optional - default: false
- `cancelable` `bool` optional - default: false
- `min` `int` optional - default: 1
- `max` `int` optional - default: 1

## Returns

- `Card|nil` - Chosen card, or nil if the selection is canceled.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:916`
