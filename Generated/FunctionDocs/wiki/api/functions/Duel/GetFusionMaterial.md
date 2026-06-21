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

- `Group` - material_all includes cards affected by EFFECT_EXTRA_FUSION_MATERIAL
- `Group` - material_base contains only cards from the requested locations

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5000`
