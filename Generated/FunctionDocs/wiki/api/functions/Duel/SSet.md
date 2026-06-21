# Duel.SSet

## Signature

```lua
Duel.SSet(int player, Card|Group targets, [int target_player], [bool confirm]) -> int
```

## Description

让玩家player把targets盖放到target_player的魔法陷阱区， confirm 表示是否需要确认
若targets为Group，则返回成功操作的数量

## Parameters

- `player` `int`
- `targets` `Card|Group`
- `target_player` `int` optional - default: player
- `confirm` `bool` optional - default: true

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4871`
