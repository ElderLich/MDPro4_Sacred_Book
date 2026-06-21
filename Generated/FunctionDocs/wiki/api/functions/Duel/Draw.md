# Duel.Draw

## Signature

```lua
Duel.Draw(int player, int count, int reason) -> int
```

## Description

让玩家player以原因reason抽count张卡，返回实际抽的卡的数量
如果reason含有REASON_RULE则此次抽卡不受“不能抽卡”的效果的影响

## Parameters

- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4900`
