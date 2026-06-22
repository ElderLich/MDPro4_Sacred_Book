# Card.IsDefenseBelow

## Signature

```lua
Card.IsDefenseBelow(Card c, int def) -> bool
```

## Description

Checks whether c has known current DEF less than or equal to def.
Link Monsters and non-monsters return false, and unknown or negative DEF also returns false.

## Parameters

- `c` `Card`
- `def` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3620`
