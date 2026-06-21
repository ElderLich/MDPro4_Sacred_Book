# Duel.Equip

## Signature

```lua
Duel.Equip(int player, Card c1, Card c2, [bool up], [bool is_step]) -> bool
```

## Description

把c1作为玩家player的装备卡装备给c2，返回值表示是否成功
up=false则保持装备卡之前的表示形式
is_step=true则是装备过程的分解，需要配合Duel.EquipComplete使用

## Parameters

- `player` `int`
- `c1` `Card`
- `c2` `Card`
- `up` `bool` optional - default: true
- `is_step` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4904`
