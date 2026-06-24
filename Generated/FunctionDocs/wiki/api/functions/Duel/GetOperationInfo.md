# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group|nil,int|nil,int|nil,int|nil
```

## Description

Returns operation information recorded for category on chainc.
The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.
Use this in response checks that need to inspect what a Chain Link announced, such as whether it is expected to destroy cards or move cards from a location.

## Parameters

- `chainc` `int` - Chain Link number to inspect. Use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* flag whose operation info should be read.

## Returns

- `bool` - true if operation info for category exists; false if not.
- `Group|nil` - Recorded target cards, or nil when only count/player/param were recorded.
- `int|nil` - Recorded expected count.
- `int|nil` - Recorded target player.
- `int|nil` - Recorded category-specific parameter, often a location or amount.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`
