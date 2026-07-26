# Card.IsCanBeDisabledByEffect

## Signature

```lua
Card.IsCanBeDisabledByEffect(Card c, Effect e, [bool isMonsterEffect]) -> bool
```

## Description

Checks whether c's effects can be negated by e.
Cards that are already negated, have no original effects, or are unaffected by e cannot be negated.
The optional third parameter indicates whether this is a monster effect.

## Parameters

- `c` `Card`
- `e` `Effect`
- `isMonsterEffect` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3650`
