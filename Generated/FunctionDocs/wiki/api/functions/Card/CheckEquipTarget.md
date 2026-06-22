# Card.CheckEquipTarget

## Signature

```lua
Card.CheckEquipTarget(Card c1, Card c2) -> bool
```

## Description

Checks whether c2 is a valid Equip target for c1.
The core requires c1 to be affected by an EFFECT_EQUIP_LIMIT that accepts c2, and it also enforces old and modern Union count limits.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3521`
