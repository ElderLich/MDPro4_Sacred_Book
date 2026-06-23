# Duel.GetRitualMaterialEx

## Signature

```lua
Duel.GetRitualMaterialEx(int player) -> Group
```

## Description

Returns an extended Ritual Material pool, including monsters without a Level.
Local Drytron-style scripts use this when the Ritual procedure compares something other than ordinary Levels, such as an ATK-based value.
After collecting the group, still apply the script's own race, card text, and Ritual Monster material checks.

## Parameters

- `player` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4998`
