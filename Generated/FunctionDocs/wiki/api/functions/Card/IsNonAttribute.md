# Card.IsNonAttribute

## Signature

```lua
Card.IsNonAttribute(Card c, int attribute) -> bool
```

## Description

Checks whether c has any Attribute other than attribute.
For example, if a monster is both DARK and WIND, IsAttribute(DARK) is true, but IsNonAttribute(DARK) is also true.

## Parameters

- `c` `Card`
- `attribute` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3500`
