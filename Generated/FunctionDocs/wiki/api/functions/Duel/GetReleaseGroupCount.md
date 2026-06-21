# Duel.GetReleaseGroupCount

## Signature

```lua
Duel.GetReleaseGroupCount(int player, [bool use_hand], [int reason]) -> int
```

## Description

Return player player can be liberated (non-superior summoned with) the number of cards, use_hand is true, including the hand card

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4975`
