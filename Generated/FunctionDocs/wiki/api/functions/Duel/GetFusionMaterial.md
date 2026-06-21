# Duel.GetFusionMaterial

## Signature

```lua
Duel.GetFusionMaterial(int player, [int location]) -> Group,Group
```

## Description

返回玩家player可用的用于融合召唤素材的卡片组

## Parameters

- `player` `int`
- `location` `int` optional - default: LOCATION_HAND + LOCATION_MZONE

## Returns

- `Group` - material_all 包含受EFFECT_EXTRA_FUSION_MATERIAL影响的卡
- `Group` - material_base 只取那些区域的卡

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5000`
