# Card.IsPreviousSetCard

## Signature

```lua
Card.IsPreviousSetCard(Card c, int setcode1, [int setcode2], [... int]) -> bool
```

## Description

Checks whether c's previous card-code or added previous set-code data matches any supplied setcode value.
Nil setcode arguments are skipped. This uses the previous state recorded before the last relevant field or position update, not c's current Set membership.

## Parameters

- `c` `Card`
- `setcode1` `int`
- `setcode2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3395`
