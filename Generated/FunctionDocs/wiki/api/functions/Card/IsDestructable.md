# Card.IsDestructable

## Signature

```lua
Card.IsDestructable(Card c, [Effect e]) -> bool
```

## Description

Checks whether c can be destroyed.
Without e, the core only rejects Xyz Materials and cards already in the GY or banished. With e, it checks whether c is affected by e and whether effect-destruction protection applies for the current reason player.

## Parameters

- `c` `Card`
- `e` `Effect` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3571`
