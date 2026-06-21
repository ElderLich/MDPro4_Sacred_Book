# Duel.GetReleaseGroupCount

## Signature

```lua
Duel.GetReleaseGroupCount(int player, [bool use_hand], [int reason]) -> int
```

## Description

Returns the number of cards player can Tribute/Release for effect purposes. If use_hand is true, valid cards in the hand are included.

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4975`
