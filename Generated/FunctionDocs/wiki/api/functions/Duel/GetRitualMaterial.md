# Duel.GetRitualMaterial

## Signature

```lua
Duel.GetRitualMaterial(int player) -> Group
```

## Description

Returns the cards player can use as basic Ritual Material.
The group includes cards in the hand or field that can be Tributed, plus Ritual-material exceptions such as suitable cards in the Graveyard.
This is only the starting pool. After a Ritual Monster is chosen, filter the group with Card.IsCanBeRitualMaterial and then perform the exact or greater-or-equal material total check.

## Parameters

- `player` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4997`
