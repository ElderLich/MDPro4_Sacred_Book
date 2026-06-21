# Duel.CheckTribute

## Signature

```lua
Duel.CheckTribute(Card c, int min, [int|nil max], [Group|nil mg], [int|nil toplayer], [int|nil zone]) -> Group
```

## Description

判断场上[或mg中]是否存在用于通常召唤c[到toplayer场上的区域 zone]的min[到max]个祭品

## Parameters

- `c` `Card`
- `min` `int`
- `max` `int|nil` optional - default: min
- `mg` `Group|nil` optional
- `toplayer` `int|nil` optional - default: c:GetControler()
- `zone` `int|nil` optional - default: 0x1f

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4982`
