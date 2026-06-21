# Duel.SelectSynchroMaterial

## Signature

```lua
Duel.SelectSynchroMaterial(int player, Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> Group
```

## Description

让玩家player从场上[或mg中]选择用于同调c需要的[必须包含smat在内（如果有mg~=nil则忽略此参数）]满足条件的一组素材
f1是 1 只需要满足的过滤条件，f2是 min-max 只需要满足的过滤条件
f1,f2 之中，至少有一种为调整的条件

## Parameters

- `player` `int`
- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `smat` `Card|nil` optional
- `mg` `Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4993`
