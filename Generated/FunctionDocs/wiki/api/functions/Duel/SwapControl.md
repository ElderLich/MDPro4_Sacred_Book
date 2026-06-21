# Duel.SwapControl

## Signature

```lua
Duel.SwapControl(Card|Group targets1, Card|Group targets2, [int reset_phase], [int reset_count]) -> bool
```

## Description

交换targets1与targets2的控制权，返回值表示是否成功
第三个第四个参数同 Duel.GetControl

## Parameters

- `targets1` `Card|Group`
- `targets2` `Card|Group`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4907`
