# Duel.CheckTunerMaterial

## Signature

```lua
Duel.CheckTunerMaterial(Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> bool
```

## Description

检查场上[或mg中]是否存在一组以tuner作为调整,并且满足条件的卡作为同调召唤c的素材
f1是 1 只需要满足的过滤条件，f2是 min-max 只需要满足的过滤条件

## Parameters

- `c` `Card`
- `tuner` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4996`
