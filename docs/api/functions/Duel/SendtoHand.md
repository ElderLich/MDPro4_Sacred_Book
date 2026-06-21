# Duel.SendtoHand

## Signature

```lua
Duel.SendtoHand(Card|Group targets, [int|nil player], int reason, [int reason_player]) -> int
```

## Description

The reason to target the player sent to the player's hand, the return value is the actual number of operations
If player is nil, the card's holder's hand is returned

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4861`
