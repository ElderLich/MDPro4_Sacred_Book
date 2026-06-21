# Duel.SendtoDeck

## Signature

```lua
Duel.SendtoDeck(Card|Group targets, [int|nil player], int seq, int reason, [int reason_player], [bool send_activating]) -> int
```

## Description

Returns targets to the Deck or Extra Deck for reason and returns the number of cards moved.
If player is nil, each card returns to its owner. seq=0 places cards on top of the Deck, seq=1 places them on the bottom, and other values use the default shuffle/return handling.

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
