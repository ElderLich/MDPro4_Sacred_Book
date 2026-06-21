# Duel.XyzSummon

## Signature

```lua
Duel.XyzSummon(int player, Card c, [Group|nil mg], [int min], [int max]) -> void
```

## Description

让玩家player用场上的卡[或mg][选min-max个素材]对c进行XYZ召唤手续
mg非空且min为0则直接把mg全部作为XYZ素材

## Parameters

- `player` `int`
- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4868`
