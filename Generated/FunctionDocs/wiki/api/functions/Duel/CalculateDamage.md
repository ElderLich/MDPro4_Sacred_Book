# Duel.CalculateDamage

## Signature

```lua
Duel.CalculateDamage(Card c1, Card c2, [bool new_attack]) -> void
```

## Description

令c1与c2进行战斗伤害计算（c1 攻击 c2）
若 new_attack=true 则视为 攻击的卡进行过攻击宣言（？）

## Parameters

- `c1` `Card`
- `c2` `Card`
- `new_attack` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4921`
