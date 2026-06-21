# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool
```

## Description

To return the form c to the field pos, pos default value is the expression before leaving the field, the return value indicates whether the success
C must be a REASON_TEMPORARY reason to leave, and leave the position did not leave that position

## Parameters

- `c` `Card`
- `pos` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`
