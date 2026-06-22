# Card.IsSynchroSummonable

## Signature

```lua
Card.IsSynchroSummonable(Card c, [Card|nil tuner], [Group mg]) -> bool
```

## Description

Checks whether c can be Synchro Summoned with tuner and the available material group mg.
If tuner is nil, this behaves like the regular Special Summon procedure check for c.

## Parameters

- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`
