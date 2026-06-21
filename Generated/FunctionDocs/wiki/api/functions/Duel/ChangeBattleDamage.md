# Duel.ChangeBattleDamage

## Signature

```lua
Duel.ChangeBattleDamage(int player, int value, [bool check]) -> void
```

## Description

把玩家player在本次战斗中受到的伤害变成value，若 check=false 则原本战斗伤害就算为0也改变伤害

## Parameters

- `player` `int`
- `value` `int`
- `check` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4923`
