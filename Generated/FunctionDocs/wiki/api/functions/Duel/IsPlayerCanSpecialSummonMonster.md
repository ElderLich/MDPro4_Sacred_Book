# Duel.IsPlayerCanSpecialSummonMonster

## Signature

```lua
Duel.IsPlayerCanSpecialSummonMonster(int player, int code, [int|nil setcode], [int|nil type], [int|nil atk], [int|nil def], [int|nil level], [int|nil race], [int|nil attribute], [int pos], [int target_player], [int sumtype], [int zone]) -> bool
```

## Description

Check player player can be pos to the form of special summon the parameters of the monster to the target_player field
This function is usually used to determine whether it is possible to trick token and trap monsters

## Parameters

- `player` `int`
- `code` `int`
- `setcode` `int|nil` optional
- `type` `int|nil` optional
- `atk` `int|nil` optional
- `def` `int|nil` optional
- `level` `int|nil` optional
- `race` `int|nil` optional
- `attribute` `int|nil` optional
- `pos` `int` optional - default: POS_FACEUP
- `target_player` `int` optional - default: player
- `sumtype` `int` optional - default: 0
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5052`
