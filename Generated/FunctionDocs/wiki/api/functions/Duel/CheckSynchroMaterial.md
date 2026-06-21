# Duel.CheckSynchroMaterial

## Signature

```lua
Duel.CheckSynchroMaterial(Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> bool
```

## Description

检查场上[或mg中]是否存在一组[必须包括smat在内的（如果有mg~=nil则忽略此参数）]满足条件的卡作为同调召唤c的素材
f1是 1 只需要满足的过滤条件，f2是 min-max 只需要满足的过滤条件
f1,f2 之中，至少有一种为调整的条件

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `smat` `Card|nil` optional
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4994`
