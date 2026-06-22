# Duel.SelectFusionMaterial

## Signature

```lua
Duel.SelectFusionMaterial(int player, Card c, Group g, [Card|nil gc], [int chkf], [bool not_material]) -> Group
```

## Description

Lets player select a valid Fusion Material group for Fusion Monster c from g and returns the selected Group.
gc, when supplied, must be included. The returned Group also contains gc, matching the core selection behavior.

## Parameters

- `player` `int`
- `c` `Card`
- `g` `Group`
- `gc` `Card|nil` optional
- `chkf` `int` optional - default: PLAYER_NONE
- `not_material` `bool` optional - default: false

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4989`
