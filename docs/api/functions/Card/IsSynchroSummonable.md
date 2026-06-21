# Card.IsSynchroSummonable

## Signature

```lua
Card.IsSynchroSummonable(Card c, [Card|nil tuner], [Group mg]) -> bool
```

## Description

Check whether tuner can be used as an adjustment, the field card \[or mg\] for the coherent material on the c cohomology summon procedures
If the tuner is nil, this function has the same effect as Card.IsSpecialSummonable

## Parameters

- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`
