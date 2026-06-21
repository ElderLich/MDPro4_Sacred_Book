# Duel.CheckXyzMaterial

## Signature

```lua
Duel.CheckXyzMaterial(Card c, [function|nil f], int lv, int min, int max, [Group|nil mg]) -> bool
```

## Description

检查场上[或mg中]是否存在XYZ召唤c的XYZ用等级为lv的min-max个满足条件f的叠放素材

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `lv` `int`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5012`
