# Duel.IsEnvironment

## Signature

```lua
Duel.IsEnvironment(int code, [int player], [int loc]) -> bool
```

## Description

Checks whether code is currently treated as the environment card or as a matching face-up card in the requested locations.
player defaults to PLAYER_ALL and loc defaults to LOCATION_ONFIELD. The core checks Field Zones first; if no face-up Field Zone card exists, it can also match the latest EFFECT_CHANGE_ENVIRONMENT effect.

## Parameters

- `code` `int`
- `player` `int` optional - default: PLAYER_ALL
- `loc` `int` optional - default: LOCATION_ONFIELD

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4898`
