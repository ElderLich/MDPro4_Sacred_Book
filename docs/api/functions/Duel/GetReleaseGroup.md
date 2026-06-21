# Duel.GetReleaseGroup

## Signature

```lua
Duel.GetReleaseGroup(int player, [bool use_hand], [int reason]) -> Group
```

## Description

Returns the cards player can Tribute/Release for effect purposes. If use_hand is true, valid cards in the hand are included.

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4974`
