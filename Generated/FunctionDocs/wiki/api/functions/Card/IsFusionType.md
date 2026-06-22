# Card.IsFusionType

## Signature

```lua
Card.IsFusionType(Card c, int type) -> bool
```

## Description

Checks whether c's type while used as Fusion Material contains type.
For an original Monster Card in the Spell & Trap Zone, the core uses the card-data type while material checks are active; otherwise it uses c's current type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3483`
