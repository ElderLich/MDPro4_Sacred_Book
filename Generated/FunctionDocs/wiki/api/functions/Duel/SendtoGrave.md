# Duel.SendtoGrave

## Signature

```lua
Duel.SendtoGrave(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Sends targets to the Graveyard for reason, optionally treating reason_player as the player that moved them, and returns the number actually moved.

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4860`
