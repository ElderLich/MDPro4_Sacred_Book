# Duel.LinkSummon

## Signature

```lua
Duel.LinkSummon(int player, Card pcard, [Group|nil mg], [Card lcard], [int minc], [int maxc]) -> void
```

## Description

让玩家player以mg[中除lcard以外的最少minc，最多maxc张卡]为素材将pcard连接召唤。

## Parameters

- `player` `int`
- `pcard` `Card`
- `mg` `Group|nil` optional
- `lcard` `Card` optional
- `minc` `int` optional
- `maxc` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4869`
