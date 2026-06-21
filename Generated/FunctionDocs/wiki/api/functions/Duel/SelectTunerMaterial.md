# Duel.SelectTunerMaterial

## Signature

```lua
Duel.SelectTunerMaterial(int player, Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> Group
```

## Description

让玩家从场上[或mg中]选择用于同调c需要的满足条件的以tuner作为调整的min-max张卡的一组素材
f1是 1 只需要满足的过滤条件，f2是 min-max 只需要满足的过滤条件

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4995`
