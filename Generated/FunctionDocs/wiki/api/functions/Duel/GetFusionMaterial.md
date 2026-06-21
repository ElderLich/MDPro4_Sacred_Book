# Duel.GetFusionMaterial

## Signature

```lua
Duel.GetFusionMaterial(int player, [int location]) -> Group,Group
```

## Description

Return the group of cards available to player for Fusion Summon materials
Includes monsters in hand, on the field, and cards affected by EFFECT_EXTRA_FUSION_MATERIAL

## Parameters

- `player` `int`
- `location` `int` optional - default: LOCATION_HAND + LOCATION_MZONE

## Returns

- `Group` - material_all 包含受EFFECT_EXTRA_FUSION_MATERIAL影响的卡
- `Group` - material_base 只取那些区域的卡

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5000`
