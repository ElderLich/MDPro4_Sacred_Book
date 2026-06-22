# Duel.GetSynchroMaterial

## Signature

```lua
Duel.GetSynchroMaterial(int player, [bool facedown]) -> Group
```

## Description

Gets the group of cards player can use as Synchro Material.
Face-down cards in the Monster Zone are omitted unless facedown is true.

## Parameters

- `player` `int`
- `facedown` `bool` optional - default: false

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4992`
