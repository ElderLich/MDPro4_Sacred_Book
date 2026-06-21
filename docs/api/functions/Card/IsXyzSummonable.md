# Card.IsXyzSummonable

## Signature

```lua
Card.IsXyzSummonable(Card c, [Group|nil mg], [int min], [int max]) -> bool
```

## Description

Check whether mg can be selected in the \[min-max months\] excessive material on the c to call the excess procedure
If mg is nil, this function has the same effect as Card.IsSpecialSummonable

## Parameters

- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3577`
