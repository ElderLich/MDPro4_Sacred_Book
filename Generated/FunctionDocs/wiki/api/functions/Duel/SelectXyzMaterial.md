# Duel.SelectXyzMaterial

## Signature

```lua
Duel.SelectXyzMaterial(int player, Card c, [function|nil f], int lv, int min, int max, [Group|nil mg]) -> Group
```

## Description

让玩家player为XYZ怪兽c从场上[或mg中]选择XYZ用等级为lv的min-max个满足条件f的叠放素材

## Parameters

- `player` `int`
- `c` `Card`
- `f` `function|nil` optional
- `lv` `int`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5013`
