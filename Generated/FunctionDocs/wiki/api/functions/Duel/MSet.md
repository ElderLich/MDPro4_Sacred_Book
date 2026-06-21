# Duel.MSet

## Signature

```lua
Duel.MSet(int player, Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> void
```

## Description

让玩家 player 以效果e对c[在区域 zone]进行通常召唤的Set，至少使用min个祭品
如果e=nil,那么就按照一般的通常召唤规则进行通常召唤
如果ignore_count=true，则忽略每回合的通常召唤次数限制

## Parameters

- `player` `int`
- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4870`
