# Duel.SetFusionMaterial

## Signature

```lua
Duel.SetFusionMaterial(Group g) -> void
```

## Description

Replaces the core's current Fusion Material set with the cards in g.
Fusion Material procedure operations use this after selecting a legal group so the later Fusion Summon operation can read the selected materials.
This function records the selection only; it does not move the materials or return a value.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4990`
