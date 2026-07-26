# Group.CancelableSelect

## Signature

```lua
Group.CancelableSelect(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group|nil
```

## Description

Lets player select min to max cards from g, excluding ex; the selection can be canceled and return nil.

## Parameters

- `g` `Group`
- `player` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional

## Returns

- `Group|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:918`
