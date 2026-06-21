# Duel.IsEnvironment

## Signature

```lua
Duel.IsEnvironment(int code, [int player], [int loc]) -> bool
```

## Description

Check whether the player player is the source code of the venue code
The site code refers to the code of the venue card in effect, or the value of the effect of the venue change
Source Player is the controller of the card in effect, or the controller of the Poseidon Witch, etc.

## Parameters

- `code` `int`
- `player` `int` optional - default: PLAYER_ALL
- `loc` `int` optional - default: LOCATION_ONFIELD

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4898`
