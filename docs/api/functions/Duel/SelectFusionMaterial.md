# Duel.SelectFusionMaterial

## Signature

```lua
Duel.SelectFusionMaterial(int player, Card c, [Group|nil g], [Card|nil gc], [int chkf], [bool not_material]) -> Group
```

## Description

Let the player player from the g to select a group [must contain gc] fusion fusion monster c material

## Parameters

- `player` `int`
- `c` `Card`
- `g` `Group|nil` optional - cannot be nil when selecting materials
- `gc` `Card|nil` optional
- `chkf` `int` optional - default: PLAYER_NONE
- `not_material` `bool` optional - default: false

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4989`
