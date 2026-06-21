# Group.CancelableSelect

## Signature

```lua
Group.CancelableSelect(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group
```

## Description

让玩家player从g中选择min-max张不等于ex的卡，可以取消并返回nil

## Parameters

- `g` `Group`
- `player` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:918`
