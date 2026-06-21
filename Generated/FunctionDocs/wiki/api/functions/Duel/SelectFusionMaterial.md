# Duel.SelectFusionMaterial

## Signature

```lua
Duel.SelectFusionMaterial(int player, Card c, [Group|nil g], [Card|nil gc], [int chkf], [bool not_material]) -> Group
```

## Description

让玩家player从g中选择一组[必须包含gc在内的]融合怪兽c的融合素材
##根据c的种类为EFFECT_FUSION_MATERIAL的效果的Operation操作

## Parameters

- `player` `int`
- `c` `Card`
- `g` `Group|nil` optional - 不能为空
- `gc` `Card|nil` optional
- `chkf` `int` optional - default: PLAYER_NONE
- `not_material` `bool` optional - default: false

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4989`
