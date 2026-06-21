# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group,int,int,int
```

## Description

Returns the operation information of the chained chainc category, with a return value of 5,
The first return value is false to indicate that the class does not exist
The last four return values ​​correspond to the last four parameters of Duel.SetOperationInfo: Card|Group targets, int count, int target_player, int target_param

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
