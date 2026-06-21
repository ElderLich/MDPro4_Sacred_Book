# Duel.GetReleaseGroup

## Signature

```lua
Duel.GetReleaseGroup(int player, [bool use_hand], [int reason]) -> Group
```

## Description

返回玩家player能以原因reason解放的卡片组， use_hand=true 则包括手卡

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4974`
