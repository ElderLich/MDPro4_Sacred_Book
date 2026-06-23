# Duel.CheckLocation

## Signature

```lua
Duel.CheckLocation(int player, int location, int sequence) -> bool
```

## Description

Checks whether player can use the given sequence in location.
For Pendulum Zone checks, use LOCATION_PZONE with sequence 0 for the left Pendulum Zone or sequence 1 for the right Pendulum Zone.

## Parameters

- `player` `int`
- `location` `int` - Location constant to inspect, such as LOCATION_MZONE, LOCATION_SZONE, or LOCATION_PZONE.
- `sequence` `int` - Sequence inside that location.

## Returns

- `bool` - true if that exact location sequence is usable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4944`
