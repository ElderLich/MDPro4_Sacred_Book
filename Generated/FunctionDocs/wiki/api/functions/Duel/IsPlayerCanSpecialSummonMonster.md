# Duel.IsPlayerCanSpecialSummonMonster

## Signature

```lua
Duel.IsPlayerCanSpecialSummonMonster(int player, int code, [int|nil setcode], [int|nil type], [int|nil atk], [int|nil def], [int|nil level], [int|nil race], [int|nil attribute], [int pos], [int target_player], [int sumtype]) -> bool
```

## Description

Checks whether player can Special Summon a virtual monster with the supplied card data.
Optional arguments override the loaded card data, then pos, target_player, and sumtype describe how and where the monster would be Summoned. This MDPro4 binding does not read a zone argument.

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
- `pos` `int` optional
- `target_player` `int` optional
- `sumtype` `int` optional

## Returns

- `bool` - true if the virtual monster can be Special Summoned.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5052`
