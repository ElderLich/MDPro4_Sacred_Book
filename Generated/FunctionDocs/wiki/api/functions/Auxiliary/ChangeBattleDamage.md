# Auxiliary.ChangeBattleDamage

## Signature

```lua
Auxiliary.ChangeBattleDamage(int player, any value) -> void
```

## Description

Returns a value function for EFFECT_CHANGE_BATTLE_DAMAGE. player=0 changes damage taken by the effect owner, player=1 changes damage taken by the opponent; otherwise it returns -1 to keep the damage unchanged.

## Parameters

- `player` `int`
- `value` `any`

## Source

- `Utilities/utility.lua:726`
