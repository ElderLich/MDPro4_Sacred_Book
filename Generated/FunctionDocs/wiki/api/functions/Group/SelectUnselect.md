# Group.SelectUnselect

## Signature

```lua
Group.SelectUnselect(Group cg, [Group|nil sg], int player, bool btok, bool cancelable, int minc, int maxc) -> Card|nil
```

## Description

让玩家 player 从 cg 中选择 1 张卡放入 sg ，并返回选的卡。
btok 表示是否可以点击完成选择的按钮， cancelable 表示是否可以取消整个选择返回 nil，
minc 和 maxc 是客户端的文字缓冲提示，表示需要选择 minc-maxc 张卡，但是这个只是影响视觉效果，并不代表必须要选择那个数量

## Parameters

- `cg` `Group`
- `sg` `Group|nil` optional - 已选的卡，可以从中取消选择
- `player` `int`
- `btok` `bool` - default: false
- `cancelable` `bool` - default: false
- `minc` `int`
- `maxc` `int`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:916`
