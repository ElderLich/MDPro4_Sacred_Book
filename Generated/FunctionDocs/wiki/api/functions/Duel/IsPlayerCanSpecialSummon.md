# Duel.IsPlayerCanSpecialSummon

## Signature

```lua
Duel.IsPlayerCanSpecialSummon(int player, [int sumtype], [int sumpos], [int target_player], [Card c]) -> bool
```

## Description

With only player, checks whether player is allowed to perform a Special Summon and still has Special Summon count available.
With the optional card-specific arguments, checks whether player can Special Summon c to target_player in sumpos with sumtype, using the current reason effect.

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `sumpos` `int` optional
- `target_player` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5050`
