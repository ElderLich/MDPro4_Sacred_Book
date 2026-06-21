# Duel.Summon

## Signature

```lua
Duel.Summon(int player, Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> void
```

## Description

Makes player Normal Summon c, not Set it, optionally by effect e and requiring at least min Tributes.
If e is nil, regular Normal Summon rules are used. If ignore_count is true, the once-per-turn Normal Summon limit is ignored.

## Parameters

- `player` `int`
- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4865`
