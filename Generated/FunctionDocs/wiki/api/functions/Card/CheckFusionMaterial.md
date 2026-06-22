# Card.CheckFusionMaterial

## Signature

```lua
Card.CheckFusionMaterial(Card c, [Group|nil g], [Card|nil gc], [int chkf], [bool not_material]) -> bool
```

## Description

Checks whether c's Fusion Material requirements can be satisfied by g, optionally requiring gc to be included.
chkf is forwarded to the Fusion Material condition check, and not_material is used by procedures that check material availability without treating the cards as actual materials yet.

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
