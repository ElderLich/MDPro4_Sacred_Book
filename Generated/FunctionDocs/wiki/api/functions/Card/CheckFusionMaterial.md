# Card.CheckFusionMaterial

## Signature

```lua
Card.CheckFusionMaterial(Card c, [Group|nil g], [Card|nil gc], [int chkf], [bool not_material]) -> bool
```

## Description

检查场上[或g]是否包含了c需要[必须包含gc在内]的一组融合素材
##根据c的种类为EFFECT_FUSION_MATERIAL的效果的Condition函数检查

## Parameters

- `c` `Card`
- `g` `Group|nil` optional
- `gc` `Card|nil` optional
- `chkf` `int` optional - default: PLAYER_NONE
- `not_material` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3644`
