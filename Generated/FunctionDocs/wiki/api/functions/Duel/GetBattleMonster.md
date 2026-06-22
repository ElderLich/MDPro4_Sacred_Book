# Duel.GetBattleMonster

## Signature

```lua
Duel.GetBattleMonster(int player) -> Card|nil,Card|nil
```

## Description

Returns the monster controlled by player that is currently in battle, followed by the monster controlled by the opponent that is currently in battle.
Each return can be nil if there is no attacker or attack target for that controller.

## Parameters

- `player` `int`

## Returns

- `Card|nil` - Monster controlled by player.
- `Card|nil` - Monster controlled by the opponent.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4959`
