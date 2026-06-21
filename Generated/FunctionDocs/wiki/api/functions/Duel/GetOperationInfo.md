# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group,int,int,int
```

## Description

返回连锁chainc的category分类的操作信息，存在的话，则返回值为5个， chainc=0 则是表示当前连锁
第一个返回值是false的话表示不存在该分类
后4个返回值对应Duel.SetOperationInfo的后4个参数：Card|Group targets, int count, int target_player, int target_param

## Parameters

- `chainc` `int`
- `category` `int`

## Returns

- `bool`
- `Group` - 可能为空
- `int` - 可能为空
- `int` - 可能为空
- `int` - 可能为空

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`
