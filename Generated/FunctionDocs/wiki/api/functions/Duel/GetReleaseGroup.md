# Duel.GetReleaseGroup

## Signature

```lua
Duel.GetReleaseGroup(int player, [bool use_hand], [int reason]) -> Group
```

## Description

Return to the player player can be liberated (non-superior summoned use) of the deck, use_hand is true, including the hand card

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4974`
