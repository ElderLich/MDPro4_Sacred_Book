# Card.IsSynchroSummonable

## Signature

```lua
Card.IsSynchroSummonable(Card c, [Card|nil tuner], [Group mg], [int min], [int max]) -> bool
```

## Description

Checks whether c can be Synchro Summoned with tuner and the available material group mg.
If tuner is nil, this behaves like the regular Special Summon procedure check for c.
min and max restrict the number of non-Tuner Synchro Materials used by the procedure.

## Parameters

- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`
