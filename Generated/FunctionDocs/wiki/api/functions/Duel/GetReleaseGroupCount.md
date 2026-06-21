# Duel.GetReleaseGroupCount

## Signature

```lua
Duel.GetReleaseGroupCount(int player, [bool use_hand], [int reason]) -> int
```

## Description

返回玩家player能以原因reason解放的卡片数量， use_hand=true 则包括手卡

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4975`
