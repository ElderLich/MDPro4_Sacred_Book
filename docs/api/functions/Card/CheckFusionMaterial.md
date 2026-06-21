# Card.CheckFusionMaterial

## Signature

```lua
Card.CheckFusionMaterial(Card c, [Group|nil g], [Card|nil gc], [int chkf], [bool not_material]) -> bool
```

## Description

Check if g contains a set of fusion material that c needs [must contain gc]

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
