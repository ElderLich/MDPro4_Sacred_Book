# Duel.SelectTribute

## Signature

```lua
Duel.SelectTribute(int player, Card c, int min, int max, [Group|nil mg], [int|nil toplayer]) -> Group
```

## Description

让玩家player从场上[或mg中]选择用于通常召唤c的min-max个祭品，召唤到 toplayer 场上

## Parameters

- `player` `int`
- `c` `Card`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional
- `toplayer` `int|nil` optional - default: c:GetControler()

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4983`
