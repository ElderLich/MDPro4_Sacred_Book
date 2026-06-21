# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group,int,int,int
```

## Description

Returns operation information recorded for category on chainc.
The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.

## Parameters

- `chainc` `int`
- `category` `int`

## Returns

- `bool`
- `Group` - may be nil
- `int` - may be nil
- `int` - may be nil
- `int` - may be nil

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`
