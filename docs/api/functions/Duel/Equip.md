# Duel.Equip

## Signature

```lua
Duel.Equip(int player, Card c1, Card c2, [bool up], [bool is_step]) -> bool
```

## Description

The player as a player c1 equipment card equipment to the c2, the return value that is successful
Up = false to retain the card before the representation
Is_step = true is the decomposition of the equipment process, the need to cooperate with Duel.EquipComplete use

## Parameters

- `player` `int`
- `c1` `Card`
- `c2` `Card`
- `up` `bool` optional - default: true
- `is_step` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4904`
