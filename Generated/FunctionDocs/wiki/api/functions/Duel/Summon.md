# Duel.Summon

## Signature

```lua
Duel.Summon(int player, Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> void
```

## Description

Let the player to the effect of e to c is usually called (not set), at least use min sacrifice
If e = nil, then in accordance with the general rules of the general call usually call
If ignore_count = true, the usual number of calls per turn limit is ignored

## Parameters

- `player` `int`
- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4865`
