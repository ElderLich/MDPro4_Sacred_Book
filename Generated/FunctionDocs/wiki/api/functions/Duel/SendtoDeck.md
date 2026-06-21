# Duel.SendtoDeck

## Signature

```lua
Duel.SendtoDeck(Card|Group targets, [int|nil player], int seq, int reason, [int reason_player], [bool send_activating]) -> int
```

## Description

The reason for the targets sent to the players player card group, the return value is the actual number of operations
If player is nil, the card holder of the card is returned
If seq = 0, it is the top of the returned card group; seq = 1 is the bottom of the returned card group;
The rest of the case is to return to the top and mark the need to wash the card group

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `seq` `int`
- `reason` `int`
- `reason_player` `int` optional
- `send_activating` `bool` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4862`
