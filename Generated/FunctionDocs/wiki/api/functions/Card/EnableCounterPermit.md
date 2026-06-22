# Card.EnableCounterPermit

## Signature

```lua
Card.EnableCounterPermit(Card c, int countertype, [int location], [function condition]) -> void
```

## Description

Registers a single-card counter permit effect allowing c to receive counters of countertype in the chosen range.
If location is omitted, monsters default to LOCATION_MZONE and non-monsters default to LOCATION_SZONE + LOCATION_FZONE. An optional condition callback is stored on the permit effect.

## Parameters

- `c` `Card`
- `countertype` `int`
- `location` `int` optional
- `condition` `function` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3631`
