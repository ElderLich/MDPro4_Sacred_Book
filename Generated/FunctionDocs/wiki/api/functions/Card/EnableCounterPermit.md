# Card.EnableCounterPermit

## Signature

```lua
Card.EnableCounterPermit(Card c, int countertype, [int location], [function condition]) -> void
```

## Description

Registers a single-card counter permit effect allowing c to receive counters of countertype in the chosen range.
If location is omitted, monsters default to LOCATION_MZONE and non-monsters default to LOCATION_SZONE + LOCATION_FZONE. An optional condition callback is stored on the permit effect.

## Parameters

- `c` `Card` - Card receiving the counter permit effect.
- `countertype` `int` - Counter type that c is allowed to hold.
- `location` `int` optional - Single-effect range for the permit. Omitted defaults to LOCATION_MZONE for monsters, otherwise LOCATION_SZONE + LOCATION_FZONE.
- `condition` `function` optional - Optional condition callback stored on the permit effect; ignored unless this argument is a function.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3686`
